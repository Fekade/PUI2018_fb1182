from __future__ import print_function
import sys
import json
try:
   import urllib2 as urllib
except ImportError:
   import urllib.request as urllib

if not len(sys.argv) == 3:
    print ("Usage: python show_bus_location_fb1182.py <MTA_KEY> <BUS_LINE")
    sys.exit()


bus_line = sys.argv[2]
key = sys.argv[1]
bus_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(key, bus_line)

response = urllib.urlopen(bus_url)
data = response.read().decode("utf-8")
data = json.loads(data)


detail = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']

print ("Bus LIne: {}".format(bus_line))
print ("Number of Active Buses: {}".format(len(detail[0]['VehicleActivity'])))
for i in range(len(detail[0]['VehicleActivity'])):
    print ("Bus {} is at latitude {} and longitude {}".format(i, detail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], detail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
