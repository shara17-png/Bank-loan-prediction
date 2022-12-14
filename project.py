# -*- coding: utf-8 -*-
"""project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w3bbjykLFKUNdt1B0YJinWvEmWg-apeP

### **Predicting Approval for Bank Loan**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('bank_loan.csv')
df

df.info()

df.head(5)

df.tail(3)

df.sample(2)

df.columns

df.shape

df.describe()

df['Loan_Status'].value_counts()

df['Property_Area'].value_counts()

df['Education'].value_counts()

df.isnull().sum()

"""categorical values converted into numerical form"""

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
v=df.columns
for i in v:
  df[i]=le.fit_transform(df[i])

df

"""gender: male-1,female-0

married: no-0,yes-1

education:NOT GRADUATE-1,graduate-0

self employed:0-no,1-yes

loan status:0-no,1-yes

property area:0-rural,1-semiurban,2-urban
"""

df['Dependents']=df['Dependents'].fillna(df['Dependents'].median())
df['Gender']=df['Gender'].fillna(df['Gender'].median())
df['Married']=df['Married'].fillna(df['Married'].median())
df['Self_Employed']=df['Self_Employed'].fillna(df['Self_Employed'].median())
df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term']=df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
df['Credit_History']=df['Credit_History'].fillna(df['Credit_History'].median())

"""data visualization"""

df['ApplicantIncome'].hist()

plt.title('histogram')
plt.xlabel('ApplicantIncome')
plt.ylabel('Credit_History ')
plt.hist(df['Loan_Status'])
plt.show()

df.boxplot(column='ApplicantIncome')

sns.barplot(x='Credit_History',y='Loan_Status',data=df)

sns.countplot(x='Loan_Status',data=df)

df['LoanAmount'].hist(bins=50)

df.boxplot(column='ApplicantIncome',by='Education')

sns.boxplot(x='Loan_Status',y='Gender',data=df)

sns.boxplot(x='Loan_Status',y='LoanAmount',data=df)

sns.violinplot(x='Loan_Status',y='Gender',data=df)

x=df.drop(['Loan_Status','Loan_ID'],axis=1)
y=df['Loan_Status']

x

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

x_train

y_train

x_test

y_test

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

x_train

x_test

"""Logistic regression"""

from sklearn.linear_model import LogisticRegression
my_model=LogisticRegression()
result=my_model.fit(x_train,y_train)

predictions=result.predict(x_test)
predictions

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print('accuracy_score:',accuracy_score(y_test,predictions))
print('confusion_matrix:\n',confusion_matrix(y_test,predictions))
print('classification_report:\n',classification_report(y_test,predictions))

pred_new=my_model.predict([[1,0,0,0,0,376,0,203,8,1,2]])
pred_new

"""Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
my_model=DecisionTreeClassifier(random_state=1)
result=my_model.fit(x_train,y_train)

predictions=result.predict(x_test)
predictions

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print('accuracy_score:',accuracy_score(y_test,predictions))
print('confusion_matrix:\n',confusion_matrix(y_test,predictions))
print('classification_report:\n',classification_report(y_test,predictions))

pred_new=my_model.predict([[1,0,0,0,0,376,0,81,8,1,2]])
pred_new

"""Random Forest"""

from sklearn.ensemble import RandomForestClassifier
my_model=RandomForestClassifier(n_estimators=50,criterion='entropy',random_state=1)
result=my_model.fit(x_train,y_train)

predictions=result.predict(x_test)
predictions

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print('accuracy_score:',accuracy_score(y_test,predictions))
print('confusion_matrix:\n',confusion_matrix(y_test,predictions))
print('classification_report:\n',classification_report(y_test,predictions))

pred_new=my_model.predict([[1,0,0,0,0,376,0,81,8,1,2]])
pred_new

"""KNN"""

from sklearn.neighbors import KNeighborsClassifier
my_model=KNeighborsClassifier(n_neighbors=5)
result=my_model.fit(x_train,y_train)

predictions=result.predict(x_test)
predictions

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print('accuracy_score:',accuracy_score(y_test,predictions))
print('confusion_matrix:\n',confusion_matrix(y_test,predictions))
print('classification_report:\n',classification_report(y_test,predictions))

pred_new=my_model.predict([[1,0,0,0,0,376,0,81,8,1,2]])
pred_new

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,predictions)
sns.heatmap(cm,annot=True,fmt='2.0f')

"""SVM"""

from sklearn.svm import SVC
my_model=SVC(kernel='rbf',random_state=1)
result=my_model.fit(x_train,y_train)

predictions=result.predict(x_test)
predictions

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print('accuracy_score:',accuracy_score(y_test,predictions))
print('confusion_matrix:\n',confusion_matrix(y_test,predictions))
print('classification_report:\n',classification_report(y_test,predictions))

pred_new=my_model.predict([[1,0,0,0,0,376,0,81,8,1,2]])
pred_new

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,predictions)
sns.heatmap(cm,annot=True,fmt='2.0f')

"""the model with highest accuracy is:- logistic regression """

