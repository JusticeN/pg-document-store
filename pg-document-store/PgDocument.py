import psycopg2
from db_utils import *

class PgTable:
    def __init__(self, cursor, name):
        '''
        usage:
        '''
        self.name = name
        print(sql_create_table(name))

    def insert(self, data):
        print(sql_insert_in_table(self.name, data))
        #cursor.execute();
    
    def delete(self):
        print(sql_delete_table(self.name, "name='test1'"))
    
    def fetch(self):
        print(sql_read_table(self.name, "name='test1'"))

        
class PgDocument:
    def __init__(self, *args, **kwargs):
        '''
        usage:
        doc = PgDocument(name="Jjo", last_name="bla")
        doc.save()
        '''
        self._keyPairs = kwargs

class PgDocumentClient(object):
    def __init__(self, host="localhost", port=5432, schema="public"):
        self._host = host
        self._port = port
        self._schema = schema
        self._db_name = ''
        self._cursor = None
        self._tables = []
        #self._connect()

    def __init__(self, connection_string):
        self._connection_string = connection_string
        self._cursor = None
        self._tables = {}
        #self._connect()

    def _connect(self):
        conn = psycopg2.connect("dbname=test user=postgres")
        self._cursor = conn.cursor()

    def __getattr__(self, name):
         for k, v in self._tables.items():
             if name == k:
                 return self._tables[name]
         else:
             print("create table ", name)
             self._tables[name]=PgTable(self._cursor, name)
             return self._tables[name]

def main():
    conn = PgDocumentClient("")
    customers = conn.customers
    data = {"name": "Justice"}
    customers.insert(data)
    customers.delete()
    customers.fetch()

if __name__ == '__main__':
    main()