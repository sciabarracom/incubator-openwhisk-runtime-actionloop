from sys import stdin
from os import fdopen
import json
from exec__ import main as main

out = fdopen(3, "w")
while True:
  line = stdin.readline()
  if not line: break
  args = json.loads(line)
  payload = {}
  if "value" in args:
    payload = args["value"]
  res = main(payload)
  print(json.dumps(res), file=out)
  out.flush()

