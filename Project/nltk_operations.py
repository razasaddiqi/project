import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as st
from nltk.stem import WordNetLemmatizer
def tokenize(text):
    tokens=word_tokenize(text)
    return tokens
def stop(tokens):
    stopwords=set(st.words("english"))
    filtered_sentence=[]
    for w in tokens:
        if w not in stopwords:
            filtered_sentence.append(w)
    return filtered_sentence
def stemming(filtered_sentence):
    ps=PorterStemmer()
    stem=[]
    for i in filtered_sentence:
        psw=ps.stem(i)
        stem.append(psw)
    return '\n'.join(stem)
##print("..............")
##print("####part of spech tagging####")
def chunking(filtered_sentence):
    tagged=nltk.pos_tag(filtered_sentence)
    ##print(tagged)
    ##print("..............")
    ##print("#### chunking####")
    chunkgrammer=r"""chunk:{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    ChunkParser=nltk.RegexpParser(chunkgrammer)
    chunked=ChunkParser.parse(tagged)
    chunked.draw()
def lematize(filtered_sentence):
    lemmatizer = WordNetLemmatizer()
    lemm=[]
    for t in filtered_sentence:
        lemmas = lemmatizer.lemmatize(t)
        lemm.append(lemmas)
    return lemm



