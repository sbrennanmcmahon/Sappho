// Transcrypt'ed from Python, 2021-05-20 22:11:34
var re = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
import {chain} from './itertools.js';
var __name__ = '__main__';
export var LEXICON_FILE = 'wordlist.csv';
export var get_fragment = function () {
	var fragment = document.getElementById ('fragment').value;
	return fragment;
};
export var match_word = function (word, fragment) {
	return re.fullmatch (fragment, word);
};
export var success = function (result) {
	document.getElementById ('idPlace').innerHTML = 'Got words, searching...';
	var words = get_words (result);
	var combined = '<p>Results:</p>';
	for (var w of words) {
		var combined = combined + '<p>{}</p>'.format (w);
	}
	document.getElementById ('idPlace').innerHTML = combined;
};
export var fail = function (a, b, c) {
	document.getElementById ('idPlace').innerHTML = 'failed!';
};
export var load_wordlist = function () {
	$.ajax (dict ([['url', 'wordlist.csv'], ['type', 'GET'], ['datatype', 'text'], ['success', success], ['fail', fail]]));
};
export var get_words = function (wordlist) {
	var words = wordlist.py_split ('\n');
	var fragment = get_fragment ();
	var list_of_words = [];
	for (var word of words) {
		var word = word.strip ('\n');
		if (match_word (word, fragment)) {
			list_of_words.append (word);
		}
	}
	return list_of_words;
};
export var Thing = function () {
	var response = get_words ();
	document.getElementById ('idPlace').innerHTML = response;
};
export var DoThing = function () {
	document.getElementById ('idPlace').innerHTML = 'working...';
	load_wordlist ();
};

//# sourceMappingURL=hello.map