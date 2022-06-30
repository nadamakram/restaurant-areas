import scrapy


class QuotesSpider(scrapy.Spider):
    name = "talabat"

    def start_requests(self):
        urls = [
            'https://www.talabat.com/egypt/sitemap',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('/html/body/div/div[4]/div[1]/div/div[8]/div'):
            yield {
                'area': row.xpath('p/a//text()').get(),
            }

