from tkinter import *#Modul GUI
from tkinter import messagebox
from turtle import width

#Modul class
class newborn:
    def daftar(): #Modul function
        global pais

        new = Toplevel(root)
        new.geometry("500x300")
        new.title("Program Cek List Akun")
        root.withdraw()
        accountlist = [] #Modul Array(variabel)

        nama = StringVar()#Modul variabel untuk menyimpan nama,imel,pass
        imel = StringVar()
        pais = StringVar()
       
        frame = Frame(new)
        frame.pack(side = RIGHT)

        #Modul variabel
        scroll = Scrollbar(frame, orient = VERTICAL)
        select = Listbox(frame, yscrollcommand = scroll.set, height =25)
        scroll.config(command = select.yview)
        scroll.pack(side = RIGHT, fill = Y)
        select.pack(side = RIGHT, fill = BOTH, expand = 3)

        def Selected():
            return int(select.curselection()[0])

        def addaccount(): #Modul pengkondisian if-else (Memasukan data" ke array account list)
            if (nama.get() == "" or imel.get() == "" or pais.get() == ""):
                messagebox.showerror("warrning", "Please fill the blank")
            else:
                accountlist.append([nama.get(), imel.get(), pais.get()])
                Select_set()

        def edit():
            if (nama.get() == "" or imel.get() == "" or pais.get() == ""):
                messagebox.showerror("warrning", "Please fill the blank")
            else:
                accountlist[Selected()] = [nama.get(), imel.get(), pais.get()]
                Select_set()

        def hapus():
            del accountlist[Selected()]
            Select_set()

        def lihat():
            NAMA,EMAIL,PASS = accountlist[Selected()]
            nama.set(NAMA)
            imel.set(EMAIL)
            pais.set(PASS)

        def Select_set():
            accountlist.sort()
            select.delete(0,END)
            for nama,email,pasw in accountlist: #Modul perulangan for loop (Untuk menambah daftar yg ada list, tapi hanya menampilkan nama dari akun yg kita buat)
                select.insert(END,nama)
        Select_set()

        def kabur():
            root.destroy()

        #Modul GUI
        text1 = Label(new, text = "Nama akun",font = ("Times New Roman", 12, "bold")).place(x=40, y=30)
        text2 = Label(new, text = "Email",font = ("Times New Roman", 12, "bold")).place(x=40, y=80)
        text3 = Label(new, text = "Password",font = ("Times New Roman", 12, "bold")).place(x=40, y=130)

        entry3 = Entry(new, width = 40, textvariable = nama).place(x=30, y=50)
        entry4 = Entry(new, width = 40, textvariable = imel).place(x=30, y=100)
        entry5 = Entry(new, width = 25, textvariable = pais).place(x=30, y=150)

        title = Label(new, text = "Account List",fg = "white", bg = "black", width = "300", height = "1", font = ("Times New Roman", 16, "bold")).pack()

        tambah = Button(new, text = "New", height = "1", width = "30", command = addaccount).place(x=40, y=180)
        ubah = Button(new, text = "Change", height = "1", width = "30", command = edit).place(x=40, y=210)
        kurang = Button(new, text = "Delete", height = "1", width = "30", command = hapus).place(x=40, y=240)
        view = Button(new, text = "Check", height = "1", width = "30", command = lihat).place(x=40, y=270)
        quit = Button(new, text = "Exit", height = "1", width = "10", command = kabur).place(x=270, y=270)

def check():
    check1 = email.get()#Modul Getter
    check2 = password.get()

    if (check1 == "" and check2 == ""): #Modul pengkondisian if-else
        messagebox.showinfo("", "Please fill the blank")

    elif (check1 == "feriarifin304@gmail.com" and check2 == "arifin304"):
        messagebox.showinfo("", "login success")
        newborn.daftar()
        
    else:
        messagebox.showinfo("", "Wrong identity")

root = Tk()#Modul GUI
root.geometry("300x200")
root.title ("Check Credential")


judul = Label(root, text = "Login",fg = "white", bg = "black", width = "300", height = "1", font = ("Times New Roman", 16, "bold")).pack()
mail = Label(root, text = "Email",font = ("Times New Roman", 12, "bold")).place(x=40, y=30)
pas = Label(root, text = "Password",font = ("Times New Roman", 12, "bold")).place(x=40, y=90)

masuk = Button(text = "Login", height = "1", width = "30", command = check).place(x=40, y=150)

email = StringVar()
entry1 = Entry(root, width = 40, textvariable = email).place(x=30, y=60)

password = StringVar()
entry2 = Entry(root, width = 40, textvariable = password).place(x=30, y=120)


root.mainloop()