# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import mysql.connector
import pandas as pd
import numpy as np

class MysqlIO:
    """Connect to MySQL server with python and excecute SQL commands."""
    def __init__(self, database='test'):
        try:
            # Change the host, user and password as needed
            connection = mysql.connector.connect(host='localhost',
                                                 database=database,
                                                 user='Zhou',
                                                 password='jojojo',
                                                 use_pure=True
                                                 )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version", db_info)
                print("Your're connected to database:", database)
                self.connection = connection
        except Error as e:
            print("Error while connecting to MySQL", e)
            
    def execute(self, query, header=False):
        """Execute SQL commands and return retrieved queries."""
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(query)
        try:
            record = cursor.fetchall()
            if header:
                header = [i[0] for i in cursor.description]
                return {'header': header, 'record': record}
            else:    
                return record
        except:
            pass
        
        
    def table_to_df(self, table):
        """Return the retrieved SQL queries into pandas dataframe."""
        res = self.execute('SELECT * FROM ' + table, header=True)
        df = pd.DataFrame(res['record'])
        df.columns = res['header']
        return df
    
    def df_to_table(self, df, title, data_type='auto', replace=False):
        """Insert pandas dataframe into database table."""
        # If the tables exists and we don't want to replace
        if self.execute("SHOW TABLES LIKE '{0}'".format(title)) and not replace:
            raise FileExistsError("The table with name '{0}' already exists in current database!".format(title))
            
        # Automatically decide datatype for mysql from dataframe
        if data_type == 'auto':
            d_type = {}
            for i in df.columns:
                if str(df[i].dtype) == 'int64':
                    d_type[i] = 'INT'
                elif str(df[i].dtype) == 'float64':
                    d_type[i] = 'FLOAT'
                elif str(df[i].dtype) == 'object':
                    d_type[i] = 'VARCHAR(50)'
                else:
                    print("Failed using 'auto'. Please specify the datatypes!")
        else:
            if type(data_type) is not dict:
                raise NameError("data_type is not correctly specified!")
            else:
                d_type = data_type
        
        # Insert table
        l_data_type = [(k, v, ',') for k, v in d_type.items()]
        l_data_type = np.array(l_data_type).flatten().tolist()[:-1]
        self.execute('DROP TABLE IF EXISTS {0}'.format(title))
        self.execute('CREATE TABLE {0}({1})'.format(title, ' '.join(l_data_type)))
        
        # Insert data
        ncols = len(df.columns)
        cursor = self.connection.cursor(buffered=True)
        df = df.where(df.notnull(), None) # Replace nan with None (for proper inserting NULL)
        cursor.executemany("INSERT INTO {0} VALUES({1})".format(title, ','.join(['%s']*ncols)),
                           df.values.tolist())
        self.connection.commit()
        
    def leetcode_to_table(self, d, data_type='auto'):
        """Import leetcode testcase dictionary to MySQL."""
        for title in d['headers'].keys():
            df = pd.DataFrame(d['rows'][title])
            df.columns = d['headers'][title]
            if data_type == 'auto' or data_type[title] == 'auto':
                self.df_to_table(df, title, replace=True)
            else:
                self.df_to_table(df, title, data_type=data_type[title], replace=True)
