from transformers import pipeline
from huggingface_hub import login

class ImageAnalyzer:
    def __init__(self, model_path, token):
        self.model_path = model_path
        self.HF_TOKEN = token
        login(token=self.HF_TOKEN)
        self.pipe = pipeline("image-text-to-text", model=self.model_path)

    def analyse_image(self, image, filename):
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image
                        }
                    },
                    {
                        "type": "text",
                        "text": f"Analyze the health of the plant in the image {filename}. Tell me if it's Healthy or Sick. As an answer, only write Healthy or Sick.",
                    },
                ]
            },
        ]

        return self.pipe(text=messages)

    def get_health_status(self, image, filename):
        # Get the health status of the plant based on the analysis
        prediction = self.analyse_image(image, filename)
        return prediction