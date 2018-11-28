report.txt:
	echo "Performance report">report.txt
	echo "*** actionloop-golang-v1.11 (improved)" >>report.txt
	make -C golang golang | grep '/sec' >>report.txt
	echo "*** nodejs6action" >>report.txt
	make -C nodejs classic | grep '/sec' >>report.txt
	echo "*** actionloop-nodejs6action" >>report.txt
	make -C nodejs actionloop | grep '/sec' >>report.txt
	echo "*** python3action" >>report.txt
	make -C python classic | grep '/sec' >>report.txt
	echo "*** actionloop-python" >>report.txt
	make -C python actionloop | grep '/sec' >>report.txt
