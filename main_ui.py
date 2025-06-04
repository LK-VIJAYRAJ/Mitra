import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import random

from nlp.emotion_rules import basic_emotion_rule
from utils.helpers import format_message
from vector_db.memory import store_embedding

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compassionate Calendar Companion")

        self.event_entry = tk.Entry(root, width=40)
        self.event_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Event", command=self.add_event)
        self.add_button.pack(pady=5)

        self.events_display = tk.Text(root, width=50, height=15)
        self.events_display.pack(pady=10)

        self.events = []

    def add_event(self):
        event_text = self.event_entry.get()
        if not event_text:
            messagebox.showwarning("Empty Entry", "Please enter an event.")
            return

        emotion = basic_emotion_rule(event_text)
        message = format_message(event_text, emotion)

        store_embedding(event_text, [0.1] * 128)  # Dummy embedding

        event_time = datetime.now() + timedelta(minutes=len(self.events) * 5)
        formatted_time = event_time.strftime('%H:%M')

        display_text = f"[{formatted_time}] {event_text} → {message}\n"
        self.events_display.insert(tk.END, display_text)

        self.events.append((event_text, emotion))
        self.event_entry.delete(0, tk.END)

def launch_ui():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
