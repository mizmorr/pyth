#!/usr/bin/python
from natasha import (Segmenter, NewsEmbedding,NewsMorphTagger,NewsSyntaxParser,Doc)
segm=Segmenter()
emb=NewsEmbedding()
m_tagger=NewsMorphTagger(emb)
s_parser=NewsSyntaxParser(emb)
text="Существуют разные методы для чтения данных из открытого ранее файла"
doc=Doc(text)
doc.segment(segm)
doc.tag_morph(m_tagger)
doc.parse_syntax(s_parser)
print(doc.tokens[:10])
doc.sents[0].syntax.print()