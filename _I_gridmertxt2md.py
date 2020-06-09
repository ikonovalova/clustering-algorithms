#!/usr/bin/env python3

from __future__ import annotations
from typing import List, Tuple

import sys
import os
import textwrap
import html

import enum

class States(enum.Enum):
    NOPE = 0
    CAPT = enum.auto()
    BODY = enum.auto()


def main():
    state = States.CAPT
    ccap = ""
    cbody = ""

    with \
        open(sys.argv[1], 'r', encoding='utf-8') as inpf,\
        open(sys.argv[2], 'w', encoding='utf-8') as otpf:

        def release():
            nonlocal state, cbody, ccap
            state = States.CAPT
            ccap = ccap.strip()
            cbody = cbody.strip()
            if ccap == "":
                return
            print(f"## {html.escape(ccap)}", file=otpf)
            print("", file=otpf)
            print(textwrap.indent(cbody, 8 * ' '), file=otpf)
            print("", file=otpf)
            ccap = ""
            cbody = ""

        for fl in inpf:
            l = fl.strip()
            if l == '':
                continue
            if state == States.CAPT:
                ccap = l
                state = States.BODY
            elif state == States.BODY:
                if l != "----------------------":
                    cbody += l + '\n'
                else:
                    release()
        release()

if __name__=='__main__':
    main()
