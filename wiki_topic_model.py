# -*- coding: utf-8 -*-
"""
@author: Abhijeet Kumar
"""

import os
import random
import codecs
import cPickle
from gensim.models.ldamodel import LdaModel as Lda
from gensim import corpora
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer


# Function to remove stop words from sentences & lemmatize verbs. 
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    normalized = " ".join(lemma.lemmatize(word,'v') for word in stop_free.split())
    x = normalized.split()
    y = [s for s in x if len(s) > 2]
    return y


corpus_path = "articles-corpus/"
article_paths = [os.path.join(corpus_path,p) for p in os.listdir(corpus_path)]

# Read contents of all the articles in a list "doc_complete"
doc_complete = []
for path in article_paths:
    fp = codecs.open(path,'r','utf-8')
    doc_content = fp.read()
    doc_complete.append(doc_content)  

# Randomly sample 70000 articles from the corpus created from the 1st blog-post (wiki_parser.py)      
docs_all = random.sample(doc_complete, 70000)
docs = open("docs_wiki.pkl",'wb')
cPickle.dump(docs_all,docs)

# Use 60000 articles for training.
docs_train = docs_all[:60000]

# Cleaning all the 60,000 simplewiki articles
stop = set(stopwords.words('english'))
lemma = WordNetLemmatizer()
doc_clean = [clean(doc) for doc in docs_train]

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(doc_clean)

# Filter the terms which have occured in less than 3 articles and more than 40% of the articles 
dictionary.filter_extremes(no_below=4, no_above=0.4)

# List of some words which has to be removed from dictionary as they are content neutral words
stoplist = set('also use make people know many call include part find become like mean often different \
                usually take wikt come give well get since type list say change see refer actually iii \
                aisne kinds pas ask would way something need things want every str'.split())
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
dictionary.filter_tokens(stop_ids)

#words,ids = dictionary.filter_n_most_frequent(50)
#print words,"\n\n",ids

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]


#Creating the object for LDA model using gensim library & Training LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=50, id2word = dictionary, passes=50, iterations=500)
ldafile = open('lda_model_sym_wiki.pkl','wb')
cPickle.dump(ldamodel,ldafile)
ldafile.close()

#Print all the 50 topics
for topic in ldamodel.print_topics(num_topics=50, num_words=10):
    print topic[0]+1, " ", topic[1],"\n"





















           
                       
                       
                       
