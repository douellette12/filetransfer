import tkinter as tk
from send_file1 import *

window = tk.Tk()
window.title("File Transfer Application")
window.geometry("700x250")
window.maxsize(width=700, height=250)
frame1 = tk.Frame(window, height=250, width=700)
frame1.pack()
title = tk.Label(frame1, text="Transfer newest text File to Remote Server", font="helvetica 11")
title.pack()
text_box = tk.Text(frame1, height=10, width=80)
text_box.pack()


def transfer_and_display_info():
    text_box.insert("1.0", "searching for the newest text file...\n")
    file = newest_file()
    frame1.update_idletasks()
    notify = move_files(file)
    text_box.insert("2.0", f"{notify}\n")
    frame1.update_idletasks()
    appt_import_txt(file)
    text_box.insert("3.0", "\n")
    text_box.insert("4.0", f"You can now find the file on the server.\n")
    frame1.update_idletasks()
    text_box.insert("5.0", "\n")


def clear_info():
    text_box.delete("1.0", tk.END)


btn = tk.Button(frame1, text="Send File", command=transfer_and_display_info,
                height=1, width=22)
btn.pack()
btn1 = tk.Button(frame1, text="Clear", command=clear_info, height=1, width=22)
btn1.pack()


window.mainloop()
