#!/usr/bin/env python3

from __future__ import annotations
from typeguard import typechecked
from typing import Iterable, List, Optional, Tuple

import sys
import pathlib
import re
import os
import io
import tqdm
import _io
import javalang
import repetitions_dataset as rd


_javadoc_re = re.compile(
    r"/\*\*\s*?(.+?)\s*?\*/\s*(.+?)(;|=|\{|\),)", re.S | re.M | re.U)
_jdocraw_re = re.compile(
    r"/\*\*\s*?(.+?)\s*?\*/\s*(.+?)(;|=|\{|\),)", re.S | re.M | re.U)
_jd_bol_re = re.compile(r"^\s*\*\s*", re.U)
_s_re = re.compile(r"\s+", re.U | re.M | re.S)
_java_decl = re.compile(r"\s*(.+?)(;|=|\{|\),)", re.S | re.M | re.U)


@typechecked
def get_java_files(dir: str) -> Iterable[str]:
    return sorted(str(p) for p in pathlib.Path(dir).rglob("*.java"))


@typechecked
def splitlines(s: str) -> Iterable[str]:
    return s.replace('\r', '').split('\n')


@typechecked
def get_docs_0(filename: str, output: _io._TextIOBase) -> rd.BuiltInDocs:
    with open(filename, 'r', encoding='utf-8') as fc:
        src = fc.read()

        fileid = filename.replace(".java", "").replace("\\", "/")

        print(
            f"# File: `{fileid}`"
            f"\n",
            file=output
        )

        entities: List[rd.EntityDeclWithDoc] = []

        for m in _javadoc_re.finditer(src):

            d = m.group(1)
            e = _s_re.sub(' ', m.group(2).strip())

            dls = ['        ' + _jd_bol_re.sub("", l).strip()
                   for l in splitlines(d)]
            cd = '\n'.join(dls).rstrip()

            print(
                f"## Entity: `{fileid}` / `{e}`"
                f"\n\n"
                f"{cd}\n",
                file=output
            )

            entities.append(rd.EntityDeclWithDoc('entity', e, cd, filename))

        return rd.BuiltInDocs(filename, entities)


@typechecked
def get_docs_1(filename: str, output: _io._TextIOBase) -> rd.BuiltInDocs:

    with open(filename, 'r', encoding='utf-8') as fc:
        src = fc.read().replace('\r', '')

        lines = src.split('\n')
        lstarts = [0]
        lstart = 0
        for l in lines:
            lstart += len(l) + 1
            lstarts.append(lstart)

        @typechecked
        def get_decl_doc_and_entity(n: javalang.tree.Declaration) -> Tuple[str, Optional[str], str]:
            if hasattr(n, 'documentation') and n.documentation is not None:
                d: str = n.documentation
                if d.startswith("/**"):
                    d = d[3:]
                if d.endswith("*/"):
                    d = d[:-2]

                dls = ['        ' + _jd_bol_re.sub("", l).strip()
                       for l in splitlines(d) if not l.isspace()]
                cd = '\n'.join(dls).rstrip()
            else:
                cd = ''

            e: Optional[str] = None

            # if n.position is None:
            #     print(n, repr(n))

            entity_start = lstarts[n.position.line - 1] + n.position.column - 1
            m = _java_decl.search(src, pos=entity_start)
            if m is None:
                print("!!!1", file=sys.stderr)
            e = _s_re.sub(" ", m.group(1)).strip()
            et = type(n).__name__.replace("Declaration", "")
            return cd, e, et

        fileid = filename.replace(".java", "").replace("\\", "/")
        print(
            f"# File: `{fileid}`"
            f"\n",
            file=output
        )

        tree = javalang.parse.parse(src)

        entities: List[rd.EntityDeclWithDoc] = []
        for path, node in tree.filter(javalang.tree.Declaration):
            n: javalang.tree.Declaration = node
            # p: javalang.tree.CompilationUnit = path
            if hasattr(n, 'documentation') and n.documentation is not None:
                d, e, t = get_decl_doc_and_entity(n)

                p = ""
                """  Not ready yet
                if len(path) > 1:
                    parent = path[-1][0]
                    pd, pe = get_decl_doc_and_entity(parent)
                    p = f"{p}{pe}::"
                """

                print(
                    f"## {t}: `{fileid}` / `{p}{e}`"
                    f"\n\n"
                    f"{d}\n",
                    file=output
                )

                entities.append(rd.EntityDeclWithDoc(
                    t, f"{p}{e}", d, filename))

        return rd.BuiltInDocs(filename, entities)


@typechecked
def get_docs(filename: str, output: _io._TextIOBase) -> rd.BuiltInDocs:
    fdoc = io.StringIO()
    try:
        r = get_docs_1(filename, fdoc)
    except Exception as e:
        print(f"Error on {filename} via parser: {e}", file=sys.stderr)
        # Fallback
        fdoc = io.StringIO()
        r = get_docs_0(filename, fdoc)
    finally:
        output.write(fdoc.getvalue())
        return r


if __name__ == "__main__":
    with open(sys.argv[2], 'w+', encoding='utf-8') as ofi:
        docs: List[rd.BuiltInDocs] = []
        for f in tqdm.tqdm(list(get_java_files(sys.argv[1]))):
            # sio = io.StringIO()
            docs.append(get_docs(f, ofi))
            # print(sio.getvalue(), file=ofi)
        # rd.save(sys.argv[3], docs) takes long and unnecessary
