import requests
import json

url = "https://cae-autreg-dev.cisco.com/cgi-bin/autoregRPF.pl?userid=AutoRegTest1&sopo=42466404&custnum=19988&org_name=GLOBAL%20DATA%20SYSTEMS%20INC"
# header = "Access-Control-Allow-Origin: *"
r = requests.get(url)
#print ("Access-Control-Allow-Origin: *")
print(r.text)