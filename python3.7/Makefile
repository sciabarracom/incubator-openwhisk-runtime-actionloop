HUB=docker.io/actionloop
IMG=python-v3.7
VER=1

build:
	docker build -t actionloop-$(IMG) .
	docker tag actionloop-$(IMG) $(HUB)/$(IMG):$(VER)

publish:
	docker push $(HUB)/$(IMG):$(VER)

clean:
	docker rmi -f $(HUB)/$(IMG):$(VER) actionloop-$(IMG)

enter: build
	docker run -p 8080:8080 -ti actionloop-$(IMG) $(OPT)


.PHONY: build publish clean run shell
