import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

import XuLy

conn = sqlite3.connect("GiaiVoDich.db")


###################################################
class LapLichThiDau:
    def __init__(self, master):
        # create connection
        conn = sqlite3.connect("GiaiVoDich.db")
        self.c = conn.cursor()
        # create header frame
        self.master = master
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        # creata header label
        ttk.Label(self.frame_header, text="LẬP LỊCH THI ĐẤU", font=('Arial', 18, 'italic')).pack()
        # create content frame
        self.frame_content = ttk.Frame(self.master)
        self.frame_content.pack()
        # create Label
        ttk.Label(self.frame_content, text="Chọn Vòng Đấu:").grid(row=0, column=0, sticky=W)
        # Query data
        k = self.c.execute("SELECT luotdau FROM vongdau").fetchall()
        Matchlist = []
        for i in k:
            Matchlist.append(i[0])
        # create combobox for the Label
        self.mavong = StringVar()
        #######################################
        self.cbLabel = ttk.Combobox(self.frame_content, width=7, textvariable=self.mavong, state="readonly")
        self.cbLabel['values'] = Matchlist
        self.cbLabel.current(0)
        self.cbLabel.grid(row=0, column=1, padx=15, sticky=W)
        # Button Xac Nhan
        ttk.Button(self.frame_content, text='Xác Nhận', command=self.create_listGUI_ListMatches).grid(row=0, column=2,
                                                                                                      columnspan=2)
        self.listGUI_ListMatches = None

        # So luong Tran dau Dien ra
        f = self.c.execute("SELECT COUNT(*) FROM doibong").fetchone()[0]
        self.a = int(f / 2)

        ##############################

    def create_listGUI_ListMatches(self):
        self.b = self.mavong.get()
        flag = 0
        checkMV = self.c.execute("SELECT idvong FROM trandau").fetchall()
        for i in checkMV:
            if (i[0] == int(self.b)):
                flag = 1
                break
        if (flag == 1):
            messagebox.showerror(title='Error', message=("Vòng đấu bạn chọn đã được lập lịch thi đấu"))
        elif hasattr(self.listGUI_ListMatches, 'newFrame') and hasattr(self.listGUI_ListMatches, 'buttonFrame'):
            self.listGUI_ListMatches.buttonFrame.destroy()
            self.listGUI_ListMatches.newFrame.destroy()
            self.listGUI_ListMatches = ListMatches(self.master, self.a, self.b)
        else:
            self.listGUI_ListMatches = ListMatches(self.master, self.a, self.b)


class Matches:
    def __init__(self, master, stt):
        self.master = master
        if stt == 1:
            ttk.Label(self.master, text="STT").grid(row=0, column=0, padx=3, pady=2)
            ttk.Label(self.master, text="Team1").grid(row=0, column=1, padx=10, pady=2)
            ttk.Label(self.master, text="Team2").grid(row=0, column=2, padx=10, pady=2)
            ttk.Label(self.master, text="DD").grid(row=0, column=3, padx=2, pady=2)
            ttk.Label(self.master, text="MM").grid(row=0, column=4, padx=3, pady=2)
            ttk.Label(self.master, text="YYYY").grid(row=0, column=5, padx=4, pady=2)
            ttk.Label(self.master, text="Hour").grid(row=0, column=6, padx=2, pady=2)
            ttk.Label(self.master, text="Min").grid(row=0, column=7, padx=2, pady=2)
            ttk.Label(self.master, text="Stadium").grid(row=0, column=8, padx=10, pady=2)
        ##############################################

        ttk.Label(self.master, text=stt).grid(row=stt, column=0, padx=10)
        ##############################################

        c = conn.cursor()

        ListTeam = c.execute("SELECT ten FROM doibong").fetchall()
        TeamList = []
        for i in ListTeam:
            TeamList.append(i[0])
        ##############################################
        # Set Teams
        self.Team1 = StringVar()
        self.cbTeam1 = ttk.Combobox(self.master, width=24, textvariable=self.Team1, state="readonly")
        self.cbTeam1['values'] = TeamList
        self.cbTeam1.current(0)
        self.cbTeam1.grid(row=stt, column=1, padx=10, pady=2)
        self.cbTeam1.bind("<<ComboboxSelected>>", self.capnhatsannha)
        ##############################################
        self.Team2 = StringVar()
        self.cbTeam2 = ttk.Combobox(self.master, width=24, textvariable=self.Team2, state="readonly")
        self.cbTeam2['values'] = TeamList
        self.cbTeam2.current(0)
        self.cbTeam2.grid(row=stt, column=2, padx=10, pady=2)
        ##############################################
        # Set Date
        self.dob_day = StringVar()
        self.dob_month = StringVar()
        self.dob_year = StringVar()
        Spinbox(self.master, from_=1, to=31, textvariable=self.dob_day, width=2, state="readonly").grid(row=stt,
                                                                                                        column=3,
                                                                                                        sticky='e')
        Spinbox(self.master, from_=1, to=12, textvariable=self.dob_month, width=3, state="readonly").grid(row=stt,
                                                                                                          column=4,
                                                                                                          sticky='e')
        Spinbox(self.master, from_=2017, to=2100, textvariable=self.dob_year, width=4, state="readonly").grid(row=stt,
                                                                                                              column=5,
                                                                                                              sticky='e')

        ##############################################
        # Set Time
        self.time_hour = StringVar()
        self.time_minute = StringVar()
        Spinbox(self.master, from_=0, to=23, textvariable=self.time_hour, width=2, state="readonly").grid(row=stt,
                                                                                                          column=6,
                                                                                                          sticky='e')
        Spinbox(self.master, from_=00, to=59, textvariable=self.time_minute, width=2, state="readonly").grid(row=stt,
                                                                                                             column=7,
                                                                                                             sticky='e')
        ##############################################
        self.tensannha = StringVar()
        self.sanNha = ttk.Label(self.master, width=18, textvar=self.tensannha,
                                state="disable").grid(
            row=stt, column=8, padx=7,
            pady=2, sticky='e')
        self.tensannha.set(XuLy.get_san_doi_chu_nha(self.Team1.get()))

    def capnhatsannha(self, status=None, afk=False):
        self.tensannha.set(XuLy.get_san_doi_chu_nha(self.Team1.get()))


class ListMatches:
    def __init__(self, master, a, b):
        # Frame.__init__(self, master)
        self.newFrame = Frame(master)
        self.newFrame.pack()
        self.master = master

        self.canvas = Canvas(self.newFrame, borderwidth=1, background="#ffffff", width=700)
        self.frame_Matches = Frame(self.canvas)
        self.vsb = Scrollbar(self.newFrame, orient="vertical", command=self.canvas.yview)
        self.vsb1 = Scrollbar(self.newFrame, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.vsb1.set)
        self.vsb.pack(side="right", fill="y")
        self.vsb1.pack(side="bottom", fill="x")

        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame_Matches, anchor="nw",
                                  tags="self.frame_Matches")
        self.frame_Matches.bind("<Configure>", self.onFrameConfigure)
        ######################################
        # So Tran Dau
        self.n_Matches = a
        # Ma Vong dau
        self.mv = b
        ######################################
        self.dictMatches = []
        for i in range(self.n_Matches):
            self.dictMatches.append(Matches(self.frame_Matches, i + 1))

        self.buttonFrame = Frame(master)
        self.buttonFrame.pack(side='bottom')
        ttk.Button(self.buttonFrame, text='submit', command=self.Finish).pack()
        ######################################

    def Finish(self):
        c = conn.cursor()
        # Tao cac bien gia tri
        check = 0
        checktontai = 0
        checktrung = 0
        lms = []
        #####################################################
        for i in self.dictMatches:
            T1 = i.Team1.get()
            T2 = i.Team2.get()
            lms.append(T1)
            lms.append(T2)
        ####################################################
        leng = len(lms)
        # Kiem Tra Trung vs Kiem Tra Nhap Lieu vs Kiem Tra tran dau da ton tai trong csdl chua

        for i in range(0, leng):
            if (lms[i] == ''):
                checktontai = 1
                break
            if i == leng:
                break
            j = i + 1
            for k in range(j, leng):
                if (lms[i] == lms[k]):
                    checktrung = 1
                    break
        for i in self.dictMatches:
            T1 = i.Team1.get()
            Team1 = c.execute("SELECT id FROM doibong WHERE doibong.ten == (?)", (T1,)).fetchone()[0]
            T2 = i.Team2.get()
            Team2 = c.execute("SELECT id FROM doibong WHERE doibong.ten == (?)", (T2,)).fetchone()[0]
            k = c.execute("SELECT iddoinha,iddoikhach FROM trandau").fetchall()
            for d in k:
                if (d[0] == Team1 and d[1] == Team2):
                    check = 1
                    break
        ####################################################
        if (checktontai == 1):
            messagebox.showerror(title='Error', message=("Bạn chưa chọn đội bóng"))
        elif (checktrung == 1):
            messagebox.showerror(title='Error', message=("Bạn nhập trùng đội bóng"))
        elif (check == 1):
            messagebox.showerror(title='Error', message=("Cặp đấu bạn nhập đã tồn tại trong lịch thi đấu"))
        else:
            for i in self.dictMatches:
                T1 = i.Team1.get()
                Team1 = c.execute("SELECT id FROM doibong WHERE doibong.ten == (?)", (T1,)).fetchone()[0]
                T2 = i.Team2.get()
                Team2 = c.execute("SELECT id FROM doibong WHERE doibong.ten == (?)", (T2,)).fetchone()[0]
                ##########################
                Day = i.dob_day.get()
                D = 0
                if int(Day) < 10:
                    D = 1
                ##########################
                Month = i.dob_month.get()
                M = 0
                if int(Month) < 10:
                    M = 1
                ##########################
                Year = i.dob_year.get()
                ##########################
                Hour = i.time_hour.get()
                H = 0
                if int(Hour) < 10:
                    H = 1
                ##########################
                Minute = i.time_minute.get()
                Mi = 0
                if int(Minute) < 10:
                    Mi = 1
                ##########################
                # check dieu kien va xay dung form Datetime Standard
                if (D == 1 and M == 1 and H == 1 and Mi == 1):
                    self.Date = Year + "-0" + Month + "-0" + Day + " 0" + Hour + ":0" + Minute + ":00"
                elif (D == 1 and M == 1 and H == 1 and Mi == 0):
                    self.Date = Year + "-" + Month + "-0" + Day + " 0" + Hour + ":" + Minute + ":00"
                elif (D == 1 and M == 1 and H == 0 and Mi == 1):
                    self.Date = Year + "-0" + Month + "-0" + Day + " " + Hour + ":0" + Minute + ":00"
                elif (D == 1 and M == 1 and H == 0 and Mi == 0):
                    self.Date = Year + "-0" + Month + "-0" + Day + " " + Hour + ":" + Minute + ":00"
                elif (D == 1 and M == 0 and H == 1 and Mi == 1):
                    self.Date = Year + "-" + Month + "-0" + Day + " 0" + Hour + ":0" + Minute + ":00"
                elif (D == 1 and M == 0 and H == 1 and Mi == 0):
                    self.Date = Year + "-" + Month + "-0" + Day + " 0" + Hour + ":" + Minute + ":00"
                elif (D == 1 and M == 0 and H == 0 and Mi == 1):
                    self.Date = Year + "-" + Month + "-0" + Day + " " + Hour + ":0" + Minute + ":00"
                elif (D == 1 and M == 0 and H == 0 and Mi == 0):
                    self.Date = Year + "-" + Month + "-0" + Day + " " + Hour + ":" + Minute + ":00"
                elif (D == 0 and M == 1 and H == 1 and Mi == 1):
                    self.Date = Year + "-0" + Month + "-" + Day + " 0" + Hour + ":0" + Minute + ":00"
                elif (D == 0 and M == 1 and H == 1 and Mi == 0):
                    self.Date = Year + "-0" + Month + "-" + Day + " 0" + Hour + ":" + Minute + ":00"
                elif (D == 0 and M == 1 and H == 0 and Mi == 1):
                    self.Date = Year + "-0" + Month + "-" + Day + " " + Hour + ":0" + Minute + ":00"
                elif (D == 0 and M == 1 and H == 0 and Mi == 0):
                    self.Date = Year + "-0" + Month + "-" + Day + " " + Hour + ":" + Minute + ":00"
                elif (D == 0 and M == 0 and H == 1 and Mi == 1):
                    self.Date = Year + "-" + Month + "-" + Day + " 0" + Hour + ":0" + Minute + ":00"
                elif (D == 0 and M == 0 and H == 1 and Mi == 0):
                    self.Date = Year + "-" + Month + "-" + Day + " 0" + Hour + ":" + Minute + ":00"
                elif (D == 0 and M == 0 and H == 0 and Mi == 1):
                    self.Date = Year + "-" + Month + "-" + Day + " " + Hour + ":0" + Minute + ":00"
                elif (D == 0 and M == 0 and H == 0 and Mi == 0):
                    self.Date = Year + "-" + Month + "-" + Day + " " + Hour + ":" + Minute + ":00"
                ###########################################
                # Thao Tac Den database
                stadium = c.execute("SELECT san FROM doibong WHERE ten=?", (T1,)).fetchone()[0]
                c.execute("INSERT INTO trandau (iddoinha,iddoikhach,ngaygio,san,idvong) VALUES (?,?,?,?,?)",
                          (Team1, Team2, self.Date, stadium, self.mv))
                conn.commit()
            # Close connection
            conn.close()

            # thong bao thanh cong
            messagebox.showinfo('Thành công', 'Lập lịch thi đấu thành công')
            # thoat chuong trinh
            self.master.destroy()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


def main():
    root = Tk()
    root.title("Lập Lịch Thi Đấu")
    root.minsize(300, 50)
    LapLichThiDau(root)
    root.mainloop()


if __name__ == "__main__":
    main()
