import tkinter as tk
import pyshorteners
from tkinter import messagebox

def shorten_url():
    try:
        # Create Shortener instance
        shortener = pyshorteners.Shortener()

        # Get long URL from entry field
        long_url = longurl_entry.get()

        if long_url:
            # Shorten the URL using Google's service
            short_url = shortener.tinyurl.short(long_url)
            shorturl_entry.delete(0, tk.END)
            shorturl_entry.insert(0, short_url)
        else:
            messagebox.showwarning("Warning", "Please enter a URL.")

    except Exception as e:
        print(f"Error: {str(e)}")
        shorturl_entry.delete(0, tk.END)
        shorturl_entry.insert(0, "Error: An error occurred during shortening.")

# Create main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("300x150")

# Create and position widgets
longurl_label = tk.Label(root, text="Enter Long URL")
longurl_entry = tk.Entry(root)
shorturl_label = tk.Label(root, text="Output Shortened URL")
shorturl_entry = tk.Entry(root)
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()

# Start main loop
root.mainloop()
