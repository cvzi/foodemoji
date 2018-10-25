# -*- coding: utf-8 -*-
# https://github.com/cvzi/foodemoji
"""
Decorate a German text (e.g. restaurant menu) with food specific emojis
https://github.com/cvzi/foodemoji

Unicode country code emoji flags for Python
~~~~~~~~~~~~~~~~
    >>> import foodemoji
    >>> foodemoji.decorate("Apfelrotkraut")
    'Apfelrotkraut :red_apple:'
    >>> import emoji
    >>> emoji.emojize(foodemoji.decorate("Apfelrotkraut"))
    'Apfelrotkraut 🍎'
"""
__version__ = '1.1.0'
__author__ = 'cuzi'
__email__ = 'cuzi@openmail.cc'
__source__ = 'https://github.com/cvzi/foodemoji'
__license__ = """
MIT License

Copyright (c) cuzi 2018

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__all__ = ['decorate']

import pkg_resources
import json
import re
import sys
import os

_emoji_re = {}
_wordend = None
_PY2 = sys.version_info.major is 2

def _load():
    global _emoji_re
    global _wordend

    # Load json file
    if os.path.isfile(os.path.join(os.path.dirname(__file__), 'foodemojis.json')): # pragma: no cover
        with open(os.path.join(os.path.dirname(__file__), 'foodemojis.json'), 'rb') as fs:
            emoji_list = json.loads(fs.read().decode('utf-8'))
    else: # pragma: no cover
        with pkg_resources.resource_stream(__name__, 'foodemojis.json') as fs:
            emoji_list = json.loads(fs.read().decode('utf-8'))

    # Pre compile regular expressions
    _wordend = re.compile('(:|,|\\(|\\[|\\s|$)', flags=re.MULTILINE)

    _emoji_re = {}
    for emo in emoji_list:
        emokey = emo
        if _PY2:
            emokey = emokey.encode('utf-8')
        _emoji_re[emokey] = []
        try:
            for q in emoji_list[emo]:
                _emoji_re[emokey].append(re.compile(q,flags=re.MULTILINE|re.IGNORECASE|re.UNICODE))
        except re.error as e: # pragma: no cover
            e.args = ("%s: %r -> %r" % (str(e.args[0]), emokey, q),)
            raise e

def decorate(text, line_by_line=False):
    """Decorate text with food-specific emoji in the form ':emoji_name:'

    :param str text: the text to decorate
    :param bool line_by_line: if true the text is decorated line by line and an emoji can only occur once per line.
    :return: the decorated text
    :rtype: str
    """

    if _PY2:
        if not isinstance(text, unicode):
            try:
                text = text.decode("ascii", errors="strict")
            except UnicodeDecodeError:
                raise TypeError("Argument 'text' must be unicode.")

    if line_by_line:
        return decorate_lines(text)
    return decorate_whole(text)

def decorate_whole(text):
    """Decorates text with food-specific emojis
     - Whole text at once approch
     - Emoji can occur several times per line

    :param str text: the text to decorate
    :return: the decorated text
    :rtype: str
    """

    if len(_emoji_re) == 0:
        _load()

    for emo in _emoji_re:
        for regex in _emoji_re[emo]:
            cursor = 0
            m = regex.search(text, pos=cursor)
            while m:
                # find next space:
                lastchar = m.group(0)[-1]
                if len(lastchar.strip()) == 0: # last char in pattern is white space
                    space = m.end()-1
                else:  # find next whitespace or end of line
                    space = _wordend.search(text, pos=m.end()).start()

                # put emoji in the whitespace
                text = text[:space] + ' ' + emo + text[space:]

                cursor = space + len(emo) + 1

                m = regex.search(text, pos=cursor)

    return text

def decorate_lines(text):
    """Decorates text with food-specific emojis
     - Line by line approch
     - An emoji can only occur once per line (last occurunce)
    """
    if len(_emoji_re) == 0:
        _load()

    # Split by lines
    text = re.split('(\r?\n)', text)

    for emo in _emoji_re:

        for i, line in enumerate(text):
            if not line.strip():
                continue

            set_position = []
            for regex in _emoji_re[emo]:
                cursor = 0

                m = regex.search(line, pos=cursor)
                while m:
                    if set_position:
                        # remove last emoji
                        last = set_position.pop()
                        line = line[:last[0]] + line[last[1]:]
                        cursor -= last[1] - last[0]
                        m = regex.search(line, pos=cursor)

                    # find next space:
                    lastchar = m.group(0)[-1]
                    if len(lastchar.strip()) == 0: # last char in pattern is white space
                        space = m.end()-1
                    else:  # find next whitespace or end of line
                        space = _wordend.search(line, pos=m.end()).start()

                    # put emoji in the whitespace
                    line = line[:space] + ' ' + emo + line[space:]

                    cursor = space + len(emo) + 1

                    # remember emoji position
                    set_position.append((space, cursor))

                    # search for next match
                    m = regex.search(line, pos=cursor)

                text[i] = line


    return ''.join(text)

if __name__ == '__main__':
    text = """Hähnchenbrust mit Hähnchensauce
Vegetarische Maultaschen mit vegetarischen Ravioli
Kartoffelknödel mit Kartoffeln
Paniertes Schnitzel mit Schwein
Rinderbraten mit Rindersauce"""
    print(decorate(text))
    print(decorate(text, line_by_line=True))




