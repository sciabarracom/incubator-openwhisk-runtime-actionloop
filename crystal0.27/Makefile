USER=docker.io/juice10
IMG=$(USER)/actionloop-crystal-v0.27

build:
	docker build -t $(IMG) .

publish:
	docker push  $(IMG)

clean:
	docker rmi $(IMG)


.PHONY: build publish clean
