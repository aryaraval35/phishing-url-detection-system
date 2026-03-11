import pandas as pd
from FeatureExtraction import getAttributess
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle

# load raw CSVs
leg = pd.read_csv("../extracted_csv_files/legitimate-urls.csv")
phi = pd.read_csv("../extracted_csv_files/phishing-urls.csv")

# augment
def augment(df,label):
    rows=[]
    for _,r in df.iterrows():
        url=r.get('Domain','')
        if not url.startswith('http'):
            url='http://'+url
        feats=getAttributess(url)
        feats['label']=label
        rows.append(feats)
    return pd.concat(rows,ignore_index=True)

print('augmenting legitimate...')
leg2=augment(leg,0)
print('augmenting phishing...')
phi2=augment(phi,1)
all_df=pd.concat([leg2,phi2],ignore_index=True)
print('dataset shape',all_df.shape)

# drop any leftover non-feature columns
for col in ['Domain','Path','Protocol']:
    if col in all_df.columns:
        all_df.drop(columns=[col],inplace=True)

X=all_df.drop('label',axis=1)
y=all_df['label']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=100)
clf=RandomForestClassifier()
clf.fit(X_train,y_train)
print('train acc',clf.score(X_train,y_train),'test acc',clf.score(X_test,y_test))
print('confusion',confusion_matrix(y_test,clf.predict(X_test)))
pickle.dump(clf, open('RandomForestModel.sav','wb'))
print('model saved to RandomForestModel.sav')
