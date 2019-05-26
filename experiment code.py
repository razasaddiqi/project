import nltk
from nltk.tokenize import word_tokenize
word=input("Enter String")
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
psw=[]
for i in filtered_sentence:
    
    psw.append(ps.stem(i))
print(psw)    
print("..............")
print("Lemmatization")
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
for t in filtered_sentence:
    lemmas=lemmatizer.lemmatize(t)
    print(lemmas)

    

