# -*- coding: utf-8 -*-
import scrapy
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class ZaobaoSpider(scrapy.Spider):

    name = 'zaobao'
    allowed_domains = ['zaobao.com']
    start_urls = ['http://www.zaobao.com/special/report/politic/fincrisis']

    def __init__(self):
        try:
            self.dbpool = adbapi.ConnectionPool(
                'MySQLdb',
                db = 'test',
                user = 'root',
                passwd = 'ganZHEyu',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = True,
             )

        except Exception as e:
            self.logger.warning(e)


    def parse(self, response):
        for href in response.xpath('//*[@id="l_title"]/ul/li/a[1]/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_acticle)


    def parse_acticle(self, response):
        titles = response.xpath('//*[@id="a_title"]/h1/text()').extract()
        times = response.xpath('//*[@id="a_credit"]/p[2]/text()').extract()
        contents = response.xpath('//*[@id="article_content"]/div[1]').extract()
        link = response.url

        try:
            #dbpool.runQuery("insert into zaobao VALUES(NULL, '%s', '%s', '%s')" %(titles[0].encode('utf-8'),times[0].encode('utf-8'),contents[0].encode('utf-8')))
            self.dbpool.runQuery("insert into zaobao values(NULL,'{}', '{}', '{}', '{}')".format(titles[0].encode('utf-8'), contents[0].encode('utf-8'), times[0].encode('utf-8'), link))

        except Exception as e:
            self.logger.warning(e)

        yield{
            'title':titles,
            'time':times,
            'content':contents,
            'link':link,
        }



