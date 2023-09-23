from tkinter import*
from tkinter import messagebox
import numpy as np

#tao cua so chinh
w = Tk()
w.title('giai he pt')

#tao nhan va o nhap lieu cho bien
lb_sobien = Label(w, text = 'hay nhap so bien')
lb_sobien.grid(column = 0, row = 0)
en_sobien = Entry(w, width = 5)
en_sobien.grid(column = 1, row = 0)

# tao o nhap lieu cho cac hang so va he so
en_he_so = []
en_hang_so=[]
so_bien = 0

def tinh_toan():
    sobien = int(en_sobien.get())
    heso = []
    hangso=[]

    for i in range(sobien):
        o_heso = []
        for j in range(sobien):
            o_heso.append(float(en_he_so[i][j].get()))
        heso.append(o_heso)
        hangso.append(float(en_hang_so[i].get()))

    #tao ma tra he so A va hang so b
    A = np.array(heso)
    b = np.array(hangso)

    #giai he pt
    try:
        kq = np.linalg.solve(A,b)
        kq_text = 'ket qua:\n'
        for i in range(sobien):
            kq_text +=f'x{i+1}= {kq[i]}\n'
        kq_label.config(text = kq_text)
    except np.linalg.LinAlgError:
        kq_label.config(text = 'he phuong trinh vo nghiem.')

def nhap():
    global so_bien
    so_bien = int(en_sobien.get())

    for en_row in en_he_so:
        for entry in en_row:
            entry.grib_forget()

    en_he_so.clear()
    en_hang_so.clear()

    for i in range(so_bien):
        o_heso= []
        for j in range(so_bien):
            label = Label(w, text = f'nhap a{i+1}{j+1}:')
            en = Entry(w, width=5)
            o_heso.append(en)
            label.grid(row = i + 1, column = 2 * j)
            en.grid(row = i +1, column = 2 * j + 1)
        en_he_so.append(o_heso)
        label_hangso = Label(w, text = f'nhap b{i+1}:')
        en_hangso = Entry(w, width = 5)
        en_hang_so.append(en_hangso)
        en_hangso.grid(row = i +1, column = so_bien * 2 + 1)
        label_hangso.grid(row = i + 1, column = so_bien *2)

bt1 = Button(w, text = 'cap nhat', command=nhap)
bt1.grid(row = 0, column = 2)

bt2 = Button(w, text='giai phuong trinh', command=tinh_toan)
bt2.grid(row = 5, columnspan= 9)

kq_label = Label(w, text = 'ket qua :')
kq_label.grid(row = 6, columnspan= 7)

w.mainloop()








