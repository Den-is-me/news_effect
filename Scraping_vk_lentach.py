import requests
from bs4 import BeautifulSoup
import json
import datetime

def return_moscow_time(time):       # Возвращет время + этот год
    time = datetime.datetime.strptime('2022 ' + time, '%Y %d %b at %I:%M %p')
    return str(time)

headers = {'date': 'Thu, 29Dec 2022 15:34:59 GMT',
           'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
            'content-type': 'application/json; ''charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 ' \
                              'Safari/537.36'}
URL = ('https://vk.com/wall-29534144?own=1&offset=40')
count = 40
project_data_list = []

for _ in range(293):
    r = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    post_cards = soup.find_all('div', class_='_post_content')

    for post in post_cards:
        try:
            post_text = post.find('div', class_='post_info').find('div', class_='wall_post_text').text
            if 'Ночные новости' in post_text or 'Дневные новости' in post_text or 'а' not in post_text:
                continue
        except Exception:
            continue
        try:
            post_time = post.find('div', class_='post_date').find('span', class_='rel_date').text
            post_time = return_moscow_time(post_time)
        except Exception:
            post_time = None
        try:
            post_reactions = post.find('div', class_='PostButtonReactions__title _counter_anim_container').text
        except Exception:
            post_reactions = None
        try:
            post_share = post.find('div', class_='PostBottomAction PostBottomAction--withBg share _share').find('span',
                                                                                                                class_='PostBottomAction__count _like_button_count _counter_anim_container PostBottomAction__count--withBg').text.strip()
        except Exception:
            post_share = None
        try:
            post_views = post.find('span', class_='_views').text
        except Exception:
            post_views = None

        project_data_list.append({'post_time': post_time, 'post_text': post_text.strip(),
                                  'post_reactions':
            post_reactions, 'post_share': post_share, 'post_views': post_views})
    count += 20
    URL = 'https://vk.com/wall-29534144?own=1' + '&offset=' + str(count)
    print(count)

with open('data/news_vk_lentach.json', 'w', encoding='UTF8') as file:
    json.dump(project_data_list, file, ensure_ascii=False)






