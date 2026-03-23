# setup_models.py
from huggingface_hub import snapshot_download, hf_hub_download
import os

# Folder to store models
MODELS_DIR = "models"
os.makedirs(MODELS_DIR, exist_ok=True)

SD_MODEL_FILENAME = "v1-5-pruned-emaonly.safetensors"
SD_MODEL_PATH = os.path.join(MODELS_DIR, SD_MODEL_FILENAME)

if not os.path.exists(SD_MODEL_PATH):
    print("Downloading Stable Diffusion v1.5 pruned model...")
    hf_hub_download(
        repo_id="runwayml/stable-diffusion-v1-5",
        filename=SD_MODEL_FILENAME,
        local_dir=MODELS_DIR,
        local_dir_use_symlinks=False
    )
    print(f"Downloaded SD pruned model to {SD_MODEL_PATH}")
else:
    print(f"Pruned SD model already exists at {SD_MODEL_PATH}")

LCM_DIR = os.path.join(MODELS_DIR, "lcm-lora-sdv1-5")

if not os.path.exists(LCM_DIR):
    print("Downloading LCM LoRA for Stable Diffusion v1.5...")
    snapshot_download(
        repo_id="latent-consistency/lcm-lora-sdv1-5",
        local_dir=LCM_DIR,
        local_dir_use_symlinks=False
    )
    print(f"Downloaded LCM LoRA to {LCM_DIR}")
else:
    print(f"LCM LoRA already exists at {LCM_DIR}")

print("\nAll models are ready! You can now run gui.py or generator.py")