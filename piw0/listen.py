import requests
import time
import brewmodule
import control

serverip = "52.232.56.213"

control.actuator(0, True)
for i in range (1, 5):
    control.actuator(i, False)

r = requests.get("http://" + serverip + "/authenticate?code=FacebookLadyWeLoveYou")
print(r.json())



while True:
    print("Searching for requests")
    r = requests.get("http://" + serverip + "/dequeue")
    data = r.json()
    print(data)
    success = data['success']
    if success:
        temp = int(data['temp'])
        tyme = int(data['time'])
        mode = data['mode']
        if mode == "brew":
            brewmodule.brew(temp, tyme)
        elif mode == "rinse":
            brewmodule.rinse()

#    requests.get("http://" + serverip + "/dequeue")
    time.sleep(1)
