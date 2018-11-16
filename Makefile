USER=docker.io/msciab

SWIFT=actionloop-swift-v4.2.1 

swift:
	cd swift4.2.1 ; docker build -t $(USER)/$(SWIFT) .

publish:
	docker login
	docker push $(USER)/$(SWIFT)
