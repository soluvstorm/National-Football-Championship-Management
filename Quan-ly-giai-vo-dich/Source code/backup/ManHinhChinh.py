import sqlite3
from tkinter import *
from tkinter import messagebox

import GhiNhanKetQua
import LapBaoCaoGiai
import LapLichThiDau
import ThayDoiQuyDinh
import TiepNhanHoSoThiDau
import XuLy


class App1:
    def __init__(self, master):
        self.background_image = PhotoImage(file='bongda.gif')
        Label(master, image=self.background_image).place(x=0, y=0, relwidth=1, relheight=1)
        self._ghinhanketqua = None
        self._laplichthidau = None

        Button(master, text='Tiếp nhận hồ sơ đăng ký', bg='medium spring green', width=20,
               command=self.tiepnhanhosothidau).grid(row=0,
                                                     column=0,
                                                     padx=30,
                                                     pady=5)

        Button(master, text='Tra cứu cầu thủ', bg='medium spring green', width=20).grid(row=0,
                                                                                        column=1,
                                                                                        padx=30,
                                                                                        pady=5)

        Button(master, text='Lập lịch thi đấu', bg='medium spring green', width=20,
               command=self.LapLichThiDau).grid(
            row=1,
            column=0,
            padx=30,
            pady=5)

        Button(master, text='Lập báo cáo giải', bg='medium spring green', width=20, command=self.LapBaoCaoGiai).grid(
            row=1,
            column=1,
            padx=30,
            pady=5)

        Button(master, text='Ghi nhận kết quả trận đấu', bg='medium spring green', width=20,
               command=self.GhiNhanKetQua).grid(row=2,
                                                column=0,
                                                padx=30,
                                                pady=5)

        Button(master, text='Thay đổi quy định', bg='medium spring green', width=20,
               command=self.ThayDoiQuyDinh).grid(
            row=2,
            column=1,
            padx=30,
            pady=5)

    def GhiNhanKetQua(self):
        self._ghinhanketqua = Toplevel()
        GhiNhanKetQua.App(self._ghinhanketqua)

    def LapLichThiDau(self):

        if XuLy.get_so_doi() % 2 == 0:
            self._laplichthidau = Toplevel()
            self.Cap_Nhat_Vong_Dau()
            LapLichThiDau.LapLichThiDau(self._laplichthidau)
        else:
            messagebox.showerror("Lỗi", "Số đội bóng hiện tại là số lẻ!")

    def ThayDoiQuyDinh(self):
        self._thaydoiquydinh = Toplevel()
        ThayDoiQuyDinh.App(self._thaydoiquydinh)

    def tiepnhanhosothidau(self):
        self._tiepnhanhosothidau = Toplevel()
        TiepNhanHoSoThiDau.TiepNhanHoSoThiDau(self._tiepnhanhosothidau)

    def LapBaoCaoGiai(self):
        self._lapbaocaogiai = Toplevel()
        LapBaoCaoGiai.App(self._lapbaocaogiai)

    def Cap_Nhat_Vong_Dau(self):
        conn = sqlite3.connect("GiaiVoDich.db")
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS vongdau")
        c.execute("CREATE TABLE vongdau (id INTEGER PRIMARY KEY AUTOINCREMENT, luotdau INTEGER NOT NULL)")
        for i in range((XuLy.get_so_doi() - 1) * 2):
            c.execute("INSERT INTO vongdau(luotdau) VALUES (?)", (i + 1,))

        conn.commit()
        conn.close()


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x600")
    root.resizable(width=False, height=False)
    root.title("Phần mềm quản lý giải vô địch bóng đá quốc gia")

    app = App1(root)
    root.mainloop()
