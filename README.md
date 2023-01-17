# news_effect
**📈 Project on impact of news on the stock market**
 ## Plan
 - [Idea](#the-idea)
 - [Tasks](#tasks)
 - [Research objects](#research-objects)
 - [Stack](#the-teach-stack)
 
 ## Realization
 - [Extract data from a news source](#extract-data-from-a-news-source)
 ___

### The Idea
  The behavior of investors in the stock market depends on various factors:
  - State of the world economy
  - Macroeconomic indicators of the resident country
  - Financial income of individual companies
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

For extraction, I developed [this scraper in python](/Scraping_vk_lentach.py)
