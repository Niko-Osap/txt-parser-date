import json
import re
import datetime


rawText = open("text.txt", "r")

splitText = rawText.read().split("\n")



# active = True

# while active:
#     active = False
#     for index in range(len(splitText)):
#         print(index)
#         if splitText[index]=="":
#             active = True
#             print(splitText[index])
#             splitText.pop(index)
#             break
#         print(splitText)

emptyList = []

# lines start at 1, index at 0

for index in range(len(splitText)-1, -1, -1):
    if splitText[index] == "":
        emptyList.append(index)

for empty in emptyList:
    splitText.pop(empty)

print(splitText)

for index in range(len(splitText)):
    if re.match("^[0-9]{2}\.[0-9]{2}\.[0-9]{4}", splitText[index]):
        print(splitText[index][:10])
    elif re.match("^[0-9]{2}:[0-9]{2}\.", splitText[index]):
        print(splitText[index][:5])
    else:
        print("no date here")