import os
from dotenv import load_dotenv

load_dotenv()

ORIGIN = os.getenv("ORIGIN")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")
