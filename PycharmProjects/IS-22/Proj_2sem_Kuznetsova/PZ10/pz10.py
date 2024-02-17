#на трех участках выращиваются следующие сельскохозяйственные культуры:
#картофель, лук, морковь, горох, капуста, редис. Определить, какие из этих культур имеются на каждом участке,
# имеются хотя бы на одном из участков и не имеются ни на одном участке.

ovoshi = {'картофель', 'лук', 'морковь', 'горох', 'капуста', 'редис'}

uchastok_1 = {'картофель', 'лук', 'морковь'}
uchastok_2 = {'лук', 'морковь', 'горох'}
uchastok_3 = {'лук', 'горох', 'капуста'}

vse = uchastok_1 & uchastok_2 & uchastok_3

odin = uchastok_1 | uchastok_2 | uchastok_3

net = ovoshi - odin

print('На каждом участке имеются ', vse)
print('Имеются хoтя бы на одном участке ', odin)
print('Не имеются ни на одном из участков ', net)