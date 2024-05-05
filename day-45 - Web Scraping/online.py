# How scraping live website
import requests
from bs4 import BeautifulSoup

URL = 'https://news.ycombinator.com/'


response = requests.get(URL)
row_data = response.text

# Uncomment to use data from file:
# with open('livesite.html') as file:
#     row_data = file.read()

# print(row_data)

# Task: get all titles, links and points for all articles on the page:
soup = BeautifulSoup(row_data, 'html.parser')

all_title_tags = soup.select(selector='.titleline')
# print(all_title_tags)
# print(all_title_tags)

all_titles = []
all_links = []
all_points = [int(score.text.split()[0]) for score in soup.select(selector='.score')]

for tag in all_title_tags:
    all_titles.append(tag.a.text)
    all_links.append(tag.a.get('href'))

# for tag in all_score_tags:
#     all_points.append(tag.text)
#     # print(tag.text.split(" ")[0])

print(all_titles)
print(all_links)
print(all_points)

# Task print title and link with the highest number of points

max_value = max(all_points)
index_ = all_points.index(max_value)

print(f'title = {all_titles.__getitem__(index_)}')
print(f'link = {all_links.__getitem__(index_)}')
print(f'points = {max_value}')
