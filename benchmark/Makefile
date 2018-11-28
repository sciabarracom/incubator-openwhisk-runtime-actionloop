all: golang node node-actionloop python python-actionloop php

report.txt:
	@echo "Performance report">report.txt
	@echo "*** actionloop-golang" >>report.txt
	make  golang | grep '/sec' >>report.txt
	@echo "*** nodejs6action" >>report.txt
	make node | grep '/sec' >>report.txt
	@echo "*** actionloop-nodejs6action" >>report.txt
	make node-actionloop | grep '/sec' >>report.txt
	@echo "*** python3action" >>report.txt
	make python | grep '/sec' >>report.txt
	@echo "*** actionloop-python" >>report.txt
	make python-actionloop | grep '/sec' >>report.txt

clean:
	docker kill under-test

golang:
	bash test.sh whisk/actionloop-golang-v1.11 main.go

node:
	bash test.sh openwhisk/nodejs6action main.js

node-actionloop:
	bash test.sh msciab/actionloop-nodejs-v6.14 main.js

python:
	bash test.sh openwhisk/python3action main.py

python-actionloop:
	bash test.sh msciab/actionloop-python-v3.6 main.py

php:
	bash test.sh openwhisk/action-php-v7.2 main.php




