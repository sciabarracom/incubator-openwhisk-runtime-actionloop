IMG?=openwhisk/actionloop-golang-v1.11

all: classic turbo

classic:
	echo "*** Current ActionLoop Image ***"
	docker run -d --name under-test --rm -p 8080:8080 $(IMG)
	invoke init exec.go
	wrk -t1 -c1 -stest.lua http://localhost:8080/run
	docker kill under-test

turbo: image
	echo "*** Proto ActionLoop NoGoroutine ***"
	docker run -p 8080:8080 -d --name under-test --rm under-test
	wrk -t1 -c1 -stest.lua http://localhost:8080/run
	docker kill under-test

image: exec http
	docker build -t under-test .

clean:
	-rm http exec
	-docker rmi under-test

http:
	GOARCH=amd64 GOOS=linux go build http.go

exec:
	docker run -i openwhisk/actionloop-golang-v1.11 -compile main <exec.go >exec.zip
	unzip exec.zip

.PHONY: image test
