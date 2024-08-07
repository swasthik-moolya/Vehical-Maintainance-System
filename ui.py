import tkinter as tk
from tkinter import messagebox
from db import get_db_connection

class VehicleMaintenanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Maintenance Tracker")

        self.create_widgets()

    def create_widgets(self):
        # Create widgets for vehicle entry
        self.vehicle_frame = tk.Frame(self.root)
        self.vehicle_frame.pack()

        tk.Label(self.vehicle_frame, text="Make").grid(row=0, column=0)
        tk.Label(self.vehicle_frame, text="Model").grid(row=0, column=1)
        tk.Label(self.vehicle_frame, text="Year").grid(row=0, column=2)
        tk.Label(self.vehicle_frame, text="VIN").grid(row=0, column=3)

        self.make_entry = tk.Entry(self.vehicle_frame)
        self.model_entry = tk.Entry(self.vehicle_frame)
        self.year_entry = tk.Entry(self.vehicle_frame)
        self.vin_entry = tk.Entry(self.vehicle_frame)

        self.make_entry.grid(row=1, column=0)
        self.model_entry.grid(row=1, column=1)
        self.year_entry.grid(row=1, column=2)
        self.vin_entry.grid(row=1, column=3)

        self.add_vehicle_button = tk.Button(self.vehicle_frame, text="Add Vehicle", command=self.add_vehicle)
        self.add_vehicle_button.grid(row=1, column=4)

        # Create listbox to display vehicles
        self.vehicle_listbox = tk.Listbox(self.root)
        self.vehicle_listbox.pack()

        self.refresh_vehicle_list()

    def add_vehicle(self):
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        vin = self.vin_entry.get()

        conn = get_db_connection()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO vehicle (make, model, year, vin) VALUES (?, ?, ?, ?)",
                      (make, model, year, vin))
            conn.commit()
            messagebox.showinfo("Success", "Vehicle added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Vehicle with this VIN already exists.")
        finally:
            conn.close()

        self.refresh_vehicle_list()

    def refresh_vehicle_list(self):
        self.vehicle_listbox.delete(0, tk.END)
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM vehicle")
        vehicles = c.fetchall()
        conn.close()

        for vehicle in vehicles:
            self.vehicle_listbox.insert(tk.END, f"{vehicle[1]} {vehicle[2]} ({vehicle[3]}) - {vehicle[4]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleMaintenanceApp(root)
    root.mainloop()
