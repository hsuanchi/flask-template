import os
from dotenv import load_dotenv

# load .env
# dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path, override=True)

from app import create_app
app = create_app('testing')
# app = create_app('development')

if __name__ == "__main__":
    app.run(debug=True)
