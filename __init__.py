import json
import re


def _load():
    global emoji_re
    global wordend
    
    wordend = re.compile("(,|\(|\[|\s|\b|$)", flags=re.MULTILINE)
    
    # Load json file
    with open("foodemojis.json", "rb") as fs:
        emoji_list = json.load(fs)
    
    # Pre compile regular expressions
    emoji_re = {}
    for emo in emoji_list:
        emoji_re[emo] = []
        for q in emoji_list[emo]:
            emoji_re[emo].append(re.compile(q,flags=re.MULTILINE|re.IGNORECASE))


def decorate(text):
    """
    Decorates the text with food-specific emojis
    """
    global emoji_re
    global wordend
    
    
    for emo in emoji_re:
        for regex in emoji_re[emo]:
            cursor = 0
            m = regex.search(text, pos=cursor)
            while m:
                # find next space:
                lastchar = m.group(0)[-1]
                if len(lastchar.strip()) == 0: # last char in pattern is white space
                    space = m.end()-1
                else:  # find next whitespace or end of line
                    space = wordend.search(text, pos=m.end()).start()
                
                # put emoji in the whitespace
                text = text[:space] + ' '+ emo + text[space:]
                
                cursor = space + len(emo) + 1
                
                m = regex.search(text, pos=cursor)
    
    return text



_load()



if __name__ == "__main__":
    text = """Hähnchenbrust mit Apfelrotkraut
Vegetarische Maultaschen
Kartoffelknödel
Paniertes Schnitzel mit Pommes frites
Rinderbraten, Rotweinsauce und Spätzle"""
    print(decorate(text))

