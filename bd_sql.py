import pandas as pd
from sqlalchemy import create_engine
#del archivo original copie a mysql solo algunas columnas
df=pd.read_csv('./data/exportaciones.csv')
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/exportaciones')
expot=df[['producto' ,'pais_destino','año','totales_tn','totales_usd']]
expot.to_sql('exp',engine, if_exists = 'replace' ,index=False)





