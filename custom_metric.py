import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
# from time import sleep

# def adder():
# 	x = 100
# 	sleep(5)
# 	y = 200
# 	return x + y

# def sub():
# 	x = 200
# 	sleep(5)
# 	y = 100
# 	return x-1

# def tester():
# 	x =100
# 	y = 200
# 	return x + y

def foo():
	x = 1
	y = 2
	return x + y


application = newrelic.agent.register_application()

def report_custom_metrics():
	# newrelic.agent.record_custom_metric('Custom/adder', adder(), application)
	# newrelic.agent.record_custom_metric('Custom/sub', sub(), application)
	# newrelic.agent.record_custom_metric('Custom/tester', tester(), application)
	newrelic.agent.record_custom_metric('Custom/foo', foo(), application)

report_custom_metrics()
