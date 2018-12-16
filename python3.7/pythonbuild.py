#!/usr/bin/env python3
"""Python Action Compiler
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""

from __future__ import print_function
import os
import re
import sys
import codecs
import subprocess


# The crazy logic of this assembling:
# - a single exec is renamed to __main__.py
# - otherwise if there is a __main__ and an exec, the __main__ win
# - the __main__ is copied to main___
# - if there is a "if __name__ == __main__" it is executed
# otherwise a launcher is created 
def sources(launcher, source_dir, main):
    # source and dest
    src = "%s/exec" % source_dir
    dst = "%s/__main__.py" % source_dir 
    # copy exec to __main__
    # detect if it is also an entry point
    body = ""
    if os.path.isfile(src) and not os.path.isfile(dst):
        with codecs.open(src, 'r', 'utf-8') as s:
            body = s.read()
        with codecs.open(dst, 'w', 'utf-8') as d:
            d.write(body)

    # renaming __main__ to main__
    has_main = False
    body = ""
    src = "%s/__main__.py" % source_dir
    dst = "%s/main__.py" % source_dir 
    if os.path.isfile(src):
        with codecs.open(src, 'r', 'utf-8') as s:
            body = s.read()
        has_main = body.find("""if __name__ == '__main__':""") != -1
        with codecs.open(dst, 'w', 'utf-8') as d:
            d.write(body)

    # we have a main, we can return
    if has_main:
        return dst

    # copy a launcher
    starter = "%s/exec__.py" % source_dir
    with codecs.open(launcher, 'r', 'utf-8') as s:
        with codecs.open(starter, 'w', 'utf-8') as d:
            body = s.read()
            body = body.replace("from main__ import main as main", 
                         "from main__ import %s as main" % main)
            d.write(body)
    return starter

def build(source_dir, target_file, launcher):
    with codecs.open(target_file, 'w', 'utf-8') as d:
        d.write("""#!/bin/bash
cd %s
if test -d virtualenv
then export PYTHONPATH="$PWD/virtualenv"
fi
exec python3 %s
""" % (source_dir, launcher))
    os.chmod(target_file, 0o755)

def main(argv):
    if len(argv) < 4:
        print("usage: <main-function> <source-dir> <target-dir>")
        sys.exit(1)

    main = argv[1]
    source_dir = os.path.abspath(argv[2])
    target_file = os.path.abspath("%s/exec" % argv[3])
    launcher = os.path.abspath(argv[0]+".launcher.py")
    starter = sources(launcher, source_dir, main)
    build(source_dir, target_file, starter)

if __name__ == '__main__':
    main(sys.argv)
