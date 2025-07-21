class ImageParser:
    def __init__(self, directory):
        self.directory = directory

    def load_images(self):
        import os
        from PIL import Image

        images = []
        for filename in os.listdir(self.directory):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(self.directory, filename)
                with Image.open(img_path) as img:
                    images.append((filename, img.copy()))  # Store tuple (filename, image)
        return images

    def preprocess_images(self, images):
        processed_images = []
        for img in images:
            img = img.resize((224, 224))  # Resize to model input size
            processed_images.append(img)
        return processed_images