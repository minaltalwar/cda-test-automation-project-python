import configparser
import json
from utils import library

# Fetch Configurable parameters
config = configparser.ConfigParser()
config.read('Configuration.cfg')
xlFileName = config['Files']['fileNamePath']
xlSheetName = config['Files']['sheetName']
inputFromColumn = int(config['Files']['inputFromColumn'])
inputToColumn = int(config['Files']['inputToColumn'])
expectedFromColumn = int(config['Files']['expectedFromColumn'])
expectedToColumn = int(config['Files']['expectedToColumn'])

# Fetch the column names (both request and expected) from testcase xls
obj = library.Common(xlFileName, xlSheetName)
rows = obj.fetch_row_count()
inputkeyList = obj.fetch_key_names(inputFromColumn, inputToColumn)
expectedKeyList = obj.fetch_key_names(expectedFromColumn, expectedToColumn)

def input_request():
    input_dict = []
    for i in range(2, rows + 1):
        inputJSON = obj.return_dictionary(keyList=inputkeyList, rowNumber=i)
        jsonInputFile = json.dumps(inputJSON)
        with open('data1.json', 'w') as f:
            f.write(jsonInputFile)
        with open('data1.json', 'r') as j:
            requestDict = json.loads(j.read())
        expectedDict = obj.return_expected_dictionary(expectedKeyList=expectedKeyList, rowNumber=i)
        test_input = (requestDict, expectedDict)
        input_dict.append(test_input)
    return input_dict


