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
FROM openwhisk/actionloop as builder

FROM node:6.14.4-jessie

RUN mkdir -p /nodejsAction/action
WORKDIR /nodejsAction
COPY --from=builder /bin/proxy /bin/proxy
ADD nodejsbuild.py /bin/compile
ADD nodejsbuild.py.launcher.js /bin/compile.launcher.js
ENV OW_COMPILER=/bin/compile
ENTRYPOINT [ "/bin/proxy" ]
