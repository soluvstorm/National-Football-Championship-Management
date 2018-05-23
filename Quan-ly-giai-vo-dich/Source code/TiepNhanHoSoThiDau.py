import sqlite3
import string
from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re

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
        loai_values = ('trong nuoc', 'ngoai nuoc')
        self.loaiCauThu = StringVar()
        cb_loaiCauThu = ttk.Combobox(self.master, value=loai_values, textvariable=self.loaiCauThu, width=12,
                                     state='readonly')
        cb_loaiCauThu.grid(row=stt, column=5, padx=5, pady=5)
        cb_loaiCauThu.current(0)

        self.ghichu = StringVar()
        ttk.Entry(self.master, width=24, textvariable=self.ghichu).grid(row=stt, column=6, padx=5, pady=5)


class ListFootballers(Frame):
    def __init__(self, master, n_footballers, name, stadium):
        Frame.__init__(self, master)

        # Ten va SVD cua doi bong
        self.footballName = name
        self.footballStadium = stadium
        ###################################

        # sqlite3.connect("QL_VDBDQG.db")
        self.master = master
        self.newFrame = Frame(master)
        self.newFrame.pack()

        self.canvas = Canvas(self.newFrame, borderwidth=0, background="#ffffff", width=670)
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

        # Lấy tên và SVĐ của đội bóng
        football_name = self.footballName.get()
        football_stadium = self.footballStadium.get()


        list_footballerNames = [] # Danh sách các tên cầu thủ cần kiểm tra
        list_footballerYears = [] # Dãy số để kiểm tra tuổi cầu thủ có vượt tuổi tối đa hay thấp hơn tuổi tối thiểu hay không
        list_footballerDOB = [] # Danh sách tuổi các cầu thủ
        list_footballerType = [] # Danh sách loại các cầu thủ

        for footballer in self.dictfootballer:
            list_footballerNames.append(footballer.name.get())
            dob = footballer.dob_year.get() + '-' + footballer.dob_month.get() + '-' + footballer.dob_day.get()
            # Nếu (XuLy.get_so_tuoi_cau_thu(dob) - XuLy.get_tuoi_toi_thieu())*(XuLy.get_tuoi_toi_da() - XuLy.get_so_tuoi_cau_thu(dob)) > 0 ===> Tuổi hợp lệ
            list_footballerYears.append((XuLy.get_so_tuoi_cau_thu(dob) - XuLy.get_tuoi_toi_thieu())*(XuLy.get_tuoi_toi_da() - XuLy.get_so_tuoi_cau_thu(dob)))
            list_footballerType.append(footballer.loaiCauThu.get())
            list_footballerDOB.append(footballer.dob_year.get() + '-' + footballer.dob_month.get() + '-' + footballer.dob_day.get())

        message_error = ""

        # Kiểm tra tên và tuổi cầu thủ có hợp lệ hay không
        for i in range(len(self.dictfootballer)):
            ngayhople = 1
            try:
                date(int(self.dictfootballer[i].dob_year.get()), int(self.dictfootballer[i].dob_month.get()), int(self.dictfootballer[i].dob_day.get()))
            except ValueError:
                ngayhople = 0
            if (list_footballerNames[i] != "" and list_footballerYears[i] > 0 and (re.match("^[A-Za-z]*$", list_footballerNames[i])) and ngayhople):
                continue
            else:
                message_error = message_error + str(i+1) + ", "

        if (len(message_error) > 0):
            final_message_error = "Cầu thủ số " + message_error + "vi phạm một trong những quy định: " +"\nTên chỉ bao gồm ký tự) \nNgày sinh phải là ngày hợp lệ \nTuổi cầu thủ không được thấp hơn tuổi tối thiểu và cao hơn tuổi tối đa"
            messagebox.showerror("Lỗi", final_message_error)
            return
        # Nếu không có cầu thủ nào lỗi, ghi vào CSDL
        else:
            self.conn = sqlite3.connect("GiaiVoDich.db")
            c1 = self.conn.cursor()
            c1.execute("INSERT INTO doibong (ten, san) VALUES (?, ?)", (football_name, football_stadium,))
            self.conn.commit()
            id_doibong = XuLy.get_id_doi(football_name)

            for i in range(len(self.dictfootballer)):
                c1.execute("INSERT INTO cauthu (ten, ngaysinh, loai, ghichu, iddoi) VALUES (?, ?, ?, ?, ?)",
                           (list_footballerNames[i], list_footballerDOB[i], list_footballerType[i], self.dictfootballer[i].ghichu.get(), id_doibong,))
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
            return

        for char in self.footballName.get():
            if char not in string.ascii_uppercase + string.ascii_lowercase + ' ':
                messagebox.showerror('Lỗi',
                                     'Tên đội phải bao gồm những kí tự trong bảng chữ cái và phải được để không dấu.')
                return

        for char in self.footballStadium.get():
            if char not in string.ascii_uppercase + string.ascii_lowercase + string.digits + ' ':
                messagebox.showerror('Lỗi',
                                     'Tên sân phải bao gồm số hoặc những kí tự trong bảng chữ cái và phải được để không dấu.')
                return
        if hasattr(self.listGUI_footballers, 'newFrame') and hasattr(self.listGUI_footballers, 'buttonFrame'):
            self.listGUI_footballers.buttonFrame.destroy()
            self.listGUI_footballers.newFrame.destroy()
            self.listGUI_footballers = ListFootballers(self.master, self.n_footballers, self.footballName,
                                                       self.footballStadium)

        else:
            self.listGUI_footballers = ListFootballers(self.master, self.n_footballers, self.footballName,
                                                       self.footballStadium)


def main():
    root = Tk()
    TiepNhanHoSoThiDau(root)  # TiepNhanHoSoThiDau.__init__(tiepnhanhoso, root)
    root.title("Tiếp nhận hồ sơ thi đấu")
    root.mainloop()


if __name__ == "__main__":
    main()
