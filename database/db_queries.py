import pymysql
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123@Parth@321',
            database='car_security'
        )

    def query_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql(query, self.conn)

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db = DatabaseManager()
    dos_data = db.query_data("dos")
    print(dos_data.head())
    db.close_connection()
