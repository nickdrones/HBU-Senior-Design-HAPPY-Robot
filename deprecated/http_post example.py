import requests

response = requests.post('http://172.17.21.145:8080/api/jobreceive', json={'orderNumber':'000000','destinationCode': 'D01', 'originCode': 'D08','customerUsername':'belbasnj', 'authCode':'000000'})

print("Status code: ", response.status_code)
#print("Printing Entire Post Request")
#print(response.json())