# https://github.com/ollama/ollama-python/blob/main/pyproject.toml
# https://medium.com/@simon3458/ollama-llm-model-as-a-service-introduction-d849fb6d9ced
# https://ollama.com/library?sort=popular

from ollama import Client, ResponseError
from api.llm_api import LlmApi

class OllamaApi(LlmApi):
    """
    class of ollama api
    """

    def __init__(self):
        self.client = Client(host = self.envdata.ollama_server)

    def generate_resopnse(self, input_text: str = "Hello, I worked very hard today. Could you please give me some warm feedback?", model: str = "llama2:13b"):
        """
        generate response
        """
        messages = [
            {"role": "system", "content": self.role_description},
            {"role": "user", "content": input_text}
        ]

        response = self.client.chat(
            model = model,
            messages = messages
        )

        return response['message']['content']


if __name__ == '__main__':
    llm = OllamaApi()
    resopnse = llm.generate_resopnse()
    print(resopnse)