HUB=docker.io/actionloop
IMG=java-v8
VER=0

build: gson-2.8.5.jar
	docker build -t actionloop-$(IMG) .
	docker tag actionloop-$(IMG) $(HUB)/$(IMG):$(VER)

gson-2.8.5.jar:
	curl -LO http://central.maven.org/maven2/com/google/code/gson/gson/2.8.5/gson-2.8.5.jar

push: build
	docker push $(HUB)/$(IMG):$(VER)

clean:
	docker rmi -f $(HUB)/$(IMG):$(VER) actionloop-$(IMG)

enter: build
	docker run -p 8080:8080 -ti actionloop-$(IMG) $(OPT)


.PHONY: build publish clean run shell
