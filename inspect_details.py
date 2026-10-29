import pandas as pd

df = pd.read_excel('academic_stress_database_2005_2010.xlsx')
print("Unique Article Titles:", df['Article Title'].nunique())
print("Unique Summaries:", df['Context & Findings Summary'].nunique())
print("\nUnique Summaries list:")
for s in df['Context & Findings Summary'].unique():
    print("-", s)

print("\nValue counts of Summary:")
print(df['Context & Findings Summary'].value_counts())

print("\nDates breakdown:")
print(df['Date'].value_counts().sort_index())

print("\nCheck if there are differences across years or editions:")
print(df.groupby(['Year' if 'Year' in df else df['Date'].apply(lambda x: x.split('-')[-1]), 'Core Theme']).size())

