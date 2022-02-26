
import pandas as pd
from sqlalchemy import create_engine
#recupere de mysql solo los de manzana
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/exportaciones')
sql = 'select * from exp where producto="Manzana"'
df_manzana= pd.read_sql(sql, engine)
df_manzana.to_csv('manzana.csv')
print(df_manzana)
