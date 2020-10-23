# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
import sqlite3


class MoponStoreDbPipeline:
    settings = get_project_settings()
    file_name = settings.get('SQLITE_FILE_NAME')
    table_name = settings.get('SQLITE_TABLE_NAME')


    def __init__(self):
        self._connect()
        self._create_table()


    def _connect(self):
        self.connection = sqlite3.connect(self.file_name)
        self.curr = self.connection.cursor()


    def _create_table(self):
        self._drop_table_if_exists()
        self._create_table_columns()
    
    
    def _drop_table_if_exists(self):
        self.curr.execute("DROP TABLE IF EXISTS {}".format(self.table_name))

    
    def _create_table_columns(self):
        columns = """name text,
        discount_value text,
        details text,
        expiration_time text,
        discount_code text,
        liked_count text,
        disliked_count text"""
        self.curr.execute("create table {} ({})".format(self.table_name, columns))


    def process_item(self, item, spider):
        self._store_item_in_db(item)
        return item

    
    def _store_item_in_db(self, item):
        self.curr.execute(
            "insert into {} values(?, ?, ?, ?, ?, ?, ?)".format(self.table_name),
                (
                    item['name'],
                    item['discount_value'],
                    item['details'],
                    item['expiration_time'],
                    item['liked_count'],
                    item['disliked_count'],
                    item['discount_code']
                )
            )
        self.connection.commit()


    def __del__(self):
        self.connection.close()

