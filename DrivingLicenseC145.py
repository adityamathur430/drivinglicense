from tkinter import *

root=Tk()

root.title("Driver's License")
root.geometry("400x400")

label_series = Label(root, text="")
label_id = Label(root)
label_name = Label(root)
label_DOB = Label(root)
label_Pin = Label(root)
label_address = Label(root)
label_CarAuth = Label(root)



def Fibonnaci():
        label_id['text'] = "ID: 19827198349"
        label_name["text"] = "Name: Winnie the Pooh"
        label_DOB["text"] ="Date of Birth: 21 August 1921"
        label_Pin["text"] = "Pin no.: 451478"
        label_address["text"] = "Address: Disney Land, Hong Kong"
        label_CarAuth["text"] = "Authorized to drive: HK 83A82H1, HK 19H21SA"

btn = Button(root, text="Find Driver's License info", command=Fibonnaci)
btn.pack()
label_series.pack()
label_id.pack()
label_name.pack()
label_DOB.pack()
label_Pin.pack()
label_address.pack()
label_CarAuth.pack()
root.mainloop()