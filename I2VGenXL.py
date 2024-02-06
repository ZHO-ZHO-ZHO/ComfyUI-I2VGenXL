import os
import cv2
import torch
import numpy as np
from PIL import Image
import folder_paths

from huggingface_hub import hf_hub_download
from diffusers import I2VGenXLPipeline

current_directory = os.path.dirname(os.path.abspath(__file__))
device = "cuda" if torch.cuda.is_available() else "cpu"

class I2VGenXL_ModelLoader_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_model_path": ("STRING", {"default": "ali-vilab/i2vgen-xl"}),
            }
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("pipe",)
    FUNCTION = "load_model"
    CATEGORY = "📽️I2VGenXL"
  
    def load_model(self, base_model_path):
        # Code to load the base model
        pipe = I2VGenXLPipeline.from_pretrained(
            base_model_path,
            torch_dtype=torch.float16,
            variant="fp16"
        )
        pipe.enable_model_cpu_offload()
        return [pipe]


class I2VGenXL_Generation_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pipe": ("MODEL",),
                "image": ("IMAGE",),
                "positive": ("STRING", {"default": "Papers were floating in the air on a table in the library", "multiline": True}),
                "negative": ("STRING", {"default": "Distorted, discontinuous, Ugly, blurry, low resolution, motionless, static, disfigured, disconnected limbs, Ugly faces, incomplete arms", "multiline": True}),
                "steps": ("INT", {"default": 50, "min": 1, "max": 100, "step": 1}),
                "guidance_scale": ("FLOAT", {"default": 9, "min": 0, "max": 10}),
                "width": ("INT", {"default": 1280, "min": 512, "max": 2048, "step": 32}),
                "height": ("INT", {"default": 704, "min": 512, "max": 2048, "step": 32}), 
                "num_frames": ("INT", {"default": 16, "min": 1, "max": 100, "step": 1}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "i2vgenxl_generate_image"
    CATEGORY = "📽️I2VGenXL"
                       
    def i2vgenxl_generate_image(self, image, pipe, positive, negative, steps, guidance_scale, seed, width, height, num_frames):
        
        pil_images = []
        image_np = (255. * image.cpu().numpy().squeeze()).clip(0, 255).astype(np.uint8)
        pil_image = Image.fromarray(image_np)
        pil_images.append(pil_image)
        
        generator = torch.Generator(device=device).manual_seed(seed)

        output = pipe(
            image=pil_images,
            prompt=positive,
            negative_prompt=negative,
            num_inference_steps=steps,
            generator=generator,
            guidance_scale=guidance_scale,
            num_frames=num_frames,
            width=width,
            height=height,
            output_type="pt",
            )

        video_tensor = output.frames 
        video_nhwc = video_tensor[0].permute(0, 2, 3, 1)

        video_nhwc = video_nhwc[:-1]

        return (video_nhwc,) 

NODE_CLASS_MAPPINGS = {
    "I2VGenXL_ModelLoader_Zho": I2VGenXL_ModelLoader_Zho,
    "I2VGenXL_Generation_Zho": I2VGenXL_Generation_Zho,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "I2VGenXL_ModelLoader_Zho": "📽️I2VGenXL Model Loader",
    "I2VGenXL_Generation_Zho": "📽️I2VGenXL Generation",
}
