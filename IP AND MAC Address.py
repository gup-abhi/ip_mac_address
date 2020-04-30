# importing tkinter
import tkinter as tk
# importing showinfo from tkinter as messagebox
from tkinter.messagebox  import showinfo
# importing socket module
import socket
# importing getmac module
from getmac import getmac

# creating window
win = tk.Tk()
# specifying background color
win.config(bg="#F1C40F")
# giving title to our window
win.title("Find IP and MAC Address")

# creating a function to get ip address
def ip():
    # getting hostname of the machine
    hostname = socket.gethostname()
    # getting ip address of the hostname
    ip_add = socket.gethostbyname(hostname)
    # showing ip address in a show info box
    showinfo("IP Address", f"IP Address : {ip_add}")

# creating a function to get mac address
def mac():
    # getting mac address
    mac_add = getmac.get_mac_address()
    # showing mac address in a showinfo box
    showinfo("MAC Address", f"MAC Address : {mac_add}")

# creating a button to show ip address and calling our function to display it
ip_button = tk.Button(win,text = "Show IP Address", bg="#F1C40F", font = ("times new roman",16,"bold"),command=ip)
ip_button.pack()

# creating a button to show mac address and calling our function to display it
mac_button = tk.Button(win,text = "Show MAC Address", bg="#F1C40F", font = ("times new roman",16,"bold"),command=mac)
mac_button.pack()

# creating window loop
win.mainloop()
