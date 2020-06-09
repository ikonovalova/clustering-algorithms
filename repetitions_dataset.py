from __future__ import annotations
import yaml
from dataclasses import dataclass
from typeguard import typechecked
from typing import Tuple, List, Iterable, Dict, DefaultDict
from abc import ABC

import uuid
import re
from collections import defaultdict

@dataclass
class EntityDeclWithDoc:
    entity_type: str
    entity_decl: str
    entity_doc:  str
    filename: str


@dataclass
class BuiltInDocs:
    filename: str
    entity_docs: List[EntityDeclWithDoc]


def save(filename: str, docs: Iterable[BuiltInDocs])-> None:
    with open(filename, 'w+', encoding='utf-8') as reps:
        yaml.dump_all(docs, reps)  # type: ignore

def load(filname: str)-> List[BuiltInDocs]:
    with open(filname, 'r', encoding='utf-8') as reps:
        r: List[BuiltInDocs] = list(yaml.load_all(reps))  # to deserialize while it is opened =)
        return r

class InputFile(ABC):
    @typechecked
    def __init__(self, model: Model, filename: str):
        self.filename = filename
        self.model = model
        with open(filename, 'r', encoding='utf-8') as ifl:
            self.text = ifl.read()
    
    def save(self, filename: str = None):
        if filename is None:
            filename = self.filename
        with open(filename, 'w+', encoding='utf-8') as ofl:
            ofl.write(self.text)

    def __repr__(self) -> str:
        return f"Inputfile[{self.filename}]"

DuplicateT = Tuple[InputFile, int, int]

# from duplicate finder sourcemarkers.py
# http://stackoverflow.com/a/12843265/539470
_uuid_re_text = "[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
_open_marker_re_text = "<!-- (%s) <=< (ACCEPT|IGNORE) -->" % (_uuid_re_text,)
_close_marker_re_text = "<!-- (ACCEPT|IGNORE) >=> (%s) -->" % (_uuid_re_text,)
_uuidlen = 36
_markerlen = 56
_duplicate_re = re.compile(_open_marker_re_text + r"(.*?)" + _close_marker_re_text, re.M | re.S | re.U)

def _open_marker(group_id: uuid.UUID, marker_type: str = 'ACCEPT') -> str:
    return f"<!-- {group_id} <=< {marker_type} -->"

def _close_marker(group_id: uuid.UUID, marker_type: str = 'ACCEPT') -> str:
    return f"<!-- {marker_type} >=> {group_id} -->"


class Group(ABC):
    @typechecked
    def __init__(self: Group, model: Model, group_id: uuid.UUID, duplicates: List[DuplicateT] = []):
        self.group_id = group_id
        self.model = model
        self.duplicates = duplicates
        self.marker_len = _markerlen  # can potentially be different

    @typechecked
    def duplicate_texts(self: Group, index: int) -> str:
        fl, s, e = self.duplicates[index]
        return fl.text[s:e]

    @typechecked
    def __len__(self: Group) -> int:
        return len(self.duplicates)

    @typechecked
    def __repr__(self: Group) -> str:
        return f"Group[{self.group_id}] = {{" + ','.join(repr(d) for d, i in zip(self.duplicates, range(len(self.duplicates)))) + "}"

    @typechecked
    def __str__(self: Group) -> str:
        return repr(self)

    @typechecked
    def change_id(self: Group, new_id: uuid.UUID, save: bool = True):
        ifiles = set(fl for (fl, s, e) in self.duplicates)
        for f in ifiles:
            f.text = f.text.\
                replace(_open_marker(self.group_id), _open_marker(new_id)).\
                replace(_close_marker(self.group_id), _close_marker(new_id))
            if save:
                f.save()
        del self.model.groups[self.group_id]
        self.model.groups[new_id] = self
        self.group_id = new_id
    
    @typechecked
    def delete(self: Group, save: bool = True):
        ifiles = set(fl for (fl, s, e) in self.duplicates)
        for f in ifiles:
            f.text = f.text.\
                replace(_open_marker(self.group_id), '').\
                replace(_close_marker(self.group_id), '')
            if save:
                f.save()
        del self.model.groups[self.group_id]


class Model(ABC):
    @typechecked
    def __init__(self: Model):
        self.files: List[InputFile] = []
        self.groups: Dict[str, Group]  = {}

    @typechecked
    def _parse_groups(self: Model):
        dd: DefaultDict[str, List[DuplicateT]] = defaultdict(lambda : [])
        for f in self.files:
            for m in _duplicate_re.finditer(f.text):
                uid_s, uid_e = m.span(1)
                text_s, text_e = m.span(3)
                g_uuid = uuid.UUID(f.text[uid_s:uid_e])
                dd[g_uuid].append((f, text_s, text_e))

        for gu in dd:
            self.groups[gu] = Group(self, gu, dd[gu])

@typechecked
def load_model_1_file(filename: str) -> Model:
    m = Model()
    f = InputFile(m, filename)
    m.files = [f]
    m._parse_groups()
    return m

@typechecked
def save_model_1_file(m: Model, filename: str):
    if len(m.files) != 1:
        raise ValueError("Needed model with 1 input file")

    f = m.files[0]
    f.save(filename)
