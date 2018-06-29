from flask import Flask
from flask_restful import Resource, Api
from random import *

app = Flask(__name__)
app.debug = True
api = Api(app)

jobList = ["citizen", "citizen", "citizen", "citizen", "mafia", "mafia", "police", "doctor", "host"]
nameDic = {"minha" : "", "gijung" : "", "subeom" : "", "sangyeob" : "", "geonhong" : "", "changhyeon" : "", "inhan" : "", "sungwoo" : "", "sieon" : "" }

def shuffle_job() :
    jobList_copy = jobList[:]
    shuffle(jobList_copy)
    for name in nameDic.keys() :
        nameDic[name] = jobList_copy.pop()

shuffle_job()

class Getjob(Resource):
    def get(self, name):
        return {name : nameDic[name]}

api.add_resource(Getjob,'/getjob/<name>' )
if __name__ == '__main__':
    app.run(host='218.51.230.202')