import tkinter as tk
from tkinter import messagebox, scrolledtext
import time
import threading

# Helper functions for the layers
def to_binary(data):
    return ''.join(format(ord(char), '08b') for char in data)

def framing(data):
    datadd1 = ' '.join(format(ord(char), '08b') for char in data)
    Datadd1 = datadd1.split(" ")
    datadd1f = [format(len(i), '08b') + i for i in Datadd1]
    return datadd1f

def checksum_calc(binary_data):
    sum_val = sum(int(b, 2) for b in binary_data)
    val = bin(sum_val)[2:]
    return ''.join('1' if b == '0' else '0' for b in val)

def bit_stuff(data_list):
    BIT = ""
    one = 0
    for i in data_list:
        for j in i:
            BIT += j
            if j == "1":
                one += 1
            else:
                one = 0
            if one == 5:
                BIT += '0'
                one = 0
        BIT += " "
    return BIT.strip()

def mac_to_bin(mac):
    z1 = mac.replace(":", "")
    return bin(int(z1, 16))[2:].zfill(48)

# GUI Implementation
def run_simulation():
    sender_email = sender_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    msg = body_entry.get("1.0", tk.END).strip()

    if not sender_email or not receiver_email or not subject or not msg:
        messagebox.showwarning("Input Error", "Please fill all email fields!")
        return

    output_area.delete(1.0, tk.END)

    sender_mac = "6E:1A:2B:3C:4D:5E"
    receiver_mac = "5E:3B:2B:7C:4A:5E"

    output_area.insert(tk.END, f"Application Layer:\nEmail From: {sender_email}\nTo: {receiver_email}\nSubject: {subject}\nMessage: {msg}\n")
    output_area.insert(tk.END, f"Sender MAC: {sender_mac}\nReceiver MAC: {receiver_mac}\n\n")

    time.sleep(1)
    binary_data = to_binary(msg)
    output_area.insert(tk.END, f"Binary Conversion:\n{binary_data}\n\n")

    time.sleep(1)
    framed = framing(msg)
    output_area.insert(tk.END, f"Data Link Layer - Framing:\nFramed Data: {framed}\n\n")

    time.sleep(1)
    checksum = checksum_calc([b[8:] for b in framed])
    output_area.insert(tk.END, f"Checksum: {checksum}\n\n")

    time.sleep(1)
    bitstuffed = bit_stuff(framed)
    output_area.insert(tk.END, f"Bit Stuffed Data:\n{bitstuffed}\n\n")

    time.sleep(1)
    sender_bin = mac_to_bin(sender_mac)
    receiver_bin = mac_to_bin(receiver_mac)
    output_area.insert(tk.END, f"Physical Layer:\nSender MAC (bin): {sender_bin}\nReceiver MAC (bin): {receiver_bin}\n\n")

    time.sleep(1)
    output_area.insert(tk.END, "Network Layer:\nSource IP: 192.168.1.1\nDestination IP: 192.168.1.2\nRouting Protocol: RIP\n\n")

    time.sleep(1)
    output_area.insert(tk.END, "Transport Layer:\nProtocol: TCP\nSource Port: 12345\nDestination Port: 80\n\n")

    time.sleep(1)
    output_area.insert(tk.END, f"Session Layer:\nSession ID: 1234\nSession Between: {sender_mac} and {receiver_mac}\n\n")

def start_simulation():
    threading.Thread(target=run_simulation).start()

# Main GUI Window
root = tk.Tk()
root.title("Email Transmission Simulator - OSI Layers")
root.geometry("1000x900")
root.configure(bg="#f2f4f8")

# Email Form Frame
email_frame = tk.LabelFrame(root, text="Compose Email", padx=20, pady=20, font=("Arial", 14, "bold"), bg="white", fg="#333")
email_frame.pack(pady=15)

tk.Label(email_frame, text="From:", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky='e')
sender_entry = tk.Entry(email_frame, width=50, font=("Arial", 12))
sender_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(email_frame, text="To:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky='e')
receiver_entry = tk.Entry(email_frame, width=50, font=("Arial", 12))
receiver_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(email_frame, text="Subject:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky='e')
subject_entry = tk.Entry(email_frame, width=50, font=("Arial", 12))
subject_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(email_frame, text="Body:", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky='ne')
body_entry = tk.Text(email_frame, width=60, height=10, font=("Arial", 12), bg="#fdfdfd", relief=tk.GROOVE, bd=2)
body_entry.grid(row=3, column=1, padx=10, pady=5)

# Button to Start Simulation
send_btn = tk.Button(root, text="Send Email", command=start_simulation, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=20, pady=5)
send_btn.pack(pady=10)

# Output Display Area - Bigger and More Readable
output_area = scrolledtext.ScrolledText(
    root,
    width=100,         # Increased width
    height=165,         # Increased height
    font=("Courier", 12),  # Increased font size
    bg="black",
    fg="lime"
)
output_area.pack(pady=10)

root.mainloop()
