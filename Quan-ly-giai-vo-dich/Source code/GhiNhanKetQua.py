import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from XuLy import *


class CauThuGhiBan:
    def __init__(self, master, dong, tendoinha, tendoikhach):
        self.tenCauThu = StringVar()
        self.tenDoi = StringVar()
        self.loaiBanThang = StringVar()
        self.thoiDiem = IntVar()
        self.master = master

        # STT
        Label(self.master, text=1 + dong).grid(row=1 + dong, column=0, padx=5, pady=5)

        # TÊN CẦU THỦ
        Entry(self.master, textvariable=self.tenCauThu).grid(row=1 + dong, column=1, padx=5, pady=5)

        # TÊN ĐỘI
        cb_cac_doi = ttk.Combobox(self.master, textvariable=self.tenDoi, state='readonly',
                                  value=[tendoinha, tendoikhach])
        cb_cac_doi.current(0)
        cb_cac_doi.grid(row=1 + dong, column=2, padx=5, pady=5)

        # LOẠI BÀN THẮNG
        cb_loai_ban_thang = ttk.Combobox(self.master, textvariable=self.loaiBanThang,
                                         value=get_cac_loai_ban_thang().split(','),
                                         state='readonly')
        cb_loai_ban_thang.current(0)
        cb_loai_ban_thang.grid(row=1 + dong, column=3, padx=5, pady=5)

        # THỜI ĐIỂM GHI BÀN
        Entry(self.master, textvariable=self.thoiDiem).grid(row=1 + dong, column=4, padx=5, pady=5)


class DanhSachCauThuGhiBan(Frame):
    def __init__(self, socauthughiban, master, sobanthangdoinha,
                 sobanthangdoikhach, vongduocchon, tendoinha, tendoikhach):  # socauthughiban = số dòng của bảng

        self.sobanthangdoinha = sobanthangdoinha
        self.sobanthangdoikhach = sobanthangdoikhach
        self.vongduocchon = vongduocchon
        self.tendoinha = tendoinha.get()
        self.tendoikhach = tendoikhach.get()
        self.id_doinha = get_id_doi(self.tendoinha)
        self.id_doikhach = get_id_doi(self.tendoikhach)

        self.master = master

        Frame.__init__(self, master)
        self.newFrame = Frame(master)
        self.newFrame.pack()

        # canvas
        self.canvas = Canvas(self.newFrame, borderwidth=0, width=610, background='steel blue')
        self.frame_DanhSachCauThu = Frame(self.canvas, background="steel blue")
        self.vsb = Scrollbar(self.newFrame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame_DanhSachCauThu, anchor="nw",
                                  tags="self.frame_DanhSachCauThu")
        self.frame_DanhSachCauThu.bind("<Configure>", self.onframeconfigure)
        # self.frame_DanhSachCauThu.pack()

        # Tạo headers của table
        self.LabelSTT = Label(self.frame_DanhSachCauThu, text='STT', bg='deep sky blue')
        self.LabelSTT.grid(row=0,
                           column=0,
                           padx=5,
                           pady=5)

        self.LabelCauThu = Label(self.frame_DanhSachCauThu, text='Cầu thủ', bg='deep sky blue')
        self.LabelCauThu.grid(row=0,
                              column=1,
                              padx=5,
                              pady=5)

        self.LabelDoi = Label(self.frame_DanhSachCauThu, text='Đội', bg='deep sky blue')
        self.LabelDoi.grid(row=0,
                           column=2,
                           padx=5,
                           pady=5)

        self.LabelLoaiBanThang = Label(self.frame_DanhSachCauThu, text='Loại bàn thắng', bg='deep sky blue')
        self.LabelLoaiBanThang.grid(row=0,
                                    column=3,
                                    padx=5,
                                    pady=5)
        self.LabelThoiDiem = Label(self.frame_DanhSachCauThu, text='Thời điểm', bg='deep sky blue').grid(row=0,
                                                                                                         column=4,
                                                                                                         padx=5,
                                                                                                         pady=5)
        # tao list cau thu
        self.list_cau_thu = []
        # add entries
        for dong in range(socauthughiban):
            self.list_cau_thu.append(CauThuGhiBan(self.frame_DanhSachCauThu, dong, self.tendoinha, self.tendoikhach))

        # BUTTON THÊM KẾT QUẢ
        self.ButtonFrame = Frame(master)
        self.ButtonFrame.pack(side='bottom')
        Button(self.ButtonFrame, text='Thêm kết quả', command=self.submit_cauthu_ghiban).pack()

    def onframeconfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def submit_cauthu_ghiban(self):
        import sqlite3

        conn = sqlite3.connect('GiaiVoDich.db')
        c = conn.cursor()

        # get id vong
        id_vong = get_id_vong(self.vongduocchon)

        # get id tran
        id_tran = get_id_tran_dau(self.id_doinha, self.id_doikhach, id_vong)

        # update tỉ số
        try:
            c.execute(
                "UPDATE trandau SET doinhathang=(?), doikhachthang=(?) WHERE idvong=(?) AND iddoinha=(?) AND iddoikhach=(?)",
                (
                    self.sobanthangdoinha.get(), self.sobanthangdoikhach.get(), id_vong, self.id_doinha,
                    self.id_doikhach,))
        except TclError:
            messagebox.showerror('Lỗi', 'Tỉ số phải là số nguyên!')
            return

        # update danh sách cầu thủ ghi bàn
        for cauthu in self.list_cau_thu:
            # flag thông tin hợp lệ
            thong_tin_hop_le = True

            # get entry thông tin của 1 cầu thủ
            name = cauthu.tenCauThu.get()
            loaibanthang = cauthu.loaiBanThang.get()
            try:
                thoidiem = cauthu.thoiDiem.get()
            except TclError:
                messagebox.showerror('Lỗi', 'Thời điểm ghi bàn phải là số nguyên!')
                conn.rollback()
                return

            doi = cauthu.tenDoi.get()

            # get điều kiện hợp lệ
            danh_sach_cau_thu_hop_le = get_danh_sach_cau_thu(doi)
            thoi_diem_ghi_ban_toi_da = get_thoi_diem_ghi_ban_toi_da()

            # kiểm tra điều kiện
            if name not in danh_sach_cau_thu_hop_le:
                thong_tin_hop_le = False
                tkinter.messagebox.showerror('Lỗi', 'Cầu thủ ' + name + ' không có trong đội ' + doi)
                conn.rollback()
                return

            if thoidiem > thoi_diem_ghi_ban_toi_da:
                thong_tin_hop_le = False
                tkinter.messagebox.showerror('Lỗi', 'Thời điểm ghi bàn tối đa là ' + str(thoi_diem_ghi_ban_toi_da))
                conn.rollback()
                return

            if thong_tin_hop_le is True:
                # get mã cầu thủ
                id_cauthu = get_id_cau_thu(name)

                # thêm cầu thủ ghi bàn vào bảng bàn thắng(danh sách cầu thủ ghi bàn)
                c.execute("INSERT INTO banthang(idcauthu,idtrandau,loaibanthang,thoidiem) VALUES (?,?,?,?)",
                          (id_cauthu, id_tran, loaibanthang, thoidiem,))

                # update điểm và hiệu số của 2 đội
                ########################################################################################################
                # get điểm hiện tại của đội nhà
                diemdoinha = c.execute("SELECT diem FROM doibong WHERE ten=(?)", (self.tendoinha,)).fetchone()[0]

                # get điểm hiện tại của đội khách
                diemdoikhach = c.execute("SELECT diem FROM doibong WHERE ten=(?)", (self.tendoikhach,)).fetchone()[0]

                # get hiệu số hiện tại của đội nhà
                hieusodoinha = c.execute("SELECT hieuso FROM doibong WHERE ten=(?)", (self.tendoinha,)).fetchone()[0]

                # get hiệu số hiện tại của đội khách
                hieusodoikhach = c.execute("SELECT hieuSo FROM doibong WHERE ten=(?)", (self.tendoikhach,)).fetchone()[
                    0]

                if self.sobanthangdoinha.get() > self.sobanthangdoikhach.get():  # đội nhà thắng
                    # điểm mới
                    diemdoinha += get_diem_khi_thang()
                    diemdoikhach += get_diem_khi_thua()

                    # hiệu số mới
                    hieusodoinha += (self.sobanthangdoinha.get() - self.sobanthangdoikhach.get())
                    hieusodoikhach -= (self.sobanthangdoinha.get() - self.sobanthangdoikhach.get())

                    # get tổng số bàn thắng hiện tại của đội nhà
                    tongsobanthangdoinha = \
                        c.execute("SELECT thang FROM doibong WHERE ten=(?)", (self.tendoinha,)).fetchone()[0]

                    # get tổng số bàn thua hiện tại của đội khách
                    tongsobanthuadoikhach = \
                        c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (self.tendoikhach,)).fetchone()[0]

                    # giá trị mới cho số bàn thắng,thua của đội nhà và đội khách
                    tongsobanthangdoinha += 1
                    tongsobanthuadoikhach += 1

                    # cập nhật điểm,số bàn thắng và hiệu số đội nhà
                    c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thang=(?) WHERE ten=(?)",
                              (diemdoinha, hieusodoinha, tongsobanthangdoinha, self.tendoinha,))

                    # cập nhật điểm,số bàn thua và hiệu số đội khách
                    c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thua=(?) WHERE ten=(?)",
                              (diemdoikhach, hieusodoikhach, tongsobanthuadoikhach, self.tendoikhach,))

                elif self.sobanthangdoikhach.get() > self.sobanthangdoinha.get():  # đội khách thắng
                    # điểm mới
                    diemdoikhach += get_diem_khi_thang()
                    diemdoinha += get_diem_khi_thua()

                    # hiệu số mới
                    hieusomoi_doikhach = hieusodoikhach + (self.sobanthangdoikhach.get() - self.sobanthangdoinha.get())
                    hieusomoi_doinha = hieusodoinha - (self.sobanthangdoikhach.get() - self.sobanthangdoinha.get())

                    # get tổng số bàn thua hiện tại của đội nhà
                    tongsobanthuadoinha = \
                        c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (self.tendoinha,)).fetchone()[0]

                    # get tổng số bàn thắng hiện tại của đội khách
                    tongsobanthangdoikhach = \
                        c.execute("SELECT thang FROM doibong WHERE ten=(?)", (self.tendoikhach,)).fetchone()[0]

                    # giá trị mới cho số bàn thắng thua của đội khách,đội nhà
                    tongsobanthangdoikhach += 1
                    tongsobanthuadoinha += 1

                    # cập nhật điểm,số bàn thắng và hiệu số đội khách
                    c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thang=(?) WHERE ten=(?)",
                              (diemdoikhach, hieusomoi_doikhach, tongsobanthangdoikhach, self.tendoikhach,))

                    # cập nhật điểm,số bàn thua và hiệu số đội nhà
                    c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thua=(?) WHERE ten=(?)",
                              (diemdoinha, hieusomoi_doinha, tongsobanthuadoinha, self.tendoinha,))

                else:  # hòa

                    diemdoikhach += get_diem_khi_hoa()
                    diemdoinha += get_diem_khi_hoa()

                    # get tổng số bàn hòa hiện tại của đội nhà
                    tongsobanhoadoinha = \
                        c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (self.tendoinha,)).fetchone()[
                            0]

                    # get tổng số bàn hòa hiện tại của đội khách
                    tongsobanhoadoikhach = \
                        c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (self.tendoikhach,)).fetchone()[0]

                    tongsobanhoadoikhach += 1
                    tongsobanhoadoinha += 1

                    c.execute("UPDATE doibong SET diem=(?),hoa=(?) WHERE ten=(?)",
                              (diemdoinha, tongsobanhoadoinha, self.tendoinha,))
                    c.execute("UPDATE doibong SET diem=(?),hoa=(?) WHERE ten=(?)",
                              (diemdoikhach, tongsobanhoadoikhach, self.tendoikhach,))
                ########################################################################################################

        # commit
        conn.commit()
        # Thông báo thành công
        tkinter.messagebox.showinfo('Thành công', 'Thêm cầu thủ thành công')
        # thoát chương trình
        self.master.destroy()


class App:
    def __init__(self, master):
        self.master = master
        self.master.title = 'Ghi nhận kết quả'
        self.frame = Frame(self.master)
        self.frame.pack()

        # label chọn vòng
        self.LabelChonVong = Label(self.frame, text='Chọn lượt đấu:')
        self.LabelChonVong.grid(row=0, column=0, padx=5)

        # combobox số vòng
        self.SoVongVar = IntVar()
        self.ComboboxSoVong = ttk.Combobox(self.frame, textvariable=self.SoVongVar, state='readonly')
        self.ComboboxSoVong['values'] = get_list_so_vong()

        try:
            self.ComboboxSoVong.current(0)
        except TclError:
            messagebox.showerror('Lỗi', 'Không có lượt đấu nào trong cơ sở dữ liệu!')
            self.master.destroy()

        self.ComboboxSoVong.grid(row=0, column=1, padx=5)

        # button chọn vòng
        self.ButtonChonVong = Button(self.frame, text='Chọn lượt',
                                     command=self.cap_nhat_cac_cap_dau)  # cập nhật value mỗi khi được bấm
        self.ButtonChonVong.grid(row=0, column=2, padx=5)

        # label chọn cặp đấu
        self.LabelChonCapDau = Label(self.frame, text='Chọn cặp đấu:')
        self.LabelChonCapDau.grid(row=1, column=0, padx=5)

        # combobox chọn cặp đấu
        self.CapDauVar = StringVar()
        self.ComboboxCapDau = ttk.Combobox(self.frame, textvariable=self.CapDauVar, state='readonly')
        self.ComboboxCapDau.grid(row=1, column=1, padx=5)

        # label số cầu thủ ghi bàn
        self.LabelSoCauThuGhiBan = Label(self.frame, text='Số cầu thủ ghi bàn:')
        self.LabelSoCauThuGhiBan.grid(row=2, column=0, padx=5)

        # input số cầu ghủ ghi bàn
        self.InputSoCauThuGhiBan = Entry(self.frame)
        self.InputSoCauThuGhiBan.grid(row=2, column=1, padx=5)

        # button cập nhật số cầu thủ ghi bàn
        self.ButtonCapNhatSoCauThuGhiBan = Button(self.frame, text='Cập nhật', command=self.taodanhsachcauthughiban)
        self.ButtonCapNhatSoCauThuGhiBan.grid(row=2, column=2, padx=5)

        ################################################################################################################
        # FLAG: khi nhấn nút cập nhật từ lần thứ 2,sẽ check và xóa frame hiện tại,sau đó tạo frame mới
        self.FLAG = None

    def cap_nhat_cac_cap_dau(self):
        # get value của combobox ComboboxSoVong
        self.vongduocchon = self.SoVongVar.get()

        self.ComboboxCapDau['values'] = get_cac_cap_dau(self.vongduocchon)
        self.ComboboxCapDau.current(0)

    def taodanhsachcauthughiban(self):
        # '''kiểm tra giá trị hiện tại của combobox chọn vòng
        #  có hợp lệ với giá trị hiện tại của combobox chọn cặp đấu hay không'''
        vong = self.SoVongVar.get()
        caccapdau = get_cac_cap_dau(vong)
        valueComboboxChonCapDau = self.CapDauVar.get()

        if caccapdau[0] == 'Không có cặp đấu nào':
            tkinter.messagebox.showerror('Lỗi', 'Vòng này không có cặp đấu nào.')

        elif valueComboboxChonCapDau not in caccapdau:
            tkinter.messagebox.showerror('Lỗi',
                                         'Vui lòng chọn lại vòng và cặp đấu.\n(Bạn có quên nhất nút "Chọn vòng" không?)')

        else:
            # BẢNG NHẬP TỈ SỐ

            # tạo title bảng nhập tỉ số
            Label(self.frame, text='Bảng tỉ số:', font=("Helvetica", 16)).grid(row=3, column=0)

            # set kiểu dữ liệu
            self.TenDoiChuNha = StringVar()
            self.TenDoiKhach = StringVar()
            self.NgayGio = StringVar()
            self.TenSan = StringVar()
            self.SoBanThangDoiNha = IntVar()
            self.SoBanThangDoiKhach = IntVar()

            # get dữ liệu
            self.TenDoiChuNha.set(self.CapDauVar.get().split('-')[0])
            self.TenDoiKhach.set(self.CapDauVar.get().split('-')[1])
            self.NgayGio.set(
                get_ngaygio_bang_ti_so(self.TenDoiChuNha.get(), self.TenDoiKhach.get(),
                                       self.vongduocchon))

            self.TenSan.set(get_san_doi_chu_nha(self.TenDoiChuNha.get()))
            id_vong = get_id_vong(self.SoVongVar.get())
            id_doinha = get_id_doi(self.TenDoiChuNha.get())
            id_doikhach = get_id_doi(self.TenDoiKhach.get())

            ###
            self.SoBanThangDoiNha.set(get_so_ban_thang_doi_nha_trong_tran_dau(id_doinha, id_doikhach, id_vong))
            self.SoBanThangDoiKhach.set(get_so_ban_thang_doi_khach_trong_tran_dau(id_doinha, id_doikhach, id_vong))
            ###

            # tạo headers của bảng nhập tỉ số
            self.LabelDoiChuNha = Label(self.frame, text='Đội chủ nhà', bg='light sky blue').grid(row=4, column=0,
                                                                                                  padx=5)
            self.LabelDoiKhach = Label(self.frame, text='Đội khách', bg='light sky blue').grid(row=4, column=1, padx=5)
            self.LabelSoBanThangDoiNha = Label(self.frame, text='Số bàn thắng của đội nhà', bg='light sky blue').grid(
                row=4,
                column=2,
                padx=5)
            self.LabelSoBanThangDoiKhach = Label(self.frame, text='Số bàn thắng của đội khách',
                                                 bg='light sky blue').grid(row=4,
                                                                           column=3,
                                                                           padx=5)
            self.LabelNgayGio = Label(self.frame, text='Ngày Giờ', bg='light sky blue').grid(row=4, column=4, padx=5)
            self.LabelSan = Label(self.frame, text='Sân', bg='light sky blue').grid(row=4, column=5, padx=5)

            # tạo entries của bảng nhập tỉ số
            self.EntryDoiChuNha = Entry(self.frame, state='disabled', textvariable=self.TenDoiChuNha)
            self.EntryDoiChuNha.grid(row=5, column=0, padx=5)

            self.EntryDoiKhach = Entry(self.frame, state='disabled', textvariable=self.TenDoiKhach)
            self.EntryDoiKhach.grid(row=5, column=1, padx=5)

            self.EntrySoBanThangDoiNha = Entry(self.frame, textvariable=self.SoBanThangDoiNha)
            self.EntrySoBanThangDoiNha.grid(row=5, column=2, padx=5)

            self.EntrySoBanThangDoiKhach = Entry(self.frame, textvariable=self.SoBanThangDoiKhach)
            self.EntrySoBanThangDoiKhach.grid(row=5, column=3, padx=5)

            self.EntryNgayGio = Entry(self.frame, state='disabled', textvariable=self.NgayGio)
            self.EntryNgayGio.grid(row=5, column=4, padx=5)

            self.EntrySan = Entry(self.frame, state='disabled', textvariable=self.TenSan)
            self.EntrySan.grid(row=5, column=5, padx=5)

            ############################################################################################################
            # BẢNG DANH SÁCH CẦU THỦ GHI BÀN

            # tạo title bảng danh sách cầu thủ ghi bàn
            Label(self.frame, text='Danh sách cầu thủ ghi bàn:', font=("Helvetica", 16)).grid(row=6, column=0)

            # Get giá trị để truyền vào DanhSachCauThuGhiBan()
            try:
                self.SoCauThuGhiBan = int(self.InputSoCauThuGhiBan.get())
            except ValueError:
                messagebox.showerror('Lỗi', 'Số cầu thủ ghi bàn phải là số nguyên!')

            # TẠO CÁC ENTRIES
            # check FLAG
            if hasattr(self.FLAG, 'newFrame') and hasattr(self.FLAG, 'ButtonFrame'):
                self.FLAG.ButtonFrame.destroy()
                self.FLAG.newFrame.destroy()

                self.FLAG = DanhSachCauThuGhiBan(self.SoCauThuGhiBan, self.master, self.SoBanThangDoiNha,
                                                 self.SoBanThangDoiKhach, self.vongduocchon, self.TenDoiChuNha,
                                                 self.TenDoiKhach)
            else:

                self.FLAG = DanhSachCauThuGhiBan(self.SoCauThuGhiBan, self.master, self.SoBanThangDoiNha,
                                                 self.SoBanThangDoiKhach, self.vongduocchon, self.TenDoiChuNha,
                                                 self.TenDoiKhach)


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
