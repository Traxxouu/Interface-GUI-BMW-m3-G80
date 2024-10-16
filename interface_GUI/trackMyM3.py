import tkinter as tk
from tkinter import ttk
import obd
import time
import threading

connection = obd.OBD()

cmd_speed = obd.commands.SPEED
cmd_rpm = obd.commands.RPM
cmd_temp = obd.commands.COOLANT_TEMP

def update_data():
    if connection.status() == obd.OBDStatus.CAR_CONNECTED:
        speed = connection.query(cmd_speed)
        rpm = connection.query(cmd_rpm)
        temp = connection.query(cmd_temp)
        
        speed_value.set(f"Vitesse : {speed.value.magnitude if speed.value else 0} km/h")
        rpm_value.set(f"RPM : {rpm.value.magnitude if rpm.value else 0}")
        temp_value.set(f"Température moteur : {temp.value.magnitude if temp.value else 0} °C")
    else:
        speed_value.set("Pas de connexion à l'OBD-II")
        rpm_value.set("Pas de connexion à l'OBD-II")
        temp_value.set("Pas de connexion à l'OBD-II")

    root.after(1000, update_data)

root = tk.Tk()
root.title("M3 Performance Tracker")

style = ttk.Style()
style.theme_use('clam')

speed_value = tk.StringVar()
rpm_value = tk.StringVar()
temp_value = tk.StringVar()

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

speed_label = ttk.Label(frame, textvariable=speed_value, font=('Helvetica', 16))
speed_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

rpm_label = ttk.Label(frame, textvariable=rpm_value, font=('Helvetica', 16))
rpm_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

temp_label = ttk.Label(frame, textvariable=temp_value, font=('Helvetica', 16))
temp_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

quit_button = ttk.Button(frame, text="Quitter", command=root.quit)
quit_button.grid(row=3, column=0, padx=5, pady=5)

update_data()

root.mainloop()
