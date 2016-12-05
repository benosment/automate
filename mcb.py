#!/usr/bin/env python3

import argparse
import sys
import pyperclip
import os

'''
Multiclipboard
 - saves/restores clipboard text

'''

MCB_DIR = 'mcb_saves'

def usage():
    print("mcb - save/restore clipboard text")
    print("  Arguments:")
    print("    list - list all clipboards")
    print("    [name] - load a clipboard with a given name")
    print("    save [name] - save a clipboard with a given name)")
    exit()

def list_clipboard():
    files = os.listdir(MCB_DIR)
    for f in files:
        print(f)

def save_clipboard(name):
    text = str(pyperclip.paste())
    filename = os.path.join(MCB_DIR, name)
    with open(filename, 'w') as f:
        f.write(text)

def restore_clipboard(name):
    filename = os.path.join(MCB_DIR, name)
    if not os.path.exists(filename):
        print("ERROR: no clipboard named %s found" % name)
        return
    with open(filename) as f:
        pyperclip.copy(f.read())

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    if len(sys.argv) > 3:
        usage()

    if not os.path.exists(MCB_DIR):
        os.makedirs(MCB_DIR)

    if sys.argv[1] == 'list':
        list_clipboard()
    elif sys.argv[1] == 'save':
        if len(sys.argv) != 3:
            usage()
        save_clipboard(sys.argv[2])
    else:
        if len(sys.argv) != 2:
            usage()
        restore_clipboard(sys.argv[1])
