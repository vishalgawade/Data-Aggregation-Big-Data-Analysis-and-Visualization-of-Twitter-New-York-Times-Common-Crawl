from flask import Flask, request
from flask_restful import Resource, Api
# from json import dumps
from flask_jsonpify import jsonify
import json
import pdb
import csv
from datetime import datetime
import time
from nytimesarticle import articleAPI


app = Flask(__name__)

@app.route("/")
def nyDataFunc():
    api = articleAPI("wL9jacwKcc7zrn4UrgRtD59ikr8cHe5s")
    with open('nyTimes_Rugby_Data1.csv', 'a',newline='') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(['nyTimes_Rugby_Data'])
    for i in range(10):
        articles = api.search(q = 'Rubgy',begin_date = 20190101, page = i)
        #pdb.set_trace()
        data = articles['response']['docs']
        dataLength = len(data)
        with open('nyTimes_Rugby_Data1.csv', 'a',newline='') as newFile:
            newFileWriter = csv.writer(newFile)
            for j in range(dataLength):
                newFileWriter.writerow([data[j]['web_url']])

nyDataFunc()

if __name__ == '__main__':
    app.run(port = 5002)