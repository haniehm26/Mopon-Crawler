# Montazeri & Mahdavi Mopon.ir Crawler

## Setup

```bash
$ pip install -r requirements.txt
```
## How To Run

```bash
$ cd mopon_crawler
```

* if you want to run the crawler every hour:

1. 
```bash
$ cd spiders
```

2. make sure that you import MoponCrawlerItem in mopon_spider.py like this exactly:
```
from items import MoponCrawlerItem
```

3. 
```bash
$ python mopon_spider.py
```

* if you want to run the crawler and get json output:

1. 
```bash
$ cd spiders
```

2. make sure that you import MoponCrawlerItem in mopon_spider.py like this exactly:
```
from .items import MoponCrawlerItem
```

3. 
```bash
$ cd ..
$ scrapy crawl mopon -o out.json
```
