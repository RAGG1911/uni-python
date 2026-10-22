import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("librerias/datosVentas.csv")

plt.figure(figsize=(10, 6))
plt.bar(df['Mes'], df['Ventas'])

plt.title('Ventas Mensuales Primer Semestre 2026')
plt.xlabel('Meses')
plt.ylabel('Ventas ($)')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('librerias/Ventas2026'+'.jpeg')
plt.savefig('librerias/Ventas2026'+'.png')
plt.show()