from __future__ import print_function
import fileinput
import json
import copy

legends = {
    "init": "",
    "run": ""
}

groups = { }

def process_line(info, time):
    global legends, groups
    i = info.split(" ")
    t = time.split(" ")
    time = float(t[1])
    key = i[0]
    #label = "%s %s" % (i[1], i[2])
    label = i[1]
    legend = "%s_%s" % (i[0], i[3])
    legends[key] = legend
    if not label in groups:
        groups[label] = { "init":0, "run":0}
    groups[label][key] = time


def process_input():
    buf = ""
    buf2 = ""
    for line in fileinput.input():
        line = line.strip()
        if line.startswith("init"): buf = line
        elif line.startswith("run"): buf = line
        elif line.startswith("run"): buf = line
        elif line.startswith("real"): buf2 = line
        elif line.startswith("sys"): process_line(buf, buf2)

sampleData = {
    "labels": [],
    "datasets": [{
	    "label": 'init',
	    "backgroundColor": '#4dc9f6',
	    "borderColor": 'cyan',
		"borderWidth": 1,
		"data": []
	}, {
	    "label": 'run',
	    "backgroundColor": '#00a950',
	    "borderColor": 'green',
	    "borderWidth": 1,
	    "data": []
	}]
}

def make_bar_data(keys):
    barData = copy.deepcopy(sampleData)
    for label in keys:
        barData["labels"].append(label)
        barData["datasets"][0]["data"].append(groups[label]["init"])
        barData["datasets"][1]["data"].append(groups[label]["run"])
    barData["datasets"][0]["label"] = legends["init"]
    barData["datasets"][1]["label"] = legends["run"]
    return json.dumps(barData)

init_json = ""
run_json = ""

def post_process():
    global init_json, run_json
    m = groups
    ls = [ (m[k]['init'], k,m[k]) for k in m]
    ls.sort(key=lambda x: x[0])
    keys = [k[1] for k in ls]
    #print(keys)
    init_json = make_bar_data(keys)
    ls1 = [ (m[k]['run'], k,m[k]) for k in m]
    ls1.sort(key=lambda x: x[0])
    keys1 = [k[1] for k in ls1]
    run_json = make_bar_data(keys1)

#print(json.dumps(result))
def html():
    return """
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.bundle.js"></script>
</head>
<body>
</body>
<h1>OpenWhisk Runtimes Benchmark</h1>
<p>Test procedure: it uses a multipost Go application, able to run multiple init and run sequentially.</p>
<p><b>Run</b>: Started and Initialized one runtime with an "Hello" action, then executed 1000 run on the same runtime.</p>
<p><b>Init</b>: Started 100 runtimes on different ports, then executed 100 inits in sequence.</p>
<p>Time is measured in seconds using <tt>time</tt> on a single execution of <tt>multipost</tt>.</p>
<h1>Sorted by Run</h1>
<canvas id="runChart"></canvas>
<h1>Sorted by Init</h1>
<canvas id="initChart"></canvas>
<script>
var barDataRun = %s;
var barDataInit = %s;
Chart.scaleService.updateScaleDefaults('linear', {
    ticks: { min: 0 }
});
var ctx1 = document.getElementById('runChart').getContext('2d');
var chart1 = new Chart(ctx1, {
    type: 'horizontalBar',
    data: barDataRun
});
var ctx2 = document.getElementById('initChart').getContext('2d');
var chart1 = new Chart(ctx2, {
    type: 'horizontalBar',
    data: barDataInit
});
</script>
</html>
""" %  (run_json, init_json)


process_input()
#print(groups)
post_process()
print(html())
#print(json.dumps(barData))
