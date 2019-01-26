# python-webscraping
Web Scraping with Scrapy


## Start Project

**1. Create a virtualenv**
```
virtualenv -p python3 .venv
```

**2. Activate virtualenv**
```
source .venv/bin/activate
```

**3. Install scrapy lib**
```
pip install scrapy
```


## Execute Scrapy Spiders

**1. List all spiders**
```
scrapy list
```

**2. Execute web scrapping**
```
scrapy crawl quotes [opicional: -o output.json]
```

**3. Shell test scrapy**
```
scrapy shell 'http://exemplo.com'
```