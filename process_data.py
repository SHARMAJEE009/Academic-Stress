import pandas as pd
import numpy as np
import json
import re
from collections import Counter

# Load the dataset
df = pd.read_excel('academic_stress_database_2005_2010.xlsx')
df['Parsed_Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Year'] = df['Parsed_Date'].dt.year
df['Month'] = df['Parsed_Date'].dt.month
df['Month_Name'] = df['Parsed_Date'].dt.strftime('%B')
df['Season'] = df['Month_Name'].map({
    'March': 'Board Exam Season (March)',
    'May': 'Result & Cut-off Cycle (May)',
    'June': 'Admissions & Intake (June)',
    'December': 'Pre-Board & Prep (December)'
})

print(f"Loaded {len(df)} records.")

# Vocabulary extraction from Title and Context & Findings Summary
stopwords = set([
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren\'t', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can\'t', 'cannot', 'could',
    'couldn\'t', 'did', 'didn\'t', 'do', 'does', 'doesn\'t', 'doing', 'don\'t', 'down', 'during', 'each', 'few', 'for',
    'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t', 'have', 'haven\'t', 'having', 'he', 'he\'d', 'he\'ll', 'he\'s',
    'her', 'here', 'here\'s', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'how\'s', 'i', 'i\'d', 'i\'ll', 'i\'m',
    'i\'ve', 'if', 'in', 'into', 'is', 'isn\'t', 'it', 'it\'s', 'its', 'itself', 'let\'s', 'me', 'more', 'most', 'mustn\'t',
    'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours',
    'ourselves', 'out', 'over', 'own', 'same', 'shan\'t', 'she', 'she\'d', 'she\'ll', 'she\'s', 'should', 'shouldn\'t',
    'so', 'some', 'such', 'than', 'that', 'that\'s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there',
    'there\'s', 'these', 'they', 'they\'d', 'they\'ll', 'they\'re', 'they\'ve', 'this', 'those', 'through', 'to', 'too',
    'under', 'until', 'up', 'very', 'was', 'wasn\'t', 'we', 'we\'d', 'we\'ll', 'we\'re', 'we\'ve', 'were', 'weren\'t',
    'what', 'what\'s', 'when', 'when\'s', 'where', 'where\'s', 'which', 'while', 'who', 'who\'s', 'whom', 'why', 'why\'s',
    'with', 'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll', 'you\'re', 'you\'ve', 'your', 'yours', 'yourself',
    'yourselves', 'report', 'schools', 'reports', 'like'
])

def tokenize(text):
    words = re.findall(r'[a-zA-Z0-9%\+\-]+', text.lower())
    return [w for w in words if len(w) > 2 and w not in stopwords]

df['tokens'] = (df['Article Title'] + " " + df['Context & Findings Summary']).apply(tokenize)

# Top terms per core theme
theme_vocab = {}
corpus_tokens = [w for tokens in df['tokens'] for w in tokens]
corpus_counter = Counter(corpus_tokens)
total_corpus_words = len(corpus_tokens)

for theme, grp in df.groupby('Core Theme'):
    theme_tokens = [w for tokens in grp['tokens'] for w in tokens]
    theme_counter = Counter(theme_tokens)
    total_theme_words = len(theme_tokens)
    
    # Calculate Probability, Lift, and FREX-like metrics
    term_metrics = []
    for term, count in theme_counter.most_common(20):
        prob = count / total_theme_words
        corpus_prob = corpus_counter[term] / total_corpus_words
        lift = prob / corpus_prob if corpus_prob > 0 else 1.0
        # FREX heuristic
        exclusivity = count / corpus_counter[term]
        frex = 0.7 * (prob / max([c/total_theme_words for c in theme_counter.values()])) + 0.3 * exclusivity
        term_metrics.append({
            'term': term,
            'count': count,
            'prob': round(prob, 4),
            'lift': round(lift, 2),
            'exclusivity': round(exclusivity, 2),
            'frex': round(frex, 3)
        })
    theme_vocab[theme] = term_metrics

print("Calculated theme vocabularies.")
for theme, terms in theme_vocab.items():
    print(f"{theme}: {[t['term'] for t in terms[:6]]}")

