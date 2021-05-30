from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import re 
from collections import Counter

data_i = []
with open("friends_corpus.txt", 'r') as f: 
    for line in f: 
        line = line.strip() 
        label = ' '.join(line[1:line.find("]")].strip().split())
        text = line[line.find("]")+1:].strip()
        data_i.append([label, text])

def ngram(token, n): 
    output = []
    for i in range(n-1, len(token)): 
        ngram = ' '.join(token[i-n+1:i+1])
        output.append(ngram) 
    return output
def create_feature(text, nrange=(1, 1)):
    text_features = [] 
    text = text.lower()
    text_alphanum = re.sub('[^a-z0-9#]', ' ', text)
    for n in range(nrange[0], nrange[1]+1): 
        text_features += ngram(text_alphanum.split(), n)
    text_punc = re.sub('[a-z0-9]', ' ', text)
    text_features += ngram(text_punc.split(), 1)
    return Counter(text_features)
def convert_label(item, name): 
    items = list(map(float, item.split()))
    label = ""
    for idx in range(len(items)): 
        if items[idx] == 1: 
            label += name[idx] + " "
    
    return label.strip()
emotions = ["joy", 'fear', "anger", "sadness", "disgust", "shame", "guilt"]
X_all = []
y_all = []
for label, text in data_i:
    y_all.append(convert_label(label, emotions))
    X_all.append(create_feature(text, nrange=(1, 4)))
print("features example: ")
print(X_all[0])

X_train, X_test, y_train, y_test = \
    train_test_split(X_all, y_all, test_size = 0.2, random_state = 123)

vectorizer = DictVectorizer(sparse = True)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


parameters = {'C':[1, 2, 3, 5, 10, 15, 20, 30, 50, 70, 100], 
             'tol':[0.1, 0.01, 0.001, 0.0001, 0.00001]}
print("h1")
lsvc = LinearSVC(random_state=123,dual=False)
print("h2")
grid_obj = GridSearchCV(lsvc, param_grid = parameters, cv=5)
print("h3")
grid_obj.fit(X_train, y_train)

emoji_dict ={"joy":"a", "fear":"b", "anger":"c", "sadness":"d", "disgust":"e", "shame":"f", "guilt":"g","neutral":"h"}
def predict_emoji(text):
    features = create_feature(text)
    features = vectorizer.transform(features)
    prediction = grid_obj.predict(features)[0]
    return emoji_dict[prediction]







