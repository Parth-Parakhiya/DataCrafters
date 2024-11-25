import pymysql
import pandas as pd

def setup_database():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123@Parth@321',
        database='car_security'
    )
    cursor = conn.cursor()

    # Define the tables and corresponding dataset files
    datasets = {
        'dos': 'data/DoS_dataset.csv',
        'fuzzy': 'data/Fuzzy_dataset.csv',
        'gear': 'data/gear_dataset.csv',
        'rpm': 'data/RPM_dataset.csv'
    }

    tables = {
        'dos': """
            CREATE TABLE IF NOT EXISTS dos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                can_id VARCHAR(10),
                dlc INT,
                data_0 VARCHAR(10),
                data_1 VARCHAR(10),
                data_2 VARCHAR(10),
                data_3 VARCHAR(10),
                data_4 VARCHAR(10),
                data_5 VARCHAR(10),
                data_6 VARCHAR(10),
                data_7 VARCHAR(10),
                flag VARCHAR(10)
            )
        """,
        'fuzzy': """
            CREATE TABLE IF NOT EXISTS fuzzy (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                can_id VARCHAR(10),
                dlc INT,
                data_0 VARCHAR(10),
                data_1 VARCHAR(10),
                data_2 VARCHAR(10),
                data_3 VARCHAR(10),
                data_4 VARCHAR(10),
                data_5 VARCHAR(10),
                data_6 VARCHAR(10),
                data_7 VARCHAR(10),
                flag VARCHAR(10)
            )
        """,
        'gear': """
            CREATE TABLE IF NOT EXISTS gear (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                can_id VARCHAR(10),
                dlc INT,
                data_0 VARCHAR(10),
                data_1 VARCHAR(10),
                data_2 VARCHAR(10),
                data_3 VARCHAR(10),
                data_4 VARCHAR(10),
                data_5 VARCHAR(10),
                data_6 VARCHAR(10),
                data_7 VARCHAR(10),
                flag VARCHAR(10)
            )
        """,
        'rpm': """
            CREATE TABLE IF NOT EXISTS rpm (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                can_id VARCHAR(10),
                dlc INT,
                data_0 VARCHAR(10),
                data_1 VARCHAR(10),
                data_2 VARCHAR(10),
                data_3 VARCHAR(10),
                data_4 VARCHAR(10),
                data_5 VARCHAR(10),
                data_6 VARCHAR(10),
                data_7 VARCHAR(10),
                flag VARCHAR(10)
            )
        """
    }

    # Create tables and load data
    for table, create_query in tables.items():
        cursor.execute(create_query)

        # Clear existing data
        cursor.execute(f"DELETE FROM {table}")

        # Load and insert data
        file_path = datasets[table]
        # Define expected column names
        columns = [
            'timestamp', 'CAN ID', 'DLC',
            'DATA[0]', 'DATA[1]', 'DATA[2]', 'DATA[3]',
            'DATA[4]', 'DATA[5]', 'DATA[6]', 'DATA[7]', 'Flag'
        ]
        
        
        # Read the dataset with column names explicitly set
        df = pd.read_csv(file_path, header=None, names=columns)

        # Convert timestamp column with error handling
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')  # Coerce invalid timestamps to NaT
        df['timestamp'] = df['timestamp'].fillna(pd.Timestamp.min)  # Replace NaT with the minimum timestamp value

        # Replace missing values in other columns with 'NULL'
        df.fillna('NULL', inplace=True)

        for _, row in df.iterrows():
            # Skip rows with invalid timestamps
            if row['timestamp'] == pd.Timestamp.min:
                continue

            sql = f"""
            INSERT INTO {table} (
                timestamp, can_id, dlc, data_0, data_1, data_2, data_3,
                data_4, data_5, data_6, data_7, flag
            ) VALUES (
                '{row['timestamp']}', '{row['CAN ID']}', {row['DLC']}, 
                '{row['DATA[0]']}', '{row['DATA[1]']}', '{row['DATA[2]']}',
                '{row['DATA[3]']}', '{row['DATA[4]']}', '{row['DATA[5]']}',
                '{row['DATA[6]']}', '{row['DATA[7]']}', '{row['Flag']}'
            )
            """
            cursor.execute(sql)


    conn.commit()
    conn.close()
    print("Database setup completed.")

if __name__ == "__main__":
    setup_database()
