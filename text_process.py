from collections import Counter, defaultdict
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import fileinput

TEST_PATHS = ["./test_docs/doc%d.txt" % (i) for i in range(1,7)]


class TextProcessor:
    def __init__(self, language='english', exclude=[]):
        self.stop_words = set(stopwords.words(language)) | set(exclude)

    def get_token_set(self, doc):
        return set(self.preprocess_string(doc))

    def preprocess_string(self, s):
        tokens = word_tokenize(s)
        lower_tokens = [t.lower() for t in tokens if t.lower() not in self.stop_words and t.isalpha()]
        return lower_tokens


class Corpus:
    def __init__(self, docs=[], paths=None, language='english', exclude=[]):
        tp = TextProcessor(language=language)
        self.docs = [docs] if type(docs) == "string" else docs

        if paths: 
            for path in paths:
                with fileinput.input(files=path) as f:
                    doc = ""
                    for line in f:
                        doc += line
                    self.docs.append(doc)

        self.sentences = [sent_tokenize(doc) for doc in self.docs]
        
        self.counts = Counter()
        for doc in self.docs:
            tokens = tp.preprocess_string(doc)
            self.counts.update(tokens)

        self.sentence_locations = defaultdict(list)

        for i, doc in enumerate(self.sentences):
            j = 0
            for sent in doc:
                tokens = tp.get_token_set(sent)
                for token in tokens:
                    self.sentence_locations[token].append((i,j,))
                j += 1

    def word_data(self, word, n_sentences=5):
        sentence_locations = self.sentence_locations[word]

        docs = set()
        sentences = []
        for s in sentence_locations[:n_sentences]:
            docs.add(s[0] + 1)
            sentences.append(self.sentences[s[0]][s[1]])

        return {
            "word": word,
            "docs": sorted(docs),
            "sentences": sentences
        }

    def word_list_data(self, word_list):
        data = []
        for word in word_list:
            data.append(self.word_data(word))
        return data

    def most_common_words(self, n=5, range=None, print_result=False):
        if range:
            word_list = set(self.counts.most_common(0, range[1])) - set(self.counts.most_common(0, range[0]))
        else:
            word_list = self.counts.most_common(n)

        data = self.word_list_data([word[0] for word in word_list])

        if print_result:
            for i, x in enumerate(data):
                print("Word %d:" % (i+1), x["word"], "in documents", ", ".join(str(d) for d in x["docs"]))
                for sentence in x["sentences"]:
                    print('\t', sentence)
                print("*" * 40)
        return data



