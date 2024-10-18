from os import system
import time

system("cls")

for i in "Hello World!":
    print(i, end="", flush=True)
    time.sleep(0.08)

print()

with open("data.txt", "w") as file:
    data = input("Type a text to save it in a file: ")
    file.write(data)
