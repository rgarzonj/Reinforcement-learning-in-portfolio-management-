import json
import os.path

class ExpLogger:
    def __init__(self):
        self.res = {}

    def logResults(self,agent,metric,value):
        if agent not in self.res:
            self.res[agent]={}
        self.res[agent][metric] = value
        return self.res

    def logConfig(self,configuration):
        self.res["config"] = configuration

    def saveResults (self,fileName='results.json'):
        with open(fileName, 'w') as fp:
            json.dump(self.res, fp)
        if os.path.isfile(fileName):
            return True
        else:
            return False