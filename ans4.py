import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

def clean_and_preprocess(df):
    
    df.fillna(df.mean(), inplace=True)  
    
   
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    
    return df


data = {
    'A': [1, 2, 3, 4, 5, None],
    'B': [10, 20, 30, 40, 50, 60],
    'C': ['cat1', 'cat2', 'cat1', 'cat3', 'cat2', 'cat1'],
    'D': [True, False, True, False, True, False]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_clean = clean_and_preprocess(df)

print("\nCleaned and Preprocessed DataFrame:")
print(df_clean)