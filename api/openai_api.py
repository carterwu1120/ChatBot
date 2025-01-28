import base64
from openai import OpenAI
from api.llm_api import LlmApi

class OpenAiApi(LlmApi):

    def __init__(self) -> None:
        self.openai = OpenAI(api_key=self.envdata.openai_api_key)

    @staticmethod
    def __encode_image(image_path):
        """
        encode image
        """
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def generate_resopnse(self, input_text: str = "Hello, I worked very hard today. Could you please give me some warm feedback?", model: str = "gpt-4o"):
        """
        get openai response
        """

        response = self.openai.chat.completions.create(
            model=model,
            messages = [
                {
                    "role": "developer",
                    "content": self.role_description
                },
                {
                    "role": "user",
                    "content": input_text
                }
            ],
            max_tokens = 300,
            temperature = 0.7
        )
        return response.choices[0].message