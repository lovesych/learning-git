import os,sys
print(sys.executable)
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
db_password = os.getenv("DB_PSSWORD")
print(f"API Key: {api_key}")
print(f"Database Password: {db_password}")