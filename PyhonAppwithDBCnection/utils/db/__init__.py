#  Copyright (c) 2023.

# python codes to connect and query on DB
import pandas as pd
import mysql.connector as database
from mysql.connector import pooling as database


def connect(configs):
    '''
    Connect with mariaDB
        input:
            configs:dict ->contain connection details
        return:
            connection:object
    '''
    print("connecting .....")
    connection = database.MySQLConnectionPool(
                user = configs['user'],
                password = configs['password'],
                host = configs['host'],
                database = configs['database'],
                pool_size = configs['pool_size'],
                pool_reset_session = True,
                pool_name= configs['pool_name']
                )
    print(connection)
    return connection

def disconnect(connection):
    """ 
    Disconnects with DB
        input:
            connection:object
        return:
            True
    """
    connection.close()
    print("Connection with DB closed Succesfully")
    return True

def queryDb(connection, year, where_feild, where_data):
    """
    query DB to get information required
        input:
            connection:object
            year:str
            where_feild:str
            where_data:str
        return:
            data:list
    """

    datas = []
    cursor = connection.cursor()
    query = f"""
                with dated_data as(
                    SELECT * FROM sales
                    where year(Sold_Date) = '{year}')
                select * 
                    from dated_data 
                    where {where_feild} in {tuple(where_data)}
                    limit 10;
            """
    
    cursor.execute(query)
    print("query executed succesfully")
    feilds = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=feilds)
    cursor.close()
    return df.to_json(orient='records', date_format='iso')

def queryList(connection):
    """
    Query the list of columns from DB that can have unique datas
        input:
            connection: object
        return:
            data: list
    """
    data = ["historical_year"]
    cursor = connection.cursor()
    query = "desc sales;"
    cursor.execute(query)
    print("query executed succesfully")
    rows = cursor.fetchall()
    for row in rows:
        if 'varchar' in row[1]:
            if  row[1] != str("varchar(100)"):
                data.append(row[0])
    return data

def queryUniList(connection,column):
    """
    Query the list of unique values in the column
        input:
            connection: object
            column: str
        return:
            data: list
    """
    cursor = connection.cursor()
    query = f"select distinct({column}) from sales;"
    if column == 'historical_year':
        query=f"select distinct(year(Sold_Date) from sales;"
    cursor.execute(query)
    print(query)
    rows = cursor.fetchall()
    print(rows)
    if rows == [(None,)]:
        return ''
    data= [i[0] for i in rows]
    return {column:data}