import pandas as pd
import matplotlib.pyplot as plt
df_u=pd.read_csv('./data/uva.csv')
df_m=pd.read_csv('./data/manzana.csv')
df_p=pd.read_csv('./data/Pera.csv')
df_p.drop(columns='_id',inplace=True)
df_final =pd.concat([df_p,df_m,df_u])
columnas=['producto','pais_desito','año','totales_tn','totales_usd']

u_media=df_u['totales_tn'].mean()
u_mediana=df_u['totales_tn'].median()

p_media=df_p['totales_tn'].mean()
p_mediana=df_p['totales_tn'].median()

m_media=df_m['totales_tn'].mean()
m_mediana=df_m['totales_tn'].median()


total_u=df_u['totales_tn'].sum()
total_p=df_p['totales_tn'].sum()
total_m=df_m['totales_tn'].sum()

pesos=[0.3 , 0.3,0.4]
media_ponderada=((pesos[0] * total_u) + (pesos[1] * total_p)+(pesos[2] * total_m))/(pesos[0]+pesos[1]+pesos[2])

columna=['producto','pais_desito','año','totales_tn','totales_usd']
data_final=df_final.filter(columna)
moda=data_final['año'].mode()#busque el el año que mas se importo uva pera manzana con la moda

total_general=data_final['totales_tn'].sum()

data_final=df_final.filter(columnas)
moda=data_final['año'].mode()#busque el el año que msa se importo uva pera manzana con la moda
moda_f=int(moda)


columnas=['uva-media','pera-media','manzana-media','manazana-mediana','uva-mediana','pera-madiana','año-mayor-exp.','med-pondera']
valores=[u_media ,p_media,m_mediana,m_mediana,u_mediana,p_mediana,moda_f,media_ponderada]
resumen=pd.DataFrame([valores],columns=columnas)
print(resumen.transpose())

data_final.to_csv('final.csv')


#grafico

etiquetas = ['total uva','total pera','total manzana','total general']
valores = [total_u,total_p,total_m,total_general]
colores = ['red','green','blue','yellow']

plt.pie(x=valores, labels=etiquetas, colors = colores)
plt.title('totale ')
plt.show()
