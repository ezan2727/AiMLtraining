import datetime
import inspect
dateclass = inspect.getmembers(datetime, inspect.isclass)

print ('\n--current date and time--')
print (datetime.datetime.now())
print ('\n--current time--\n')
print (datetime.datetime.now().time())
print (datetime.datetime.now().time())

cttime = datetime.datetime.now().time()
formatedtime = datetime.datetime.now().strftime("%H:%M:%S")
print(datetime.date.today().strftime("%B %d, %Y"))

print ('current time:', cttime)
print ('formatted time:', formatedtime)


