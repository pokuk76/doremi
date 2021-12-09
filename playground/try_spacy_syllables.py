import spacy
from spacy_syllables import SpacySyllables

nlp  = spacy.load('en_core_web_trf')
syllables = SpacySyllables(nlp)
nlp.add_pipe('syllables', after='tagger')

doc = nlp('terribly long')

data = [
    (token.text, token._.syllables, token._.syllables_count)
    for token in doc
]

print(data)

assert data == [
    ('terribly', ['ter', 'ri', 'bly'], 3),
    ('long', ['long'], 1)
]