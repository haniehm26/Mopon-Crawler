import scrapy
# if you want to run this file with python command change ".items" to "items" in next line 
from .items import MoponCrawlerItem
from scrapy.loader import ItemLoader
# import logging
import datetime as dt
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

def remove_white_space(str):
    return str.strip()


class MoponSpider(scrapy.Spider):
    name = 'mopon'
    start_urls = [
      'http://www.mopon.ir/%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D8%BA%D8%B0%D8%A7/%DA%A9%D9%88%D9%BE%D9%86'
    ]
    #page_number 1 is crawled first and then we continue from page_number 2
    page_number = 2 

    def parse(self, response):
        div_items = response.css('div.col-lg-6')
        for item in div_items:
            is_not_expired = item.css('span.valid-date')
            # we checked items until an expired date has been found
            # instead of checking this condition, we could have checked whether a page is None
            if is_not_expired:
                a = item.css('h2.line-h-1-half a')
                url = a.xpath('@href').extract_first()
                yield response.follow(url, callback=self.parse_discount_info)
            else:
                return

        # self.logger.info('\n\nPage number is %d\n\n', MoponSpider.page_number)
        next_page = self.start_urls[0] + "?page=" + str(self.page_number)
        self.page_number += 1
        yield response.follow(next_page, callback=self.parse)

    def parse_discount_info(self, response):
        css_selector = response.css
        item = MoponCrawlerItem()
        item['name'] = css_selector('h2.text-center-sm a::text').extract_first()
        item['discount_value'] = remove_white_space(css_selector('h1.font-weight-bold::text').re(r'^(\d+\W+ |\d+\W+هزار تومان)')[0])
        item['details'] = css_selector('p.line-h-2::text').extract_first()
        item['expiration_time'] = remove_white_space(css_selector('small.text-danger::text').extract_first())
        item['liked_count'] = css_selector('span#liked::text').extract_first()
        item['disliked_count'] = css_selector('span#disliked::text').extract_first()
        discount_code = css_selector('p.discount-code-input::text').extract_first()
        no_discount_code = css_selector('span.font-weight-normal::text').extract_first()
        item['discount_code'] = remove_white_space(discount_code) if no_discount_code is None else remove_white_space(no_discount_code)

        yield item
                


def schedule_next_crawl(null):
    next_hour = (dt.datetime.now() + dt.timedelta(hours=1))
    print("Crawled at",dt.datetime.now())
    sleep_time = (next_hour - dt.datetime.now()).total_seconds()
    reactor.callLater(sleep_time, crawl)


def crawl_job():
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    return runner.crawl(MoponSpider)


def crawl():
    job = crawl_job()
    job.addCallback(schedule_next_crawl)


def run():
    crawl()
    reactor.run()

if __name__ == '__main__':
    run()
    