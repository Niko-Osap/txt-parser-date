import json
import re
import datetime


rawText = open("text.txt", "r")

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
    if re.match("^[0-9]{2}\.[0-9]{2}\.[0-9]{4}", splitText[index]):
        tempDate = splitText[index]
        dateDict[tempDate] = {}
    elif re.match("^[0-9]{2}:[0-9]{2}\.", splitText[index]):
        try:
            # takes previous line to check for a date to insert the current line's time into
            dateDict[splitText[index-1][:10]][splitText[index][:5]] = splitText[index][6:]
        except IndexError:
            print(f"ERROR: Index out of bounds, line {index}")
        except:
            reverseIndexCount = 2
            while True:
                try:
                    if re.match("^[0-9]{2}\.[0-9]{2}\.[0-9]{4}", splitText[index-reverseIndexCount]):
                        dateDict[splitText[index-reverseIndexCount][:10]][splitText[index][:5]] = splitText[index][6:]
                        break
                    reverseIndexCount+=1
                except IndexError:
                    print(f"ERROR: Index out of bounds, line {index}")
                    break
                except:
                    print(f"Unknown Error between line {index} and {index-reverseIndexCount}")
                    break
                if reverseIndexCount >= 100:
                    print(f"ERROR: too many lines parsed caused by inproper formatting of date. Start of issue {index}")
                    break

    else:
        continue
        # print("no date here")

dateJson = json.dumps(dateDict)

print(dateJson)
