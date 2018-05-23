import string
from sqlite3 import *
from tkinter import messagebox


# ngay_sinh: ngày tháng năm sinh theo format: yyyy-mm-dd
def get_so_tuoi_cau_thu(ngay_sinh):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute("SELECT strftime('%Y',datetime('now')) - strftime('%Y',?)", (ngay_sinh,))
    r = c.fetchone()
    conn.close()
    return r[0]


# trả về tuple
def get_so_ngay_trong_1_thang():
    return (
        '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19',
        '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')


# trả về tuple
def get_so_thang_trong_1_nam():
    return ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')


def get_tuoi_toi_thieu():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT tuoitoithieu FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_tuoi_toi_da():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT tuoitoida FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_so_doi():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(id) FROM doibong')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_so_cau_thu_toi_thieu():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT socauthutoithieu FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_so_cau_thu_toi_da():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT socauthutoida FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_so_cau_thu_nuoc_ngoai_toi_da():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT socauthunuocngoaitoida FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_so_ban_thang_doi_nha_trong_tran_dau(id_doinha, id_doikhach, id_vong):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute("SELECT doinhathang FROM trandau WHERE iddoinha=(?) AND iddoikhach=(?) AND idvong=(?)",
              (id_doinha, id_doikhach, id_vong,))
    r = c.fetchone()
    conn.close()
    return r[0]


def get_so_ban_thang_doi_khach_trong_tran_dau(id_doinha, id_doikhach, id_vong):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute("SELECT doikhachthang FROM trandau WHERE iddoinha=(?) AND iddoikhach=(?) AND idvong=(?)",
              (id_doinha, id_doikhach, id_vong,))
    r = c.fetchone()
    conn.close()
    return r[0]


def get_diem_khi_thang():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT diemthang FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_cac_loai_ban_thang():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT cacloaibanthang FROM quydinh')
    r = c.fetchall()
    conn.close()
    ds = []
    for i in range(len(r)):
        ds.append(r[i][0])
    return ds[0]


def get_diem_khi_thua():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT diemthua FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_diem_khi_hoa():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT diemhoa FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_thoi_diem_ghi_ban_toi_da():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT thoidiemtoida FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_uu_tien_xep_hang():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT uutienxephang FROM quydinh')
    r = c.fetchone()
    conn.close()
    return r[0]


def get_ten_cau_thu(id_cau_thu):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT ten FROM cauthu WHERE id=(?)', (id_cau_thu,))
    r = c.fetchone()
    conn.close()
    return r[0]


def get_danh_sach_cau_thu(ten_doi):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    r = c.execute('SELECT cauthu.ten FROM cauthu,doibong WHERE cauthu.iddoi=doibong.id AND doibong.ten=(?)',
                  (ten_doi,)).fetchall()
    conn.close()
    ds = []
    for i in range(len(r)):
        ds.append(r[i][0])
    return ds


def get_id_vong(luotdau):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT id FROM vongdau WHERE luotdau=(?)', (luotdau,))
    r = c.fetchone()
    conn.close()
    return r[0]


def get_id_cau_thu(ten_cau_thu):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    r = c.execute('SELECT id FROM cauthu WHERE ten=(?)', (ten_cau_thu,)).fetchone()[0]
    conn.close()
    return r


def get_id_tran_dau(id_doinha, id_doikhach, id_vong):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute("SELECT id FROM trandau WHERE iddoinha=(?) AND iddoikhach=(?) AND idvong=(?)",
              (id_doinha, id_doikhach, id_vong,))
    r = c.fetchone()
    conn.close()
    return r[0]


def get_ten_doi(id_doi):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT ten FROM doibong WHERE id=(?)', (id_doi,))
    r = c.fetchone()
    conn.close()
    return r[0]


def get_danh_sach_ten_doi():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    r = c.execute('SELECT ten FROM doibong').fetchall()
    ds = []
    for i in range(len(r)):
        ds.append(r[i][0])
    conn.close()
    return ds


def get_id_doi(ten_doi):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    r = c.execute('SELECT id FROM doibong WHERE ten=(?)', (ten_doi,)).fetchone()[0]
    conn.close()
    return r


def get_list_so_vong():
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    tongsovong = c.execute('SELECT count(*)FROM vongdau').fetchone()[0]
    listcacsovong = []
    for i in range(tongsovong):
        listcacsovong.append(i + 1)
    conn.close()
    return listcacsovong


def get_cac_cap_dau(so_vong):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()

    # get list các cặp id đội đấu
    c.execute(
        'SELECT trandau.iddoinha,trandau.iddoikhach FROM trandau INNER JOIN vongdau ON trandau.idvong=vongdau.id AND vongdau.luotdau=(?)',
        (so_vong,))
    list_raw = c.fetchall()
    conn.close()

    # list chứa các cặp tên đội đấu
    final_list = []
    for cap_id in list_raw:
        doinha = get_ten_doi(cap_id[0])
        doikhach = get_ten_doi(cap_id[1])
        final_list.append(doinha + '-' + doikhach)

    # nếu danh sách rỗng(không có cặp đấu nào trong vòng đấu) thì set final_list[0]="Không có cặp đấu nào"
    if len(final_list) == 0:
        final_list.append("Không có cặp đấu nào")

    return final_list


def get_ngaygio_bang_ti_so(doichunha, doikhach, so_vong):
    id_doinha = get_id_doi(doichunha)
    id_doikhach = get_id_doi(doikhach)
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    ngay = c.execute(
        "SELECT ngaygio FROM trandau,vongdau WHERE trandau.iddoinha=(?) AND trandau.iddoikhach=(?) AND vongdau.id=trandau.idvong AND vongdau.luotdau=(?)",
        (id_doinha, id_doikhach, so_vong)).fetchone()[0]
    conn.close()
    return ngay


def get_san_doi_chu_nha(doichunha):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    san = c.execute("SELECT san FROM doibong WHERE doibong.ten= (?)", (doichunha,)).fetchone()[0]
    conn.close()
    return san


def cap_nhat_diem_va_hieu_so_cua_doi(tendoichunha, tendoikhach, sobanthangdoinha, sobanthangdoikhach):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()

    # get điểm hiện tại của đội nhà
    diemdoinha = c.execute("SELECT diem FROM doibong WHERE ten=(?)", (tendoichunha,)).fetchone()[0]

    # get điểm hiện tại của đội khách
    diemdoikhach = c.execute("SELECT diem FROM doibong WHERE ten=(?)", (tendoikhach,)).fetchone()[0]

    # get hiệu số hiện tại của đội nhà
    hieusodoinha = c.execute("SELECT hieuso FROM doibong WHERE ten=(?)", (tendoichunha,)).fetchone()[0]

    # get hiệu số hiện tại của đội khách
    hieusodoikhach = c.execute("SELECT hieuSo FROM doibong WHERE ten=(?)", (tendoikhach,)).fetchone()[0]

    if sobanthangdoinha > sobanthangdoikhach:  # đội nhà thắng
        # điểm mới
        diemdoinha += get_diem_khi_thang()
        diemdoikhach += get_diem_khi_thua()

        # hiệu số mới
        hieusodoinha += (sobanthangdoinha - sobanthangdoikhach)
        hieusodoikhach -= (sobanthangdoinha - sobanthangdoikhach)

        # get tổng số bàn thắng hiện tại của đội nhà
        tongsobanthangdoinha = c.execute("SELECT thang FROM doibong WHERE ten=(?)", (tendoichunha,)).fetchone()[0]

        # get tổng số bàn thua hiện tại của đội khách
        tongsobanthuadoikhach = c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (tendoikhach,)).fetchone()[0]

        # giá trị mới cho số bàn thắng,thua của đội nhà và đội khách
        tongsobanthangdoinha += 1
        tongsobanthuadoikhach += 1

        # cập nhật điểm,số bàn thắng và hiệu số đội nhà
        c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thang=(?) WHERE ten=(?)",
                  (diemdoinha, hieusodoinha, tongsobanthangdoinha, tendoichunha,))

        # cập nhật điểm,số bàn thua và hiệu số đội khách
        c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thua=(?) WHERE ten=(?)",
                  (diemdoikhach, hieusodoikhach, tongsobanthuadoikhach, tendoikhach,))

    elif sobanthangdoikhach > sobanthangdoinha:  # đội khách thắng
        # điểm mới
        diemdoikhach += get_diem_khi_thang()
        diemdoinha += get_diem_khi_thua()

        # hiệu số mới
        hieusomoi_doikhach = hieusodoikhach + (sobanthangdoikhach - sobanthangdoinha)
        hieusomoi_doinha = hieusodoinha - (sobanthangdoikhach - sobanthangdoinha)

        # get tổng số bàn thua hiện tại của đội nhà
        tongsobanthuadoinha = c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (tendoichunha,)).fetchone()[0]

        # get tổng số bàn thắng hiện tại của đội khách
        tongsobanthangdoikhach = c.execute("SELECT thang FROM doibong WHERE ten=(?)", (tendoikhach,)).fetchone()[0]

        # giá trị mới cho số bàn thắng thua của đội khách,đội nhà
        tongsobanthangdoikhach += 1
        tongsobanthuadoinha += 1

        # cập nhật điểm,số bàn thắng và hiệu số đội khách
        c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thang=(?) WHERE ten=(?)",
                  (diemdoikhach, hieusomoi_doikhach, tongsobanthangdoikhach, tendoikhach,))

        # cập nhật điểm,số bàn thua và hiệu số đội nhà
        c.execute("UPDATE doibong SET diem=(?),hieuso=(?),thua=(?) WHERE ten=(?)",
                  (diemdoinha, hieusomoi_doinha, tongsobanthuadoinha, tendoichunha,))

    else:  # hòa

        diemdoikhach += get_diem_khi_hoa()
        diemdoinha += get_diem_khi_hoa()

        # get tổng số bàn hòa hiện tại của đội nhà
        tongsobanhoadoinha = c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (tendoichunha,)).fetchone()[0]

        # get tổng số bàn hòa hiện tại của đội khách
        tongsobanhoadoikhach = c.execute("SELECT hoa FROM doibong WHERE ten=(?)", (tendoikhach,)).fetchone()[0]

        tongsobanhoadoikhach += 1
        tongsobanhoadoinha += 1

        c.execute("UPDATE doibong SET diem=(?),hoa=(?) WHERE ten=(?)", (diemdoinha, tongsobanhoadoinha, tendoichunha,))
        c.execute("UPDATE doibong SET diem=(?),hoa=(?) WHERE ten=(?)",
                  (diemdoikhach, tongsobanhoadoikhach, tendoikhach,))

    conn.commit()
    conn.close()


def cap_nhat_ti_so(sobanthangdoinha, sobanthangdoikhach, id_vong, id_doinha, id_doikhach):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute(
        "UPDATE trandau SET doinhathang=(?), doikhachthang=(?) WHERE idvong=(?) AND iddoinha=(?) AND iddoikhach=(?)",
        (sobanthangdoinha, sobanthangdoikhach, id_vong, id_doinha, id_doikhach,))
    conn.commit()
    conn.close()


# tuoi : StringVar()
def cap_nhat_tuoi_toi_thieu(tuoi):
    if tuoi.get().isdigit():
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET tuoitoithieu=(?)", (tuoi.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Tuổi tối thiểu đã được cập nhật thành " + tuoi.get())
    else:
        messagebox.showerror("Lỗi", "Giá trị không hợp lệ!")


# tuoi : StringVar()
def cap_nhat_tuoi_toi_da(tuoi):
    if tuoi.get().isdigit():
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET tuoitoida=(?)", (tuoi.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Tuổi tối đa đã được cập nhật thành " + tuoi.get())
    else:
        messagebox.showerror("Lỗi", "Giá trị không hợp lệ!")


# soluong : StringVar()
def cap_nhat_so_luong_cau_thu_toi_thieu(soLuong):
    if soLuong.get().isdigit():
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET socauthutoithieu=(?)", (soLuong.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Số lượng cầu thủ tối thiểu đã được cập nhật thành " + soLuong.get())
    else:
        messagebox.showerror("Lỗi", "Giá trị không hợp lệ!")


# soLuong : StringVar()
def cap_nhat_so_luong_cau_thu_toi_da(soLuong):
    if soLuong.get().isdigit():
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET socauthutoida=(?)", (soLuong.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Số lượng cầu thủ tối đa đã được cập nhật thành " + soLuong.get())
    else:
        messagebox.showerror("Lỗi", "Giá trị không hợp lệ!")


# cacLoaiBanThang : StringVar()
def cap_nhat_cac_loai_ban_thang(cacLoaiBanthang):
    cac_ki_tu_hop_le = string.ascii_lowercase + string.ascii_uppercase + string.digits + ','

    hop_le = True

    for kitu in cacLoaiBanthang.get():
        if kitu not in cac_ki_tu_hop_le:
            hop_le = False

    if hop_le is True:
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET cacloaibanthang=(?)", (cacLoaiBanthang.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Các loại bàn thắng đã được cập nhật thành:\n" + cacLoaiBanthang.get())
    else:
        messagebox.showerror("Lỗi",
                             "Giá trị không hợp lệ!\nCác kí tự hợp lệ bao gồm các số tự nhiên,chữ cái và dấu phẩy dùng để ngăn cách các loại bàn thắng.")


# thoiDiemGhiban : StringVar()
def cap_nhat_thoi_diem_ghi_ban_toi_da(thoiDiemGhiBan):
    if not thoiDiemGhiBan.get().isdigit():
        messagebox.showerror("Lỗi", "Giá trị không hợp lệ!")
    else:
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET thoidiemtoida=(?)", (thoiDiemGhiBan.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Thời điểm ghi bàn tối đa đã được cập nhật thành " + thoiDiemGhiBan.get())


# diem: StringVar()
def cap_nhat_diem_so_khi_thang(diem):
    if diem.get().isdigit():
        if (int(diem.get()) > get_diem_khi_hoa()) and int(diem.get()) > get_diem_khi_thua():
            conn = connect('GiaiVoDich.db')
            c = conn.cursor()
            c.execute("UPDATE quydinh SET diemthang=(?)", (diem.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thành công", "Điểm số khi thắng đã được cập nhật thành " + diem.get())
        else:
            messagebox.showerror("Lỗi", "Điểm thắng phải lớn hơn điểm hòa và điểm thua!")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")


# diem: StringVar()
def cap_nhat_diem_so_khi_hoa(diem):
    if diem.get().isdigit():
        if int(diem.get()) < get_diem_khi_thang() and int(diem.get()) > get_diem_khi_thua():
            conn = connect('GiaiVoDich.db')
            c = conn.cursor()
            c.execute("UPDATE quydinh SET diemhoa=(?)", (diem.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thành công", "Điểm số khi hòa đã được cập nhật thành " + diem.get())
        else:
            messagebox.showerror("Lỗi", "Điểm hòa phải nhỏ hơn điểm thắng và lớn hơn điểm thua!")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên")


# diem: StringVar()
def cap_nhat_diem_so_khi_thua(diem):
    if diem.get().isdigit():
        if int(diem.get()) < get_diem_khi_hoa() and int(diem.get()) < get_diem_khi_thang():
            conn = connect('GiaiVoDich.db')
            c = conn.cursor()
            c.execute("UPDATE quydinh SET diemthua=(?)", (diem.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thành công", "Điểm số khi thua đã được cập nhật thành " + diem.get())
        else:
            messagebox.showerror("Lỗi", "Điểm thua phải nhỏ hơn điểm thắng và điểm hòa!")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")


# thu_tu_uu_tien: StringVar()
def cap_nhat_thu_tu_uu_tien(thu_tu_uu_tien):
    if thu_tu_uu_tien.get() == 'Tổng điểm':
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET uutienxephang='diem'")
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Ưu tiên xếp hạng đã được cập nhật thành " + thu_tu_uu_tien.get())

    elif thu_tu_uu_tien.get() == 'Hiệu số':
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET uutienxephang='hieuso'")
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Ưu tiên xếp hạng đã được cập nhật thành " + thu_tu_uu_tien.get())

    else:
        conn = connect('GiaiVoDich.db')
        c = conn.cursor()
        c.execute("UPDATE quydinh SET uutienxephang='thang'")
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Ưu tiên xếp hạng đã được cập nhật thành " + thu_tu_uu_tien.get())


def them_cau_thu_ghi_ban(id_cauthu, id_tran, loaibanthang, thoidiem):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute("INSERT INTO banthang(idcauthu,idtrandau,loaibanthang,thoidiem) VALUES (?,?,?,?)",
              (id_cauthu, id_tran, loaibanthang, thoidiem,))
    conn.commit()
    conn.close()


def xep_hang():
    uuTienXepHang = get_uu_tien_xep_hang()
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    r = c.execute("SELECT ten,thang,thua,hoa,diem,hieuso FROM doibong ORDER BY %s DESC" % uuTienXepHang).fetchall()
    conn.close()
    return r


def get_tong_so_ban_thang_cua_cau_thu(id_cau_thu):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()

    c.execute("SELECT DISTINCT idcauthu FROM banthang")
    temp = c.fetchall()

    danh_sach_id_cau_thu_ghi_ban = []

    for i in range(len(temp)):
        danh_sach_id_cau_thu_ghi_ban.append(temp[i][0])

    if id_cau_thu not in danh_sach_id_cau_thu_ghi_ban:
        return 0
    else:
        c.execute("SELECT count(idcauthu) FROM banthang WHERE idcauthu=(?)",(id_cau_thu,))
        r = c.fetchone()
        return r[0]


if __name__ == '__main__':
    print(get_tong_so_ban_thang_cua_cau_thu(2))
