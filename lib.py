from random import randint
from time import sleep

def approximateValue(value):
    lowerValue = value - 0.1 * value
    higherValue = value + 0.1 * value
    return randint(lowerValue, higherValue)


def goodbye(goodbye):
    print(10 * "\n")
    for i in goodbye:
        sleep(0.00001)
        print(i, end="")
    for i in range(3):
        sleep(1)
        print("\n")


bye = f"""
   _____                    _  _                   _ 
  / ____|                  | || |                 | |
 | |  __   ___    ___    __| || |__   _   _   ___ | |
 | | |_ | / _ \  / _ \  / _` || '_ \ | | | | / _ \| |
 | |__| || (_) || (_) || (_| || |_) || |_| ||  __/|_|
  \_____| \___/  \___/  \__,_||_.__/  \__, | \___|(_)
                                       __/ |         
                                      |___/ """