import requests

try:
    # Fetch data from API
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # Check for API errors
    response.raise_for_status()

    # Convert JSON response to Python object
    users = response.json()

    print("\n===== USER DETAILS =====\n")

    # Save output to file
    with open("output.txt", "w") as file:

        for user in users:
            print(f"Name : {user['name']}")
            print(f"Email: {user['email']}")
            print("-" * 30)

            file.write(f"Name : {user['name']}\n")
            file.write(f"Email: {user['email']}\n")
            file.write("-" * 30 + "\n")

    # Search functionality
    search_name = input("\nEnter name to search: ")

    found = False

    for user in users:
        if search_name.lower() in user["name"].lower():
            print("\nUser Found")
            print("Name :", user["name"])
            print("Email:", user["email"])
            found = True

    if not found:
        print("User not found")

except requests.exceptions.RequestException as e:
    print("API Error:", e)

except Exception as e:
    print("Error:", e)