import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    doc = nlp(sentences)
    print(doc)

sentences = 'John ate an apple Oh John'
anonympipize_text(sentences)