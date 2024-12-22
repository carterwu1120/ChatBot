"""
Get api key from this script.
"""
import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from dotenv import set_key
from utils.singleton import Singleton

class EnvData(metaclass=Singleton):
    """
    env data
    """

    def __init__(self) -> None:
        self.env_path = r"./.env"
        self.env_example_path = r"./.env.example"
        self.openai_api_key = str
        self.copy_env_file()
        self.load_env_file()
    
    def copy_env_file(self):
        """
        Copies .env.example to .env if .env does not exit.
        """
        if not os.path.exists(self.env_path):
            if os.path.exists(self.env_example_path):
                shutil.copyfile(self.env_example_path, self.env_path)
                print(f"Copied {self.env_example_path} to {self.env_path}")
                exit(1)
            else:
                print(f"{self.env_example_path} does not exist.")
        else:
            print(f"{self.env_path} already exists")

    def load_env_file(self):
        """
        load env file to get api
        """
        dotenv_path = Path(self.env_path)
        load_dotenv(dotenv_path=dotenv_path, override=True)
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.ollama_server = os.getenv("OLLAMA_SERVER")

    def save_env_file(self):
        """
        save env file
        """
        set_key(
            dotenv_path=self.env_path,
            key_to_set="OPENAI_API_KEY",
            value_to_set=self.openai_api_key
        )
        set_key(
            dotenv_path=self.env_path,
            key_to_set="OLLAMA_SERVER",
            value_to_set=self.ollama_server
        )

