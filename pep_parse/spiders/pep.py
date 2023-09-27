import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_SPIDER_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_SPIDER_URL]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response, **kwargs):
        for pep_url in response.css('tbody tr a[href^="pep-"]'):
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        _, number, _, *title = response.css(
            'h1.page-title::text'
        ).get().split()
        yield PepParseItem(
            dict(
                number=number,
                name=' '.join(title).strip(),
                status=response.css(
                    'dt:contains("Status")+dd abbr::text'
                ).get()
            )
        )
