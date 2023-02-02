# -*- coding: utf-8 -*-
# https://github.com/cvzi/foodemoji
import sys
import packaging.version

try:
    import foodemoji
except ImportError:
    import os
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, include)
    import foodemoji
    print("Imported foodemoji from %s" % os.path.abspath(os.path.join(include, "foodemoji")))


try:
    import emoji
    assert packaging.version.Version(emoji.__version__) >= packaging.version.Version('1.6.3')
except AssertionError as e:
    print("Module/Package `emoji` is version %s, it needs to be at least version 1.6.3" % emoji.__version__)
    e.args = ("emoji module version < 1.6.3", )
    raise e

PY2 = sys.version_info.major == 2

def test_check_circular():
    foodemoji.decorate("ensure loaded") # ensure emojis are loaded
    assert len(foodemoji._emoji_re) > 0

    text = ' '.join(foodemoji._emoji_re.keys())
    if text != foodemoji.decorate(text):
        # Find the circular emoji
        for emojiname in foodemoji._emoji_re:
            try:
                assert emojiname == foodemoji.decorate(emojiname)
            except AssertionError as e:
                print("Error: Circular emoji: `%s`" % emojiname)
                print("Result: `%s`" % foodemoji.decorate(emojiname))
                print("Maybe use `:[^\\:]%s`" % emojiname[1:])
                e.args = ("Circular emoji: `%s`" % emojiname, )
                raise e

def test_good_regex():
    foodemoji.decorate("ensure loaded") # ensure emojis are loaded
    assert len(foodemoji._emoji_re) > 0

    def is_in_brackets(query, text):

        if query in text:
            cursor = 0
            while query in text[cursor:]:
                pos = text.index(query, cursor)
                if text.rfind("[", 0, pos) == -1 and text.rfind("(", 0, pos) == -1:
                    return False
                if text.find("]", pos) == -1 and text.find(")", pos) == -1:
                    return False
                cursor = pos + len(query)

            return True
        else:
            return True

    for emojiname in foodemoji._emoji_re:
        for regex in foodemoji._emoji_re[emojiname]:
            for symbol in ("$", "^"):
                try:
                    assert is_in_brackets(symbol, regex.pattern)
                except AssertionError as e:
                    desc = "Error: `%s` should be in brackets: `%s`" % (symbol, regex.pattern)
                    e.args = (desc, )
                    raise e



def test_basic():
    pairs = [
        ("", ""), # empty
        (" ", " "), # space
        ("Fish & chips", "Fish :fish: & chips :french_fries:"), # circular
        ("Tintenfisch", "Tintenfisch :squid:"), # no fish
        ("Haifisch", "Haifisch :fish:"),
        ("Grießflammerie", "Grießflammerie"), # lamm
        (u"Kürbis", u"Kürbis :jack-o-lantern:"),
        ("Reis\nPommes frites", "Reis :cooked_rice:\nPommes frites :french_fries:"),
        ("Sate sauce", "Sate :flag_for_Indonesia: sauce"),
        ("Mensateria", "Mensateria"),
        ("Satesauce", "Satesauce :flag_for_Indonesia:"),
        ("Currygericht", "Currygericht :curry_rice:"),
        ("Currysauce", "Currysauce"),
        ("Currysoße", "Currysoße"),
        ("Curry-soße", "Curry-soße"),
        ("Currywurst", "Currywurst :pig:"),
        ("Currydip", "Currydip"),
        ("Flussbarbe", "Flussbarbe :fish:"),
        ("Rhabarber", "Rhabarber"),
    ]
    for text, text_with_emoji in pairs:
        text = text.decode("utf8") if PY2 and not isinstance(text, unicode) else text
        text_with_emoji = text_with_emoji.decode("utf8") if PY2 and not isinstance(text_with_emoji, unicode) else text_with_emoji
        try:
            assert text_with_emoji == foodemoji.decorate(text)
        except AssertionError as e:
            desc = "Error: `%s` should be `%s`" % (foodemoji.decorate(text).encode("utf8"), text_with_emoji.encode("utf8"))
            e.args = (desc, )
            raise e


def test_example_text():
    text = """Hähnchenbrust mit Apfelrotkraut
    Vegetarische Maultaschen
    Kartoffelknödel
    Paniertes Schnitzel mit Pommes frites
    Rinderbraten, Rotweinsauce und Spätzle"""
    text = text.decode("utf8") if PY2 else text
    text_decorated = foodemoji.decorate(text)
    for x in ( ':rooster:', ':red_apple:', ':green_heart:',
               ':dumpling:', ':potato:', ':french_fries:',
               ':cow:', ':wine_glass:' ):
        assert x in text_decorated


    text = """Wir essen Mousakás mit Pommes und öhren.\nDas Hackfleisch wird aus Oktopus zubereitet."""
    text = text.decode("utf8") if PY2 else text
    text_decorated = foodemoji.decorate(text)
    for x in ( ':eggplant:', ':french_fries:', ':octopus:' ):
        assert x in text_decorated

def test_double_decorate():
    text = """Hähnchenbrust mit Apfelrotkraut
    Vegetarische Maultaschen
    Kartoffelknödel
    Paniertes Schnitzel mit Pommes frites
    Rinderbraten, Rotweinsauce und Spätzle"""
    text = text.decode("utf8") if PY2 else text
    text_with_emoji = foodemoji.decorate(foodemoji.decorate(text))
    for x in ( ':rooster:', ':red_apple:', ':green_heart:',
               ':dumpling:', ':potato:', ':french_fries:',
               ':cow:', ':wine_glass:' ):
        assert x in text_with_emoji

def test_already_has_emoji():
    text = """💬Hähnchenbrust😈 mit Apfelrotkraut
    Vegetarische Maultaschen‍💋‍👨👃
    ‍❤️ Kartoffelknödel
    Paniertes 👃Schnitzel💋 mit Pommes👯‍♂ frites
    Rinderbraten, 😡Rotweinsauce😕 und Spätzle😼"""
    text = text.decode("utf8") if PY2 else text
    text_with_emoji = foodemoji.decorate(foodemoji.decorate(text))
    for x in ( ':rooster:', ':red_apple:', ':green_heart:',
               ':dumpling:', ':potato:', ':french_fries:',
               ':cow:', ':wine_glass:' ):
        assert text_with_emoji.count(x) == 2

def test_position_in_whitespace():
    pairs = [
        ('Hähnchenbrust', 'Hähnchenbrust :rooster:'),
        ('Hähnchenbrust.', 'Hähnchenbrust. :rooster:'),
        ('Hähnchenbrust. ', 'Hähnchenbrust. :rooster: '),
        ('Hähnchenbrust .', 'Hähnchenbrust :rooster: .'),
        ('Hähnchenbrust: Apfelrotkraut', 'Hähnchenbrust :rooster:: Apfelrotkraut :red_apple:'),
        ('Hähnchenbrust.\n', 'Hähnchenbrust. :rooster:\n'),
        ('Hähnchenbrust.\r\n', 'Hähnchenbrust. :rooster:\r\n'),
        ('Hähnchenbrust Apfelrotkraut', 'Hähnchenbrust :rooster: Apfelrotkraut :red_apple:'),
        ('Hähnchenbrust\nApfelrotkraut', 'Hähnchenbrust :rooster:\nApfelrotkraut :red_apple:'),
        ('Hähnchenbrust.\nApfelrotkraut', 'Hähnchenbrust. :rooster:\nApfelrotkraut :red_apple:'),
        ('Hähnchenbrust  Apfelrotkraut', 'Hähnchenbrust :rooster:  Apfelrotkraut :red_apple:'),
        ('pancake', 'pancake :pancakes:'),
        ('pancakes ', 'pancakes :pancakes: '),
        ('Pancake  Gericht', 'Pancake :pancakes:  Gericht'),
        ('Pancake  ', 'Pancake :pancakes:  '),
    ]
    for text, text_with_emoji in pairs:
        text = text.decode("utf8") if PY2 else text
        text_with_emoji = text_with_emoji.decode("utf8") if PY2 else text_with_emoji
        try:
            assert text_with_emoji == foodemoji.decorate(text)
        except AssertionError as e:
            desc = "Error: Got `%s` expected `%s`" % (foodemoji.decorate(text).encode("utf8"), text_with_emoji.encode("utf8"))
            e.args = (desc, )
            raise e

    for text, text_with_emoji in pairs:
        text = text.decode("utf8") if PY2 else text
        text_with_emoji = text_with_emoji.decode("utf8") if PY2 else text_with_emoji
        try:
            assert text_with_emoji == foodemoji.decorate(text, line_by_line=True)
        except AssertionError as e:
            desc = "Error: Got `%s` expected `%s`" % (foodemoji.decorate(text, line_by_line=True).encode("utf8"), text_with_emoji.encode("utf8"))
            e.args = (desc, )
            raise e


def test_same_result_whole_linebyline_approach():
    examples = [
        'Hähnchenbrust',
        'Hähnchenbrust.',
        'Hähnchenbrust. ',
        'Hähnchenbrust .',
        'Hähnchenbrust.\n',
        'Hähnchenbrust.\r\n',
        'Hähnchenbrust Apfelrotkraut',
        'Hähnchenbrust\nApfelrotkraut',
        'Hähnchenbrust.\nApfelrotkraut',
        'Hähnchenbrust  Apfelrotkraut',
        'Gegrillte Hähnchenbrust',
        'Gegrillte Hähnchenbrust ',
        'Gegrillte Hähnchenbrust. ',
    ]
    for text in examples:
        text = text.decode("utf8") if PY2 else text
        try:
            assert foodemoji.decorate(text, line_by_line=False) == foodemoji.decorate(text, line_by_line=True)
        except AssertionError as e:
            desc = "Error: `%s` (line_by_line=False) != `%s` (line_by_line=True)" % (foodemoji.decorate(text, line_by_line=False).encode("utf8"), foodemoji.decorate(text, line_by_line=True).encode("utf8"))
            e.args = (desc, )
            raise e

def test_linebyline_multiple_occurrences():
    pairs = [
        ('Hähnchenbrust Hähnchenbrust', 'Hähnchenbrust Hähnchenbrust :rooster:'),
        ('Hähnchenbrust Hähnchenbrust.', 'Hähnchenbrust Hähnchenbrust. :rooster:'),
        ('Hähnchenbrust Hähnchenbrust. ', 'Hähnchenbrust Hähnchenbrust. :rooster: '),
        ('Hähnchenbrust Hähnchenbrust .', 'Hähnchenbrust Hähnchenbrust :rooster: .'),
        ('Hähnchenbrust Hähnchenbrust.\n', 'Hähnchenbrust Hähnchenbrust. :rooster:\n'),
        ('Hähnchenbrust Hähnchenbrust.\r\n', 'Hähnchenbrust Hähnchenbrust. :rooster:\r\n'),
        ('Hähnchenbrust Hähnchenbrust Apfelrotkraut Apfelrotkraut', 'Hähnchenbrust Hähnchenbrust :rooster: Apfelrotkraut Apfelrotkraut :red_apple:'),
        ('Hähnchenbrust Hähnchenbrust\nApfelrotkraut Apfelrotkraut', 'Hähnchenbrust Hähnchenbrust :rooster:\nApfelrotkraut Apfelrotkraut :red_apple:'),
        ('Gegrillte Hähnchenbrust, gekochte Hähnchenbrust.\nApfelrotkraut Apfelrotkraut', 'Gegrillte Hähnchenbrust, gekochte Hähnchenbrust. :rooster:\nApfelrotkraut Apfelrotkraut :red_apple:'),
        ('Gegrillte Hähnchenbrust, gekochte Hähnchenbrust  Apfelrotkraut Apfelrotkraut', 'Gegrillte Hähnchenbrust, gekochte Hähnchenbrust :rooster:  Apfelrotkraut Apfelrotkraut :red_apple:'),
        ('Hähnchenbrust\nHähnchenbrust','Hähnchenbrust :rooster:\nHähnchenbrust :rooster:' )
    ]
    for text, text_with_emoji in pairs:
        text = text.decode("utf8") if PY2 else text
        text_with_emoji = text_with_emoji.decode("utf8") if PY2 else text_with_emoji
        try:
            assert text_with_emoji == foodemoji.decorate(text, line_by_line=True)
        except AssertionError as e:
            desc = "Error: Got `%s` expected `%s`" % (foodemoji.decorate(text, line_by_line=True).encode("utf8"), text_with_emoji.encode("utf8"))
            e.args = (desc, )
            raise e


def test_unicode():
    if not PY2:
        print("Skipping test_unicode on Python 3")
        return

    pairs = [
        ("Grießflammerie", "Grießflammerie"),
        (u"Grießflammerie", "Grießflammerie"),
        ("Kürbis", "Kürbis :jack-o-lantern:"),
        (u"Kürbis", u"Kürbis :jack-o-lantern:"),
        ("Curry-soße", "Curry-soße"),
        (u"Curry-soße", "Curry-soße"),
    ]

    # Without decoding. Expecting errors.
    for text, text_with_emoji in pairs:
        try:
            foodemoji.decorate(text)
        except TypeError as e:
            if isinstance(text, unicode):
                raise e
        except Exception as e:
            desc = "Error: Unexpected %r for %r" % (e, text)
            raise Exception(desc)
        else:
            if not isinstance(text, unicode):
                desc = "Error: Expected TypeError not raised for %r" % (text)
                raise Exception(desc)

    # With decoding. No errors expected.
    for text, text_with_emoji in pairs:
        text = text.decode("utf8") if PY2 and not isinstance(text, unicode) else text
        text_with_emoji = text_with_emoji.decode("utf8") if PY2 and not isinstance(text_with_emoji, unicode) else text_with_emoji
        try:
            assert text_with_emoji == foodemoji.decorate(text)
        except AssertionError as e:
            desc = "Error: `%s` should be `%s`" % (foodemoji.decorate(text).encode("utf8"), text_with_emoji.encode("utf8"))
            e.args = (desc, )
            raise e


def test_valid_emojis():
    import emoji

    foodemoji.decorate("ensure loaded") # ensure emojis are loaded
    assert len(foodemoji._emoji_re) > 0

    if PY2:
        # Python 2
        for x in foodemoji._emoji_re:
            try:
                assert len(x) > 3
            except AssertionError as e:
                desc = "Error: Invalid emoji name: `%s`" % x
                e.args = (desc, )
                raise e


            if not x.startswith(':flag_for_'):
                try:
                    assert len(emoji.emojize(x)) in (1, 2, 3)
                except AssertionError as e:
                    print("Error: Invalid emoji: `%s`" % x)
                    print("converted to `%s`" % emoji.emojize(x).encode("utf8"))
                    print("Length: %d" % len(emoji.emojize(x)))
                    e.args = ("Invalid emoji: `%s`" % x, )
                    raise e

            try:
                assert len(emoji.emojize(x, language='alias')) in (1, 2, 3, 4, 5)
            except AssertionError as e:
                print("Error: Invalid emoji: `%s`" % x)
                print("converted to `%s`" % emoji.emojize(x, language='alias').encode("utf8"))
                print("Length: %d" % len(emoji.emojize(x, language='alias')))
                e.args = ("Invalid emoji: `%s`" % x, )
                raise e

    else:
        # Python 3
        for x in foodemoji._emoji_re:
            try:
                assert len(x) > 3
            except AssertionError as e:
                desc = "Error: Invalid emoji name: `%s`" % x
                e.args = (desc, )
                raise e


            if not x.startswith(':flag_for_'):
                try:
                    assert len(emoji.emojize(x)) in (1,2)
                    assert ord(emoji.emojize(x)[0]) > 254
                except AssertionError as e:
                    print("Error: Invalid emoji: `%s`" % x)
                    print("converted to `%s`" % emoji.emojize(x).encode("utf8"))
                    print("Length: %d" % len(emoji.emojize(x)))
                    e.args = ("Invalid emoji: `%s`" % x, )
                    raise e

            try:
                assert len(emoji.emojize(x, language='alias')) in (1, 2)
            except AssertionError as e:
                print("Error: Invalid emoji: `%s`" % x)
                print("converted to `%s`" % emoji.emojize(x, language='alias').encode("utf8"))
                print("Length: %d" % len(emoji.emojize(x, language='alias')))
                e.args = ("Invalid emoji: `%s`" % x, )
                raise e


def test_book():
    import os
    import emoji
    try:
        filename = 'italienische-reise.txt'
        url = 'https://github.com/GITenberg/Italienische-Reise-Band-1_2404/raw/master/2404-8.txt'

        if not os.path.isfile(filename):
            if PY2:
                import urllib2
                furl = urllib2.urlopen(url)
                text = furl.read().decode('cp1252' ,errors='ignore')
                furl.close()
            else:
                import urllib.request
                with urllib.request.urlopen(url) as furl:
                    text = furl.read().decode('cp1252' ,errors='ignore')
            with open(filename, 'wb') as fout:
                fout.write(text.encode('utf-8'))
        else:
            with open(filename, 'rb') as fin:
                text = fin.read().decode('utf-8')
    except Exception as e:
        print("#### Skipping test_book(): ####")
        print("#### %s" % str(e))
        return

    text = emoji.emojize(foodemoji.decorate(text), language='alias')

    with open('italienische-reise_emoji.txt', 'wb') as fres:
        fres.write(text.encode('utf-16'))

def run_all():
    for fname, f in list(globals().items()):
        if fname.startswith('test_'):
            print("%s()" % fname)
            f()
            print("Ok.")




if __name__ == '__main__':
    if 'idlelib' in sys.modules:
        print("Please run this file in a console!")

    run_all()
