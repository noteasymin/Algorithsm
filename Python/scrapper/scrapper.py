import requests
import os

def check_url():
    checkurl = input().split(",")
    

    for i in range(len(checkurl)):
        for j in range(len(checkurl)):
            if "http://" in checkurl[j]:
                checkurl[j] = checkurl[j].replace(" ","")

            else:
                checkurl[j] = "http://" + checkurl[j].replace(" ","")
        try:
            url = requests.get(checkurl[i])
            print(checkurl[i] + " is up!")
        except:
            print(checkurl[i] + " is down..")

def restart():
    while True:
        print("Do you want to start over? (y/n)")
        answer = input()

        if answer == "y":
            break
        elif answer == "n":
            exit()
        else:
            print("That's not a vaild answer")
            continue

while True:
    check_url()
    restart()