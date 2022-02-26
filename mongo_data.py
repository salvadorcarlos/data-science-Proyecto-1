import pandas as pd
from pymongo import MongoClient
#recupere de mongo solo los de pera
client=MongoClient("mongodb://localhost:27017")
db=client.frutas
collection = db.get_collection('exportaciones')

df= pd.DataFrame(list(collection.find()))
df_pera=df.loc[df['producto']=='pera']
df_pera.to_csv('Pera.csv')

