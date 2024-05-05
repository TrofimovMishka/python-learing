# Beautiful Soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import lxml

with open('website.html') as file:
    content = file.read()

# soup = BeautifulSoup(content, 'lxml') # can use language from lxml

soup = BeautifulSoup(content, 'html.parser') # read xml or html file

# print(soup.h1) # get first h1 from html
# print(soup.h1.string) # get data from first html h1 tag
#
# print(soup.li) # get first li tag

# How get all tags:

list_of_li_tags = soup.find_all('li') # return list of all li tags

print(list_of_li_tags[1])

list_of_text_only = []

for tag in list_of_li_tags:
    list_of_text_only.append(tag.getText())
    # list_of_text_only.append(tag.get('can pass attribute here'))

print(list_of_text_only[1])

#how find by attribute:

heading = soup.find(name='h1', id='name') # find first element with proper 'id' attribute
heading_2 = soup.find(name='h3', class_='heading') # find first element with proper 'class' attribute
print(heading)
print(heading_2.get('class'))

# How find elements in proper position
company_url = soup.select_one(selector="p a") # find first <a> element what inside <p> tag
print(company_url)

print(soup.select_one(selector='#name')) # #-means id, .-means class
print(soup.select(selector='.heading')) # #-means id, .-means class







