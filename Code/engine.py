import eel
import pymysql as pm
#from gpiozero import Relay, Switch

import Server1003 as sv


sc = sv.Emysql()
onlineStatus = sc.connect("35.240.152.59",3306,"pi","raspberry","electro_db")

"""relay1 = Relay(10)
relay2 = Relay(11)
switch1 = Switch(9)"""


eel.init("web")
eel.start("main.html", block=False, size=(480, 8000))



@eel.expose
def queryLocalBarcode(localBarcodeNum):
    """barcodeNum = barcodeNum + " barcode number returned"
    print(barcodeNum)
    return barcodeNum"""

    timeFile = open("timeDatabase.txt", "r")
    f1 = timeFile.readlines()
    for lines in f1:
        line = lines.split(" ")
        if line[0] == localBarcodeNum:
            setTime(line[1] + " " + line[2])
            return lastTime

@eel.expose
def queryWebBarcode(webBarcodeNum):
    """get time      from server"""
    if sc.is_serial_data_sql(int(webBarcodeNum)):
        getData = sc.get_data_serial(int(webBarcodeNum))
        if getData[4] == None:
            setTime(str(str(getData[2])+" "+str(getData[3])))
            return lastTime
        else:
            return str(getData[1])+" "+str(getData[2])+" "+str(getData[3])+" "+str(getData[4])
    else:
        return False

@eel.expose
def setTime(num1):
    global lastTime
    lastTime = num1

@eel.expose
def getTime():
    return lastTime

@eel.expose
def switch(param):
    """turn on or off relays here"""

@eel.expose
def checkIfOnline():
    if onlineStatus == True:
        #return 1 if online
        return "1"
    elif onlineStatus == False:
        #return 0 if offline
        return "0"

'''https://jsfiddle.net/Daniel_Hug/pvk6p/'''

"""
@eel.expose
def door(param):
    # read door pin
    # 0 is closed
    # 1 is open
    """



while True:
    eel.sleep(10)

