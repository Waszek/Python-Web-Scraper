import requests

def main():

    
 try:
    url1 = "https://jsonplaceholder.typicode.com/users"
    url2= "https://api.github.com/some_fake_page_that_does_not_exist"
    response = requests.get(url1)
    response.raise_for_status()
    data = response.json()

    if not data:
        print("Server response but no data was fetch!")
    else:
        for user in data:
            user_name = user["name"]
            user_company = user["company"]["name"]

            print(f"{user_name} works in {user_company}")
 except requests.exceptions.ConnectionError:
    print("Error: Can't connect to the server!")
 except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: Something goes wrong! Detail: {err}")


if __name__ == "__main__":
    main()