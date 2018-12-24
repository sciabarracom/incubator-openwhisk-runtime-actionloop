N?=100
NN?=1000

index.html: run_tests
	@python report.py *.test >index.html
	-rm ../index.html
	cp index.html ..

all_tests:
	@grep '.test:' Makefile | grep -v grep | sed -e 's/:.*//'


run_tests:
	for i in $(shell $(MAKE) all_tests) ; do $(MAKE) $$i ; done

multipost: multipost.go
	go build -o multipost multipost.go

main_gccgo.zip: main.go
	docker run -i actionloop/gccgo-v1.10:1 -compile main <$< >$@

main_go.zip: main.go
	docker run -i openwhisk/actionloop-golang-v1.11 -compile main <$< >$@

go.test: multipost main_go.zip main_gccgo.zip
	bash test.sh $(N) $(NN) actionloop/gccgo-v1.10:1 main_gccgo.zip $@
	bash test.sh $(N) $(NN) openwhisk/actionloop-golang-v1.11:latest main_go.zip $@

node.test: multipost
	bash test.sh $(N) $(NN) openwhisk/nodejs6action main.js $@
	bash test.sh $(N) $(NN) openwhisk/action-nodejs-v8 main.js $@
	bash test.sh $(N) $(NN) openwhisk/action-nodejs-v10 main.js $@
	#bash test.sh $(N) $(NN) msciab/actionloop-nodejs-v6.14 main.js $@

python.test: multipost
	bash test.sh $(N) $(NN) openwhisk/python2action main.py $@
	bash test.sh $(N) $(NN) openwhisk/python3action main.py $@
	bash test.sh $(N) $(NN) actionloop/python-v3.7:1 main.py $@

php.test: multipost
	bash test.sh $(N) $(NN) openwhisk/action-php-v7.1 main.php $@
	bash test.sh $(N) $(NN) openwhisk/action-php-v7.2 main.php $@
	bash test.sh $(N) $(NN) openwhisk/action-php-v7.3 main.php $@

main_swift.zip: main.swift
	docker run -i actionloop/swift-v4.2.1:1 -compile main <$< >$@

swift.test: multipost main.swift main_swift.zip 
	bash test.sh $(N) $(NN) openwhisk/action-swift-v3.1.1:latest main.swift $@
	bash test.sh $(N) $(NN) openwhisk/action-swift-v4.1:latest main.swift $@
	bash test.sh $(N) $(NN) actionloop/swift-v4.2.1:1 main_swift.zip $@

ruby.test: multipost
	bash test.sh $(N) $(NN) openwhisk/action-ruby-v2.5 main.rb $@

main_cr.zip: main.cr
	docker run -i juice10/actionloop-crystal-v0.27 -compile main <$< >$@

crystal.test: multipost main_cr.zip
	bash test.sh $(N) $(NN) juice10/actionloop-crystal-v0.27 main_cr.zip $@

clean:
	-rm *.test *.zip 

kill:
	-docker ps -q | xargs docker kill
	-docker ps -q -q | xargs docker rm
