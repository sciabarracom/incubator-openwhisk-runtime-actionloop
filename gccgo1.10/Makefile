USER=docker.io/msciab
IMG=$(USER)/actionloop-gccgo-v1.10

build:
	docker build -t $(IMG) .

publish:
	docker push  $(IMG)

clean:
	docker rmi $(IMG)


.PHONY: build publish clean
