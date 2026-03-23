# generator.py
import os
from diffusers import StableDiffusionPipeline, LCMScheduler
import torch
### save your model paths
SD_MODEL_PATH = "models/v1-5-pruned-emaonly.safetensors"
LCM_LORA_PATH = "models/lcm-lora-sdv1-5"
####

pipe = StableDiffusionPipeline.from_single_file(
    SD_MODEL_PATH,
    torch_dtype=torch.float32,
    local_files_only=True
).to("cpu")

pipe.load_lora_weights(LCM_LORA_PATH)
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
pipe.enable_attention_slicing()

# Function to generate image
def generate_image(prompt, output_file="output.png", steps=6, guidance=1.0):
    """
    Generate an image from a text prompt using your local SD + LCM LoRA.

    Args:
        prompt (str): The text prompt
        output_file (str): Output filename
        steps (int): Number of inference steps (LCM can be low)
        guidance (float): Guidance scale (LCM works best ~1.0)
    
    Returns:
        str: Path to saved image
    """
    image = pipe(
        prompt,
        num_inference_steps=steps,
        guidance_scale=guidance
    ).images[0]

    image.save(output_file)
    return output_file