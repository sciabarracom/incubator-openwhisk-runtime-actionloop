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


require "logger"
require "json"

# requiring user's action code
require "./exec__"

# open our file descriptor, this allows us to talk to the go-proxy parent process
# code gets executed via file descriptor #3
# bash equivalent: `crystal this-file.cr 3>&1`
out = IO::FileDescriptor.new(3)

# run this until process gets killed
while true
  # JSON arguments get passed via STDIN
  line = STDIN.gets()

  # empty line is unexpected, lets stop this process when that happens
  break unless line

  # parse JSON arguments that come in via the value parameter
  args = JSON.parse(line)
  payload = {} of String => String
  if args["value"]?
    payload = args["value"]
  end

  # execute the user's action code
  res = main(payload)

  # start passing the result & a line break to the go-proxy parent process via STDOUT
  out.puts(res.to_json)
  # send STDOUT to parent process
  out.flush()
end
