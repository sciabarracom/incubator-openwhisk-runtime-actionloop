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
FROM openwhisk/actionloop:latest as builder

FROM library/openjdk:8u181-jdk-stretch

RUN rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get update \
	&& apt-get install -y --no-install-recommends locales python vim \
	&& rm -rf /var/lib/apt/lists/* \
	&& locale-gen en_US.UTF-8

ENV LANG="en_US.UTF-8" \
	LANGUAGE="en_US:en" \
	LC_ALL="en_US.UTF-8" \
	VERSION=8 \
	UPDATE=162 \
	BUILD=12

RUN locale-gen en_US.UTF-8 ;\
    mkdir -p /javaAction/action /usr/java/src /usr/java/lib
WORKDIR /javaAction
COPY --from=builder /bin/proxy /bin/proxy
ADD javabuild.py /bin/javabuild
ADD exec__.java /usr/java/src/exec__.java
ADD gson-2.8.5.jar /usr/java/lib
ENV OW_COMPILER=/bin/javabuild
ENTRYPOINT /bin/proxy
