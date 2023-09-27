from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

PEP_SPIDER_URL = 'peps.python.org'

BASE_DIR = Path(__file__).parent.parent

DIR_OUTPUT = 'results'

FEEDS = {
    f'{DIR_OUTPUT}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
