# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from generator import generate_image

root = tk.Tk()
root.title("Image Generator")
root.geometry("500x200")

# Prompt label
tk.Label(root, text="Enter your prompt:").pack(pady=5)
prompt_entry = tk.Entry(root, width=60)
prompt_entry.pack(pady=5)

# Steps
tk.Label(root, text="Number of steps (LCM fast 4-8):").pack(pady=5)
steps_entry = tk.Entry(root, width=10)
steps_entry.insert(0, "6")
steps_entry.pack()

# Guidance
tk.Label(root, text="Guidance scale (~1.0 for LCM):").pack(pady=5)
guidance_entry = tk.Entry(root, width=10)
guidance_entry.insert(0, "1.0")
guidance_entry.pack()

# Generate button
def on_generate():
    prompt = prompt_entry.get()
    steps = int(steps_entry.get())
    guidance = float(guidance_entry.get())
    
    if not prompt.strip():
        messagebox.showerror("Error", "Please enter a prompt!")
        return
    
    output_file = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save generated image as..."
    )
    
    if not output_file:
        return
    
    try:
        generate_image(prompt, output_file, steps, guidance)
        messagebox.showinfo("Success", f"Image saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="Generate Image", command=on_generate).pack(pady=10)

root.mainloop()