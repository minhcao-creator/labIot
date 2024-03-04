import serial.tools.list_ports


def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    # return commPort
    return "/dev/pts/5"


if getPort() != None:
    ser = serial.Serial(getPort(), baudrate=115200)
    print(ser)


def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("cambien1", splitData[2])


mess = ""


def readSerial(client):
    if ser.isOpen():
        # print('haha')
        bytesToRead = ser.inWaiting()
        if (bytesToRead > 0):
            global mess
            mess = mess + ser.read(bytesToRead).decode("UTF-8")
            print(mess)
            while ("#" in mess):
                end = mess.find("#")
                processData(client, mess[0:end + 1])
                if (end == len(mess)):
                    mess = ""
                else:
                    mess = mess[end+1:]
    else:
        print('huhu')
