USER=docker.io/msciab
IMG=$(USER)/actionloop-gccgo-v8

build:
	docker build -t $(IMG) .

publish:
	docker push  $(IMG)

clean:
	docker rmi $(IMG)


.PHONY: build publish clean
