HUB?=docker.io/actionloop
IMG=gccgo-v1.10
VER=1

build:
	docker build -t whisk/actionloop-$(IMG) .
	docker tag whisk/actionloop-$(IMG) $(HUB)/$(IMG):$(VER)

publish:
	docker push $(HUB)/$(IMG):$(VER)

clean:
	docker rmi $(HUB)/$(IMG):$(VER) whisk/actionloop-$(IMG) 


.PHONY: build publish clean