import requests
import csv
from bs4 import BeautifulSoup

def main():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Something goes wrong with connection!")

    soup = BeautifulSoup(response.text, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")

    print(f"Find job offers: {len(job_elements)}\n")

    job_offers = []
    for job in job_elements:
        title_element = job.find("h2", class_="title")
        company_element = job.find("h3", class_="company")

        
        title = title_element.text.strip()
        company = company_element.text.strip()

        # print(f"Position: {title}")
        # print(f"Company: {company}")

        job_offers.append({"Title": title, "Company": company})

    with open("job_offers.csv", mode="w", encoding="utf-8", newline="") as csvfile:
        fieldnames = ['Title', 'Company']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row_offer in job_offers:
            print(row_offer)
            writer.writerow(row_offer)
if __name__ == "__main__":
    main()