import os
from dotenv import load_dotenv
import requests
# Load environment variables from .env file
load_dotenv()
##
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")
env = os.getenv("ENV")

print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")
print(f"Environment: {env}")

if debug_mode == "True":
    print("Debug mode is on.")

if env == "development":
    print("Running in development\ci environment.")
else:
    print("Running in production environment.")    
# Example request
try:
    response = requests.get("https://api.github.com")
    print(f"GitHub API Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
