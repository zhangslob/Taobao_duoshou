# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    area = scrapy.Field()
    url = scrapy.Field()
    fastPostFee = scrapy.Field()
    sales = scrapy.Field()
    nick = scrapy.Field()
    id = scrapy.Field()
    price = scrapy.Field()
    originalPrice = scrapy.Field()
    loc = scrapy.Field()
    count = scrapy.Field()
    img_url = scrapy.Field()
    comment_url = scrapy.Field()


