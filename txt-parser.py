import json
import re
import datetime


def convDateString(dateLine: str):
    dateLine = dateLine.strip("[]")
    return dateLine[0:2] + "/" + dateLine[3:5] + "/" + dateLine[6:10]



splitText = ""

with open("text.txt", "r") as rawText:

    splitText = rawText.read().split("\n")


emptyList = []

# lines start at 1, index at 0

for index in range(len(splitText)-1, -1, -1):
    if splitText[index] == "":
        emptyList.append(index)

for empty in emptyList:
    splitText.pop(empty)

# print(splitText)

dateDict = {}

for index in range(len(splitText)):
    if re.match("^\[[0-9]{2}[\.\/][0-9]{2}[\.\/][0-9]{4}\]", splitText[index]):
        tempDate = convDateString(splitText[index])
        dateDict[tempDate] = {}
    elif re.match("^[0-9]{2}:[0-9]{2}\.", splitText[index]):
        try:
            # takes previous line to check for a date to insert the current line's time into
            tempDate = convDateString(splitText[index-1])
            dateDict[tempDate][splitText[index][:5]] = splitText[index][7:]
        except IndexError:
            print(f"ERROR: Index out of bounds, line {index}")
        except:
            reverseIndexCount = 2
            while True:
                try:
                    # checks for date in prev lines
                    if re.match("^\[[0-9]{2}[\.\/][0-9]{2}[\.\/][0-9]{4}\]", splitText[index-reverseIndexCount]):
                        # takes date from that line and inserts time (timeStamp) and associated text (timeText) into date dictionary of found date
                        timeStamp = splitText[index][:5]
                        timeText = splitText[index][7:]
                        # clean and standardize date into "12/34/5678"
                        tempDate = convDateString(splitText[index-reverseIndexCount])
                        dateDict[tempDate][timeStamp] = timeText
                        break
                    reverseIndexCount+=1
                except IndexError:
                    print(f"ERROR: Index out of bounds, line {index}")
                    break
                except:
                    print(f"Unknown Error between line {index} and {index-reverseIndexCount}")
                    break
                if reverseIndexCount >= 100:
                    print(f"ERROR: too many lines parsed caused by improper formatting of date. Start of issue {index}")
                    break

    else:
        continue
        # print("no date here")

dateJson = json.dumps(dateDict)

print(dateJson)

with open("text.json", "w") as jsonFile:

    jsonFile.write(dateJson)

