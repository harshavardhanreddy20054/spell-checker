import re
import nltk
from collections import Counter, defaultdict
from nltk.util import bigrams, trigrams
from nltk.corpus import words, reuters, brown

# Download required datasets
#nltk.download('punkt')
#nltk.download('words')
#nltk.download('reuters')
#nltk.download('brown')

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return nltk.word_tokenize(text)

# Prepare vocabulary and frequency
corpus_text = ' '.join(brown.words())
tokens = preprocess(corpus_text)
vocab = set(words.words())
word_freq = Counter(tokens)

def train_trigram_model(tokens):
    bigram_counts = Counter(bigrams(tokens))
    trigram_counts = Counter(trigrams(tokens))
    model = defaultdict(lambda: defaultdict(lambda: 0))
    for (w1, w2, w3), count in trigram_counts.items():
        model[(w1, w2)][w3] = count / bigram_counts[(w1, w2)]
    return model

def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    inserts = [L + c + R for L, R in splits for c in letters]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    return set(deletes + inserts + replaces + transposes)



def known(words_set):
    return set(w for w in words_set if w in vocab)

trigram_model = train_trigram_model(tokens)

def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def correct_word(word):
    if word in vocab:
        return word
    candidates = known(edits1(word)) or known(edits2(word)) or {word}
    return max(candidates, key=lambda w: word_freq[w])


def correct_word_trigram(w1, w2, word):
    if word in vocab:
        return word
    candidates = known(edits1(word)) or {word}
    scored = []
    for cand in candidates:
        trigram_prob = trigram_model[(w1, w2)].get(cand, 1e-6)
        total_score = trigram_prob * (word_freq[cand] + 1)
        scored.append((total_score, cand))
    return max(scored)[1]

common_typos = {
    "hw": "how",
    "r": "are",
    "yu": "you",
    "tody": "today",
    "teh": "the",
    "hve": "have",
    "dreem": "dream",
    "studnt": "student",
    "succed": "succeed",
    "exmple": "example",
    "splel": "spell",
    "chcker": "checker",
    "borwn": "brown",
    "jmps": "jumps",
    "lzay": "lazy",
    "oevr": "over"
}


def correct_sentence_trigram(sentence):
    words = sentence.split()
    corrected = []
    for i, word in enumerate(words):
        w = word.lower()
        if w in common_typos:
            corrected.append(common_typos[w])
        else:
            w1 = corrected[i-2] if i >= 2 else ''
            w2 = corrected[i-1] if i >= 1 else ''
            corrected.append(correct_word_trigram(w1, w2, w))
    return ' '.join(corrected)


