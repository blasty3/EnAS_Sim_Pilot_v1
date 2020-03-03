'''
LICENSED under Apache 2.0 (http://directory.fsf.org/wiki/License:Apache2.0)
Created by: Md Shahedul Alam (Research Assistant, Aalto University), Udayanto Dwi Atmojo
February, 2020
'''
import http.client
import requests
import json
import time
http_server = "10.100.41.98:8080"
connect = http.client.HTTPConnection(http_server)
if connect:
    print("connected to EnAS API server")

Conveyor_One_Variables = {
        "Cnv_Id": "One",
        "Cnv_State": "On",
        "Cnv_Direction": "Left",
        "Cnv_RFID_Station": "On",
}
Conveyor_Two_Variables = {
        "Cnv_Id": "Two",
        "Cnv_State": "On",
        "Cnv_Direction": "Up",
        "Cnv_RFID_Station": "On",
}
Conveyor_Three_Variables = {
        "Cnv_Id": "Three",
        "Cnv_State": "On",
        "Cnv_Direction": "Right",
        "Cnv_RFID_Station": "On",
}
Conveyor_Four_Variables = {
        "Cnv_Id": "Four",
        "Cnv_State": "On",
        "Cnv_Direction": "Down",
        "Cnv_RFID_Station": "On",
}
url = "http://10.100.41.98:8080/"
while True:
        post_response_1 = requests.post(url, data=json.dumps(Conveyor_One_Variables))
        time.sleep(3)
        post_response_2 = requests.post(url, data=json.dumps(Conveyor_Two_Variables))
        time.sleep(3)
        post_response_3 = requests.post(url, data=json.dumps(Conveyor_Three_Variables))
        time.sleep(3)
        post_response_4 = requests.post(url, data=json.dumps(Conveyor_Four_Variables))
        time.sleep(3)

