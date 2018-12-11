USER=docker.io/msciab
IMG=$(USER)/actionloop-python-v3.6

build:
	docker build -t $(IMG) .

publish:
	docker push  $(IMG)

clean:
	docker rmi $(IMG)


.PHONY: build publish clean