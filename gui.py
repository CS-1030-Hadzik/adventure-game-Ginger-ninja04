# gui.py
import tkinter as tk
import game_logic  # your main game file

def submit_text():
    result = game_logic.process_command(entry.get())
    output_label.config(text=result)

# Tkinter setup ...
