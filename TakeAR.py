import numpy as np
import cv2
import serial

aruco = cv2.aruco  # arucoライブラリ
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)


def chk(_png):
    img = cv2.imread(_png)  # ファイルを読み込み
    ids: object
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)  # マーカを検出
    # まさかの読み込み時に下から順になっていた。
    send_serial = ""
    if ids is not None:
        for k in reversed(ids): # 逆順に読み込むことで上から読み込む
            i = k[0]  # 配列からIDを読み込み
            # print (k)
            send_serial = send_serial + id_List(i)
        send_serial = send_serial + 'z'  # zは終了コマンド
        print(send_serial)
        ser = serial.Serial()  # ポートを開ける
        ser.port = "COM12"  # 各自ポート番号を変更
        ser.baurate = 9600
        ser.setDTR(False)  # DTRをセットしない(セットするとArduinoUNOが動かない)
        ser.open()
        ser.write(bytes(send_serial, 'UTF-8'))  # シリアル送信
        ser.close()  # 閉じる


def id_List(i):
    if i in {5}:
        # print("前に進む")
        return "A"  # Aは前に進む
    elif i in {10,6}:
        # print("右に90度曲がる")
        return "R"  # Rは右90度
    elif i in {15}:
        # print("左に90度曲がる")
        return "L"  # Lは左90度
    else:
        return ""


def name_List(i):
    if i in {"A"}:
        return "前に進む\n"  # Aは前に進む
    elif i in {"R"}:
        return "右に90度曲がる\n"  # Rは右90度
    elif i in {"L"}:
        return "左に90度曲がる\n"  # Lは左90度
    else:
        return ""


if __name__ == '__main__':
    png = "test.png"
    chk(png)
