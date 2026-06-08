import requests
from db_example import add_user, init_database, add_post

def main():
 init_database()
    
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

            
            add_user(user_name, user_company)
 except requests.exceptions.ConnectionError:
    print("Error: Can't connect to the server!")
 except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: Something goes wrong! Detail: {err}")

def fetch_and_save_posts():
   init_database()

   try:
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if not data:
        print("Server response but no data was fetch!")
    else:
        for post in data:
            post_title = post["title"]
            post_body = post["body"]
            post_user_id = post["userId"]
            
            add_post(post_title, post_body, post_user_id)
   except requests.exceptions.ConnectionError:
    print("Error: Can't connect to the server!")
   except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: Something goes wrong! Detail: {err}")



if __name__ == "__main__":
    main()
    fetch_and_save_posts()