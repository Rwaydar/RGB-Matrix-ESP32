import requests
import json

payload = {"height": 32, "pixels": [{"x_pos": 2, "y_pos": 0, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 1, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 2, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 3, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 4, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 5, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 6, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 7, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 8, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 9, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 10, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 11, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 12, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 13, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 14, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 15, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 16, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 17, "values": 
[0, 0, 0]}, {"x_pos": 2, "y_pos": 18, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 19, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 20, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 21, "values": [0, 0, 0]}, {"x_pos": 2, 
"y_pos": 22, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 23, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 24, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 25, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 26, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 27, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 28, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 29, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 30, "values": [0, 0, 0]}, {"x_pos": 2, "y_pos": 31, "values": [0, 0, 0]}]}

header = {'Content-type': 'application/json'}
request = requests.post("http://192.168.20.35/image", json = payload, headers=header)

print(request.url)
print(request.text)
print(request.request)
print(request.ok)
print(request.content)