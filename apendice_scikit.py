#Importa o algoritmo de clustering do kmeans da biblioteca scikit
from sklearn.cluster import KMeans

#Importa a biblioteca de pre-processamento
from sklearn.preprocessing import StandardScaler

#Definir os dados de exemplo
#Será uma lista de listas
x = [[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]]

#Vamos instanciar o standard scaler para padronizar os dados
scaler = StandardScaler()

#Vamos aplicar  o escalador nos dados para que tenham média 0 e desvio padrão 1
X_scaled = scaler.fit_transform(x)

#Criar a instancia do algoritmo KMeans com 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42)

#Vamos aplicar o algoritmo nos dados padronizados
kmeans.fit(X_scaled)

#Vamos exibir os rotulos dos clusters atribbuidos a cada ponto
print(kmeans.labels_)
