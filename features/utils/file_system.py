import json
from pprint import pprint

class FileSystem:

    def __init__(self, pathFolder=''):
        self._load_folder(pathFolder)

    def _load_folder(self, pathFolder=''):
        self.path = json.load(open(pathFolder))

    def _get_DataJson(self):
        return self.path

    def _compare_to(self, resultFileJson, resultJsonRequest):
        self.resultCompareTo = (resultFileJson == resultJsonRequest)
        return self.resultCompareTo

    def _print_structure_json(self, json):
        self.json = json
        pprint(self.json)

    def _cleanup(self):
        self.path = 'Empty'
        self.json = 'Empty'
        self.resultCompareTo = 'Empty'