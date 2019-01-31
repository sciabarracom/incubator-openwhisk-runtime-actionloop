go.test:
	docker run -p 8080:8080 --name under-test -d openwhisk/actionloop-golang-v1.11 
	invoke init ../main.go
	hey -n 1000 -c 1 -m POST -T application/json -d '{"name":"Mike"}' http://localhost:8080/run	>$@
	$(MAKE) clean


java.test:
	docker run -p 8080:8080 --name under-test -d openwhisk/java8action 
	invoke init ../main.jar
	hey -n 1000 -c 1 -m POST -T application/json -d '{"name":"Mike"}' http://localhost:8080/run	>$@
	$(MAKE) clean

clean:
	-docker kill under-test
	-docker rm under-test
