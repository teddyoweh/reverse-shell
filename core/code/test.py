import sys
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

passs = os.getenv('password')
print(passs)