from bs4 import BeautifulSoup
import requests

"# PRACTICE EXERCISES BELOW: #"
# with open("website.html", encoding="utf8") as data:
#     contents = data.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
#
# ## FIND FIRST ##
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.a)    # gives first of each html tag
#
# ## FIND ALL ##
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# ## FIND SPECIFIC ##
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")    # NOTE "CLASS_" WITH UNDERSCORE
# # print(section_heading.get_text())
#
# ## SELECTS FIRST MATCHING ITEMS ##
# # BY tag
# company_url = soup.select_one(selector="p a")    # looking for 'a' tag within 'p' tag (line 11 in html file)
# # print(company_url)
#
# # BY id
# name = soup.select_one(selector="#name")    # looking for 'id'
# # print(name)
#
# # BY class
# headings = soup.select(selector=".heading")    # looking for "heading", can do select_one or narrow down more
# print(headings)
"#############################"

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article = soup.find(class_="titleline").select_one(selector="a")
# article_text = article.get_text()    # first article title
# print(article_text)
# article_link = article.get("href")    # link
# print(article_link)
# article_upvote = soup.find(class_="score").get_text()    # num. of up-votes
# print(article_upvote)

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    article_texts.append(article_tag.select_one(selector="a").get_text())
    article_links.append(article_tag.select_one(selector="a").get("href"))

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(class_="score")]

max_index = article_upvotes.index(max(article_upvotes))

print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])
