import random
from locust import HttpUser, task, between


class EmbeddingUser(HttpUser):
    # wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    @task
    def get_embedding(self):
        # Generate a random sentence for embedding
        google_search_queries = [
            "What is the weather like in New York today?",
            "What does 'metamorphosis' mean?",
            "Latest news about the 2024 US election",
            "Best laptops under $1000",
            "Samsung Galaxy S23 vs iPhone 14 price comparison",
            "Black Friday deals for TVs 2024",
            "Causes of chronic fatigue",
            "Best exercises to lose belly fat at home",
            "Keto diet meal plan for beginners",
            "Top things to do in Tokyo, Japan",
            "Cheap flights from LA to London in October",
            "Best hotels in Bali with ocean view",
            "What time is Oppenheimer showing near me?",
            "When does season 4 of The Witcher come out?",
            "Latest news about Taylor Swift's new album",
            "iPad Air 2024 specs",
            "How to reset my iPhone 13 to factory settings",
            "Why is my laptop overheating?",
            "How to learn Python programming",
            "Best online courses for data science",
            "What is the formula for compound interest?",
            "Best index funds for long-term investment",
            "How to file taxes as a freelancer in 2024",
            "How to create a will in California",
        ]

        random_sentence = random.choice(google_search_queries)

        # Make a POST request to the /embed endpoint
        headers = {"Content-Type": "application/json"}
        payload = {"text": random_sentence}

        with self.client.post(
            "/embed", json=payload, headers=headers, catch_response=True
        ) as response:
            if response.status_code == 200:
                # Check if the response contains an embedding
                if "embedding" in response.json():
                    response.success()
                else:
                    response.failure("Response does not contain an embedding")
            else:
                response.failure(f"Got status code {response.status_code}")

    @task(0)  # This task will be executed 3 times as often as the get_embedding task
    def get_root(self):
        # Make a GET request to the root endpoint
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                if "message" in response.json():
                    response.success()
                else:
                    response.failure("Response does not contain a message")
            else:
                response.failure(f"Got status code {response.status_code}")
