import os
from image_parser import ImageParser
from model_image_analyser import ImageAnalyzer
import argparse
from dotenv import load_dotenv

model_dic = {
    "gemma": "google/gemma-3-4b-it",
    "llava": "llava-hf/llava-1.5-7b-hf",
    "qwen": "Qwen/Qwen2.5-VL-7B-Instruct",
}

def __load_environment_variables():
    # Load environment variables from a .env file
    load_dotenv()

def main():
    # Specify the folder containing images
    image_folder = 'images/'
    
    # Initialize the image parser and load images
    parser = ImageParser(image_folder)
    images = parser.load_images()  # Now a list of (filename, image) tuples

    # Read the token from the environment variable
    __load_environment_variables()
    token = os.getenv('HF_TOKEN')
    if not token:
        raise ValueError("HF_TOKEN environment variable is not set.")

    # Read the model from the command line argument
    parser = argparse.ArgumentParser("main.py")
    parser.add_argument("--model", help="Model to use", type=str, default="gemma")
    args = parser.parse_args()

    # Initialize the Llama 4 Scout model analyzer
    analyzer = ImageAnalyzer(model_path=args.model, token=token)

    # Analyze each image and print the health status
    for filename, image in images:
        health_status = analyzer.analyse_image(image, filename)
        print(f'{filename} - {health_status}')
        # Write also the results to an output file
        with open('output/results.txt', 'a') as f:
            f.write(f'{filename} - {health_status}\n')

if __name__ == '__main__':
    main()