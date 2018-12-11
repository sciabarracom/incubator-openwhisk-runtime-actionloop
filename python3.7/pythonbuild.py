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

def sources(launcher, source_dir, main):
    src = "%s/exec" % source_dir
    dst = "%s/exec__.py" % source_dir 
    if os.path.isfile(src) and not os.path.isfile(dst):
        body = ""
        with codecs.open(src, 'r', 'utf-8') as s:
            body = s.read()
        with codecs.open(dst, 'w', 'utf-8') as d:
            d.write(body)


    launcher_file = "%s/main__.py" % source_dir
    with codecs.open(launcher_file, 'w', 'utf-8') as d:
        with codecs.open(launcher, 'r', 'utf-8') as s:
            body = s.read()
            body.replace("from exec__ import main as main", 
                         "from exec__ import %s as main" % main)
            d.write(body)

def build(source_dir, target_file):
    with codecs.open(target_file, 'w', 'utf-8') as d:
        d.write("""#!/bin/bash
cd %s
exec python3 main__.py
""" % source_dir)
    os.chmod(target_file, 0o755)


def main(argv):
    if len(argv) < 4:
        print("usage: <main-function> <source-dir> <target-dir>")
        sys.exit(1)

    main = argv[1]
    source_dir = os.path.abspath(argv[2])
    target_file = os.path.abspath("%s/exec" % argv[3])
    launcher = os.path.abspath(argv[0]+".launcher.py")
    sources(launcher, source_dir, main)
    build(source_dir, target_file)

if __name__ == '__main__':
    main(sys.argv)
