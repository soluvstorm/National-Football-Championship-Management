from tkinter import *

import XuLy


class App(Frame):
    def __init__(self, root):
        self.root = root
        Frame.__init__(self, self.root)
        self.frame = Frame(self.root)
        self.frame.pack()

        # canvas
        self.canvas = Canvas(self.frame, borderwidth=0, width=900, background='steel blue')
        self.frame_LapBaoCaoGiai = Frame(self.canvas, background="steel blue")
        self.vsb = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame_LapBaoCaoGiai, anchor="nw",
                                  tags="self.frame_LapBaoCaoGiai")
        self.frame_LapBaoCaoGiai.bind("<Configure>", self.onframeconfigure)

        # headers của table
        # STT
        self.lb_STT = Label(self.frame_LapBaoCaoGiai, text='STT', bg='deep sky blue')
        self.lb_STT.grid(row=0, column=0, padx=5, pady=5)
        # TÊN ĐỘI
        self.lb_Doi = Label(self.frame_LapBaoCaoGiai, text='Đội', bg='deep sky blue')
        self.lb_Doi.grid(row=0, column=1, padx=5, pady=5)
        # SỐ BÀN THẮNG
        self.lb_Thang = Label(self.frame_LapBaoCaoGiai, text='Thắng', bg='deep sky blue')
        self.lb_Thang.grid(row=0, column=2, padx=5, pady=5)
        # SỐ BÀN THUA
        self.lb_Thua = Label(self.frame_LapBaoCaoGiai, text='Thua', bg='deep sky blue')
        self.lb_Thua.grid(row=0, column=3, padx=5, pady=5)
        # SỐ BÀN HÒA
        self.lb_Hoa = Label(self.frame_LapBaoCaoGiai, text='Hòa', bg='deep sky blue')
        self.lb_Hoa.grid(row=0, column=4, padx=5, pady=5)
        # TỔNG ĐIỂM
        self.lb_Diem = Label(self.frame_LapBaoCaoGiai, text='Điểm', bg='deep sky blue')
        self.lb_Diem.grid(row=0, column=5, padx=5, pady=5)
        # HIỆU SỐ
        self.lb_HieuSo = Label(self.frame_LapBaoCaoGiai, text='Hiệu số', bg='deep sky blue')
        self.lb_HieuSo.grid(row=0, column=6, padx=5, pady=5)
        # HẠNG
        self.lb_Hang = Label(self.frame_LapBaoCaoGiai, text='Hạng', bg='deep sky blue')
        self.lb_Hang.grid(row=0, column=7, padx=5, pady=5)

        # số đội = số dòng trong bảng
        self.soDong = XuLy.get_so_doi()

        # trả về list các tuple với format mỗi tuple là:
        # (tên đội, số bàn thắng, số bàn thua, số bàn hòa, tổng điểm, hiệu số)
        self.data = XuLy.xep_hang()

        # đổ data vào table
        for dong in range(self.soDong):
            self.them_dong(self.data[dong][0], self.data[dong][1], self.data[dong][2], self.data[dong][3],
                           self.data[dong][4], self.data[dong][5], dong)

    def them_dong(self, tenDoi, soBanThang, soBanThua, soBanHoa, tongDiem, hieuSo, soDongHienTai):
        Label(self.frame_LapBaoCaoGiai, text=soDongHienTai + 1).grid(row=soDongHienTai + 1, column=0, padx=5, pady=5)

        tenDoi_var = StringVar()
        tenDoi_var.set(tenDoi)
        Entry(self.frame_LapBaoCaoGiai, textvariable=tenDoi_var, state='readonly').grid(row=soDongHienTai + 1, column=1,
                                                                                        padx=5,
                                                                                        pady=5)
        soBanThang_var = StringVar()
        soBanThang_var.set(str(soBanThang))
        Entry(self.frame_LapBaoCaoGiai, textvariable=soBanThang_var, state='readonly').grid(row=soDongHienTai + 1,
                                                                                            column=2, padx=5,
                                                                                            pady=5)

        soBanThua_var = StringVar()
        soBanThua_var.set(str(soBanThua))
        Entry(self.frame_LapBaoCaoGiai, textvariable=soBanThua_var, state='readonly').grid(row=soDongHienTai + 1,
                                                                                           column=3, padx=5,
                                                                                           pady=5)

        soBanHoa_var = StringVar()
        soBanHoa_var.set(str(soBanHoa))
        Entry(self.frame_LapBaoCaoGiai, textvariable=soBanHoa_var, state='readonly').grid(row=soDongHienTai + 1,
                                                                                          column=4, padx=5,
                                                                                          pady=5)

        tongDiem_var = StringVar()
        tongDiem_var.set(str(tongDiem))
        Entry(self.frame_LapBaoCaoGiai, textvariable=tongDiem_var, state='readonly').grid(row=soDongHienTai + 1,
                                                                                          column=5, padx=5,
                                                                                          pady=5)

        hieuSo_var = StringVar()
        hieuSo_var.set(str(hieuSo))
        Entry(self.frame_LapBaoCaoGiai, textvariable=hieuSo_var, state='readonly').grid(row=soDongHienTai + 1, column=6,
                                                                                        padx=5,
                                                                                        pady=5)

        Label(self.frame_LapBaoCaoGiai, text=soDongHienTai + 1).grid(row=soDongHienTai + 1, column=7, padx=5, pady=5)

    def onframeconfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == '__main__':
    root = Tk()
    App(root)
    root.mainloop()
