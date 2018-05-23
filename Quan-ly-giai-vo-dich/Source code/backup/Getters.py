from sqlite3 import *


def get_ten_cau_thu(id_cau_thu):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT ten FROM cauthu WHERE id=(?)', (id_cau_thu,))
    r = c.fetchone()
    conn.close()
    return r[0]


def get_id_cau_thu(ten_cau_thu):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT id FROM cauthu WHERE ten=(?)', (ten_cau_thu,))
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


def get_id_doi(ten_doi):
    conn = connect('GiaiVoDich.db')
    c = conn.cursor()
    c.execute('SELECT id FROM doibong WHERE ten=(?)', (ten_doi,))
    r = c.fetchone()
    conn.close()
    return r[0]


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
        diemdoinha += 3

        # hiệu số mới
        hieusomoi_doinha = hieusodoinha + (sobanthangdoinha - sobanthangdoikhach)
        hieusomoi_doikhach = hieusodoikhach - (sobanthangdoinha - sobanthangdoikhach)

        # cập nhật điểm và hiệu số đội nhà
        c.execute("UPDATE doibong SET diem=(?),hieuso=(?) WHERE ten=(?)", (diemdoinha, hieusomoi_doinha, tendoichunha,))

        # cập nhật hiệu số đội khách
        c.execute("UPDATE doibong SET hieuso=(?) WHERE ten=(?)", (hieusomoi_doikhach, tendoikhach,))

    elif sobanthangdoikhach > sobanthangdoinha:  # đội khách thắng
        # điểm mới
        diemdoikhach += 3

        # hiệu số mới
        hieusomoi_doikhach = hieusodoikhach + (sobanthangdoikhach - sobanthangdoinha)
        hieusomoi_doinha = hieusodoinha - (sobanthangdoikhach - sobanthangdoinha)

        # cập nhật điểm và hiệu số đội khách
        c.execute("UPDATE doibong SET diem=(?),hieuso=(?) WHERE ten=(?)",
                  (diemdoikhach, hieusomoi_doikhach, tendoikhach,))

        # cập nhật hiệu số đội nhà
        c.execute("UPDATE doibong SET hieuso=(?) WHERE ten=(?)", (hieusomoi_doinha, tendoichunha,))

    else:  # hòa

        diemdoikhach += 1
        diemdoinha += 1
        c.execute("UPDATE doibong SET diem=(?) WHERE ten=(?)", (diemdoinha, tendoichunha,))
        c.execute("UPDATE doibong SET diem=(?) WHERE ten=(?)", (diemdoikhach, tendoikhach,))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    print(get_cac_cap_dau(1))
