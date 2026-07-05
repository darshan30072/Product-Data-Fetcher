# API Fetcher

A small Python script that fetches random jokes from the [Official Joke API](https://official-joke-api.appspot.com/), cleans up the data, and saves the results to a local JSON file.

## What it does

1. Fetches 10 random jokes from `https://official-joke-api.appspot.com/jokes/ten`
2. Extracts just the `setup` and `punchline` from each joke
3. Saves the cleaned data to `jokes.json`
4. Prints a summary of how many items were processed

## Project structure

```
api_fetcher/
├── main.py          # Entry point - runs the fetch/process/save pipeline
├── api_client.py     # Handles the API request
├── processor.py     # Cleans the raw data and writes it to a file
├── utils.py          # Small helper utilities (e.g. summary printing)
├── jokes.json        # Output file (generated after running main.py)
└── requirements.txt   # Python dependencies
```

## Requirements

- Python 3.8+
- [`requests`](https://pypi.org/project/requests/)

## Setup

```bash
# Clone the repo
git clone https://github.com/<your-username>/api_fetcher.git
cd api_fetcher

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the script from the project root:

```bash
python main.py
```

On success, you'll see:

```
✅ Done!!!
```

and a `jokes.json` file will be created (or overwritten) in the project directory with entries like:

```json
{
  "setup": "What do you get when you cross a snowman with a vampire?",
  "punchline": "Frostbite."
}
```

## License

This project is open source and available under the [MIT License](LICENSE).