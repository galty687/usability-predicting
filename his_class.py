import nltk,re
from nltk import word_tokenize

class his_calculator():
    def __init__(self,textFile):
# define a list of neuter pronouns
        self.neuter_pronouns=["its","they","them","it"]
# read the content from textFile
        self.content=textFile.read()
# the counter of the PRP words
        self.prp_number=0
# the patter of personal senteces, which is indicated by the puncutations marks.
        self.ps_sents=re.compile(r'["?!]')

# the function to get non-neuter pronouns:
    def count_non_neuter_words(self):
# Use nltk module to tokenize all the context from text file
        tokenized_content = word_tokenize(self.content)
# Tagging POS of each word
        posed_content=nltk.pos_tag(tokenized_content)
# If the word POS equals "PRP" and the word is not in the list of neuter pronous, the counter will add 1 to itself.
        for word in posed_content:
            if word[1]=="PRP" and word[0] not in self.neuter_pronouns:
                self.prp_number+=1
        return self.prp_number

# Count all the personal sentences
    def count_ps_sents(self):
# Use personal sentence pattern to find all the ps sentences in the file content
        ps_sents_number=self.ps_sents.findall(self.content)
        return len(ps_sents_number)

    def count_total_sents(self):
# NLTK tokinizer can tokenize all the content to a list of sentences.
        tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
        sents = tokenizer.tokenize(self.content)
        total_sents_number=len(sents)
        return total_sents_number

    def get_ps_ratio(self):
        ratio= self.count_ps_sents() / self.count_total_sents()
        return round(ratio*100,0)
