from collections import defaultdict
import numpy as np





class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):
        """Return a dictionary of words and the words that follow them."""
        words = self.corpus.split()

        term_dict = defaultdict(list)

        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]

            term_dict[current_word].append(next_word)

        term_dict[words[-1]]
        self.term_dict = dict(term_dict)

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):
        """Return randomly generated text based on the corpus transitions."""
        if self.term_dict is None:
            self.get_term_dict()

        if seed_term is None:
            current_word = np.random.choice(list(self.term_dict.keys()))
        else:
            if seed_term not in self.term_dict:
                raise ValueError("Seed term is not in the corpus.")
            current_word = seed_term

        generated_words = [current_word]

        for _ in range(term_count - 1):
            possible_words = self.term_dict.get(current_word)

            if not possible_words:
                current_word = np.random.choice(list(self.term_dict.keys()))
            else:
                current_word = np.random.choice(possible_words)

            generated_words.append(current_word)

        return " ".join(generated_words)