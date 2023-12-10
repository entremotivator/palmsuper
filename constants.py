import os
import dotenv

dotenv.load_dotenv()


SESSION_HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('PALM_API_KEY')}"
}
