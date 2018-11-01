try:
    import foodemoji
except ImportError:
    import sys
    import os
    sys.path.insert(0, '..')
    import foodemoji
    path = os.path.join(os.path.abspath(".."), "foodemoji")
    print("Imported foodemoji from %s" % path)

text = """Hähnchenbrust mit Apfelrotkraut
Vegetarische Maultaschen
Kartoffelknödel
Paniertes Schnitzel mit Pommes frites
Rinderbraten, Rotweinsauce und Spätzle"""

print(foodemoji.decorate(text))
print(" ")


text2 = """Gegrillte Hähnchenbrust mit gekochter Hähnchenbrust
Gebratenes Hähnchen mit Hähnchenschnitzel"""
print(foodemoji.decorate(text2))
print(" ")

print(foodemoji.decorate(text2, line_by_line=True))
print(" ")

import emoji
print(emoji.emojize(foodemoji.decorate(text)))
print(" ")

print(emoji.emojize(foodemoji.decorate(text2)))
print(" ")

print(emoji.emojize(foodemoji.decorate(text, line_by_line=True)))
print(" ")
