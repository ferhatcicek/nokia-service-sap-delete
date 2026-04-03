import pandas as pd
from jinja2 import Environment, FileSystemLoader

# Excel dosyasını oku
df = pd.read_excel('sap_delete.xlsx')

# Jinja2 ortamını ayarla (şablon dosyası ile aynı dizinde çalıştığını varsayıyoruz)
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sap_delete_template.j2')

# Excel'den okunan veriyi listeye çevir
data = df.to_dict(orient='records')

# Jinja2 ile konfigürasyon dosyasını oluştur
output = template.render(items=data)

# Sonucu dosyaya yaz
with open('sap_delete_config.txt', 'w', encoding='utf-8') as f:
    f.write(output)
