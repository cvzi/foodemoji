# foodemoji
[![foodemoji on PyPI](https://img.shields.io/pypi/v/german-foodemoji.svg)](https://pypi.python.org/pypi/german-foodemoji)
[![Python Versions](https://img.shields.io/pypi/pyversions/german-foodemoji.svg)](https://pypi.python.org/pypi/german-foodemoji)
[![Coverage Status](https://coveralls.io/repos/github/cvzi/foodemoji/badge.svg?branch=master)](https://coveralls.io/github/cvzi/foodemoji?branch=master)
[![Build Status](https://travis-ci.org/cvzi/foodemoji.svg?branch=master)](https://travis-ci.org/cvzi/foodemoji)
[![Documentation Status](https://readthedocs.org/projects/foodemoji/badge/?version=latest)](https://foodemoji.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/37b81de096584b068763271c6a52e441)](https://app.codacy.com/app/cvzi/foodemoji?utm_source=github.com&utm_medium=referral&utm_content=cvzi/foodemoji&utm_campaign=Badge_Grade_Dashboard)
[![Maintainability](https://api.codeclimate.com/v1/badges/717455cf2690747284dc/maintainability)](https://codeclimate.com/github/cvzi/foodemoji/maintainability)

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

## Install
`pip install german-foodemoji`

See: [https://pypi.org/project/german-foodemoji/](https://pypi.org/project/german-foodemoji/)

## Requirements
*   Python 2/3

To actually print the unicode emojis and for the units tests the package [emoji](https://github.com/carpedm20/emoji)>=0.5.0 is required:
*   `pip install emoji`
