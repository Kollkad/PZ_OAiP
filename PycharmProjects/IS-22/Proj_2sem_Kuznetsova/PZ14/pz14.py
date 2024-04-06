#Из исходного текстового файла выбрать все html коды изображений. Посчитать их колличество
import re
p = re.compile(r"<img.*?>")
with open('pazzl.html') as file:
  content = file.read()
  for i in p.findall(content):
    print(i)
  print('Количество изображений -', len(p.findall(content)))