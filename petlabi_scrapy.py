import scrapy
from scrapy import Request, Spider

class QuoteSpider(scrapy.Spider):
    name = 'quote-spider'
    allowed_domains = ['petlebi.com']
    start_urls = ['https://www.petlebi.com/alisveris/ara']
    


    def parse(self, response):
        lastpage = int(response.xpath('//*[@id="pagination_area"]/ul/li[last()-1]/a/text()').get())
        print(lastpage)

        for nextpage in range(1,lastpage+1):
            pagelinkurl = "https://www.petlebi.com/alisveris/ara?page="+str(nextpage)
            yield Request(pagelinkurl, callback = self.parse_product)
 
    
    def parse_product(self, response):
        products = response.xpath('//*[@id="products"]//h3/text()').getall()
        urls = response.xpath('//*[@id="products"]//@href').getall()

        for url in urls:
            yield Request(url, callback = self.gather_info)

    def gather_info(self, response):
        NAME_SELECTOR = '/html/body/div[3]/div[2]/div/div/div[2]/h1/text()'
        PRICE_SELECTOR = '/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/span/p[2]/text()'
        BARKOD_SELECTOR = '//*[@id="hakkinda"]/div[./div[contains(text(),"BARKOD")]]/div[2]/text()'
        IMAGE_SELECTOR = '//*[@id="photoGallery"]/img/@src'
        BRAND_SELECTOR = '//*[@id="hakkinda"]/div[1]/div[2]/span/a/text()'
        CATEGORY_SELECTOR = '/html/body/div[3]/div[1]/div/div/div[1]/ol/li[2]/a/span/text()'

        safename = response.xpath(NAME_SELECTOR).get()
        safename = safename.replace("'", r"\'")
        safebrand = response.xpath(BRAND_SELECTOR).get()
        safebrand = safebrand.replace("'", r"\'")

        yield{
                'URL' : response.request.url,
                'name': safename,
                'price': response.xpath(PRICE_SELECTOR).get(),
                'barcode': response.xpath(BARKOD_SELECTOR).get(),
                'image': "https:" + response.xpath(IMAGE_SELECTOR).get(),
                'brand': safebrand,
                'category': response.xpath(CATEGORY_SELECTOR).get(),
                'sku' : "",
                'product ID' : ""

            }    