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
```

## Requirements:
 * Python 3   
  
To actually print the unicode emojis the package [emoji](https://pypi.org/project/emoji/) is required:
 * `pip install emoji`