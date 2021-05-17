#src/train.py

import os 

import config 

import jotlib
import pandas as pd
from sklearn import metrics
from sklearn import tree

def run(fold):
    train = pd.read_csv("train.csv")
    test = pd.read_csv("test.csv")
    
    df = zip(train, test)
    
    df_train = df[df.kfold  != fold].reset_index(drop=True)
    df_test = df[df.kfold == fold].reset_index(drop=True)
    
    x_train = df_train.drop("TARGET", axis = 1).values
    y_train = df_train.TARGET.values
    
    # similarly, for test data, we have 
    x_test = df_test.drop("TARGET", axis = 1).values
    y_test = df_test.TARGET.values
    
    # initialize simple decision tree classifier from sklearn 
    clf = tree.DecisionTreeClassifier()
    
    # fit the model on training data 
    clf.fit(x_train, y_train)
    
    # create predictions for test samples
    preds = clf.predict(x_test)
    
    #calculate and print accuracy 
    accuracy = metrics.accuracy_score(y_test, preds)
    print(f"Fold ={fold}, Accurcy = {accuracy}")
    
    # save the model 
    joblib.dump(
        clf, 
        os.path.join(config.MODEL_OUTPUT, f"dt_{fold}.bin")
    )
    
    if __name__ == "__main__":
        run(fold = 0)
    
    
    
    