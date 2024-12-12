import tkinter as tk
from tkinter import messagebox
import wikipediaapi

def fetch_wikipedia_info():
    keyword = entry.get()
    if not keyword.strip():
        messagebox.showwarning("Input Error", "Please enter a keyword.")
        return
    
    try:
        
        wiki = wikipediaapi.Wikipedia(
            language='en',
            user_agent="InfoFetch/1.0 (lasyareddypullur05@gmail.com)"
        )
        
        page = wiki.page(keyword)

        if page.exists():
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, page.summary)
        else:
            messagebox.showerror("Not Found", f"No information found for '{keyword}'.")
    except wikipediaapi.WikipediaException as we:
        messagebox.showerror("API Error", f"Error with Wikipedia API: {we}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

root = tk.Tk()
root.title("InfoFetch - Wikipedia Keyword Search")
root.geometry("900x600")  # Larger window for better readability
root.config(bg="#f4f6f9")  # Soft background color

title_label = tk.Label(root, text="InfoVerse: Wikipedia Keyword Search", font=("Arial", 18, "bold"), bg="#f4f6f9", fg="#333")
title_label.pack(pady=20)

label = tk.Label(root, text="Enter Keyword:", font=("Arial", 12), bg="#f4f6f9", fg="#333")
label.pack(pady=5)

entry = tk.Entry(root, width=60, font=("Arial", 14), bd=2, relief="solid", borderwidth=2, highlightthickness=1)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", width=20, height=2, command=fetch_wikipedia_info)
search_button.pack(pady=10)

text_box = tk.Text(root, wrap=tk.WORD, font=("Arial", 14), height=20, width=90, bd=2, relief="solid", highlightthickness=1, bg="#fff")
text_box.pack(pady=20)

root.mainloop()
