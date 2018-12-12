FROM openwhisk/actionloop:latest as builder
FROM ubuntu:bionic
RUN apt-get update && apt-get install -y \
    curl \
    jq \
    git \
    gccgo \
    golang \
    python \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /action
WORKDIR /action
COPY --from=builder /bin/proxy /bin/proxy
ADD gobuild.py /bin/compile
ADD gobuild.py.launcher.go /bin/compile.launcher.go
ENV OW_COMPILER=/bin/compile
ENTRYPOINT [ "/bin/proxy" ]
