from Crawler_sisu import crawler
import json

a = crawler()
dados = a.get_lista_selecionados()
with open('lista-selec.json', 'w') as f1:
    f1.write(json.dumps(dados))

dados = a.get_lista_em_espera()
with open('lista-esp.json', 'w') as f2:
    f2.write(json.dumps(dados))
  
