import sqlite3
from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import XuLy


class Footballers:
    def __init__(self, master, stt):
        self.master = master

        # tạo header
        if (stt == 1):
            ttk.Label(self.master, text="STT").grid(row=0, column=0, padx=5, pady=5)
            ttk.Label(self.master, text="Tên").grid(row=0, column=1, padx=5, pady=5)
            ttk.Label(self.master, text="Ngày sinh").grid(row=0, column=2, padx=5, pady=5)
            ttk.Label(self.master, text="Tháng sinh").grid(row=0, column=3, padx=5, pady=5)
            ttk.Label(self.master, text="Năm sinh").grid(row=0, column=4, padx=5, pady=5)
            ttk.Label(self.master, text="Loại").grid(row=0, column=5, padx=5, pady=5)
            ttk.Label(self.master, text="Ghi chú").grid(row=0, column=6, padx=5, pady=5)

        # tạo thông tin của 1 dòng
        # STT
        ttk.Label(self.master, text=stt).grid(row=stt, column=0, padx=5, pady=5)

        # TÊN CẦU THỦ
        self.name = StringVar()
        ttk.Entry(self.master, width=24, textvariable=self.name).grid(row=stt, column=1, padx=5, pady=5)

        # NGÀY SINH
        self.dob_day = StringVar()
        cb_day = ttk.Combobox(self.master, value=XuLy.get_so_ngay_trong_1_thang(), textvariable=self.dob_day, width=2,
                              state='readonly')
        cb_day.grid(row=stt, column=2, padx=5, pady=5)
        cb_day.current(0)

        # THÁNG SINH
        self.dob_month = StringVar()
        cb_month = ttk.Combobox(self.master, value=XuLy.get_so_thang_trong_1_nam(), textvariable=self.dob_month,
                                width=2, state='readonly')
        cb_month.grid(row=stt, column=3, padx=5, pady=5)
        cb_month.current(0)

        # NĂM SINH
        self.dob_year = StringVar()

        year_value = []
        for i in range(1990, date.today().year):
            year_value.append(i)
        cb_year = ttk.Combobox(self.master, value=year_value, textvariable=self.dob_year, width=4, state='readonly')
        cb_year.grid(row=stt, column=4, padx=5, pady=5)
        cb_year.current(0)

        # LOẠI CẦU THỦ
        loai_values = ('trong nước', 'ngoài nước')
        self.loaiCauThu = StringVar()
        cb_loaiCauThu = ttk.Combobox(self.master, value=loai_values, textvariable=self.loaiCauThu, width=12,
                                     state='readonly')
        cb_loaiCauThu.grid(row=stt, column=5, padx=5, pady=5)
        cb_loaiCauThu.current(0)

        ttk.Entry(self.master, width=24).grid(row=stt, column=6, padx=5, pady=5)


class ListFootballers(Frame):
    def __init__(self, master, n_footballers, name, stadium):
        Frame.__init__(self, master)

        # Ten va SVD cua doi bong
        self.footballName = name
        self.footballStadium = stadium
        ###################################

        self.conn = None

        # sqlite3.connect("QL_VDBDQG.db")
        self.master = master
        self.newFrame = Frame(master)
        self.newFrame.pack()

        self.canvas = Canvas(self.newFrame, borderwidth=0, background="#ffffff", width=900)
        self.frame_footballers = Frame(self.canvas)
        self.vsb = Scrollbar(self.newFrame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame_footballers, anchor="nw",
                                  tags="self.frame_footballers")
        self.frame_footballers.bind("<Configure>", self.onFrameConfigure)

        self.n_footballers = int(n_footballers.get())

        self.dictfootballer = []
        for i in range(self.n_footballers):
            self.dictfootballer.append(Footballers(self.frame_footballers, i + 1))

        self.buttonFrame = Frame(master)
        self.buttonFrame.pack(side='bottom')
        ttk.Button(self.buttonFrame, text='Submit', command=self.submit_footballer).pack()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def submit_footballer(self):

        self.conn = sqlite3.connect("GiaiVoDich.db")
        football_name = self.footballName.get()
        football_stadium = self.footballStadium.get()

        c1 = self.conn.cursor()
        c1.execute("INSERT INTO doibong (ten, san) VALUES (?, ?)", (football_name, football_stadium,))
        self.conn.commit()
        id_doibong = XuLy.get_id_doi(football_name)

        # # cap nhat lai bang vong dau
        # c1.execute("DROP TABLE IF EXISTS vongdau")
        # c1.execute("CREATE TABLE vongdau (id INTEGER PRIMARY KEY AUTOINCREMENT, luotdau INTEGER NOT NULL)")

        ########################################

        for footballer in self.dictfootballer:
            name = footballer.name.get()
            dob = footballer.dob_year.get() + '-' + footballer.dob_month.get() + '-' + footballer.dob_day.get()
            loai = footballer.loaiCauThu.get()
            c2 = self.conn.cursor()
            c2.execute("INSERT INTO cauthu (ten, ngaysinh,loai, iddoi) VALUES (?, ?,?, ?)",
                       (name, dob, loai, id_doibong,))

        self.conn.commit()
        self.conn.close()

        messagebox.showinfo("Thành công", "Thông tin hồ sơ được lưu thành công.")
        self.master.destroy()


class TiepNhanHoSoThiDau:
    def __init__(self, master):
        # create header frame
        self.master = master

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        # creata header label
        ttk.Label(self.frame_header, text="NHẬP HỒ SƠ ĐỘI BÓNG", font=('Arial', 18, 'bold')).pack()

        # create content frame
        self.frame_content = ttk.Frame(self.master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text="Tên đội:").grid(column=0, row=0, padx=5, pady=5)
        ttk.Label(self.frame_content, text="Tên sân:").grid(column=0, row=1, padx=5, pady=5)

        self.footballName = StringVar()
        self.footballStadium = StringVar()

        self.entry_footballName = ttk.Entry(self.frame_content, width=24, textvariable=self.footballName)
        self.entry_footballStadium = ttk.Entry(self.frame_content, width=24, textvariable=self.footballStadium)

        self.entry_footballName.grid(row=0, column=1, padx=5, pady=5)
        self.entry_footballStadium.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_content, text="Số cầu thủ: ").grid(row=2, column=0)

        self.n_footballers = StringVar()
        soLuongCauThu = []
        for i in range(XuLy.get_so_cau_thu_toi_thieu(), XuLy.get_so_cau_thu_toi_da()):
            soLuongCauThu.append(i)

        self.cb_soLuongCauThu = ttk.Combobox(self.frame_content, value=soLuongCauThu, state='readonly',
                                             textvariable=self.n_footballers)
        self.cb_soLuongCauThu.grid(row=2, column=1, padx=5, pady=5)
        self.cb_soLuongCauThu.current(0)

        ttk.Button(self.frame_content, text='OK', command=self.create_listGUI_footballers).grid(row=3, column=0,
                                                                                                columnspan=2)
        self.listGUI_footballers = None

    def create_listGUI_footballers(self):
        if (self.footballName.get() == '' or self.footballStadium.get() == ''):
            messagebox.showerror(title='Lỗi', message=('Bạn chưa nhập tên đội hoặc tên sân!'))

        if self.footballName.get().isalpha():

            if self.footballStadium.get().isalpha():

                if hasattr(self.listGUI_footballers, 'newFrame') and hasattr(self.listGUI_footballers, 'buttonFrame'):
                    self.listGUI_footballers.buttonFrame.destroy()
                    self.listGUI_footballers.newFrame.destroy()
                    self.listGUI_footballers = ListFootballers(self.master, self.n_footballers, self.footballName,
                                                               self.footballStadium)

                else:
                    self.listGUI_footballers = ListFootballers(self.master, self.n_footballers, self.footballName,
                                                               self.footballStadium)
            else:
                messagebox.showerror('Lỗi',
                                     'Tên sân phải bao gồm những kí tự trong bảng chữ cái và phải được để không dấu.')

        else:
            messagebox.showerror('Lỗi',
                                 'Tên đội phải bao gồm những kí tự trong bảng chữ cái và phải được để không dấu.')


def main():
    root = Tk()
    TiepNhanHoSoThiDau(root)  # TiepNhanHoSoThiDau.__init__(tiepnhanhoso, root)
    root.title("Tiếp nhận hồ sơ thi đấu")
    root.mainloop()


if __name__ == "__main__":
    main()
