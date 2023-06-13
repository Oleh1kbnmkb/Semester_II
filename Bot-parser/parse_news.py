'''
[
    {
        "link": посилання,
        "title": заголовок,
        "text": string
    }
]
'''
import requests
from bs4 import BeautifulSoup


def parse_default_news(date=None):
    links = []
    result = []
    if not date:
        response = requests.get("https://www.pravda.com.ua/news/")
        soup = BeautifulSoup(response.content, "html.parser")

        headers = soup.select('.article_header > a')
        for link in headers[:5]:
            l = link.get('href')
            result_link = l if l[0:5] == 'https' else 'https://www.pravda.com.ua' + l
            links.append(result_link)
        
        for link in links:
            link_response = requests.get(link)
            link_soup = BeautifulSoup(link_response.content, "html.parser")
            # print(link_soup)

            try:
                title = link_soup.select_one('.post_title').text
            except:
                title = ''

            try:
                texts = link_soup.select('.post_text > p')
            except:
                texts = ''
            
            news_body = []
            for i in texts:
                article_text = i.text
                news_body.append(f'{article_text}\n')

            article_body = ''.join(news_body)

            result.append(
                {
                    "link": link,
                    "title": title,
                    "text": article_body
                }
            )

        return result


def parse_economic_news(date=None):
    links = []
    result = []
    if not date:
        response = requests.get("https://www.epravda.com.ua/news/")
        soup = BeautifulSoup(response.content, "html.parser")

        headers = soup.select('.article__title > a')
        for link in headers[:5]:
            l = link.get('href')
            result_link = l if l[0:5] == 'https' else 'https://www.epravda.com.ua' + l
            links.append(result_link)
        
        for link in links:
            link_response = requests.get(link)
            link_soup = BeautifulSoup(link_response.content, "html.parser")

        
            title = link_soup.select_one('.post__title').text

            texts = link_soup.select('.post__text > p')
            
            news_body = []
            for i in texts:
                article_text = i.text
                news_body.append(f'{article_text}\n')

            article_body = ''.join(news_body)

            result.append(
                {
                    "link": link,
                    "title": title,
                    "text": article_body
                }
            )

        return result
    

if __name__ == '__main__':
    print(parse_economic_news())