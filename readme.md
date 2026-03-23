
A simple offline GUI for generating images using **Stable Diffusion v1.5 (pruned)** with **LCM LoRA**.  
Designed for **CPU-only systems** and fully **local usage** — no internet required after initial model download.

---

## 🗂 Project Structure


Image Generation/
├── generator.py # Core image generation logic
├── gui.py # Tkinter-based GUI
├── setup_models.py # Downloads required models
├── models/ # Local storage for models
│ ├── v1-5-pruned-emaonly.safetensors
│ └── lcm-lora-sdv1-5/
│ ├── pytorch_lora_weights.safetensors
│ ├── adapter_config.json
│ └── other files
├── output.png # Generated images (example)
├── README.md
├── .gitignore


---

## ⚡ Features

- Fully **offline** after setup  
- Uses **Stable Diffusion v1.5 (pruned)** for reduced size  
- Integrated **LCM LoRA** for **fast image generation**  
- Optimized for **CPU-only environments**  
- Simple and intuitive **Tkinter GUI**  
- Reusable **Python generator module**  
- **One-step model setup** script  

---

## 🖥️ Requirements

- Python **3.10+**

Install dependencies by running this in your terminal

   pip install diffusers transformers torch huggingface_hub safetensors peft accelerate safetensors 




🚀 Setup & Usage


1️⃣ Download Models

Run the setup script to automatically download:

Stable Diffusion v1.5 (pruned)
LCM LoRA adapter
python setup_models.py

This will create:

models/
├── v1-5-pruned-emaonly.safetensors
└── lcm-lora-sdv1-5/
    ├── pytorch_lora_weights.safetensors
    ├── adapter_config.json
    └── ...





2️⃣ Launch the GUI


python gui.py

Steps:

Enter a text prompt
Set inference steps (recommended: 4–8 for LCM)
Set guidance scale (recommended: ~1.0)
Choose output file location
Click Generate Image



3️⃣ Use in Python Scripts

You can also generate images programmatically:

from generator import generate_image

generate_image(
    prompt="a futuristic city at sunset, cinematic lighting",
    output_file="output.png",
    steps=6,
    guidance=1.0
)



🧰 Notes
Performance (CPU): ~20–40 seconds per 512×512 image
LCM LoRA: Enables high-quality output with very few steps
Keep models inside the models/ directory
.gitignore prevents uploading large model files
📝 License
Model weights follow Stable Diffusion / Hugging Face licenses
Project code can be licensed under MIT License 

⭐ Optional Enhancements

Add image preview inside the GUI
Support batch image generation
Include prompt presets / styles
Add progress indicator during generation


🤝 Contributing

Feel free to fork the repo and improve:

Performance optimizations
UI enhancements
Additional model support

Pull requests are welcome!

📌 Summary

This project provides a lightweight, offline-friendly Stable Diffusion GUI with:

Fast generation via LCM LoRA
Minimal setup using setup_models.py
Clean separation between GUI and generation logic

Perfect for low-resource systems and local experimentation.