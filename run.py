import tkinter as tk
from tkinter import ttk, messagebox

# Initialize main window
root = tk.Tk()
root.title("CyberDudeBivash's Threat Analyser App")
root.geometry("700x500")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="CyberDudeBivash's Threat Analyser", font=("Helvetica", 20, "bold"), fg="blue")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Entry Label and Field
entry_label = tk.Label(input_frame, text="Enter IP / URL / Hash:", font=("Helvetica", 12))
entry_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = tk.Entry(input_frame, width=50, font=("Helvetica", 12))
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Dropdown for Analysis Type
analysis_type_label = tk.Label(input_frame, text="Select Analysis Type:", font=("Helvetica", 12))
analysis_type_label.grid(row=1, column=0, padx=5, pady=5)

analysis_type = ttk.Combobox(input_frame, values=["IP Analysis", "URL Scan", "Hash Lookup", "CVE Lookup"], width=47)
analysis_type.grid(row=1, column=1, padx=5, pady=5)
analysis_type.current(0)

# Analyze Button
def analyze():
    input_value = input_entry.get().strip()
    analysis_choice = analysis_type.get()

    result_text.delete(1.0, tk.END)
    if not input_value:
        messagebox.showwarning("Input Required", "Please enter a value to analyze.")
        return
    result = f"Running {analysis_choice} on:\n{input_value}\n\n[Results will appear here]\n"
    result_text.insert(tk.END, result)

analyze_button = tk.Button(root, text="Run Analysis", font=("Helvetica", 12), command=analyze, bg="green", fg="white")
analyze_button.pack(pady=10)

# Result Display Frame
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

result_text = tk.Text(result_frame, height=15, width=80, font=("Courier", 10), wrap=tk.WORD)
result_text.pack()

# Run the GUI loop
root.mainloop()
