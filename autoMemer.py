import requests
import time
import random
import ctypes
memes = ["f", "r", "i", "c", "k"]

ctypes.windll.kernel32.SetConsoleTitleW("AutoMemer - Running // By Adam 774")


def announceResume():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    jsonMsg["content"] = "```fix\n[+] Resuming at "+str(current_time)+"\n```"
    requests.post(url=url1, json=jsonMsg, headers=auth)
    

def announceDelay(d):
    jsonMsg["content"] = "```fix\n[-] Sleeping for "+str(d)+"s at "+time.strftime("%H:%M:%S", time.localtime())+"...\n```"
    requests.post(url=url1, json=jsonMsg, headers=auth)


def updateTitle(job):
    ctypes.windll.kernel32.SetConsoleTitleW("AutoMemer - Running // "+job+" // By Adam 774")


def plsFish():
    updateTitle("Running Commands (\"pls fish\")")
    jsonMsg["content"] = "pls fish"
    return requests.post(url=url1, json=jsonMsg, headers=auth)


def plsHunt():
    updateTitle("Running Commands (\"pls hunt\")")
    jsonMsg["content"] = "pls hunt"
    return requests.post(url=url1, json=jsonMsg, headers=auth)


def plsBeg():
    updateTitle("Running Commands (\"pls beg\")")
    jsonMsg["content"] = "pls beg"
    return requests.post(url=url1, json=jsonMsg, headers=auth)


def plsPM():
    updateTitle("Running Commands (\"pls pm\")")
    jsonMsg["content"] = "pls pm"
    a = requests.post(url=url1, json=jsonMsg, headers=auth)
    if a.status_code == 200:
        print("["+time.strftime("%H:%M:%S", time.localtime())+"] Success on sending", jsonMsg["content"])
        print("["+time.strftime("%H:%M:%S", time.localtime())+"] Adding 3s delay for bot catch-up...")
    time.sleep(3)
    jsonMsg["content"] = str(random.choice(memes))
    requests.post(url=url1, json=jsonMsg, headers=auth)
    return a


def checkPost(request1):
    if request1.status_code == 200:
        print("["+time.strftime("%H:%M:%S", time.localtime())+"] Success on sending", jsonMsg["content"])
    else:
        print(request1.headers)
        print(request1.content)


url1 = "https://discord.com/api/v8/channels/{Channel ID Here}/messages"
auth = {"Authorization": "Token Here"}
jsonMsg = {"content": ""}
jsonMsg["content"] = "```ini\n[Starting "+time.strftime("%H:%M:%S", time.localtime())+"]\n```"
requests.post(url=url1, json=jsonMsg, headers=auth)

while True:
    announceResume()
    checkPost(plsFish())
    checkPost(plsHunt())
    checkPost(plsBeg())
    checkPost(plsPM())
    delay = random.randint(60, 120)
    updateTitle("Waiting for "+str(delay)+" seconds")
    announceDelay(delay)
    print("["+time.strftime("%H:%M:%S", time.localtime())+"] Waiting "+str(delay)+"s")
    print("-"*120)
    time.sleep(delay)
