import requests
from bs4 import BeautifulSoup
import json
import datetime
import re


class Post:
    def __init__(self, time, text, reactions, share, views):
        self.post_time = time
        self.post_text = text.strip()
        self.post_reactions = reactions
        self.post_share = share
        self.post_views = views

    def result_dict(self):
        return {'post_time': self.post_time, 'post_text': self.post_text, 'post_reactions': self.post_reactions,
                'post_share': self.post_share, 'post_views': self.post_views
                }


def correct_time(time):  # check year
    now_year = str(datetime.datetime.now().year) + ' '
    if re.findall(r'\d{4}', time):
        time = datetime.datetime.strptime(time, '%d %b %Y')
    else:
        time = datetime.datetime.strptime(now_year + time, '%Y %d %b at %I:%M %p')
    return str(time)


headers = {'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
           'content-type': 'application/json; ''charset=UTF-8',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                         'Safari/537.36'}
URL = 'https://vk.com/wall-29534144?own=1&offset=40'
count = 40  # Each page contains 20 posts, we need 'count' for start at the correct posting time 3 days ago
project_data_list = []  # list for our attributes
post_time = str(datetime.datetime.now())

while post_time > '2022-01-01':  # Parsing stop date
    r = requests.get(url=URL, headers=headers)
    if r.status_code != 200:
        print('Connection Error')
        break
    soup = BeautifulSoup(r.text, 'lxml')
    post_cards = soup.find_all('div', class_='_post_content')  # get html about news posts

    for post in post_cards:  # extract attributes
        try:
            post_text = post.find('div', class_='post_info').find('div', class_='wall_post_text').text
            if 'Ночные новости' in post_text or 'Дневные новости' in post_text or 'а' not in post_text:
                continue
        except AttributeError:
            continue
        try:
            post_time = post.find('div', class_='PostHeaderSubtitle PostHeaderSubtitle--layoutDefault')
            post_time = post_time.find('time', class_='PostHeaderSubtitle__item').text.strip()
            post_time = correct_time(post_time)
        except AttributeError:
            post_time = None
        try:
            post_reactions = post.find('div', class_='PostButtonReactions__title _counter_anim_container').text
        except AttributeError:
            post_reactions = None
        try:
            post_share = post.find('div', class_='PostBottomAction PostBottomAction--withBg share _share')
            post_share = post_share.find('span', class_='PostBottomAction__count _like_button_count _counter_anim_container '
                                                        'PostBottomAction__count--withBg').text.strip()
        except AttributeError:
            post_share = None
        try:
            post_views = post.find('span', class_='_views').text
        except AttributeError:
            post_views = None

        post = Post(post_time, post_text, post_reactions, post_share, post_views)
        project_data_list.append(post.result_dict())
    count += 20  # follow next page
    URL = 'https://vk.com/wall-29534144?own=1' + '&offset=' + str(count)
    print('Extracted', str(count - 40), 'posts')  # How many posts were extracted success

with open('data/news_vk_lentach.json', 'w', encoding='UTF8') as file:
    json.dump(project_data_list, file, ensure_ascii=False)

# Sometimes VK changes html tags, and it needs to be updates
