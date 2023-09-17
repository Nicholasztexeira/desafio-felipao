heroi = "Felipão da DIO"

experiencia = 10001

if (experiencia<1001):
    nivel = "Ferro"
elif (2001>experiencia>1000):
    nivel = "Bronze"
elif (5001>experiencia>2000):
    nivel = "Prata"
elif (6001>experiencia>5000):
    nivel = "Prata Ouro"
elif (7001>experiencia>6000):
    nivel = "Ouro"
elif (8001>experiencia>7000):
    nivel = "Platina"
elif (9001>experiencia>8000):
    nivel = "Ascendente"
elif (10001>experiencia>9000):
    nivel = "Imortal"
elif (experiencia>=10000):
    nivel = "Radiante"
  
print ("O Herói de nome {0} está no nível de {1}".format(heroi,nivel))