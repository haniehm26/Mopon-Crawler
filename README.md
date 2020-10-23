# Montazeri & Mahdavi Mopon.ir Crawler

## Setup

```bash
$ pip install -r requirements.txt
```
## How To Run

* if you want to run the crawler every hour:

1. 
```bash
$ cd spiders
```

2. make sure that you import MoponCrawlerItem like this exactly:
```
from .items import MoponCrawlerItem
```

3. 
```bash
$ python crawl mopon
```

* if you want to run the crawler and get json output:

1. 
```bash
$ cd spiders
```

2. make sure that you import MoponCrawlerItem like this exactly:
```
from items import MoponCrawlerItem
```

3. 
```bash
$ cd ..
$ scrapy crawl mopon -o out.json
```


