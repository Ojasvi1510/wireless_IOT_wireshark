import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
from datetime import datetime
import pandas as pd

#data = pd.read_csv('Wireshark/packets_0.csv')
files = ['packets_0.csv', 'packets_1.csv', 'packets_2.csv', 'packets_3.csv', 'packets_4.csv', 'packets_5.csv']
data = pd.read_csv(files[0], sep='\t') #pd.concat(pd.read_csv(f, sep='\t') for f in files)

#df = pd.concat(map(pd.read_csv, ['d1.csv', 'd2.csv','d3.csv']))

cap = data.loc[0]
#print(cap)
#print(cap['Time'])
#print(dir(cap), "\n\n")
#print(dir(cap.wlan))
#print(cap.wlan.da)
#print(dir(cap['eth']))
#print(cap.sniff_time)

packet_data = []
unique_macs = []
timestamps = []
mac_counts = []

personal_macs = []
personal_timestamps = []
macs_to_check = ['16:f4:66:9d:f2:2b', 'e2:ef:7c:ce:c3:bf', 'c2:80:5d:87:15:94', '82:63:76:00:7a:c0']

print("START")
i = 0
for i, row in data.iterrows():
	if (i % 2000 == 0):
		print(i)
	# print("Source: ", packet.wlan.addr)
 	# print("Destination: ", packet.wlan.dst)
	# print("Timestamp: ", packet.sniff_time)
	
	src_mac = str(row['Source'])
	timestamp = row['Timestamp']
	timestamp = timestamp.replace('000 CET', '')
	print(timestamp)
	timestamp = datetime.strptime(timestamp, "%b  %d, %Y %H:%M:%S.%f")
	#print(src_mac, timestamp)
	
	# x = np.array([src_mac, timestamp])
	# packet_data.insert(len(packet_data), x)
 
	if (src_mac in macs_to_check):
		personal_macs.append(src_mac)
		personal_timestamps.append(timestamp)

	if src_mac not in unique_macs:
		unique_macs.append(src_mac)
		timestamps.append(timestamp)
		mac_counts.append(len(unique_macs))

print("CLOSE")


plt.plot(timestamps, mac_counts)
plt.savefig('mac_counts_time')
plt.show()


fig,ax = plt.subplots()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a %d %H:%M:%S'))
ax.set_xlim([min(timestamps) - dt.timedelta(hours=1), max(timestamps) + dt.timedelta(hours=1)])
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=4))
plt.gca().xaxis.set_minor_locator(mdates.MinuteLocator(interval=30))
plt.gcf().autofmt_xdate()


plt.bar(timestamps, mac_counts, width=0.019)
plt.savefig('bargraph')
plt.show()

fig,ax = plt.subplots()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a %d %H:%M:%S'))
ax.set_xlim([min(timestamps) - dt.timedelta(hours=1), max(timestamps) + dt.timedelta(hours=1)])
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=4))
plt.gca().xaxis.set_minor_locator(mdates.MinuteLocator(interval=30))
plt.gcf().autofmt_xdate()

plt.scatter(personal_timestamps, personal_macs)
plt.savefig('mac_counts_time')
plt.show()