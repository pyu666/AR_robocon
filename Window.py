import tkinter
import cv2
#import sys
import numpy
import TakeAR
import PIL.Image, PIL.ImageTk
#  pip install pillow

aruco = cv2.aruco  # arucoライブラリ
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)


class App:
    def __init__(self, window, window_title, video_source=1):
        self.var = tkinter.StringVar()
        #self.var.set("")
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source  # カメラを起動　上の引数で指定
        self.vid = MyVideoCapture(self.video_source)
#        image = self.vid.get_frame()[1]
#        img = PIL.Image.fromarray(image)
#        img = window.PhotoImage(img)
        self.canvas = tkinter.Canvas(window, width=self.vid.width+100, height=self.vid.height)
        self.canvas.pack()  # ここでカメラのウインドウサイズと同じ大きさのウインドウを作る
        self.btn_snapshot = tkinter.Button(window, text="ロボットを動かす", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        self.label1 = tkinter.Label(self.window, textvariable=self.var)
        self.label1.place(x=self.vid.width, y=0)
        #self.label1 = tkinter.Label(window, text=App.block)
        #self.label1.place(x=self.vid.width, y=0)
#        self.label1.pack(anchor=tkinter.NE)
        # 15msでアップデート
        self.delay = 20
        self.update()
        self.window.mainloop()
        # window = root　たぶん。

    def snapshot(self):  # ボタンが押されたときに動作する
        ret, frame = self.vid.get_frame()  # キャプチャ
        if ret:
            cv2.imwrite('out.png',frame), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            print("Robot moving Start!")
            TakeAR.chk('out.png')

    # def update(self):
    #     # Get a frame from the video source
    #     ret, frame = self.vid.get_frame()
    #     if ret:
    #         self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    #         self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
    #     self.window.after(self.delay, self.update)

    def update(self):
        # Get a frame from the video source
        ret, frame,texts = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
            #self.label1 = tkinter.Label(self.window, text=texts)
            #self.label1.place(x=self.vid.width, y=0)
            print(texts)
            self.var.set(texts)
            #self.label1.configure(self.window, text=self.var)
        self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=1):
        self.vid = cv2.VideoCapture(video_source)  # openCVでカメラ起動
        cap.set(3, 1280)
        cap.set(4, 1024)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

     # def get_frame(self):  # フレーム取得
     #    if self.vid.isOpened():
     #        ret, frame = self.vid.read()
     #        if ret:
     #            ids: object
     #            corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, dictionary)  # マーカを検出
     #            index = numpy.argsort(corners)
     #            aruco.drawDetectedMarkers(frame, corners, ids, (0, 255, 0))  # 検出したマーカに描画する
     #            # cv2.imshow('drawDetectedMarkers', frame)  # マーカが描画された画像を表示
     #            if ids is not None:
     #                for k in reversed(ids):  # 逆順に読み込むことで上から読み込む
     #                    i = k[0]  # 配列からIDを読み込み
     #                    # self.block = self.block + TakeAR.id_List(i)
     #                    App.block = App.block + TakeAR.name_List(TakeAR.id_List(i))
     #            print(App.block)
     #            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
     #        else:
     #            return (ret, None)
     #    else:
     #        return (ret, None)

    def get_frame(self):  # フレーム取得
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                ids: object
                corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, dictionary)  # マーカを検出
                index = numpy.argsort(corners)
                aruco.drawDetectedMarkers(frame, corners, ids, (0, 255, 0))  # 検出したマーカに描画する
                # cv2.imshow('drawDetectedMarkers', frame)  # マーカが描画された画像を表示
                text = ""
                if ids is not None:
                    for k in reversed(ids):  # 逆順に読み込むことで上から読み込む
                        i = k[0]  # 配列からIDを読み込み
                        # self.block = self.block + TakeAR.id_List(i)
                        #print(i)
                        text = text + TakeAR.name_List(TakeAR.id_List(i))
                else:
                    text = ""
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),text)

            else:
                return (ret, None,None)
        else:
            return (ret, None,None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release() #ビデオキャプチャ　リリース


App(tkinter.Tk(), "AR_ROBOT")