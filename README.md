# Topic-Modelling-on-Wiki-corpus
It uses Latent Dirichlet Allocation algorithm to discover hidden topics from the articles. It is trained on 40,000 articles taken from simple wikipedia english corpus. Finally, It extracts the topic of the given input text article. 

The whole application of topic modelling is performed in 3 steps. The purpose is to build the system from scratch and provide an insight of implementation of the same to viewers.

The 3 steps are:
1. Creating an article corpus of 70.000 - 80,000 articles from the simple wiki XML dump file. (done by wiki_parser.py)
2. Automatically discovering hidden topics from the training articles (50,000 training articles)
3. Extract topic from any articles based on topic discovered in Step 2.

Best thing would be to follow series of blog-post for the same. The description about the steps to perform "Topic Modelling" from scratch can be read from my blog:

https://appliedmachinelearning.wordpress.com/2017/08/28/topic-modelling-part-1-creating-article-corpus-from-simple-wikipedia-dump/

Stay tuned for rest of the blog-posts in "Topic Modelling Series".

