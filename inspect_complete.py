import pandas as pd

df = pd.read_excel('academic_stress_database_2005_2010.xlsx')
print(df.describe(include='all'))
print("\nUnique dates:", sorted(df['Date'].unique()))
print("\nCross tab of Newspaper vs Year:")
print(pd.crosstab(df['Newspaper'], df['Date'].apply(lambda x: x.split('-')[2])))

print("\nCross tab of Newspaper vs Edition:")
print(pd.crosstab(df['Newspaper'], df['Edition']))

print("\nCross tab of Newspaper vs Core Theme:")
print(pd.crosstab(df['Newspaper'], df['Core Theme']))

print("\nCross tab of Core Theme vs Date (Year):")
df['Year'] = df['Date'].apply(lambda x: int(x.split('-')[2]))
print(pd.crosstab(df['Core Theme'], df['Year']))

print("\nCross tab of Core Theme vs Month:")
df['Month'] = df['Date'].apply(lambda x: int(x.split('-')[1]))
print(pd.crosstab(df['Core Theme'], df['Month']))

print("\nChecking all unique values of Article Title per Core Theme:")
for theme, grp in df.groupby('Core Theme'):
    print(f"Theme: {theme}")
    print("  Titles:", grp['Article Title'].unique())
    print("  Summaries:", grp['Context & Findings Summary'].unique())

