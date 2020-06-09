#!/usr/bin/env python3

from __future__ import annotations

import sys
import csv
from textwrap import dedent
from uuid import UUID

import repetitions_dataset as rd

_grp_indices = {}
_maxpos = 1
_minneg = -1
def grp_no(gv: rd.Group):
    global _maxpos, _minneg
    if gv.group_id in _grp_indices:
        return _grp_indices[gv.group_id]
    else:
        if len(gv) > 1:  # real group
            i = _maxpos
            _maxpos += 1
        else:
            i = _minneg
            _minneg -= 1
        _grp_indices[gv.group_id] = i
        return i

def main():
    m: rd.Model = rd.load_model_1_file(sys.argv[1])

    with open(sys.argv[2], 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        dups_groups = sorted([(d, gv) for gk, gv in m.groups.items() for d in gv.duplicates])
        # sorted will sort by file then begin then end, ok for us
        writer.writerows([
            [
                dedent(f.text[b: e]),
                i,
                grp_no(gv)
            ] for i, ((f, b, e), gv) in enumerate(dups_groups)
        ])

if __name__=='__main__':
    main()
