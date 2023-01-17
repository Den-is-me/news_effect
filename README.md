# News effect
**📈 Project on impact of news on the stock market**
 ## Plan
 - [Idea](#the-idea)
 - [Tasks](#tasks)
 - [Research objects](#research-objects)
 - [Stack](#the-teach-stack)
 
 ## Realization
 - [Extract data from a news source](#extract-data-from-a-news-source)
 - [Extract stock market movement data](#extract-stock-market-movement-data)
 - [Transform data for analyze](#transform-data-for-analyze)
 ___

### The Idea
  The behavior of investors in the stock market depends on various factors:
  - State of the world economy.
  - Macroeconomic indicators of the resident country.
  - Financial income of individual companies.
  - News of the country, which is interesting for the investor, etc.

If we have data on these factors, it becomes possible to predict the reaction of investors to change. For example, if in the reporting period the planned indicators of the company are not met, the company's stock prices will decline.. **A positive example**: the reduction of the key rate of the Central Bank increases the interest of investors in shares, which increases the likelihood of growth in stock quotes.

The data of economic indicators are in open source, and we can easily get them for analysis. However, the news is not so simple, because there is no generally accepted source of information and values for assessing the impact of news on the stock market.

**The idea of the project is** to create a database of news publications with a view rate to show *how people's reaction to news correlates with stock market movements*. 
  
### Tasks
1. Extract data from a news source.
3. Extract stock market movement data.
4. Transform data for analyze.
5. Identify news values that correlate with the stock market movements.
6. Visualize the result.

### Research objects
- News publications of the public Lentach social network [vk.com](https://vk.com)
- Moscow Exchange Index (IMOEX).

For the period 01/01/2022 - 12/24/2022.

### The teach stack
Python:
```Python
import requests
import bs4 from BeautifulSoup
import json
import datetime
```
Azure Databrics:
```Spark SQL```
___

### Extract data from a news source
As a database entity, I defined a news post.
As attributes that need to be extract, I highlighted:

time | text | likes | shares | number of views

![image](/lentach_post.png)

For extraction, I developed [this scraper in python](/Scraping_vk_lentach.py). And as a result I have got the [file.json](/news_vk_lentach.json), which include 4980 rows like this:

```json
{post_time": "2023-01-15 17:30:00", "post_text": "В США выбрали 'Мисс Вселенную'...", "post_reactions": "4,228", "post_share": "703", "post_views": "528К"}
```

### Extract stock market movement data
As I wrote above
>The data of economic indicators are in open source

Therefore, I downloaded ready-made information about the Moscow Exchange index from [finam.ru](https://www.finam.ru/profile/mirovye-indeksy/micex/export/) 🙂

I have got 2072 rows in the [file.csv](/IMOEX_220101_221228.csv)
```csv<TICKER>;<PER>;<DATE>;<TIME>;<OPEN>;<HIGH>;<LOW>;<CLOSE>;<VOL>
IMOEX;60;20220103;11:00;3824.4500000;3861.9000000;3824.2900000;3854.0800000;11733696859
IMOEX;60;20220103;12:00;3854.0000000;3866.1000000;3852.1600000;3855.5000000;9187850231
IMOEX;60;20220103;13:00;3855.4800000;3861.1500000;3851.6300000;3860.4500000;4309243868
IMOEX;60;20220103;14:00;3860.4500000;3864.0600000;3855.2700000;3861.7000000;4831759989
IMOEX;60;20220103;15:00;3861.6400000;3863.4700000;3855.5700000;3856.7100000;3201743988
```


## Transform data for analyze

For this and other tasks, I chose the free version of the databricks platform.
First of all I created a cluster and uploaded [file.json](/create%20table%20news_lentach.png), [file.csv](/create%20table%20imoex_csv.png) as tables.

![cluster](/create-cluster.png)
