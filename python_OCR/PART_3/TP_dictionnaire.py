# RÉSULTAT ATTENDU
fruits = DictionnaireOrdonne()
fruits # {}
fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
fruits # {'pomme': 52, 'poire': 34, 'prune': 128, 'melon': 15}
fruits.sort()
print(fruits) # {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128}
legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
print(legumes) # {'carotte': 26, 'haricot': 48}
len(legumes) # 2
legumes.reverse()
fruits = fruits + legumes
fruits # {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128, 'haricot': 48, 'carotte': 26}
del fruits['haricot']
'haricot' in fruits # False
legumes['haricot'] # 48
for cle in legumes:
    print(cle)
# haricot
# carotte
legumes.keys() # ['haricot', 'carotte']
legumes.values() # [48, 26]
for nom, qtt in legumes.items():
    print("{0} ({1})".format(nom, qtt))
# haricot (48)
# carotte (26)

# CODE
