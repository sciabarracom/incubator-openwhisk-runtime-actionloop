N?=10
NN?=100

report:
	echo "*** Benchmarch Init ***">init.result
	cat *.test | grep 'init' | sort -k 3 >>init.result
	echo "*** Benchmarch Run ***">run.result
	cat *.test | grep 'run_' | sort -k 3 >>run.result
	cat init.result run.result

tests: 
	@grep '.test:' Makefile | grep -v grep | sed -e 's/:.*//'

multipost: multipost.go
	go build -o multipost multipost.go

main_go.zip: main.go
	docker run -i openwhisk/actionloop-golang-v1.11 -compile main <$< >$@

go.test: 
	bash test.sh $(N) $(NN) openwhisk/actionloop-golang-v1.11 main.go $@
	bash test.sh $(N) $(NN) openwhisk/actionloop-golang-v1.11 main_go.zip $@

node.test:
	bash test.sh $(N) $(NN) openwhisk/nodejs6action main.js $@
	bash test.sh $(N) $(NN) openwhisk/action-nodejs-v8 main.js $@
	bash test.sh $(N) $(NN) openwhisk/action-nodejs-v10 main.js $@
	bash test.sh $(N) $(NN) msciab/actionloop-nodejs-v6.14 main.js $@

python.test:
	bash test.sh $(N) $(NN) openwhisk/python2action main.py $@
	bash test.sh $(N) $(NN) openwhisk/python3action main.py $@
	bash test.sh $(N) $(NN) msciab/actionloop-python-v3.6 main.py $@

php.test:
	bash test.sh $(N) $(NN) openwhisk/action-php-v7.1 main.php $@
	bash test.sh $(N) $(NN) openwhisk/action-php-v7.2 main.php $@

swift.test:
	bash test.sh $(N) $(NN) openwhisk/action-swift-v3.1.1 main.swift $@
	bash test.sh $(N) $(NN) openwhisk/action-swift-v4.1 main.swift $@
	bash test.sh $(N) $(NN) msciab/actionloop-swift-v4.2.1 main.swift $@

ruby.test:
	bash test.sh $(N) $(NN) openwhisk/action-ruby-v2.5 main.rb $@

clean:
	-rm *.test *.init *.run

