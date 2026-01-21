from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

def evaluate_model(model,X_test,y_test):
    

    preds = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test,preds))
    print("\n classification report:",classification_report(y_test,preds) )
    print("\n confusion_matrix:", confusion_matrix(y_test,preds))

    
