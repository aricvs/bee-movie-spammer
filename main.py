import sys
import os
import time
import pywhatkit


def get_script_lines():
    if hasattr(sys, "_MEIPASS"):
        script_path = os.path.join(sys._MEIPASS, "script.txt")
    else:
        script_path = "script.txt"

    with open(script_path, "r") as file:
        script = [line.strip() for line in file.readlines()]
    return script


def get_number():
    target_number = input(
        "WARNING: you will not be able to use your computer while this script runs\nHello BEEliever, type in the phone number that you want to target (don't forget to include the country code with the '+' sign): "
    )
    return target_number


def spam_lines(script: list, target_number: str):
    for line in script:
        time.sleep(2)
        pywhatkit.sendwhatmsg_instantly(
            phone_no=target_number, tab_close=True, message=line
        )


spam_lines(script=get_script_lines(), target_number=get_number())
