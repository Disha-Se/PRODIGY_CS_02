# PRODIGY_CS_02

# Image Encryption and Decryption

This project provides a simple Python script to encrypt and decrypt images by modifying pixel values and swapping color channels.

## Features
- **Encrypt an image**: Swaps red and blue channels, modifies the green channel.
- **Decrypt an image**: Reverses the encryption process to restore the original image.
- **Supports downloading images from URLs**.

## Requirements
Make sure you have Python installed along with the required dependencies.

### Install Dependencies
```sh
pip install pillow numpy requests
```

## Usage

### Encrypt an Image
```python
python main.py encrypt <input_image_path> <output_image_path>
```
Example:
```python
python main.py encrypt tick.jpg encrypted_image.jpg
```

### Decrypt an Image
```python
python main.py decrypt <input_image_path> <output_image_path>
```
Example:
```python
python main.py decrypt encrypted_image.jpg decrypted_image.jpg
```

## Project Structure
```
├── main.py         # Contains encryption and decryption functions
├── README.md       # This file
```

## How It Works
1. The script reads an image and converts it into a NumPy array.
2. Encryption swaps red and blue color channels and modifies the green channel.
3. Decryption reverses these changes to restore the original image.
4. The processed images are saved to the specified output file.

## Author
Disha Sejpal

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

