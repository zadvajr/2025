import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

name = os.getenv('NAME', 'No Name')
print(f'Hello {name}')