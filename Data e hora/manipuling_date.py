#Exemplo de código com timedelta

import datetime


d = datetime.date(2025, 3, 11)
print(d)
d = d + datetime.timedelta(weeks=2) #Adiciona duas semanas à data anterior
print(d)

#strftime  Módulo que formata uma objeto datetime para o modo que quisermos que seja exibido

print(d.strftime("%d/%m/%Y  %H:%M"))

#strptime converte uma string para objeto datetime

data_nascimento_str = "27/06/2006 16:00"

data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y %H:%M") #A máscara precisa estar no mesmo formato da string que será convertida.
print(data_nascimento)

#Timezone, fuso horário  se utiliza o módulo pytz.

import pytz

data_atual_finlandia = datetime.datetime.now(pytz.timezone("Europe/Helsinki"))
print(data_atual_finlandia.strftime("%d/%m/%Y %H:%M"))


#ou podemos fazer sem a biblioteca pytz
from datetime import timezone, timedelta

data_atual_finlandia2 = datetime.datetime.now(timezone(timedelta(hours = 2)))