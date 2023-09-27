import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DIR_OUTPUT

FIELDS_NAME = ('Status', 'Quantity')
SUMMARY_TABLE_TOTAL = 'Total'

DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / DIR_OUTPUT
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def close_spider(self, spider):
        time_end = dt.datetime.now().strftime(DT_FORMAT)
        file_dir = self.results_dir / FILE_NAME.format(time=time_end)
        with open(file_dir, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE,
            ).writerows([
                FIELDS_NAME,
                *self.statuses.items(),
                (SUMMARY_TABLE_TOTAL, sum(self.statuses.values())),
            ])

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item
