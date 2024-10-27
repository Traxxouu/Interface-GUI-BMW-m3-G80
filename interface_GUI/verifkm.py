import obd
import tkinter as tk
from tkinter import messagebox

# Se connecter au port OBD-II - no protocol
def connect_to_obd():
    connection = obd.OBD()  # Auto-connect to USB or Bluetooth adapter
    if connection.is_connected():
        return connection
    else:
        return None

# Récupérer le kilométrage du véhicule
def get_vehicle_mileage(connection):
    # Code OBD-II PID pour le kilométrage éventuellement disponible
    command = obd.commands.DISTANCE_W_MIL  # Distance since codes cleared (en km)
    response = connection.query(command)
    if not response.is_null():
        mileage = response.value.to("km")
        return mileage
    else:
        return None

# Interface graphique avec Tkinter
def main():
    def check_mileage():
        connection = connect_to_obd()
        if connection:
            mileage = get_vehicle_mileage(connection)
            if mileage:
                messagebox.showinfo("Kilométrage", f"Kilométrage du véhicule: {mileage}")
            else:
                messagebox.showerror("Erreur", "Impossible de récupérer le kilométrage.")
            connection.close()
        else:
            messagebox.showerror("Erreur", "Impossible de se connecter à la prise OBD-II.")

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("OBD-II Kilométrage")
    root.geometry("300x150")

    # Bouton pour vérifier le kilométrage
    check_button = tk.Button(root, text="Vérifier le kilométrage", command=check_mileage)
    check_button.pack(pady=20)

    # Boucle principale Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
