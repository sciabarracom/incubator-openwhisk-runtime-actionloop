USER=docker.io/msciab
IMG=msciab/actionloop-nodejs-v6.14

build:
	docker build -t $(IMG) .

publish:
	docker push  $(IMG)

clean:
	docker rmi $(IMG)

.PHONY: build publish clean
