from __future__ import annotations
from typeguard import typechecked
from typing import Iterable, List, Optional, Tuple, FrozenSet
from functools import lru_cache

import spacy
from spacy.lang.en import English
import spacy.lang.en

# import scipy.spatial.distance as sd

_nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

@lru_cache(maxsize = 1000000, typed=True)
def ngrams(text: str, n: int = 2) -> FrozenSet[Tuple[str, ...]]:
    doc = _nlp(text)
    lemmas = [t.lemma_ for t in doc if not t.is_space and not t.is_punct and not t.is_stop]
    ngrams = [
        tuple(lemmas[j] for j in range(i, i + n))
        for i in range(len(lemmas) - n + 1)
    ]
    return frozenset(ngrams)


@lru_cache(maxsize = 1000000, typed=True)
def jaccard_dist(fs1: FrozenSet[Tuple[str, ...]], fs2: FrozenSet[Tuple[str, ...]]) -> float:
    if fs1 == fs2:
        return 0.0

    ul = len(fs1.union(fs2))
    if ul == 0:
        return 0.0

    return len(fs1.symmetric_difference(fs2)) / ul

@lru_cache(maxsize = 100000, typed=True)
def ddist(s1: str, s2: str) -> float:
    if s1 == s2:
        return 0.0
    ng1 = ngrams(s1)
    ng2 = ngrams(s2)
    dist =jaccard_dist(ng1, ng2)
    return dist

if __name__ == '__main__':
    text = """When learning data science, you shouldn't get discouraged!
    Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""

    if False:
        nlp = English()
        # spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
        # nlp = spacy.load("en_core_web_sm")

        # print(help(nlp.pipe))

        # pipe = nlp.pipe(disable=["tagger", 'parser'])
        # enable=['sentencizer']
        # pipe.add_pipe(nlp.create_pipe('sentencizer'))

        # nlp.add_pipe(nlp.create_pipe('sentencizer'))
        doc = nlp(text, disable=['parser', 'ner'])
        """
        sents_list = []
        for sent in doc.sents:
            sents_list.append(sent.text)
        print(sents_list)
        """

        filtered_doc = []
        for word in doc:
            if word.is_space == False and word.is_punct == False and word.is_stop == False:
                filtered_doc.append(word.lemma_)
        print("Filtered Doc:", filtered_doc)

    if False:
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        doc = nlp(text)
        lemmas = [t.lemma_ for t in doc if not t.is_space and not t.is_punct and not t.is_stop]
        print('With tagger: ', lemmas)  # Lemma's are lowercase
