.. foodemoji documentation master file, created by
   sphinx-quickstart on Thu Oct 25 11:40:22 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

foodemoji
~~~~~~~~~

Decorate a German text (e.g. restaurant menu) with food specific emojis 

`Source on Github <https://github.com/cvzi/foodemoji>`_

Example
=======

.. code-block:: python


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


Install
=======

.. code-block:: shell

   pip install german-foodemoji

See: `https://pypi.org/project/german-foodemoji/ <https://pypi.org/project/german-foodemoji/>`_

Requirements
============
*   Python 3.7+

To actually print the unicode emojis and for the units tests the package `emoji <https://github.com/carpedm20/emoji>`_>=2.1.0 is required:

.. code-block:: shell

   pip install emoji


Functions
=========
.. currentmodule:: foodemoji
.. autofunction:: decorate
.. autofunction:: decorate_whole
.. autofunction:: decorate_lines
.. autofunction:: _load

Supported emojis and patterns
=============================
.. literalinclude:: ../foodemoji/foodemojis.json
   :language: JSON
   :caption: foodemojis.json
   :name: foodemojis-json

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
