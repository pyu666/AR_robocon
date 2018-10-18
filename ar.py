# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2
import sys
import numpy
import TakeAR

aruco = cv2.aruco  # arucoライブラリ
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)


def arGenerator():
    for i in range(50):
        generator = aruco.drawMarker(dictionary, i, 100)
        cv2.imwrite(str(i) + '.png', generator)


def arReader():
    cap = cv2.VideoCapture(1)  # ビデオキャプチャの開始 (0なら1台目、1なら2台目)

    while True:
        ret, frame = cap.read()  # ビデオキャプチャから画像を取得

        Height, Width = frame.shape[:2]

        # sizeを半分に縮小
        halfHeight = int(Height / 2)
        halfWidth = int(Width / 2)
        imghalf = cv2.resize(frame, (halfWidth, halfHeight))

        ids: object
        corners, ids, rejectedImgPoints = aruco.detectMarkers(imghalf, dictionary)  # マーカを検出
        #print(ids)
        #print(corners)
        # print(numpy.argsort(corners,axis=-1,kind='quicksort',order=None))
        index = numpy.argsort(corners)
        #        print(numpy.array([[corners[0, index[0, :]]], corners[1, index[1, :]]]))
        aruco.drawDetectedMarkers(imghalf, corners, ids, (0, 255, 0))  # 検出したマーカに描画する

        cv2.imshow('drawDetectedMarkers', imghalf)  # マーカが描画された画像を表示

        keybord = cv2.waitKey(500)  # キーボード入力の受付
        if keybord == 65:  # 65 = "A"
            cv2.imwrite('out.png',frame)
            print("Take")
            TakeAR.chk('out.png')
    cap.release()  # ビデオキャプチャのメモリ解放
    cv2.destroyAllWindows()  # すべてのウィンドウを閉じる


if __name__ == '__main__':
    args = sys.argv
    ar = args[1]
    if ar == "Generator":
        arGenerator()
    elif ar == "Reader":
        arReader()
    else:
        print("Please enter valid argument")
