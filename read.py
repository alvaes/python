from os import system
from time import sleep

def printFile(data:str, strReplace:str, strNew:str):
    for i in data.replace(strReplace, strNew):
        print(i, end="", flush=True)
        sleep(0.08)

system("cls")

with open("data.txt", "r") as file:
    data = file.read()

if "writing" in data:
    printFile(data, "writing", "reading")
else:
    printFile(data,"","")

