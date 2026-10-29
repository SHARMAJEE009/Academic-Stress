import pandas as pd
import json

df = pd.read_excel('academic_stress_database_2005_2010.xlsx')
print(f"Total rows: {len(df)}")
print("Columns:", df.columns.tolist())

print("\n--- Editions ---")
print(df['Edition'].value_counts())

print("\n--- Newspapers ---")
print(df['Newspaper'].value_counts())

print("\n--- Core Themes ---")
print(df['Core Theme'].value_counts())

# Parse dates
df['Parsed_Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
if df['Parsed_Date'].isna().any():
    print("Some dates failed format '%d-%m-%Y', checking alternate formats...")
    # fallback
    df['Parsed_Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['Year'] = df['Parsed_Date'].dt.year
df['YearMonth'] = df['Parsed_Date'].dt.to_period('M')

print("\n--- Articles per Year ---")
print(df['Year'].value_counts().sort_index())

print("\n--- Articles per Year by Newspaper ---")
print(pd.crosstab(df['Year'], df['Newspaper']))

print("\n--- Articles per Year by Core Theme ---")
print(pd.crosstab(df['Year'], df['Core Theme']))

print("\n--- Articles per Newspaper by Core Theme ---")
print(pd.crosstab(df['Newspaper'], df['Core Theme']))

print("\n--- Sample Articles (first 5 unique titles and context) ---")
for idx, row in df.head(10).iterrows():
    print(f"[{row['Date']}] {row['Newspaper']} ({row['Edition']}) | {row['Core Theme']}")
    print(f"Title: {row['Article Title']}")
    print(f"Summary: {row['Context & Findings Summary']}")
    print(f"URL: {row['Archival Link / Query URL']}")
    print("-" * 60)

