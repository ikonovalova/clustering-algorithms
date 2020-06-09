#!/usr/bin/env python3

from __future__ import annotations

import sys
import csv
from textwrap import indent
import uuid
from collections import defaultdict
from typing import DefaultDict

_node = 0x_33_34_45_79_34_54
class groupuiddict(defaultdict):
    def __missing__(self, key):
        self[key] = new = uuid.uuid1(node=_node, clock_seq=key)
        return new

idx2uuid = groupuiddict()

def dup_text(dup_idx: int, grp_idx: int, text: str) -> str:
    u = idx2uuid[grp_idx]
    txt = indent(f"<!-- {u} <=< ACCEPT -->\n{text.strip()}\n<!-- ACCEPT >=> {u} -->\n", 8 * ' ')
    return f"""# Group No {grp_idx} / Dup No {dup_idx}\n\n{txt}"""


def main():
    with \
        open(sys.argv[1], 'r', encoding='utf-8') as csv_file, \
        open(sys.argv[2], 'w+', encoding='utf-8') as md_file:

        reader = csv.reader(csv_file, dialect='excel')
        next(reader)

        dups = []

        for t, n, g in reader:
            dups.append(dup_text(int(n), int(g), t))

        print('\n'.join(dups), file=md_file)


if __name__=='__main__':
    main()
