import tkinter as tk
from tkinter import messagebox
import wikipediaapi
import webbrowser

def fetch_wikipedia_info():
    keyword = entry.get()
    language = lang_var.get()
    if not keyword.strip():
        messagebox.showwarning("Input Error", "Please enter a keyword.")
        return

    try:
        wiki = wikipediaapi.Wikipedia(language=language, user_agent="InfoFetch/1.0")
        page = wiki.page(keyword)

        if page.exists():
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, page.summary)
            word_count.set(f"Words: {len(page.summary.split())}")
            char_count.set(f"Characters: {len(page.summary)}")
        else:
            messagebox.showerror("Not Found", f"No information found for '{keyword}'.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def clear_content():
    entry.delete(0, tk.END)
    text_box.delete(1.0, tk.END)
    word_count.set("Words: 0")
    char_count.set("Characters: 0")

def open_in_browser():
    keyword = entry.get()
    language = lang_var.get()
    if not keyword.strip():
        messagebox.showwarning("Input Error", "Please enter a keyword.")
        return

    url = f"https://{language}.wikipedia.org/wiki/{keyword.replace(' ', '_')}"
    webbrowser.open(url)

root = tk.Tk()
root.title("InfoFetch - Wikipedia Keyword Search")
root.geometry("1000x700")
root.config(bg="#f4f6f9")

title_label = tk.Label(root, text="InfoFetch:Keyword Search", font=("Arial", 18, "bold"), bg="#f4f6f9", fg="#333")
title_label.pack(pady=20)

lang_var = tk.StringVar(value="en")
lang_menu = tk.OptionMenu(root, lang_var, "en", "es", "fr", "de", "it", "ru", "zh")
lang_menu.config(font=("Arial", 12))
lang_menu.pack(pady=5)

label = tk.Label(root, text="Enter Keyword:", font=("Arial", 12), bg="#f4f6f9", fg="#333")
label.pack(pady=5)

entry = tk.Entry(root, width=60, font=("Arial", 14), bd=2, relief="solid", borderwidth=2, highlightthickness=1)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", width=20, height=2, command=fetch_wikipedia_info)
search_button.pack(pady=10)

text_box = tk.Text(root, wrap=tk.WORD, font=("Arial", 14), height=20, width=90, bd=2, relief="solid", highlightthickness=1, bg="#fff")
text_box.pack(pady=10)

button_frame = tk.Frame(root, bg="#f4f6f9")
button_frame.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), bg="#FF5722", fg="white", width=15, command=clear_content)
clear_button.grid(row=0, column=0, padx=10)

browser_button = tk.Button(button_frame, text="Open in Browser", font=("Arial", 12), bg="#795548", fg="white", width=15, command=open_in_browser)
browser_button.grid(row=0, column=1, padx=10)

status_frame = tk.Frame(root, bg="#f4f6f9")
status_frame.pack(pady=10)

word_count = tk.StringVar(value="Words: 0")
char_count = tk.StringVar(value="Characters: 0")

word_label = tk.Label(status_frame, textvariable=word_count, font=("Arial", 12), bg="#f4f6f9", fg="#333")
word_label.grid(row=0, column=0, padx=10)

char_label = tk.Label(status_frame, textvariable=char_count, font=("Arial", 12), bg="#f4f6f9", fg="#333")
char_label.grid(row=0, column=1, padx=10)


root.mainloop()
