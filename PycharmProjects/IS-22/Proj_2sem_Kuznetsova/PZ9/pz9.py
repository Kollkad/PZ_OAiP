#организовать словарь avto, содержащий 3 ключа(марки авто) и списки из трех моделей
# в качестве значений. Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря

avto = {
    "Toyota": ["Camry", "Venza II", "Corolla Cross I"],
    "Volkswagen": ["Arteon I", "Tiguan III", "Touareg III"],
    "BMW": ["3 Series", "i4 G26", "Active Tourer U06"]
      }


for marka, models in avto.items():
    print(f"Вторая модель авто {marka}:", models[1])
print('---------')
for models in avto.values():
    for model in models:
        print(model)