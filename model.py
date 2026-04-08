import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    df = pd.read_csv("data/weatherAUS.csv")

    cols = ['MinTemp', 'MaxTemp', 'Humidity9am', 'Humidity3pm',
            'Pressure9am', 'Pressure3pm', 'WindSpeed9am', 'WindSpeed3pm']

    for col in cols:
        df[col] = df[col].fillna(df[col].mean())

    df['RainToday'] = df['RainToday'].fillna('No')
    df['RainTomorrow'] = df['RainTomorrow'].fillna('No')

    df['RainToday'] = df['RainToday'].map({'Yes': 1, 'No': 0})
    df['RainTomorrow'] = df['RainTomorrow'].map({'Yes': 1, 'No': 0})

    X = df[cols]
    y = df['RainTomorrow']

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    return model