import os
from PIL import Image

def convert_jpeg_to_png(input_path, output_path):
    """
    Convert a JPEG image to PNG format.
    
    :param input_path: Path to the input JPEG file
    :param output_path: Path to save the output PNG file
    """
    try:
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Convert to RGB mode if it's not already (handles CMYK, etc.)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save as PNG
            img.save(output_path, 'PNG')
        
        print(f"Conversion complete: {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Get the input JPEG file path
    input_file = input("Enter the path to the JPEG file: ").strip()
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print("Error: The specified input file does not exist.")
        return
    
    # Check if the input file is a JPEG
    if not input_file.lower().endswith(('.jpg', '.jpeg')):
        print("Error: The input file must be a JPEG image.")
        return
    
    # Get the output PNG file path
    output_file = input("Enter the path for the output PNG file: ").strip()
    
    # Add .png extension if not provided
    if not output_file.lower().endswith('.png'):
        output_file += '.png'
    
    # Perform the conversion
    convert_jpeg_to_png(input_file, output_file)

if __name__ == "__main__":
    main()
