import tkinter as tk
import smtplib
import random
from tkinter import messagebox
from tkinter import *

window = tk.Tk()
window.title("Email OTP Verification")
bg=PhotoImage(file="op.png")
lb=Label(window,image=bg)
lb.place(x=0,y=0)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'mansichawan2002@gmail.com'
smtp_password = 'wvlxzvrikdguituy'
otp = random.randint(100000, 999999)

def send_email():
    to_address = recipient_entry.get()
    subject = 'OTP Verification'
    body = f'Your OTP code is: {otp}'
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_address, message)
    tk.messagebox.showinfo('Email Sent', 'Your OTP code has been sent to your email address.')

def verify_otp():
    entered_otp = otp_entry.get()
    if int(entered_otp) == otp:
        tk.messagebox.showinfo('Success', 'OTP verification successful!')
    else:
        tk.messagebox.showerror('Error', 'Incorrect OTP code. Please try again.')


recipient_label = tk.Label(window, text="Recipient Email:",width=30,height=5)
recipient_label.pack()
recipient_entry = tk.Entry(window, width=40,bg='pink')
recipient_entry.pack()
send_button = tk.Button(window, text="Send OTP", command=send_email,fg='white',bg='green')
send_button.pack()
otp_label = tk.Label(window, text="Enter OTP:",width=30,height=5)
otp_label.pack()
otp_entry = tk.Entry(window, width=10,bg='lightgreen')
otp_entry.pack()
verify_button = tk.Button(window, text="Verify OTP", command=verify_otp,fg='white',bg='black')
verify_button.pack()

window.mainloop()