# -*- coding: utf-8 -*-
# https://github.com/cvzi/foodemoji
import sys
import distutils.version

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
    assert distutils.version.StrictVersion(emoji.__version__) >= distutils.version.StrictVersion('0.5.4')
except AssertionError as e:
    print("Module/Package `emoji` is version %s, it needs to be at least version 0.5.4" % emoji.__version__)
    e.args = ("emoji module version < 0.5.4", )
    raise e

PY2 = sys.version_info.major == 2

def test_basic():
    pairs = [
        ("Fish & chips", "Fish :fish: & chips :french_fries:"), # circular
        ("Tintenfisch", "Tintenfisch :squid:"), # no fish
        ("Haifisch", "Haifisch :fish:"),
        ("Grießflammerie", "Grießflammerie"), # lamm
        ("nordamerikanisch", "nordamerikanisch :flag_for_United_States:"),
        ("südamerikanisch", "südamerikanisch"),
        ("Süßer Reis", "Süßer Reis :cooked_rice:"),
        ("Reis", "Reis :cooked_rice:"),
        ("Greis", "Greis"),
        (u"Kürbis", u"Kürbis :jack-o-lantern:"),
        ("Reis\nPommes frites", "Reis :cooked_rice:\nPommes frites :french_fries:"),
    ]
    for text, text_with_emoji in pairs:
        text = text.decode("utf8") if PY2 and not isinstance(text, unicode) else text
        text_with_emoji = text_with_emoji.decode("utf8") if PY2 and not isinstance(text_with_emoji, unicode) else text_with_emoji
        try:
            assert text_with_emoji == foodemoji.decorate(text, line_by_line=True)
        except AssertionError as e:
            desc = "Error: Got `%s` expected `%s`" % (foodemoji.decorate(text, line_by_line=True), text_with_emoji)
            e.args = (desc, )
            raise e


if __name__ == '__main__':
    if 'idlelib' in sys.modules:
        print("Please run this file in a console!")

    test_basic()
    print("Ok.")