#!/usr/bin/env python3

from __future__ import annotations
from typeguard import typechecked
from typing import Iterable, List, Optional, Tuple

import re
import os
import sys
import uuid
import repetitions_dataset as rd
import textwrap

_n = 0
def new_uuid():
    # return group_uuid.uuid4() -- was used before
    # invalid MAC: 33:34:45:79:34:54 https://superuser.com/q/1210887
    global _n
    node = 0x_33_34_45_79_34_54
    _n += 1
    return uuid.uuid1(node=node, clock_seq=_n)

if __name__=='__main__':
    with \
        open(sys.argv[1], 'r', encoding='utf-8') as r, \
        open(sys.argv[2], 'w', encoding='utf-8') as w:

        buffer = ""

        def release_buffer():
            global buffer
            bu = buffer
            buffer = ""
            u = new_uuid()
            if len(rd._duplicate_re.findall(bu)) == 0:  # has no markers yet
                bu = f"\n<!-- {u} <=< ACCEPT -->\n{bu}<!-- ACCEPT >=> {u} -->\n"
            print(textwrap.indent(bu, 8 * ' '), file=w)

        indoc = False

        mre =  re.compile(fr"({rd._open_marker_re_text})|({rd._close_marker_re_text})")

        for l in r.readlines():
            ml = mre.sub("", l)
            nowdoc = ml.startswith("        ")
            l = l.rstrip()
            if  l == "" and nowdoc:
                continue

            if not indoc and nowdoc:
                indoc = True
            if indoc and not nowdoc:
                indoc = False
                release_buffer()

            if indoc:
                buffer += l.strip() + '\n'

            if not nowdoc:
                print(l, file=w)
