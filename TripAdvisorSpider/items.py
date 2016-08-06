# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class HotelItem(Item):
    name = Field() # 名称
    name_en = Field() # 英文名称
    url = Field() # 链接地址
    level = Field() # 等级
    classes = Field() # 酒店类型
    address = Field() # 地址
    locality = Field() # 地区
    review_stars = Field() # 点评星级
    review_qty = Field() # 点评数
    rank = Field() # 酒店排名
    restaurant = Field() # 酒店餐饮
    price = Field() # 价格区间
    network = Field() # 网络情况
    service = Field() # 提供的服务
    room_type = Field() # 客房类型
    activity = Field() # 活动设施
    special = Field() # 酒店特色
    lat = Field() # 经纬度
    lng = Field() 
