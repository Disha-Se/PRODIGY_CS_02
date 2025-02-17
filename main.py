import PIL
from PIL import Image
import numpy as np
import requests
from io import BytesIO

def download_image(url):
    """Download an image from a URL and return it as a PIL image."""
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception("Failed to download image from URL.")

def encrypt_image(image_url, output_path):
    """Encrypt an image by swapping color channels and modifying pixel values."""
    img = download_image(image_url)  # Download image
    pixels = np.array(img)

    # Encryption logic (swap red & blue, modify green)
    encrypted_pixels = pixels.copy()
    encrypted_pixels[:, :, 0], encrypted_pixels[:, :, 2] = pixels[:, :, 2], pixels[:, :, 0]
    encrypted_pixels[:, :, 1] = np.clip(pixels[:, :, 1] + 50, 0, 255).astype(np.uint8)


    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_pixels)
    encrypted_img.save(output_path)
    print("Image encrypted and saved to", output_path)

def decrypt_image(image_url, output_path):
    """Decrypt an image by reversing the encryption steps."""
    img = download_image(image_url)  # Download encrypted image
    pixels = np.array(img)

    # Decryption logic (reverse the encryption steps)
    decrypted_pixels = pixels.copy()
    decrypted_pixels[:, :, 0], decrypted_pixels[:, :, 2] = pixels[:, :, 2], pixels[:, :, 0]
    decrypted_pixels[:, :, 1] = np.clip(pixels[:, :, 1] - 50, 0, 255).astype(np.uint8)

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_pixels)
    decrypted_img.save(output_path)
    print("Image decrypted and saved to", output_path)

# Example usage
encrypt_image(
    'tick.jpg',
    'images.jpg'
)

decrypt_image(
    'encrypted_image.jpg',
    'decrypted_image.jpg'
)
