from tkinter import *
from tkinter import filedialog
import qrcode
from customtkinter import *
from PIL import ImageTk


root = Tk()
root.title('QRcode Generator')
root.geometry('800x500+600+100')
root.resizable(0, 0)

def generate_qr():
    global qr_image
    link = link_input.get()
    img = qrcode.make(link)
    img = img.resize((240, 240))
    if img:
        qr_image = img
        img = ImageTk.PhotoImage(img)
        qr_label.configure(image=img)
        qr_label.image = img


def download_qr():
    global qr_image
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        qr_image.save(file_path)

BG = '#494a49'
FG = 'white'
qr_image = None




main_frame = Frame(root, width=800, height=500, bg=BG)
main_frame.pack(expand=True, fill='both')


title_label = Label(main_frame, text='QrCode Generator', font='Helvetica 18', fg=FG, bg=BG)
title_label.pack(pady=4)

#gen Frame
gen_frame = Frame(main_frame, bg=BG)
gen_frame.pack(pady=15)

link_input = Entry(gen_frame, bg=BG, fg=FG, font='Helvetica 10', width=60)
link_input.pack(side='left', padx=5)

gen_button = CTkButton(gen_frame, text="Generate QrCode", command=generate_qr)
gen_button.pack(side='left', padx=5)

#out of gen frame

qr_label = Label(main_frame, bg=BG, fg=FG) #qr_image
qr_label.pack(pady=20)

download_button = CTkButton(main_frame, text="Download QrCode", command=download_qr)
download_button.pack()


root.mainloop()
