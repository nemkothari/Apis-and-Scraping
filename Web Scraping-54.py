## 2. Web Page Structure ##

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content


## 3. Retrieving Elements from a Page ##

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body

# Get the p tag from the body.
p = body.p
title_text = parser.title.text
# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)
print(title_text)

## 4. Using Find All ##

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag.
p = body[0].find_all("p")
title_text = parser.find_all("title")[0].text  
# Get the text.
print( p[0].text)
print(title_text)

## 5. Element IDs ##

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
first_paragraph = parser.find_all("p", id="first")[0]
second_paragraph_text =  parser.find_all("p", id="second")[0].text
print(first_paragraph.text)

## 6. Element Classes ##

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
second_inner_paragraph_text = parser.find_all("p", class_="inner-text")[1].text
first_outer_paragraph_text =  parser.find_all("p", class_="outer-text")[0].text
print(first_inner_paragraph.text)

## 8. Using CSS Selectors ##

# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_items = parser.select(".first-item")
first_outer = parser.select(".outer-text")
second = parser.select("p#second")
# Print the text of the first paragraph (the first element with the first-item class).
print(first_items[0].text)

first_outer_text = first_outer[0].text
second_text = second[0].text

## 10. Using Nested CSS Selectors ##

# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number of turnovers the Seahawks committed.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text

total = parser.select("#total-plays")[0]
total_turn = total.select("td")[2]
print(total_turn.text)
patriots_total_plays_count = total_turn.text

totaly = parser.select("#total-yards")[0]
total_turny = totaly.select("td")[1]
print(total_turny.text)
patriots_total_plays_count = total_turn.text


seahawks_total_yards_count = total_turny.text