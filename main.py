from api_client import fetch_data
from processor import process_data, save_to_file

def main():
    raw_data = fetch_data()
    cleaned = process_data(raw_data)
    save_to_file(cleaned)
    print("✅ Done!!!")

if __name__ == "__main__":
    main()
