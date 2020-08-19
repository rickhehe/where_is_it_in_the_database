import re

import pandas as pd

from connections import replication
from query import query

def get_df_advanced(df):

    t = input('hint for the table: ')
    c = input('hint for the column: ')

    df = df[
        df.table_name.str.contains(t, flags=re.I)
        & df.table_name.str.contains('^[^x]', flags=re.I)
        & df.column_name.str.contains(c, flags=re.I)
    ]

    return df

def sql_stream(df):

    k = input('hint for the keyword: ')

    for it in df.itertuples():
        yield f'''select {it.table_name}.{it.column_name}
                    from {it.table_name}
                   where {it.table_name}.{it.column_name}::text ~* '{k}'
        '''

if __name__ == '__main__':

    df = get_df_advanced(
        query('sql.sql', replication)
    )
    
    for x in sql_stream(df):
        df_x = pd.read_sql(x,replication)
        if not df_x.empty:
            print(x)
            print(df_x)
