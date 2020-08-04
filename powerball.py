import os
from gmail import Gmail
from datetime import datetime, timedelta
import time
import urllib3
import json

myNumbers = [
    [ {10, 19, 29, 37, 46 }, {  6 } ],
    [ { 2, 10, 15, 22, 23 }, {  4 } ],
    [ { 1,  4, 11, 20, 23 }, { 10 } ],
    [ { 2,  6,  9, 19, 27 }, { 11 } ]
]


# The key to this dictionary is whether the powerball was matched
prizes = {
    True:
    {
        0: 4,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: "!!!!!!!!!!!!!"
    },
    False:
    {
        0: 0,
        1: 0,
        2: 0,
        3: 7,
        4: 100,
        5: 1000000
    }
}

def Print(outputMessage, msg):
    outputMessage += msg
    outputMessage += "\n"
    return outputMessage


def printEntry(outputMessage: str, prefix: str, entry: list):
    numbers = list(entry[0])
    numbers = sorted(numbers)
    powerball = str(entry[1].copy().pop())
    return Print(outputMessage, prefix.format(" ".join(str(n) for n in numbers), powerball))


def checkNumbers(currentNumbers: list, outputMessage: str):
    for number, ticket in enumerate(myNumbers):

        outputMessage = printEntry(outputMessage, "Checking your numbers: {0} \tPowerball: {1}", ticket)

        powerballMatch = True if len(ticket[1] & currentNumbers[1]) else False
        matches = len(ticket[0] & currentNumbers[0])
        if powerballMatch == True:
            ouputMessage = Print (outputMessage, "Powerball matches!")
        outputMessage = Print (outputMessage, "Matched {0} numbers".format(matches))
        outputMessage = Print (outputMessage, "Ticket {0}: won {1}\n".format(number + 1,
                                                                             prizes[powerballMatch][matches]))
    return outputMessage


def getNumbers(outputMessage):
    url = "https://data.ny.gov/api/views/d6yy-54nr/rows.json"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    jsonData = json.loads(r.data)
    numbers = jsonData['data']
    latestNumbers = numbers[-1:][0][9].split(' ')
    latestNumbers = [int(x) for x in latestNumbers]
    retVal = [ set(latestNumbers[:-1])]
    retVal.append(set(latestNumbers[-1:]))
    outputMessage = printEntry(outputMessage, "Current Numbers: {0} \t\tPowerball: {1}\n", retVal)

    return retVal, outputMessage

def main(json_data, context):
    currentNumbers, outputMessage = getNumbers(outputMessage = '')
    outputMessage = checkNumbers(currentNumbers, outputMessage)

    g = Gmail()
    g.setFrom('martin.cooley@gmail.com')
    g.addRecipient('martin.cooley@gmail.com')
    g.subject("Do you want to be a milli?")
    g.message(outputMessage)
    username = os.environ['username']
    appkey = os.environ["appkey"]
    g.setAuth(username, appkey)
    g.send()

