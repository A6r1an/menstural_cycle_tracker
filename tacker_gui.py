import tkinter as tk
from tkinter import messagebox
import datetime
from Cycle_tracker import PeriodTracker

class PeriodTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Period Tracker')
        self.configure(bg='#FFD1DC') # Background color lightpink
        self.tracker = PeriodTracker()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text='Welcome to your period tracker!', bg='#FFD1DC').pack(pady=10)
        self.cycle_length_entry =tk.Entry(self)
        self.cycle_length_entry.pack(pady=5)
        tk.Button(self, text="Set Cycle Length", command=self.set_cycle_length).pack(pady=5)
        tk.Button(self, text="Calculate Next Period", command=self.calculate_next_period_date).pack(pady=5)

    def set_cycle_length(self):
        cycle_length = self.cycle_length_entry.get()
        try:
            self.tracker.set_cycle_length(int(cycle_length))
            messagebox.showinfo("Success", "Cycle length set sucessfully")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number")

    def calculate_next_period_date(self):
        try:
            next_period_date = self.tracker.calculate_next_period_date()
            messagebox.showinfo("Next Period Date", f"Your next period date is {next_period_date}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    app = PeriodTrackerApp()
    app.mainloop()
