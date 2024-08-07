from db import init_db
from ui import VehicleMaintenanceApp
import tkinter as tk

def main():
    init_db()

    root = tk.Tk()
    app = VehicleMaintenanceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
