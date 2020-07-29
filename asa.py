import requests

url = "https://192.168.198.131/api/interfaces/physical/GigabitEthernet0_API_SLASH_5"

payload = "{\r\n  \"securityLevel\": 50,\r\n  \"kind\": \"object#GigabitInterface\",\r\n  \"channelGroupMode\": \"active\",\r\n  \"flowcontrolLow\": -1,\r\n  \"name\": \"web\",\r\n  \"duplex\": \"auto\",\r\n  \"forwardTrafficSFR\": false,\r\n  \"hardwareID\": \"GigabitEthernet0/3\",\r\n  \"mtu\": 1500,\r\n  \"lacpPriority\": -1,\r\n  \"flowcontrolHigh\": -1,\r\n  \"ipAddress\": {\r\n    \"ip\": {\r\n      \"kind\": \"IPv4Address\",\r\n      \"value\": \"172.160.200.2\"\r\n    },\r\n    \"kind\": \"StaticIP\",\r\n    \"netMask\": {\r\n      \"kind\": \"IPv4NetMask\",\r\n      \"value\": \"255.255.255.0\"\r\n    }\r\n  },\r\n  \"flowcontrolOn\": false,\r\n  \"shutdown\": true,\r\n  \"interfaceDesc\": \"app_interface\",\r\n  \"managementOnly\": false,\r\n  \"channelGroupID\": \"\",\r\n  \"speed\": \"auto\",\r\n  \"forwardTrafficCX\": false,\r\n  \"flowcontrolPeriod\": -1\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46Y2lzY28xMjM='
}

response = requests.request("PUT", url, headers=headers, data = payload, verify=False)

print(response.text.encode('utf8'))

print ("You're doing great work")
