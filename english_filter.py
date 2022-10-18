import pandas as pd
from spacy_langdetect import LanguageDetector
import spacy

df = pd.read_csv('dev_dataset.csv')

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)

def english_filter(df):
    df['language'] = df['text'].apply(lambda x: nlp(x)._.language)
    df = df[df['language'] == 'en']
    df = df.drop(columns=['language'])
    return df

df = english_filter(df)
print(df.head())
