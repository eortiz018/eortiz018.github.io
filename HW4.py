import json
import matplotlib.pyplot as plt

#==============================================

with open('JSON Global Temperature Anomaly (1880-2015 vs. 1901-2000 Average).json','r') as f:
    text=f.read()
    globaltemp=json.loads(text)

with open('JSON US Annual Average Temperature and Anomaly (1880-2015 vs. 1901-2000 Average).json','r') as f:
    text=f.read()
    ustemp=json.loads(text)
    
#==============================================
 
x = list(globaltemp['data'].keys())
y = list(globaltemp['data'].values())

plt.bar(x[-10:], y[-10:], align='center')
plt.ylabel('Global Temperature Anomaly (C)')
plt.xlabel('Year')
plt.title('Global Temperature Anomaly (1880-2015 vs. 1901-2000 Average)')
plt.savefig('globaltemp.png')

#==============================================

keys = ustemp['data'].keys()
values = ustemp['data'].values()

x = [year[:-2] for year in list(keys)]
x = x[-10:]
y1 = [float(val['value']) for val in list(values)]
y1 = y1[-10:]
y2 = [float(val['anomaly']) for val in list(values)]
y2 = y2[-10:]

plt.plot(x, y1, label='Average Temperature')
plt.plot(x, y2, label='Temperature Anomaly')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (F)")
plt.title('US Annual Avg Temp & Anomaly (1880-2015 vs. 1901-2000 Avg)')
plt.savefig('ustemp.png')
