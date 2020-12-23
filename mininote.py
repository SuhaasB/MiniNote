import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    #Open a file for editing
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    textb1.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textb1.insert(tk.END, text)
    window.title(f"MiniNote - {filepath}")

def save_file():
    #Save the current file as a new file.
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = textb1.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"MiniNote - {filepath}")

window = tk.Tk()
window.title("MiniNote")

#Top Frame
frame1 = tk.Frame(width=80, borderwidth = 2)             
frame1.pack(fill=tk.X)
btn1 = tk.Button(master=frame1, text="Open", command=open_file, width=10)
btn1.grid(row=0, column=0, sticky="ew", padx=2)
btn2 = tk.Button(master=frame1, text="Save As", command=save_file, width=10)
btn2.grid(row=0, column=1, sticky="ew", padx=2)

#Main Text Box 
textb1 = tk.Text(width=80, height=30)             
textb1.pack(fill=tk.BOTH)

window.mainloop()