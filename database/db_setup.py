import pymysql
import pandas as pd

def setup_database():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='car_security',
        port=3306
    )
    cursor = conn.cursor()

    datasets = {
        'dos': 'data/DoS_dataset.csv',
        'fuzzy': 'data/Fuzzy_dataset.csv',
        'gear': 'data/gear_dataset.csv',
        'rpm': 'data/RPM_dataset.csv'
    }

    for table, file_path in datasets.items():
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        cursor.execute(f"""
            CREATE TABLE {table} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                can_id VARCHAR(10),
                dlc INT,
                data_0 VARCHAR(10),
                data_1 VARCHAR(10),
                data_2 VARCHAR(10),
                flag VARCHAR(10)
            )
        """)

        df = pd.read_csv(file_path, header=None)
        df.columns = ['timestamp', 'can_id', 'dlc', 'data_0', 'data_1', 'data_2', 'flag']
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce').fillna(pd.Timestamp.min)

        for _, row in df.iterrows():
            cursor.execute(f"""
                INSERT INTO {table} (timestamp, can_id, dlc, data_0, data_1, data_2, flag)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))
    
    conn.commit()
    conn.close()
    print("Database setup completed.")

if __name__ == "__main__":
    setup_database()