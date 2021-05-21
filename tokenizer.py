# coding=utf8
athenaeus_incipit = "Ἀθήναιος μὲν ὁ τῆς βίβλου πατήρ· ποιεῖται δὲ τὸν λόγον πρὸς Τιμοκράτην· Δειπνοσοφιστὴς δὲ ταύτῃ τὸ ὄνομα. Ὑπόκειται δὲ τῷ λόγῳ Λαρήνσιος Ῥωμαῖος, ἀνὴρ τῇ τύχῃ περιφανής, τοὺς κατὰ πᾶσαν παιδείαν ἐμπειροτάτους ἐν αὑτοῦ δαιτυμόνας ποιούμενος· ἐν οἷς οὐκ ἔσθ᾽ οὗτινος τῶν καλλίστων οὐκ ἐμνημόνευσεν. Ἰχθῦς τε γὰρ τῇ βίβλῳ ἐνέθετο καὶ τὰς τούτων χρείας καὶ τὰς τῶν ὀνομάτων ἀναπτύξεις καὶ λαχάνων γένη παντοῖα καὶ ζῴων παντοδαπῶν καὶ ἄνδρας ἱστορίας συγγεγραφότας καὶ ποιητὰς καὶ φιλοσόφους καὶ ὄργανα μουσικὰ καὶ σκωμμάτων εἴδη μυρία καὶ ἐκπωμάτων διαφορὰς καὶ πλούτους βασιλέων διηγήσατο καὶ νηῶν μεγέθη καὶ ὅσα ἄλλα οὐδ᾽ ἂν εὐχερῶς ἀπομνημονεύσαιμι, ἢ ἐπιλίποι μ᾽ ἂν ἡ ἡμέρα κατ᾽ εἶδος διεξερχόμενον. Καί ἐστιν ἡ τοῦ λόγου οἰκονομία μίμημα τῆς τοῦ δείπνου πολυτελείας καὶ ἡ τῆς βίβλου διασκευὴ τῆς ἐν τῷ δείπνῳ παρασκευῆς. Τοιοῦτον ὁ θαυμαστὸς οὗτος τοῦ λόγου οἰκονόμος Ἀθήναιος ἥδιστον λογόδειπνον εἰσηγεῖται κρείττων τε αὐτὸς ἑαυτοῦ γινόμενος, ὥσπερ οἱ Ἀθήνησι ῥήτορες, ὑπὸ τῆς ἐν τῷ λέγειν θερμότητος πρὸς τὰ ἑπόμενα τῆς βίβλου βαθμηδὸν ὑπεράλλεται."

from cltk.corpus.utils.importer import CorpusImporter
corpus_importer = CorpusImporter('greek')
corpus_importer.import_corpus('greek_models_cltk')

from cltk.tokenize.word import WordTokenizer
word_tokenizer = WordTokenizer('greek')
athenaeus_word_tokens = word_tokenizer.tokenize(athenaeus_incipit.lower())
athenaeus_word_tokens = [token for token in athenaeus_word_tokens if token not in ['.', ',', ':', ';']]

from cltk.stem.lemma import LemmaReplacer
lemmatizer = LemmaReplacer('greek')
lemmata = lemmatizer.lemmatize(athenaeus_word_tokens)

print(lemmata)
# lemmata_orig = lemmatizer.lemmatize(athenaeus_word_tokens, return_raw=True)
# print(lemmata_orig)