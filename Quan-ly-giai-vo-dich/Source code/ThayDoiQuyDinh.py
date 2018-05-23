from tkinter import *
from tkinter import ttk

import XuLy


class App():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.pack()

        # TUỔI TỐI THIỂU CỦA CẦU THỦ
        # label
        self.lbTuoiToiThieu = Label(self.frame, text='Tuổi tối thiểu của cầu thủ:')
        self.lbTuoiToiThieu.grid(column=0, row=0, padx=5, pady=5)
        # Entry
        self.TuoiToiThieu = StringVar()
        self.TuoiToiThieu.set(XuLy.get_tuoi_toi_thieu())
        self.entryTuoiToiThieu = Entry(self.frame, textvariable=self.TuoiToiThieu)
        self.entryTuoiToiThieu.grid(column=1, row=0, padx=5, pady=5)
        # Button
        self.btn_TuoiToiThieu = Button(self.frame, text='Cập nhật', bg='sky blue',
                                       command=self.cap_nhat_tuoi_toi_thieu).grid(column=2,
                                                                                  row=0,
                                                                                  padx=5,
                                                                                  pady=5)

        # TUỔI TỐI ĐA CỦA CẦU THỦ
        # label
        self.lbTuoiToiDa = Label(self.frame, text='Tuổi tối đa của cầu thủ:')
        self.lbTuoiToiDa.grid(column=0, row=1, padx=5, pady=5)
        # Entry
        self.TuoiToiDa = StringVar()
        self.TuoiToiDa.set(XuLy.get_tuoi_toi_da())
        self.entryTuoiToiDa = Entry(self.frame, textvariable=self.TuoiToiDa)
        self.entryTuoiToiDa.grid(column=1, row=1, padx=5, pady=5)
        # Button
        self.btn_TuoiToiDa = Button(self.frame, text='Cập nhật', bg='sky blue', command=self.cap_nhat_tuoi_toi_da).grid(
            column=2, row=1, padx=5, pady=5)

        # SỐ LƯỢNG CẦU THỦ TỐI THIỂU
        # label
        self.lbSoLuongCauThuToiThieu = Label(self.frame, text='Số lượng cầu thủ tối thiểu:')
        self.lbSoLuongCauThuToiThieu.grid(column=0, row=2, padx=5, pady=5)
        # Entry
        self.SoLuongCauThuToiThieu = StringVar()
        self.SoLuongCauThuToiThieu.set(XuLy.get_so_cau_thu_toi_thieu())
        self.entrySoLuongCauThuToiThieu = Entry(self.frame, textvariable=self.SoLuongCauThuToiThieu)
        self.entrySoLuongCauThuToiThieu.grid(column=1, row=2, padx=5, pady=5)
        # Button
        self.btn_SoLuongCauThuToiThieu = Button(self.frame, text='Cập nhật', bg='sky blue',
                                                command=self.cap_nhat_so_luong_cau_thu_toi_thieu).grid(column=2, row=2,
                                                                                                       padx=5, pady=5)

        # SỐ LƯỢNG CẦU THỦ TỐI ĐA
        # label
        self.lbSoLuongCauThuToiDa = Label(self.frame, text='Số lượng cầu thủ tối đa:')
        self.lbSoLuongCauThuToiDa.grid(column=0, row=3, padx=5, pady=5)
        # Entry
        self.SoLuongCauThuToiDa = StringVar()
        self.SoLuongCauThuToiDa.set(XuLy.get_so_cau_thu_toi_da())
        self.entrySoLuongCauThuToiDa = Entry(self.frame, textvariable=self.SoLuongCauThuToiDa)
        self.entrySoLuongCauThuToiDa.grid(column=1, row=3, padx=5, pady=5)
        # Button
        self.btn_SoLuongCauThuToiDa = Button(self.frame, text='Cập nhật', bg='sky blue',
                                             command=self.cap_nhat_so_luong_cau_thu_toi_da).grid(column=2, row=3,
                                                                                                 padx=5, pady=5)

        # SỐ LƯỢNG CẦU THỦ NƯỚC NGOÀI TỐI ĐA
        # label
        self.lbSoLuongCauThuNuocNgoaiToiDa = Label(self.frame, text='Số lượng cầu thủ nước ngoài tối đa:')
        self.lbSoLuongCauThuNuocNgoaiToiDa.grid(column=0, row=4, padx=5, pady=5)
        # Entry
        self.SoLuongCauThuNuocNgoaiToiDa = StringVar()
        self.SoLuongCauThuNuocNgoaiToiDa.set(XuLy.get_so_cau_thu_nuoc_ngoai_toi_da())
        self.entrySoLuongCauThuNuocNgoaiToiDa = Entry(self.frame, textvariable=self.SoLuongCauThuNuocNgoaiToiDa)
        self.entrySoLuongCauThuNuocNgoaiToiDa.grid(column=1, row=4, padx=5, pady=5)
        # Button
        self.btn_SoLuongCauThuNuocNgoaiToiDa = Button(self.frame, text='Cập nhật', bg='sky blue').grid(column=2, row=4,
                                                                                                       padx=5, pady=5)
        # CÁC LOẠI BÀN THẮNG
        # label
        self.lbCacLoaiBanThang = Label(self.frame, text='Các loại bàn thắng:')
        self.lbCacLoaiBanThang.grid(column=0, row=5, padx=5, pady=5)
        # Entry
        self.CacLoaiBanThang = StringVar()
        self.CacLoaiBanThang.set(XuLy.get_cac_loai_ban_thang())
        self.entryCacLoaiBanThang = Entry(self.frame, textvariable=self.CacLoaiBanThang)
        self.entryCacLoaiBanThang.grid(column=1, row=5, padx=5, pady=5)
        # Button
        self.btn_CacLoaiBanThang = Button(self.frame, text='Cập nhật', bg='sky blue',
                                          command=self.cap_nhat_cac_loai_ban_thang).grid(column=2, row=5,
                                                                                         padx=5, pady=5)

        # THỜI ĐIỂM GHI BÀN TỐI ĐA
        # label
        self.lbThoiDiemGhiBanToiDa = Label(self.frame, text='Thời điểm ghi bàn tối đa:')
        self.lbThoiDiemGhiBanToiDa.grid(column=0, row=6, padx=5, pady=5)
        # Entry
        self.ThoiDiemGhiBanToiDa = StringVar()
        self.ThoiDiemGhiBanToiDa.set(XuLy.get_thoi_diem_ghi_ban_toi_da())
        self.entryThoiDiemGhiBanToiDa = Entry(self.frame, textvariable=self.ThoiDiemGhiBanToiDa)
        self.entryThoiDiemGhiBanToiDa.grid(column=1, row=6, padx=5, pady=5)
        # Button
        self.btn_ThoiDiemGhiBanToiDa = Button(self.frame, text='Cập nhật', bg='sky blue',
                                              command=self.cap_nhat_thoi_diem_ghi_ban_toi_da).grid(column=2, row=6,
                                                                                                   padx=5, pady=5)

        # ĐIỂM SỐ KHI THẮNG
        # label
        self.lbDiemSoKhiThang = Label(self.frame, text='Điểm số khi thắng:')
        self.lbDiemSoKhiThang.grid(column=0, row=7, padx=5, pady=5)
        # Entry
        self.DiemSoKhiThang = StringVar()
        self.DiemSoKhiThang.set(XuLy.get_diem_khi_thang())
        self.entryDiemSoKhiThang = Entry(self.frame, textvariable=self.DiemSoKhiThang)
        self.entryDiemSoKhiThang.grid(column=1, row=7, padx=5, pady=5)
        # Button
        self.btn_DiemSoKhiThang = Button(self.frame, text='Cập nhật', bg='sky blue',
                                         command=self.cap_nhat_diem_so_khi_thang).grid(column=2, row=7,
                                                                                       padx=5, pady=5)

        # ĐIỂM SỐ KHI HÒA
        # label
        self.lbDiemSoKhiHoa = Label(self.frame, text='Điểm số khi hòa:')
        self.lbDiemSoKhiHoa.grid(column=0, row=8, padx=5, pady=5)
        # Entry
        self.DiemSoKhiHoa = StringVar()
        self.DiemSoKhiHoa.set(XuLy.get_diem_khi_hoa())
        self.entryDiemSoKhiHoa = Entry(self.frame, textvariable=self.DiemSoKhiHoa)
        self.entryDiemSoKhiHoa.grid(column=1, row=8, padx=5, pady=5)
        # Button
        self.btn_DiemSoKhiHoa = Button(self.frame, text='Cập nhật', bg='sky blue',
                                       command=self.cap_nhat_diem_so_khi_hoa).grid(column=2, row=8,
                                                                                   padx=5, pady=5)

        # ĐIỂM SỐ KHI THUA
        # label
        self.lbDiemSoKhiThua = Label(self.frame, text='Điểm số khi thua:')
        self.lbDiemSoKhiThua.grid(column=0, row=9, padx=5, pady=5)
        # Entry
        self.DiemSoKhiThua = StringVar()
        self.DiemSoKhiThua.set(XuLy.get_diem_khi_thua())
        self.entryDiemSoKhiThua = Entry(self.frame, textvariable=self.DiemSoKhiThua)
        self.entryDiemSoKhiThua.grid(column=1, row=9, padx=5, pady=5)
        # Button
        self.btn_DiemSoKhiThua = Button(self.frame, text='Cập nhật', bg='sky blue',
                                        command=self.cap_nhat_diem_so_khi_thua).grid(column=2, row=9,
                                                                                     padx=5, pady=5)

        # THỨ TỰ ƯU TIÊN KHI XẾP HẠNG
        # label
        self.lbThuTuUuTien = Label(self.frame, text='Ưu tiên xếp hạng đội bóng theo:')
        self.lbThuTuUuTien.grid(column=0, row=10, padx=5, pady=5)
        # Combobox
        self.ThuTuUuTien = StringVar()

        self.value_ThuTuUuTien = ('Tổng điểm', 'Hiệu số', 'Tổng bàn thắng')

        self.cbThuTuUuTien = ttk.Combobox(self.frame, textvariable=self.ThuTuUuTien, value=self.value_ThuTuUuTien,
                                          state='readonly')
        self.cbThuTuUuTien.grid(column=1, row=10, padx=5, pady=5)

        thuTuUuTienHienTai = XuLy.get_uu_tien_xep_hang()
        if thuTuUuTienHienTai == 'diem':
            self.cbThuTuUuTien.current(0)
        elif thuTuUuTienHienTai == 'hieuso':
            self.cbThuTuUuTien.current(1)
        else:
            self.cbThuTuUuTien.current(2)
        # Button
        self.btn_ThuTuUuTien = Button(self.frame, text='Cập nhật', bg='sky blue',
                                      command=self.cap_nhat_thu_tu_uu_tien).grid(column=2, row=10,
                                                                                 padx=5, pady=5)

    def cap_nhat_tuoi_toi_thieu(self):
        XuLy.cap_nhat_tuoi_toi_thieu(self.TuoiToiThieu)

    def cap_nhat_tuoi_toi_da(self):
        XuLy.cap_nhat_tuoi_toi_da(self.TuoiToiDa)

    def cap_nhat_so_luong_cau_thu_toi_thieu(self):
        XuLy.cap_nhat_so_luong_cau_thu_toi_thieu(self.SoLuongCauThuToiThieu)

    def cap_nhat_so_luong_cau_thu_toi_da(self):
        XuLy.cap_nhat_so_luong_cau_thu_toi_da(self.SoLuongCauThuToiDa)

    def cap_nhat_cac_loai_ban_thang(self):
        XuLy.cap_nhat_cac_loai_ban_thang(self.CacLoaiBanThang)

    def cap_nhat_thoi_diem_ghi_ban_toi_da(self):
        XuLy.cap_nhat_thoi_diem_ghi_ban_toi_da(self.ThoiDiemGhiBanToiDa)

    def cap_nhat_diem_so_khi_thang(self):
        XuLy.cap_nhat_diem_so_khi_thang(self.DiemSoKhiThang)

    def cap_nhat_diem_so_khi_hoa(self):
        XuLy.cap_nhat_diem_so_khi_hoa(self.DiemSoKhiHoa)

    def cap_nhat_diem_so_khi_thua(self):
        XuLy.cap_nhat_diem_so_khi_thua(self.DiemSoKhiThua)

    def cap_nhat_thu_tu_uu_tien(self):
        XuLy.cap_nhat_thu_tu_uu_tien(self.ThuTuUuTien)


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
