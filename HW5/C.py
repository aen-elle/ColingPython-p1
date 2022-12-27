import pymorphy2, random, pickle



class PhraseGenerator():

    def train_and_save(self):

        nouns = []
        adjectives = []
        morph = pymorphy2.MorphAnalyzer()

        with open('rus_shuffled.txt', 'r', encoding='utf-8') as f:
            for line in f:
                read = line.strip()
                parsed = morph.parse(read)[0]
                if parsed.tag.POS == 'NOUN':
                    nouns.append(parsed.normal_form)
                elif parsed.tag.POS == 'ADJF':
                    adjectives.append(parsed.normal_form)

        with open('model.pickle', 'wb') as handle:
            pickle.dump([nouns, adjectives], handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):

        with open('model.pickle', 'rb') as handle:
            words = pickle.load(handle)
            return words

    def generate(self):

        words = self.load()
        nouns = words[0]
        adjectives = words[1]
        morph = pymorphy2.MorphAnalyzer()

        my_noun = random.choice(nouns)
        my_noun_parsed = morph.parse(my_noun)[0]
        gender = my_noun_parsed.tag.gender

        my_adj = random.choice(adjectives)
        my_adj_parsed = morph.parse(my_adj)[0]
        infl = my_adj_parsed.inflect({gender}).word

        print(f'{infl} {my_noun}')


obj = PhraseGenerator()
obj.generate()
        



