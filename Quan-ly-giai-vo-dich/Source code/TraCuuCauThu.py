import sqlite3
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from XuLy import *

conn = sqlite3.connect('GiaiVoDich.db')


class Player:
    def __init__(self, master, stt, name, tendoi, loai, tongsobanthang):
        # có tham số là master
        self.master = master
        # có frameplayers là thuộc tính được gán vào self.master
        self.frame_Players = ttk.Frame(self.master)
        self.frame_Players.pack()

        self.stt = stt
        self.name = name
        self.tendoi = tendoi
        self.loai = loai
        self.tongsobanthang = tongsobanthang
        # nếu value == 1
        if self.stt == 1:
            Label(self.frame_Players, text="STT", bg='medium spring green').grid(row=0, column=0, padx=3)

            Label(self.frame_Players, text="Tên Cầu thủ", bg='medium spring green').grid(row=0, column=1, padx=3)

            Label(self.frame_Players, text="Tên Đội", bg='medium spring green').grid(row=0, column=2, padx=3)

            Label(self.frame_Players, text="Loại cầu thủ", bg='medium spring green').grid(row=0, column=3, padx=3)

            Label(self.frame_Players, text="Tổng số bàn thắng", bg='medium spring green').grid(row=0, column=4, padx=3)

        ################################### số thứ tự
        Label(self.frame_Players, text=self.stt, width=20, bg='light sky blue').grid(row=stt, column=0, sticky=W)

        ################################### cầu thủ
        Label(self.frame_Players, text=self.name, width=20, bg='light sky blue').grid(row=stt, column=1, sticky=W)
        #
        Label(self.frame_Players, text=self.tendoi, width=20, bg='light sky blue').grid(row=stt, column=2, sticky=W)
        ################################### Loại cầu thủ
        Label(self.frame_Players, text=self.loai, width=20, bg='light sky blue').grid(row=stt, column=3, sticky=W)
        ################################### Tổng số bàn thắng
        Label(self.frame_Players, text=self.tongsobanthang, width=20, bg='light sky blue').grid(row=stt, column=4,
                                                                                                sticky=W)


class ListPlayers:
    def __init__(self, master, value, tukhoa):
        self.master = master
        self.newFrame = Frame(self.master, background="brown")
        self.newFrame.pack()
        self.canvas = Canvas(self.newFrame, borderwidth=1, background="#ffffff", width=720)
        self.frame_Players = Frame(self.canvas)

        self.vsb = Scrollbar(self.newFrame, orient="vertical", command=self.canvas.yview)
        self.vsb1 = Scrollbar(self.newFrame, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.vsb1.set)
        self.vsb.pack(side="right", fill="y")
        self.vsb1.pack(side="bottom", fill="x")

        self.canvas.pack(side="left")
        self.canvas.create_window((4, 4), window=self.frame_Players, anchor="nw", tags="self.frame_Players")

        self.frame_Players.bind("<Configure>", self.onFrameConfigure)

        # truyền giá trị Radiobutton và từ khóa
        self.value = value
        self.tukhoa = tukhoa
        self.value_player = self.value
        self.tukhoa_player = self.tukhoa

        listplayer = []

        if (value == 1):  # tên cầu thủ
            clistplayers1 = conn.cursor()
            clistplayers1.execute(
                'SELECT cauthu.ten,doibong.ten,cauthu.loai,cauthu.id FROM cauthu,doibong WHERE cauthu.iddoi = doibong.id AND cauthu.ten = (?)',
                (tukhoa,))
            listcauthu1 = clistplayers1.fetchall()
            soluongcauthu1 = len(listcauthu1)
            thongtincantim1 = listcauthu1
            # lấy id từ user ra
            idcauthu1 = int(thongtincantim1[0][3])
            # rút hết tất cả các id để so sánh
            ctongbanthang1 = conn.cursor()
            ctongbanthang1.execute('SELECT idcauthu FROM banthang ')
            listtongbanthang1 = ctongbanthang1.fetchall()
            soluongid1 = len(listtongbanthang1)

            count1 = 0

            for i in range(soluongid1):
                if (idcauthu1 == listtongbanthang1[i][0]):
                    count1 = count1 + 1

            for i in range(soluongcauthu1):
                self.stt = i + 1
                self.name = thongtincantim1[i][0]
                self.tendoi = thongtincantim1[i][1]
                self.loai = thongtincantim1[i][2]
                listplayer.append(Player(self.frame_Players, self.stt, self.name, self.tendoi, self.loai, count1))



        elif (value == 2):  # tên đội bóng
            clistplayers2 = conn.cursor()
            clistplayers2.execute(
                'SELECT cauthu.ten,doibong.ten,cauthu.loai FROM doibong,cauthu WHERE  doibong.id = cauthu.iddoi AND doibong.ten = (?)',
                (tukhoa,))
            listcauthu2 = clistplayers2.fetchall()
            soluongcauthu2 = len(listcauthu2)
            thongtincantim2 = listcauthu2

            holder2 = 0
            for i in range(soluongcauthu2):
                holder2 = holder2 + 1
                self.stt = holder2
                self.name = thongtincantim2[i][0]
                self.tendoi = thongtincantim2[i][1]
                self.loai = thongtincantim2[i][2]
                self.tongsobanthang = get_tong_so_ban_thang_cua_cau_thu(get_id_cau_thu(thongtincantim2[i][0]))
                listplayer.append(
                    Player(self.frame_Players, self.stt, self.name, self.tendoi, self.loai, self.tongsobanthang))




        elif (value == 3):  # Loai cau thu

            clistplayers3 = conn.cursor()
            clistplayers3.execute(
                'SELECT cauthu.ten,doibong.ten,cauthu.loai FROM doibong,cauthu WHERE  doibong.id = cauthu.iddoi  AND cauthu.loai = (?)',
                (tukhoa,))
            listcauthu3 = clistplayers3.fetchall()
            soluongcauthu3 = len(listcauthu3)
            thongtincantim3 = listcauthu3
            # print(soluongcauthu3)
            # print(thongtincantim3)
            holder3 = 0
            for i in range(soluongcauthu3):
                if (self.tukhoa == thongtincantim3[i][2]):
                    holder3 = holder3 + 1
                    self.stt = holder3
                    self.name = thongtincantim3[i][0]
                    self.tendoi = thongtincantim3[i][1]
                    self.loai = thongtincantim3[i][2]
                    self.tongsobanthang = get_tong_so_ban_thang_cua_cau_thu(get_id_cau_thu(thongtincantim3[i][0]))
                    listplayer.append(
                        Player(self.frame_Players, self.stt, self.name, self.tendoi, self.loai, self.tongsobanthang))



        elif (value == 4):  # tổng số bàn thắng của một cầu thủ
            # lấy thông tin của 3 trường

            if (int(self.tukhoa) == 0):
                # id của 3 cầu thủ ghi bàn
                clistcauthughiban4 = conn.cursor()
                clistcauthughiban4.execute('SELECT DISTINCT idcauthu FROM banthang ')
                listcauthughiban4 = clistcauthughiban4.fetchall()
                soluonglistcauthughiban4 = len(listcauthughiban4)
                thongtinlistcauthughiban4 = listcauthughiban4

                # id của tất cả các cầu thủ
                clist4 = conn.cursor()
                clist4.execute('SELECT DISTINCT cauthu.id FROM cauthu')
                list4 = clist4.fetchall()
                soluonglist4 = len(list4)
                thongtinsoluonglist4 = list4

                listcauthughiban = []
                for i in range(soluonglistcauthughiban4):
                    listcauthughiban.append(thongtinlistcauthughiban4[i][0])

                listcauthukhongghiban = []
                for i in range(soluonglist4):
                    listcauthukhongghiban.append(thongtinsoluonglist4[i][0])

                holder = 0
                for i in listcauthukhongghiban:
                    clistplayers4 = conn.cursor()
                    clistplayers4.execute(
                        'SELECT cauthu.ten,doibong.ten,cauthu.loai FROM doibong,cauthu WHERE  doibong.id = cauthu.iddoi AND cauthu.id = (?) ',
                        (i,))
                    thongtin_tsbt_bang0 = clistplayers4.fetchone()
                    holder = holder + 1
                    self.stt = holder
                    self.name = thongtin_tsbt_bang0[0]
                    self.tendoi = thongtin_tsbt_bang0[1]
                    self.loai = thongtin_tsbt_bang0[2]
                    self.tongsobanthang = 0
                    listplayer.append(
                        Player(self.frame_Players, self.stt, self.name, self.tendoi, self.loai, self.tongsobanthang))








            else:
                clistplayers4 = conn.cursor()
                clistplayers4.execute(
                    'SELECT cauthu.ten,doibong.ten,cauthu.loai,count(*) FROM cauthu,doibong,banthang  WHERE cauthu.id = banthang.idcauthu AND cauthu.iddoi = doibong.id GROUP BY banthang.idcauthu ')
                listcauthu4 = clistplayers4.fetchall()
                soluongcauthu4 = len(listcauthu4)
                thongtincantim4 = listcauthu4

                holder = 0
                for i in range(soluongcauthu4):

                    if (int(self.tukhoa) == thongtincantim4[i][3]):
                        holder = holder + 1
                        self.stt = holder
                        self.name = thongtincantim4[i][0]
                        self.tendoi = thongtincantim4[i][1]
                        self.loai = thongtincantim4[i][2]
                        self.tongsobanthang = thongtincantim4[i][3]
                        listplayer.append(Player(self.frame_Players, self.stt, self.name, self.tendoi, self.loai,
                                                 self.tongsobanthang))

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


class TraCuuCauThu:
    def __init__(self, master):
        self.master = master

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text="TRA CỨU CẦU THỦ", font=('Arial', 18, 'bold')).pack(pady=15)

        self.frame_content = ttk.Frame(self.master)
        self.frame_content.pack()

        self.entrytext = StringVar()
        ttk.Label(self.frame_content, text="Từ Khóa: ").grid(row=0, column=0, sticky=W)
        ttk.Entry(self.frame_content, width=30, textvariable=self.entrytext).grid(row=0, column=1)

        ttk.Label(self.frame_content, text="Tra Cứu Theo:  ").grid(row=1, column=0)

        self.key_search = IntVar()
        Radiobutton(self.frame_content, text="Tên cầu thủ", variable=self.key_search, value=1).grid(row=2, column=1,
                                                                                                    sticky=W)
        Radiobutton(self.frame_content, text="Tên đội của cầu thủ", variable=self.key_search, value=2).grid(row=3,
                                                                                                            column=1,
                                                                                                            sticky=W)
        Radiobutton(self.frame_content, text="Loại cầu thủ", variable=self.key_search, value=3).grid(row=4, column=1,
                                                                                                     sticky=W)
        Radiobutton(self.frame_content, text="Tổng số bàn thắng", variable=self.key_search, value=4).grid(row=5,
                                                                                                          column=1,
                                                                                                          sticky=W)

        ttk.Button(self.frame_content, text="Bắt Đầu Tra Cứu", command=self.create_listGUI_ListPlayers).grid(row=6,
                                                                                                             column=1)

        self.listGUI_ListPlayers = None

    def create_listGUI_ListPlayers(self):
        self.value = self.key_search.get()
        self.tukhoa = self.entrytext.get()

        messbox2 = conn.cursor()
        messbox2.execute(
            'SELECT cauthu.ten,doibong.ten,cauthu.loai FROM cauthu,doibong WHERE cauthu.iddoi = doibong.id AND doibong.ten = (?)',
            (self.tukhoa,))
        listcauthumessbox2 = messbox2.fetchall()
        soluongcauthumessbox2 = len(listcauthumessbox2)
        thongtincantimmessbox2 = listcauthumessbox2

        messbox3 = conn.cursor()
        messbox3.execute(
            'SELECT cauthu.ten,doibong.ten,cauthu.loai FROM cauthu,doibong WHERE cauthu.iddoi = doibong.id AND cauthu.loai = (?)',
            (self.tukhoa,))
        listcauthumessbox3 = messbox3.fetchall()
        soluongcauthumessbox3 = len(listcauthumessbox3)
        thongtincantimmessbox3 = listcauthumessbox3

        if (self.value == 1):
            # cái này nó lấy tên cầu thủ
            messbox1 = conn.cursor()
            messbox1.execute(
                'SELECT cauthu.ten,doibong.ten,cauthu.loai FROM cauthu,doibong WHERE cauthu.iddoi = doibong.id AND cauthu.ten = (?)',
                (self.tukhoa,))
            listcauthumessbox1 = messbox1.fetchall()
            soluongcauthumessbox1 = len(listcauthumessbox1)
            thongtincantimmessbox1 = listcauthumessbox1

            if (soluongcauthumessbox1 == 0):
                tkinter.messagebox.showerror('Lỗi',
                                             ' Cầu thủ ' + self.tukhoa + ' không có trong cơ sở dữ liệu, vui lòng nhập lại ')
            else:
                if hasattr(self.listGUI_ListPlayers, 'newFrame') and hasattr(self.listGUI_ListPlayers, 'frame_Players'):
                    self.listGUI_ListPlayers.newFrame.destroy()
                    self.listGUI_ListPlayers.frame_Players.destroy()
                    self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)
                else:
                    self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)

        if (self.value == 2):
            if (soluongcauthumessbox2 == 0):
                tkinter.messagebox.showerror('Lỗi',
                                             ' Đội bóng ' + self.tukhoa + ' không có trong cơ sở dữ liệu, vui lòng nhập lại ')
            else:
                if hasattr(self.listGUI_ListPlayers, 'newFrame') and hasattr(self.listGUI_ListPlayers, 'frame_Players'):
                    self.listGUI_ListPlayers.newFrame.destroy()
                    self.listGUI_ListPlayers.frame_Players.destroy()
                    self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)
                else:
                    self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)

        if (self.value == 3):
            if (soluongcauthumessbox3 == 0):
                tkinter.messagebox.showerror('Lỗi',
                                             ' Loại ' + self.tukhoa + ' không có trong cơ sở dữ liệu, vui lòng nhập lại chính xác "trong nuoc" hoặc "ngoai nuoc"')
            else:
                if hasattr(self.listGUI_ListPlayers, 'newFrame') and hasattr(self.listGUI_ListPlayers, 'frame_Players'):
                    self.listGUI_ListPlayers.newFrame.destroy()
                    self.listGUI_ListPlayers.frame_Players.destroy()
                    self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)
                else:
                    self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)

        if (self.value == 4):
            messbox4 = conn.cursor()
            messbox4.execute(
                'SELECT count(*) FROM cauthu,doibong,banthang  WHERE cauthu.id = banthang.idcauthu AND cauthu.iddoi = doibong.id GROUP BY banthang.idcauthu')
            listcauthumessbox4 = messbox4.fetchall()
            soluongcauthumessbox4 = len(listcauthumessbox4)
            thongtincantimmessbox4 = listcauthumessbox4
            if hasattr(self.listGUI_ListPlayers, 'newFrame') and hasattr(self.listGUI_ListPlayers, 'frame_Players'):
                self.listGUI_ListPlayers.newFrame.destroy()
                self.listGUI_ListPlayers.frame_Players.destroy()
                self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)
            else:
                self.listGUI_ListPlayers = ListPlayers(self.master, self.value, self.tukhoa)


def main():
    root = Tk()
    root.title("Tra Cuu Cau Thu")
    root.minsize(150, 150)
    TraCuuCauThu(root)

    root.mainloop()


if __name__ == "__main__":
    main()
