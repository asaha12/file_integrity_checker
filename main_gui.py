import tkinter as tk
from tkinter import filedialog
from utils.integrity_checker import calculate_md5, calculate_sha256

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)

def calculate_hashes():
    file_path1 = entry_file_path1.get()
    file_path2 = entry_file_path2.get()
    
    if file_path1 and file_path2:
        md5_hash1 = calculate_md5(file_path1)
        sha256_hash1 = calculate_sha256(file_path1)
        
        md5_hash2 = calculate_md5(file_path2)
        sha256_hash2 = calculate_sha256(file_path2)
        
        entry_md5_1.delete(0, tk.END)
        entry_md5_1.insert(tk.END, md5_hash1)
        entry_sha256_1.delete(0, tk.END)
        entry_sha256_1.insert(tk.END, sha256_hash1)
        
        entry_md5_2.delete(0, tk.END)
        entry_md5_2.insert(tk.END, md5_hash2)
        entry_sha256_2.delete(0, tk.END)
        entry_sha256_2.insert(tk.END, sha256_hash2)
        
        compare_hashes(md5_hash1, sha256_hash1, md5_hash2, sha256_hash2)
    else:
        display_warning("Please select both files.")

def compare_hashes(md5_hash1, sha256_hash1, md5_hash2, sha256_hash2):
    if md5_hash1 == md5_hash2 and sha256_hash1 == sha256_hash2:
        label_warning.config(text="No changes detected.")
    else:
        label_warning.config(text="Warning: Changes detected!")

def display_warning(message):
    label_warning.config(text=message)

root = tk.Tk()
root.title("File Integrity Checker")

frame = tk.Frame(root)
frame.pack(pady=20)

label_file_path1 = tk.Label(frame, text="File 1 Path:")
label_file_path1.grid(row=0, column=0, padx=10, pady=5, sticky="E")

entry_file_path1 = tk.Entry(frame, width=40)
entry_file_path1.grid(row=0, column=1, padx=10, pady=5)

button_browse1 = tk.Button(frame, text="Browse", command=lambda: browse_file(entry_file_path1))
button_browse1.grid(row=0, column=2, padx=10, pady=5)

label_md5_1 = tk.Label(frame, text="File 1 MD5 Hash:")
label_md5_1.grid(row=1, column=0, padx=10, pady=5, sticky="E")

entry_md5_1 = tk.Entry(frame, width=40)
entry_md5_1.grid(row=1, column=1, padx=10, pady=5)

label_sha256_1 = tk.Label(frame, text="File 1 SHA256 Hash:")
label_sha256_1.grid(row=2, column=0, padx=10, pady=5, sticky="E")

entry_sha256_1 = tk.Entry(frame, width=40)
entry_sha256_1.grid(row=2, column=1, padx=10, pady=5)

label_file_path2 = tk.Label(frame, text="File 2 Path:")
label_file_path2.grid(row=3, column=0, padx=10, pady=5, sticky="E")

entry_file_path2 = tk.Entry(frame, width=40)
entry_file_path2.grid(row=3, column=1, padx=10, pady=5)

button_browse2 = tk.Button(frame, text="Browse", command=lambda: browse_file(entry_file_path2))
button_browse2.grid(row=3, column=2, padx=10, pady=5)

label_md5_2 = tk.Label(frame, text="File 2 MD5 Hash:")
label_md5_2.grid(row=4, column=0, padx=10, pady=5, sticky="E")

entry_md5_2 = tk.Entry(frame, width=40)
entry_md5_2.grid(row=4, column=1, padx=10, pady=5)

label_sha256_2 = tk.Label(frame, text="File 2 SHA256 Hash:")
label_sha256_2.grid(row=5, column=0, padx=10, pady=5, sticky="E")

entry_sha256_2 = tk.Entry(frame, width=40)
entry_sha256_2.grid(row=5, column=1, padx=10, pady=5)

button_check = tk.Button(root, text="Check Integrity", command=calculate_hashes)
button_check.pack(pady=10)

label_warning = tk.Label(root, fg="red")
label_warning.pack(pady=10)

root.mainloop()
