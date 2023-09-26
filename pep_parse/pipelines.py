import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

FIELDS_NAME = ('Status', 'Quantity')
SUMMARY_TABLE_TOTAL = 'Total'
DIR_OUTPUT = 'results'
DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'
TIME_NOW = dt.datetime.now().strftime(DT_FORMAT)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / DIR_OUTPUT
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = {}

    def close_spider(self, spider):
        file_dir = self.results_dir / FILE_NAME.format(time=TIME_NOW)
        with open(file_dir, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect=csv.unix_dialect)
            writer.writerow([FIELDS_NAME])

            for status, count in self.results.items():
                writer.writerow([status, count])

            writer.writerow([SUMMARY_TABLE_TOTAL, sum(self.results.values())])

    def process_item(self, item, spider):
        self.results[item['status']] = self.results.get(item['status'], 0) + 1
        return item
