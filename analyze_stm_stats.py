import pandas as pd
import numpy as np

df = pd.read_excel('academic_stress_database_2005_2010.xlsx')
df['Parsed_Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Year'] = df['Parsed_Date'].dt.year
df['Month'] = df['Parsed_Date'].dt.month
df['Month_Name'] = df['Parsed_Date'].dt.strftime('%B')

print("--- Theme distribution across months ---")
ct_theme_month = pd.crosstab(df['Month_Name'], df['Core Theme'], normalize='index') * 100
print(ct_theme_month.round(2))

print("\n--- Theme distribution across years ---")
ct_theme_year = pd.crosstab(df['Year'], df['Core Theme'], normalize='index') * 100
print(ct_theme_year.round(2))

print("\n--- Newspaper distribution across months ---")
ct_paper_month = pd.crosstab(df['Month_Name'], df['Newspaper'], normalize='index') * 100
print(ct_paper_month.round(2))

print("\n--- Monthly volume over years ---")
monthly_trend = pd.crosstab(df['Year'], df['Month_Name'])
print(monthly_trend)

print("\n--- Newspaper vs Month counts ---")
print(pd.crosstab(df['Newspaper'], df['Month_Name']))

print("\n--- Let's check if there are correlations or differences in Month by Theme ---")
print(pd.crosstab(df['Month_Name'], df['Core Theme']))

