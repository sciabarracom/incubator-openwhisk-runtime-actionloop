USER=docker.io/actionloop
VER=1
IMG=$(USER)/swift-v4.2.1:$(VER)

build:
	docker build -t $(IMG) .

push: build
	docker push $(IMG)

clean:
	docker rmi $(IMG)

.PHONY: build publish clean
