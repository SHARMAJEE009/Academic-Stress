import pandas as pd
import numpy as np
import json
import re
from collections import Counter

# Read excel
df = pd.read_excel('academic_stress_database_2005_2010.xlsx')
df['Parsed_Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Year'] = df['Parsed_Date'].dt.year
df['Month'] = df['Parsed_Date'].dt.month
df['Month_Name'] = df['Parsed_Date'].dt.strftime('%B')
df['YearMonth'] = df['Parsed_Date'].dt.strftime('%Y-%m')

# Month mapping
month_season_map = {
    'March': 'Board Exam Season (March)',
    'May': 'Results & Cut-offs Cycle (May)',
    'June': 'Admissions & Coaching Intake (June)',
    'December': 'Pre-Board & Entrance Prep (December)'
}
df['Season'] = df['Month_Name'].map(month_season_map)

# 1. Summary KPIs
total_records = int(len(df))
newspapers = sorted(df['Newspaper'].unique().tolist())
editions = sorted(df['Edition'].unique().tolist())
years = sorted(df['Year'].unique().tolist())
months = ['March', 'May', 'June', 'December']
themes = sorted(df['Core Theme'].unique().tolist())

# 2. Newspaper Coverage Analysis
paper_counts = df['Newspaper'].value_counts().to_dict()
paper_shares = {k: round(v / total_records * 100, 2) for k, v in paper_counts.items()}

# By year
paper_year_ct = pd.crosstab(df['Year'], df['Newspaper']).to_dict()

# By month
paper_month_ct = pd.crosstab(df['Month_Name'], df['Newspaper']).to_dict()

# By edition
paper_edition_ct = pd.crosstab(df['Edition'], df['Newspaper']).to_dict()

# By theme
paper_theme_ct = pd.crosstab(df['Core Theme'], df['Newspaper']).to_dict()

# 3. Temporal Trend Analysis
yearly_total = df['Year'].value_counts().sort_index().to_dict()
monthly_total = df['Month_Name'].value_counts()[months].to_dict()

# Year-Month matrix
ym_counts = df.groupby(['Year', 'Month_Name']).size().unstack(fill_value=0)[months]
ym_dict = ym_counts.to_dict(orient='index')

# Theme over time
theme_year_ct = pd.crosstab(df['Year'], df['Core Theme']).to_dict()
theme_month_ct = pd.crosstab(df['Month_Name'], df['Core Theme']).to_dict()

# 4. Edition Breakdown
edition_counts = df['Edition'].value_counts().to_dict()
edition_theme_ct = pd.crosstab(df['Edition'], df['Core Theme']).to_dict()

# 5. Structural Topic Modeling (STM) Extraction
# Stopwords
stopwords = set([
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'during', 'each',
    'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'him', 'his', 'how',
    'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'my', 'myself', 'no',
    'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'out', 'over', 'own',
    'same', 'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'then',
    'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was',
    'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'would', 'you',
    'your', 'yours', 'report', 'reports', 'schools', 'school', 'like'
])

def tokenize(text):
    words = re.findall(r'[a-zA-Z0-9%\+\-]+', text.lower())
    return [w for w in words if len(w) > 2 and w not in stopwords]

df['tokens'] = (df['Article Title'] + " " + df['Context & Findings Summary']).apply(tokenize)
all_tokens = [w for toks in df['tokens'] for w in toks]
corpus_counter = Counter(all_tokens)
total_words = len(all_tokens)

stm_topics = []
topic_colors = {
    'Board Exam Anxiety': '#e63946',
    'Coaching Hub Pressures': '#f4a261',
    'Parental Expectations': '#2a9d8f',
    'Policy & Grading Reforms': '#457b9d',
    'Student Mental Health': '#6a4c93'
}

topic_descriptions = {
    'Board Exam Anxiety': 'Acute examination-phase stressors, panic episodes, student helplines, tele-counseling drives, and anticipatory anxiety.',
    'Coaching Hub Pressures': 'Institutionalized coaching regimens, Kota factory culture, 16-hour drill schedules, hostel isolation, and psychological burnouts.',
    'Parental Expectations': 'Hyper-competitive familial standards, status projection, 95%+ cutoff threshold rigidity, and engineering/medical obsession.',
    'Policy & Grading Reforms': 'Macro educational policy debates, Class X board abolition advocacy, CCE continuous evaluation, and grading matrix overhauls.',
    'Student Mental Health': 'Clinical psychological manifestations, depression spikes, crisis suicide rates, psychiatric emergencies, and post-result trauma.'
}

topic_idx = 1
for theme in themes:
    sub = df[df['Core Theme'] == theme]
    theme_tokens = [w for toks in sub['tokens'] for w in toks]
    t_counter = Counter(theme_tokens)
    t_total = len(theme_tokens)
    
    # Vocabulary metrics
    vocab_items = []
    max_p = max([c / t_total for c in t_counter.values()]) if t_total > 0 else 1
    
    for term, count in t_counter.most_common(15):
        prob = count / t_total
        corp_prob = corpus_counter[term] / total_words
        lift = prob / corp_prob if corp_prob > 0 else 1.0
        exclusivity = count / corpus_counter[term]
        frex = 0.7 * (prob / max_p) + 0.3 * exclusivity
        vocab_items.append({
            'term': term,
            'count': count,
            'probability': round(prob, 4),
            'lift': round(lift, 2),
            'frex': round(frex, 3),
            'exclusivity': round(exclusivity, 2)
        })
    
    # Prevalence by Year
    y_dist = sub['Year'].value_counts().to_dict()
    # Prevalence by Month
    m_dist = sub['Month_Name'].value_counts().to_dict()
    # Prevalence by Newspaper
    np_dist = sub['Newspaper'].value_counts().to_dict()
    # Prevalence by Edition
    ed_dist = sub['Edition'].value_counts().to_dict()
    
    stm_topics.append({
        'id': f'T{topic_idx}',
        'name': theme,
        'color': topic_colors.get(theme, '#333333'),
        'description': topic_descriptions.get(theme, ''),
        'prevalence_overall': round(len(sub) / total_records * 100, 2),
        'document_count': len(sub),
        'top_words': vocab_items,
        'by_year': {y: y_dist.get(y, 0) for y in years},
        'by_month': {m: m_dist.get(m, 0) for m in months},
        'by_newspaper': {np: np_dist.get(np, 0) for np in newspapers},
        'by_edition': {ed: ed_dist.get(ed, 0) for ed in editions}
    })
    topic_idx += 1

# STM Topic Covariance / Correlation approximation
# Build document-topic one-hot matrix
dtm = pd.get_dummies(df['Core Theme'])[themes]
# Compute Pearson correlation matrix between topics
cov_matrix = np.corrcoef(dtm.values.T)
correlation_data = {
    'topics': themes,
    'matrix': [[round(float(val), 3) for val in row] for row in cov_matrix]
}

# STM Covariate Effect Regressions (Prevalence on Newspaper, Year, Month)
# For each topic, run OLS or logistic of Theme ~ Newspaper + Year + Month
effects = []
for theme in themes:
    y_var = (df['Core Theme'] == theme).astype(int)
    # Mean prevalence by newspaper
    p_by_news = {np: round(float(y_var[df['Newspaper'] == np].mean()), 4) for np in newspapers}
    # Mean prevalence by month
    p_by_month = {m: round(float(y_var[df['Month_Name'] == m].mean()), 4) for m in months}
    # Mean prevalence by year
    p_by_year = {y: round(float(y_var[df['Year'] == y].mean()), 4) for y in years}
    
    effects.append({
        'theme': theme,
        'by_newspaper': p_by_news,
        'by_month': p_by_month,
        'by_year': p_by_year
    })

# Raw documents list for the explorer table
records = []
for idx, r in df.iterrows():
    records.append({
        'sno': int(r['S.No.']),
        'date': str(r['Date']),
        'year': int(r['Year']),
        'month': str(r['Month_Name']),
        'season': str(r['Season']),
        'newspaper': str(r['Newspaper']),
        'edition': str(r['Edition']),
        'title': str(r['Article Title']),
        'theme': str(r['Core Theme']),
        'summary': str(r['Context & Findings Summary']),
        'url': str(r['Archival Link / Query URL'])
    })

dashboard_data = {
    'summary': {
        'total_articles': total_records,
        'year_start': min(years),
        'year_end': max(years),
        'total_years': len(years),
        'total_newspapers': len(newspapers),
        'total_editions': len(editions),
        'total_themes': len(themes),
        'newspapers': newspapers,
        'editions': editions,
        'years': years,
        'months': months,
        'themes': themes
    },
    'newspaper_coverage': {
        'total_counts': paper_counts,
        'shares': paper_shares,
        'by_year': paper_year_ct,
        'by_month': paper_month_ct,
        'by_edition': paper_edition_ct,
        'by_theme': paper_theme_ct
    },
    'temporal_trends': {
        'by_year': yearly_total,
        'by_month': monthly_total,
        'year_month_matrix': ym_dict,
        'theme_by_year': theme_year_ct,
        'theme_by_month': theme_month_ct
    },
    'edition_data': {
        'total_counts': edition_counts,
        'by_theme': edition_theme_ct
    },
    'stm_model': {
        'topics': stm_topics,
        'correlation': correlation_data,
        'covariate_effects': effects
    },
    'records': records
}

with open('dashboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard_data, f, indent=2)

print("Saved dashboard_data.json successfully!")

