'''
LICENSED under Apache 2.0 (http://directory.fsf.org/wiki/License:Apache2.0)
Created by: Md Shahedul Alam (Research Assistant, Aalto University), Udayanto Dwi Atmojo
February, 2020
'''
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import json
import socket
import http.client

# open json file and give it to api variable as a dictionary
with open("enas_data.json") as api_file:
    enas_data = json.load(api_file)


class ServiceHandler(BaseHTTPRequestHandler):
    # sets basic headers for the server
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        # reads the length of the Headers
        length = int(self.headers['Content-Length'])
        # reads the contents of the request
        data = json.loads(self.rfile.read(length))
        self.end_headers()
        return data

    def do_POST(self):
        cnv_data = self._set_headers()
        if cnv_data["Cnv_State"] == "Off":
            cnv_off()
        elif cnv_data["Cnv_State"] == "On":
            cnv_off()
            if cnv_data["Cnv_Id"] == "One":
                cnv_one_on(cnv_data)
            elif cnv_data["Cnv_Id"] == "Two":
                cnv_two_on(cnv_data)
            elif cnv_data["Cnv_Id"] == "Three":
                cnv_three_on(cnv_data)
            elif cnv_data["Cnv_Id"] == "Four":
                cnv_four_on(cnv_data)
            else:
                error = "Invalid Conveyor Number"
        else:
            error = "Invalid Conveyor State"


def cnv_off():
    enas_data["CNV_One_State"] = False
    enas_data["CNV_Two_State"] = False
    enas_data["CNV_Three_State"] = False
    enas_data["CNV_Four_State"] = False
    enas_data["CNV_One_Direction"] = "None"
    enas_data["CNV_Two_Direction"] = "None"
    enas_data["CNV_Three_Direction"] = "None"
    enas_data["CNV_Four_Direction"] = "None"
    enas_data["CNV_One_RFID_1"] = False
    enas_data["CNV_Two_RFID_2"] = False
    enas_data["CNV_Three_RFID_3"] = False
    enas_data["CNV_Three_RFID_4"] = False
    enas_data["CNV_Four_RFID_5"] = False
    with open("enas_data.json", 'w+') as data_file:
        json.dump(enas_data, data_file)


def cnv_one_on(cnv_data):
    enas_data["CNV_One_State"] = True
    enas_data["CNV_Two_State"] = False
    enas_data["CNV_Three_State"] = False
    enas_data["CNV_Four_State"] = False
    enas_data["CNV_One_Direction"] = cnv_data["Cnv_Direction"]
    enas_data["CNV_Two_Direction"] = "None"
    enas_data["CNV_Three_Direction"] = "None"
    enas_data["CNV_Four_Direction"] = "None"
    if cnv_data["Cnv_RFID_Station"] == "On":
        enas_data["CNV_One_RFID_1"] = True
    else:
        enas_data["CNV_One_RFID_1"] = False
    enas_data["CNV_Two_RFID_2"] = False
    enas_data["CNV_Three_RFID_3"] = False
    enas_data["CNV_Three_RFID_4"] = False
    enas_data["CNV_Four_RFID_5"] = False
    with open("enas_data.json", 'w+') as data_file:
        json.dump(enas_data, data_file)


def cnv_two_on(cnv_data):
    enas_data["CNV_One_State"] = False
    enas_data["CNV_Two_State"] = True
    enas_data["CNV_Three_State"] = False
    enas_data["CNV_Four_State"] = False
    enas_data["CNV_One_Direction"] = "None"
    enas_data["CNV_Two_Direction"] = cnv_data["Cnv_Direction"]
    enas_data["CNV_Three_Direction"] = "None"
    enas_data["CNV_Four_Direction"] = "None"
    enas_data["CNV_One_RFID_1"] = False
    if cnv_data["Cnv_RFID_Station"] == "On":
        enas_data["CNV_Two_RFID_2"] = True
    else:
        enas_data["CNV_Two_RFID_2"] = False
    enas_data["CNV_Three_RFID_3"] = False
    enas_data["CNV_Three_RFID_4"] = False
    enas_data["CNV_Four_RFID_5"] = False
    with open("enas_data.json", 'w+') as data_file:
        json.dump(enas_data, data_file)


def cnv_three_on(cnv_data):
    enas_data["CNV_One_State"] = False
    enas_data["CNV_Two_State"] = False
    enas_data["CNV_Three_State"] = True
    enas_data["CNV_Four_State"] = False
    enas_data["CNV_One_Direction"] = "None"
    enas_data["CNV_Two_Direction"] = "None"
    enas_data["CNV_Three_Direction"] = cnv_data["Cnv_Direction"]
    enas_data["CNV_Four_Direction"] = "None"
    enas_data["CNV_One_RFID_1"] = False
    enas_data["CNV_Two_RFID_2"] = False
    if cnv_data["Cnv_RFID_Station"] == "On":
        enas_data["CNV_Three_RFID_3"] = True
        enas_data["CNV_Three_RFID_4"] = True
    else:
        enas_data["CNV_Three_RFID_3"] = False
        enas_data["CNV_Three_RFID_4"] = False
    enas_data["CNV_Four_RFID_5"] = False
    with open("enas_data.json", 'w+') as data_file:
        json.dump(enas_data, data_file)


def cnv_four_on(cnv_data):
    enas_data["CNV_One_State"] = False
    enas_data["CNV_Two_State"] = False
    enas_data["CNV_Three_State"] = False
    enas_data["CNV_Four_State"] = True
    enas_data["CNV_One_Direction"] = "None"
    enas_data["CNV_Two_Direction"] = "None"
    enas_data["CNV_Three_Direction"] = "None"
    enas_data["CNV_Four_Direction"] = cnv_data["Cnv_Direction"]
    enas_data["CNV_One_RFID_1"] = False
    enas_data["CNV_Two_RFID_2"] = False
    enas_data["CNV_Three_RFID_3"] = False
    enas_data["CNV_Three_RFID_4"] = False
    if cnv_data["Cnv_RFID_Station"] == "On":
        enas_data["CNV_Four_RFID_5"] = True
    else:
        enas_data["CNV_Four_RFID_5"] = False

    with open("enas_data.json", 'w+') as data_file:
        json.dump(enas_data, data_file)


def main():
    url = '10.100.41.98'
    port = 8080
    server = HTTPServer((url, port), ServiceHandler)
    print('Starting EnAS Demo Model Server at', url, ':%d' % port)
    server.serve_forever()


main()
