from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
ps = PorterStemmer()
f = open('friends_corpus.txt')
a = sent_tokenize(f.read())
stop_words = list(stopwords.words('english'))
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
s = [(word_tokenize(a[i])) for i in range(len(a))]
outer_1 = []
for i in range(len(s)):
    inner_1 = []
    for j in range(len(s[i])):
        if s[i][j] not in (punc or stop_words):
            s[i][j] = ps.stem(s[i][j])
            if s[i][j] not in stop_words:
                inner_1.append(s[i][j].lower())
      
    outer_1.append(set(inner_1))
rvector = outer_1[0]
for i in range(1, len(s)):
    rvector = rvector.union(outer_1[i])
outer = []
for i in range(len(outer_1)):
    inner = []
    for w in rvector:
        if w in outer_1[i]:
            inner.append(1)
        else:
            inner.append(0)
    outer.append(inner)
def find(input_sent):
    check = (word_tokenize(input_sent))
    check = [ps.stem(check[i]).lower() for i in range(len(check))]
    check1 = []
    for w in rvector:
        if w in check:
            check1.append(1)
        else:
            check1.append(0)
    ds = []
    for j in range(len(outer)):
        similarity_index = 0
        c = 0
        if check1 == outer[j]:
            ds.append(0)
        else:
            for i in range(len(rvector)):
                c += check1[i]*outer[j][i]
            similarity_index += c
            ds.append(similarity_index)
    maximum = max(ds)
    cnt=0
    for i in range(len(ds)):
        if ds[i] == maximum:
            cnt+=1
            return a[i]
        

  
  
