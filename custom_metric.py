import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
from time import sleep

def adder():
	x = 100
	sleep(5)
	y = 200
	return x + y

application = newrelic.agent.register_application()

def report_custom_metrics():
	newrelic.agent.record_custom_metric('Custom/adder', adder(), application)

report_custom_metrics()