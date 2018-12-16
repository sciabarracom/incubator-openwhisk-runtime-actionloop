from __future__ import print_function
from sys import stdin
from sys import stdout
from sys import stderr
from os import fdopen
import os, json
from main__ import main as main

out = fdopen(3, "wb")
env = os.environ
while True:
  line = stdin.readline()
  if not line: break
  args = json.loads(line)
  payload = {}
  for key in args:
    if key == "value":
      payload = args["value"]
    else:
      env["__OW_%s" % key.upper()]= args[key]
  res = main(payload)
  out.write(json.dumps(res, ensure_ascii=False).encode('utf-8'))
  out.write(b'\n')
  stdout.flush()
  stderr.flush()
  out.flush()

