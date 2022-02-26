import pandas as pd
import matplotlib.pyplot as plt
#seleccion  uva de archivo original
data_frame=pd.read_csv('./data/exportaciones.csv')
df=data_frame[['producto','pais_destino','año','totales_tn','totales_usd']]

df_uva=df.loc[df['producto']=='Uva']
df_uva.to_csv('uva.csv')
#media falta cualcular mediana
media_uva=df_uva['totales_tn'].mean()

#totales de uva por año
total_u_13=df_uva.loc[df_uva['año']==2013,'año'].sum()
total_u_14=df_uva.loc[df_uva['año']==2014,'año'].sum()
total_u_15=df_uva.loc[df_uva['año']==2015,'año'].sum()
total_u_16=df_uva.loc[df_uva['año']==2016,'año'].sum()
total_u_17=df_uva.loc[df_uva['año']==2017,'año'].sum()

eje_x=['2013','2014','2015','2016','2017']
eje_y= [total_u_13,total_u_14,total_u_15,total_u_16,total_u_17]
plt.bar(eje_x, eje_y)
plt.ylabel('Año')
plt.xlabel('Toneladas')
plt.title('total toneladas de Uvas exportadas')
plt.show()

#df_total_uva=df_uva.loc[df_uva['año']=='2017']
#df_uva=df.loc[df['producto']=='Uva']

#print(df_manzana['pais_destino'].mode())
#tendriamos que acumular x años,toneladas o algo asi
#conexion= mysql.connector.connect(user='root', password='12345678',host='localhost',database='prueb1_db',port='3306')










