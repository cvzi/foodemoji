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
    assert distutils.version.StrictVersion(emoji.__version__) >= distutils.version.StrictVersion('0.5.0')
except AssertionError as e:
    print("Module/Package `emoji` is version %s, it needs to be at least version 0.5.0" % emoji.__version__)
    e.args = ("emoji module version < 0.5.0", )
    raise e

PY2 = sys.version_info.major is 2

def test_basic():
    pairs = [
        ("Fish & chips", "Fish :fish: & chips :french_fries:"), # circular
        ("Tintenfisch", "Tintenfisch :squid:"), # no fish
        ("Haifisch", "Haifisch :fish:"),
        ("Grießflammerie", "Grießflammerie"), # lamm
        
    ]
    for text, text_with_emoji in pairs:
        try:
            assert text_with_emoji == foodemoji.decorate(text, line_by_line=True)
        except AssertionError as e:
            desc = "Error: `%s` != `%s`" % (foodemoji.decorate(text, line_by_line=True), text_with_emoji)
            e.args = (desc, )
            raise e

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