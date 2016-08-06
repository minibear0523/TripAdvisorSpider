# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from TripAdvisorSpider.items import HotelItem
import re


class JapanHotelSpider(Spider):
    name = "japan_hotel"
    collection_name = 'hotel'
    level = [u'豪华', u'中等', u'经济实惠']
    start_urls = [
        # "http://www.tripadvisor.cn/Hotels-g298184-Tokyo_Tokyo_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298564-Kyoto_Kyoto_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298566-Osaka_Osaka_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298560-Sapporo_Hokkaido-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298207-Fukuoka_Fukuoka_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298561-Hiroshima_Hiroshima_Prefecture_Chugoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1120615-Hakuba_mura_Kitaazumi_gun_Nagano_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298224-Naha_Okinawa_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298173-Yokohama_Kanagawa_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298562-Kobe_Hyogo_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298106-Nagoya_Aichi_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298249-Sendai_Miyagi_Prefecture_Tohoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298172-Kawasaki_Kanagawa_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g303160-Kitakyushu_Fukuoka_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g303160-Kitakyushu_Fukuoka_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298180-Saitama_Saitama_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298124-Shizuoka_Shizuoka_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298120-Niigata_Niigata_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298213-Kumamoto_Kumamoto_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298158-Chiba_Chiba_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298134-Okayama_Okayama_Prefecture_Chugoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g303148-Hamamatsu_Shizuoka_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298115-Kanazawa_Ishikawa_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298211-Kagoshima_Kagoshima_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g654326-Sakai_Osaka_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298230-Matsuyama_Ehime_Prefecture_Shikoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298191-Himeji_Hyogo_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298183-Utsunomiya_Tochigi_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298232-Takamatsu_Kagawa_Prefecture_Shikoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298112-Gifu_Gifu_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1021282-Sagamihara_Kanagawa_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Tourism-g298215-Miyazaki_Miyazaki_Prefecture_Kyushu_Okinawa-Vacations.html",
        # "http://www.tripadvisor.cn/Hotels-g298568-Nagasaki_Nagasaki_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298126-Toyama_Toyama_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298234-Kochi_Kochi_Prefecture_Shikoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298220-Oita_Oita_Prefecture_Kyushu_Okinawa-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298204-Wakayama_Wakayama_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1060898-Hachioji_Tokyo_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298198-Nara_Nara_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g651653-Takasaki_Gunma_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1021147-Funabashi_Chiba_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1021277-Fujisawa_Kanagawa_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298131-Fukuyama_Hiroshima_Prefecture_Chugoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298151-Hakodate_Hokkaido-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1022819-Nishinomiya_Hyogo_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298118-Matsumoto_Nagano_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1023536-Higashiosaka_Osaka_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1022817-Amagasaki_Hyogo_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298110-Fukui_Fukui_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1021366-Kawaguchi_Saitama_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298133-Kurashiki_Okayama_Prefecture_Chugoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298247-Morioka_Iwate_Prefecture_Tohoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1060900-Musashino_Tokyo_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298236-Tokushima_Tokushima_Prefecture_Shikoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298107-Toyohashi_Aichi_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g319103-Asahikawa_Hokkaido-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298166-Mito_Ibaraki_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298239-Akita_Akita_Prefecture_Tohoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1023191-Yamagata_Yamagata_Prefecture_Tohoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g303156-Kamakura_Kanagawa_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298174-Yokosuka_Kanagawa_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1019661-Toyota_Aichi_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1060907-Machida_Tokyo_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298202-Otsu_Shiga_Prefecture_Kinki-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g303151-Matsudo_Chiba_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298241-Aomori_Aomori_Prefecture_Tohoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298245-Koriyama_Fukushima_Prefecture_Tohoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g780846-Iwaki_Fukushima_Prefecture_Tohoku-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g1021146-Ichikawa_Chiba_Prefecture_Kanto-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298128-Kofu_Yamanashi_Prefecture_Chubu-Hotels.html",
        # "http://www.tripadvisor.cn/Hotels-g298244-Fukushima_Fukushima_Prefecture_Tohoku-Hotels.html",
        "http://www.tripadvisor.cn/Hotels-g294232-Japan-Hotels.html",
    ]

    def __init__(self, *args, **kwargs):
        super(JapanHotelSpider, self).__init__(*args, **kwargs)
        if len(self.start_urls) == 0:
            self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        self.logger.info("Hotel list page url: %s" % response.url)
        for href in response.xpath('//div[@class="listing_title"]/a/@href'):
            url = response.urljoin(href.extract())
            yield Request(url, callback=self.parse_hotel)

        next_page = response.xpath('//div[@class="unified pagination standard_pagination"]/child::*[2][self::a]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield Request(url, self.parse)

    def parse_hotel(self, response):
        item = HotelItem()
        item['name'] = ''.join(response.xpath('//h1[@id="HEADING"]/text()').extract()).strip()
        try:
            item['name_en'] = ''.join(response.xpath('//h1[@id="HEADING"]/span[@class="altHead"]/text()').extract()).strip()
        except Exception as e:
            self.logger.error(e)
            item['name_en'] = ''


        item['review_stars'] = response.xpath('//img[@property="ratingValue"]/@content').extract()[0]
        item['review_qty'] = response.xpath('//a[@property="reviewCount"]/@content').extract()[0]

        item['classes'] = response.xpath('//div[starts-with(@class, "popRanking")]/a/text()').extract()[0].split('/')[1].split(' ')[0]
        
        rank_str = response.xpath('//div[starts-with(@class, "popRanking")]/b[@class="rank"]/text()').extract()[0]
        regx = r'(\d+)'
        pm = re.search(regx, rank_str)
        rank = pm.group(1)
        total = response.xpath('//div[starts-with(@class, "popRanking")]/a/text()').extract()[0].split('/')[1].split(' ')[2]
        item['rank'] = '/'.join([rank, total])
        item['url'] = response.url

        # 地址
        address_list = []
        region = response.xpath('//span[@property="addressRegion"]/text()').extract()
        if len(region) > 0:
            address_list.append(region[0])
        locality = response.xpath('//span[@property="addressLocality"]/text()').extract()
        if len(locality) > 0:
            address_list.append(locality[0])
        street = response.xpath('//span[@property="streetAddress"]/text()').extract()
        if len(street) > 0:            
            address_list.append(street[0])
        postal = response.xpath('//span[@property="postalCode"]/text()').extract()
        if len(postal) > 0:
            address_list.append(postal[0])
        item['address'] = ''.join(address_list)
        item['locality'] = address_list[:2]

        # 特色
        property_tags = []
        for tag in response.xpath('//ul[@class="property_tags"]/li/text()').extract():
            if len(tag.strip()) != 0:
                property_tags.append(tag.strip())
        item['special'] = property_tags

        # 等级
        try:
            item['level'] = ""
            for tag in response.xpath('//span[@class="tag"]/text()').extract():
                if tag.strip() in self.level:
                    item['level'] = tag.strip()
                    break
        except Exception as e:
            self.logger.error(e)
            item['level'] = ""

        # 活动设施, 客房类型, 网络, 服务
        for amenity in response.xpath('//div[@class="amenity_row"]'):
            t = amenity.xpath('./div[@class="amenity_hdr"]/text()')[0].extract()
            v = amenity.xpath('./div[@class="amenity_lst"]/ul/li/text()').extract()
            if t == u'活动设施':
                activity_list = []
                for activity in v:
                    if activity.strip() != "":
                        activity_list.append(activity.strip())
                item['activity'] = activity_list

            elif t == u'客房类型':
                room_type = []
                for room in v:
                    if room.strip() != "":
                        room_type.append(room.strip())
                item['room_type'] = room_type
            elif t == u'网络':
                network_list = []
                for network in v:
                    if network.strip() != "":
                        network_list.append(network.strip())
                item['network'] = network_list
            elif t == u'服务':
                service_list = []
                for service in v:
                    if service.strip() != "":
                        service_list.append(service.strip())
                item['service'] = service_list
            elif t == u'酒店餐饮':
                restaurant_list = []
                v = amenity.xpath('./div[@class="poi_card easyClear"]/div[@class="description_block"]/')
                for restaurant in v:
                    info = {}
                    info['name'] = restaurant.xpath('/a[@class="poi_title"]/text()')[0].extract()
                    info['url'] = 'http://www.tripadvisor.cn' + restaurant.xpath('/a[@class="poi_title"/@href')[0].extract()
                    stars = restaurant.xpath('/span[@class="rate sprite-rating_s rating_s"]/img/@alt')[0].extract()
                    regx = r'(\d)'
                    pm = re.search(regx, stars)
                    info['review_stars'] = pm.group(0)
                    qty =  restaurant.xpath('/div[@class="rating"]/a/text()')[0].extract()
                    regx = r'(\d+)'
                    info['review_qty'] = re.search(regx, qty).group(0)
                    classes = restaurant.xpath('/div[@class="details_block"]/span[@class="cuisines_label"]/text()')[0].extract().strip().split(',')
                    info['classes'] = map(lambda x:x.strip(), classes)
                    restaurant_list.append(info)
                item['restaurant'] = restaurant_list

            else:
                continue
        
        try:
            item['price'] = response.xpath('//span[@class="priceRange"]/text()')[0].extract()
        except Exception as e:
            self.logger.error(e)
            item['price'] = ''

        try:
            item['lat'] = response.xpath('//div[@class="mapContainer"]/@data-lat')[0].extract()
            item['lng'] = response.xpath('//div[@class="mapContainer"]/@data-lng')[0].extract()
        except Exception as e:
            self.logger.error(e)
            item['lat'] = ''
            item['lng'] = ''
        self.logger.debug(item)
        yield item
