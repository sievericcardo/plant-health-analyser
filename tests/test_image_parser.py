import os
import unittest
from src.image_parser import ImageParser

class TestImageParser(unittest.TestCase):
    def setUp(self):
        self.parser = ImageParser()
        self.test_directory = 'test_images'  # Directory for test images

        # Create a test directory if it doesn't exist
        if not os.path.exists(self.test_directory):
            os.makedirs(self.test_directory)

        # Add test images to the directory (mocking for the purpose of this test)
        # In a real scenario, you would have actual image files to test with.

    def tearDown(self):
        # Clean up the test directory after tests
        for filename in os.listdir(self.test_directory):
            file_path = os.path.join(self.test_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(self.test_directory)

    def test_load_images(self):
        # Test loading images from the directory
        images = self.parser.load_images(self.test_directory)
        self.assertIsInstance(images, list)
        self.assertGreater(len(images), 0)  # Assuming there are images to load

    def test_preprocess_image(self):
        # Test preprocessing of a single image
        test_image_path = 'image.jpg'  # Replace with an actual test image path
        processed_image = self.parser.preprocess_image(test_image_path)
        self.assertIsNotNone(processed_image)  # Ensure the image is processed

if __name__ == '__main__':
    unittest.main()