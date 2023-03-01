#This is created to extract the top trending repositories on GitHub and return the developer name, repository name and star rating

import requests
from bs4 import BeautifulSoup
import csv

def request_github_trending(URL):
    page = requests.get(URL)
    return page

def extract(page):
    soup = BeautifulSoup(page.content, "html.parser") 
    all_trending_repos = soup.find_all("article")
    return all_trending_repos

def transform(html_repos):
    all_arrays = []
    for item in range(0,25):
        repository = html_repos[item].h1.a["href"]
        repository = repository[1:]
        star_rating = html_repos[item].find("div", class_="f6 color-fg-muted mt-2").a.get_text()
        star_rating = star_rating.strip().replace("\n", "")
        developer_name = html_repos[item].find("img", class_="avatar mb-1 avatar-user").attrs["alt"]
        repo_hash = {"developer": developer_name, "repository_name": repository, "nbr_stars": star_rating}
        all_arrays.append(repo_hash)
    return all_arrays

def format(repositories_data):
    my_headers = ["Developer","Repository Name","Number of Stars"]
    filename = "mycsv.csv" 
    #print(repositories_data)
    with open(filename, "w", newline="\n") as myfile:
        fc = csv.DictWriter(myfile, fieldnames=repositories_data[0].keys())
        fc.writeheader()
        fc.writerows(repositories_data)
    file = open(filename, "r")
    return file.read() 


URL = "https://github.com/trending"
page = request_github_trending(URL)
html = extract(page)
repos_list = transform(html)
print(format(repos_list))
