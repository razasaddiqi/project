import nltk
from nltk.tokenize import word_tokenize
word=input("enter string")
tokens=word_tokenize(word)
print(tokens)
print("................")
print("####### stopword removal####")
from nltk.corpus import stopwords
stopwords=set(stopwords.words("english"))
filtered_sentence=[]
for w in tokens:
    if w not in stopwords:
        filtered_sentence.append(w)

print(filtered_sentence)
print(".................")
print("stemming")
from nltk.stem import PorterStemmer
ps=PorterStemmer()
for i in filtered_sentence:
    psw=ps.stem(i)
    print(psw)
print("..............")
print("####part of spech tagging####")
tagged=nltk.pos_tag(filtered_sentence)
print(tagged)
print("..............")
print("#### chunking####")
chunkgrammer=r"""chunk:{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
ChunkParser=nltk.RegexpParser(chunkgrammer)
chunked=ChunkParser.parse(tagged)
chunked.draw()

    


