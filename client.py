import requests

def main():
    while True:
        cust_no = input("Enter customer number (or 'q' to quit): ").strip()
        if cust_no.lower() == 'q':
            break

        try:
            url = f"http://127.0.0.1:8000/query/{cust_no}"
            resp = requests.get(url)
            resp.raise_for_status()  # raise exception for HTTP errors
            print("\n=== API Response ===")
            print(resp.json())       # pretty JSON response
            print()
        except Exception as e:
            print("Error calling API:", e)

if __name__ == "__main__":
    main()
