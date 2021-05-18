>>> from cltk import NLP
>>> vitruvius = "Architecti est scientia pluribus disciplinis et variis eruditionibus ornata, quae ab ceteris artibus perficiuntur. Opera ea nascitur et fabrica et ratiocinatione."
>>> cltk_nlp = NLP(language="lat")
‎𐤀 CLTK version 'cltk 1.0.0b10'.
Pipeline for language 'Latin' (ISO: 'lat'): `LatinNormalizeProcess`, `LatinStanzaProcess`, `LatinEmbeddingsProcess`, `StopsProcess`, `LatinNERProcess`, `LatinLexiconProcess`.
>>> cltk_doc = cltk_nlp.analyze(text=vitruvius)