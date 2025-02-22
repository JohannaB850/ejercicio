st.title("Análisis del Dataset Credit")
 
# Cargar los datos desde GitHub
df = pd.read_csv("https://raw.githubusercontent.com/giuliannaac/ejercicio/main/Credit.csv")
 
# Eliminar la columna innecesaria
df.drop(columns=["Unnamed: 0"], inplace=True)
 
# Mostrar información del dataset
st.write("### Información General del Dataset")
st.write(df.info())
 
# Gráfico de distribución de la variable Balance
st.write("### Distribución de la Variable Balance")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Balance"], bins=30, kde=True, color='blue', ax=ax)
ax.set_title("Distribución de la Variable Balance")
ax.set_xlabel("Balance")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
 
# Matriz de correlación
st.write("### Matriz de Correlación")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)
 
