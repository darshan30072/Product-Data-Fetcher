import json

def process_data(data):
    return [
        {
            "setup": joke["setup"],
            "punchline": joke["punchline"]
        }
        for joke in data
    ]

def save_to_file(data, filename="jokes.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)