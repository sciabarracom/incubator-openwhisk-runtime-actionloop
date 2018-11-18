USER=docker.io/msciab
IMG=$(USER)/actionloop-swift-v4.2.1 

build:
	docker build -t $(IMG) .

publish:
	docker push $(IMG)

clean:
	docker rmi $(IMG)

.PHONY: build publish clean