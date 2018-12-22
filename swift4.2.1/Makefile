USER=docker.io/actionloop
IMG=$(USER)/actionloop-swift-v4.2.1 

build:
	docker build -t $(IMG) .

push: build
	docker push $(IMG)

clean:
	docker rmi $(IMG)

.PHONY: build publish clean
