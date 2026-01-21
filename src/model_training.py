from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def train_model(df):

    X = df.drop('status', axis=1)
    y = df['status'] 

    # enncode cate variable

    for col in X.select_dtype(include=  'object').columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])


    X_train, X_test, y_train, y_test = train_test_split(X,  y , test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100,random_state=42)

    model.fit(X_train, y_train)
    
    return model,X_test,y_test

