report.txt:
	echo "*** nodejs6action" >report.txt
	make -C nodejs classic | grep '/sec' >>report.txt
	echo "*** python3action" >>report.txt
	make -C python classic | grep '/sec' >>report.txt
	echo "*** actionloop-golang-v1.11" >>report.txt
	make -C golang classic | grep '/sec' >>report.txt
	echo "*** PROTO new actionloop-golang-v1.11" >>report.txt
	make -C golang turbo | grep '/sec' >>report.txt
