# Web Scraping of Hacker News 
# scrape only articles with more than 100 points

from bs4 import BeautifulSoup 
import requests
import pprint
import json
from datetime import date
import sys

# Request a page by page number and parse the page
def connect_to_hn(page_num):
    res = requests.get('https://news.ycombinator.com/news?p='+str(page_num))
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

# Sort stories in a descending order by points
def sort_stories_by_points(hn):
    return sorted(hn, key=lambda k: k['points'], reverse=True)

# Creating a custom hacker news dictionary with titles, links and points
def create_custom_hn(links, subtext):
    hn = []
    for i, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None) # None if there is no link or it's broken
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'points': points})       
    return sort_stories_by_points(hn)

# run the previous functions and write the pages to the file
def run_and_save_to_txt(page_from, page_to):
    with open('hacker_news.txt', 'w') as file:

        # wrtie the today's date first
        file.write(f'{date.today()}\n')

        # loop through pages
        for i in range(page_from, page_to+1):
            print(f'Page No {i}')

            # connect to the website
            soup = connect_to_hn(i)

            # CSS selector for links and subtext(where points are)
            links = soup.select('.storylink')
            subtext = soup.select('.subtext')

            # scrape one page and print it
            page = create_custom_hn(links, subtext)
            pprint.pprint(page)

        # write the page into a file
            file.write(f'Page No {i}\n\n')
            for article in page:
                json.dump(article, file)
                file.write('\n')
            file.write('\n')
                
    

if __name__ == '__main__':
    # scrape the pages (number of pages entered in console)
    page_from = int(sys.argv[1])
    page_to = int(sys.argv[2])
    run_and_save_to_txt(page_from,page_to)
    