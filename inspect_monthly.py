import pandas as pd

df = pd.read_excel('academic_stress_database_2005_2010.xlsx')
df['Parsed_Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Month'] = df['Parsed_Date'].dt.month
df['Month_Name'] = df['Parsed_Date'].dt.strftime('%B')
df['Year'] = df['Parsed_Date'].dt.year

print("--- Month by Core Theme ---")
print(pd.crosstab(df['Month_Name'], df['Core Theme']))

print("\n--- Month by Newspaper ---")
print(pd.crosstab(df['Month_Name'], df['Newspaper']))

print("\n--- Year & Month cross-tabulation ---")
print(pd.crosstab([df['Year'], df['Month_Name']], df['Core Theme']))

print("\n--- Year & Month by Newspaper ---")
print(pd.crosstab([df['Year'], df['Month_Name']], df['Newspaper']))

print("\n--- Newspaper by Edition ---")
print(pd.crosstab(df['Newspaper'], df['Edition']))

print("\n--- Core Theme by Edition ---")
print(pd.crosstab(df['Edition'], df['Core Theme']))

print("\n--- Detailed breakdown of Theme by Year and Month ---")
for y in sorted(df['Year'].unique()):
    sub = df[df['Year'] == y]
    print(f"Year {y}:")
    print(pd.crosstab(sub['Month_Name'], sub['Core Theme']))

