import datetime # ou from datetime import date

d = datetime.date(2025, 3, 31)

print(d)
print(datetime.date.today()) #fala a data de hoje

data_hora = datetime.datetime(2025, 2, 21, 10, 10, 1) #Mostra data e hora
print(datetime.datetime.today())

print(data_hora)

#time

hora = datetime.time(20, 47, 55)
print(hora)

#now  Essa função equivale ao today, só que adiciona o fusohorário da máquina

atual = datetime.datetime.now()

#utcnow  Vem sem o fusohorário local para que depois possa ser adicionado.

atual2 = datetime.datetime.utcnow()