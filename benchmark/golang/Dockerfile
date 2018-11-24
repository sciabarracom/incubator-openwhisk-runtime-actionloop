FROM ubuntu:xenial
WORKDIR /bin
COPY http http
COPY exec exec
RUN chmod +x /bin/http /bin/exec
CMD  /bin/http /bin/exec
