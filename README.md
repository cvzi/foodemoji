# foodemoji
Decorate a German text (e.g. restaurant menu) with food emojis 


## Example

```python
>>> import foodemoji
>>> text = """Hähnchenbrust mit Apfelrotkraut
Vegetarische Maultaschen
Kartoffelknödel
Paniertes Schnitzel mit Pommes frites
Rinderbraten, Rotweinsauce und Spätzle"""

>>> print(foodemoji.decorate(text))
"""Hähnchenbrust :rooster: mit Apfelrotkraut :red_apple:
Vegetarische :green_heart: Maultaschen
Kartoffelknödel :potato:
Paniertes Schnitzel mit Pommes frites :french_fries:
Rinderbraten :cow:, Rotweinsauce :wine_glass: und Spätzle"""

>>> import emoji
>>> print(emoji.emojize(foodemoji.decorate(text)))
"""Hähnchenbrust 🐓 mit Apfelrotkraut 🍎
Vegetarische 💚 Maultaschen
Kartoffelknödel 🥔
Paniertes Schnitzel mit Pommes frites 🍟
Rinderbraten 🐮, Rotweinsauce 🍷 und Spätzle"""

>>> text2 = """Gegrillte Hähnchenbrust mit gekochter Hähnchenbrust
Gebratenes Hähnchen mit Hähnchenschnitzel"""
>>> print(foodemoji.decorate(text2))
"""Gegrillte Hähnchenbrust :rooster: mit gekochter Hähnchenbrust :rooster:
Gebratenes Hähnchen :rooster: mit Hähnchenschnitzel :rooster:"""

>>> print(foodemoji.decorate(text2, line_by_line=True))
"""Gegrillte Hähnchenbrust mit gekochter Hähnchenbrust :rooster:
Gebratenes Hähnchen mit Hähnchenschnitzel :rooster:"""
```


Install
-------

`pip install german-foodemoji`

See: https://pypi.org/project/german-foodemoji/


## Requirements:
 * Python 2/3   
  
To actually print the unicode emojis and for the units tests the package [emoji](https://github.com/carpedm20/emoji)>=0.5.0 is required:
 * `pip install emoji`
