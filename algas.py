import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'nozare': ['Finanšu un apdrošināšana', 'IT komunikācija', 'Zinātne tehnika', 'Enerģētika', 
               'Valsts pārvalde', 'Rūpniecība', 'Tirdzniecība', 'Transports', 'Būvniecība', 
               'Veselība sociālā aprūpe', 'Izglītība', 'Lauksaimniecība', 'Naktsmītnes ēdināšana'],
    'alga_eur': [2851, 2733, 2124, 2122, 1975, 1877, 1650, 1620,1580,1758,1400,1250,1107],
    'regions': ['Rīga','Rīga','Rīga','Rīga','Rīga','Vidzeme','Pierīga','Zemgale','Latgale','Rīga','Vidzeme','Kurzeme','Latgale']
}

df = pd.DataFrame(data)

print("Latvijas algas 2024 (CSB dati)")
print(f"Vidējā alga: {df['alga_eur'].mean():.0f} €")
print(f"Top 1: {df.loc[df['alga_eur'].idxmax(), 'nozare']} – {df['alga_eur'].max()} €")

plt.figure(figsize=(12,8))
sns.barplot(data=df, x='alga_eur', y='nozare', hue='nozare', palette='rocket', legend=False)
plt.title('Vidējās algas pa nozarēm Latvijā 2024')
plt.xlabel('Alga (€)')
plt.tight_layout()
plt.savefig("grafiks_nozares.png", dpi=200)
plt.show()

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
sns.barplot(data=df, x='alga_eur', y='regions', hue='regions', palette='magma', legend=False)
plt.title('Vidējās algas pa reģioniem 2024')
plt.xlabel('Alga (€)')
plt.tight_layout()
plt.savefig("grafiks_regioni.png", dpi=300, bbox_inches='tight')
plt.close()
print("=== REĢIONU GRAFIKS IZVEIDOTS ===")