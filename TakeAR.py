import numpy as np
import cv2
import serial

aruco = cv2.aruco  # arucoライブラリ
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
def chk(png):
    img = cv2.imread(png)
    ids: object
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)  # マーカを検出
    #print(ids)
    # まさかの読み込み時に下から順になっていた。
    sendSerial = ""
    if ids is not None:
        for k in reversed(ids):
            i = k[0]
            # print (k)
            if i in {5,0}:
                print("前に進む")
                sendSerial = sendSerial + "A"
            elif i in {10,12}:
                print("右に90度曲がる")
                sendSerial = sendSerial + "R"
            elif i in {15,1}:
                print("左に90度曲がる")
                sendSerial = sendSerial + "L"
            else:
                None
        sendSerial = sendSerial + 'z'
        print(sendSerial)
    #sendSerial(str(sendSerial))
#def sendSerial(str):
        ser = serial.Serial("COM10", 9600)
        ser.write(bytes(sendSerial,'UTF-8'))
        ser.close()
    #print(corners)
    # point_y_list =[]
    # for i in range(0,ids.shape[0]):
    #     point_y = corners[i][0][0][1]
    #     id = ids[0][i]
    #     point_y_list.append([point_y])
    #     print(id + point_y)
if __name__ == '__main__':
    png = ("out.png")
    chk(png)
