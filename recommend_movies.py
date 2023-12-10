# recommend_movies.py

import os
import urllib.parse
import requests
import time
from google.generativeai import palm
from constants import SESSION_HEADERS

class RecommendMovies:
    def __init__(self, api_key: str) -> None:
        self.model = palm
        self.model.configure(api_key=api_key)

        self.session = requests.Session()
        self.session.headers = SESSION_HEADERS

        self.defaults = {
            'model': 'models/text-bison-001',
            'temperature': 0.7,
            'candidate_count': 1,
            'top_k': 40,
            'top_p': 0.95,
            'max_output_tokens': 1024,
            'stop_sequences': [],
            'safety_settings': [
                {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
                # ... (other settings)
            ],
        }

    def urlify_string(self, string):
        url_encoded = urllib.parse.quote(string)
        return url_encoded

    def generate(self, movie_name=str):
        result = []

        prompt = f"""input: Th Dark Knight 
            output: Batman Begins
            The Prestige
            Se7en
            Fight Club
            The Shawshank Redemption
            input: {movie_name}
            output:"""

        response = self.model.generate_text(
            **self.defaults,
            prompt=prompt
        )

        recommendations = response.result.split("\n")
        time.sleep(0.1)
        for i in recommendations:
            movie = self.urlify_string(i)
            url = f"https://api.themoviedb.org/3/search/movie?query={movie}&include_adult=false&language=en-US&page=1"
            res = self.session.get(url).json()
            result.append(res["results"])

        return result
secrets.toml:
toml
Copy code
# secrets.toml

[palm_api]
key = "your_api_key_here"
