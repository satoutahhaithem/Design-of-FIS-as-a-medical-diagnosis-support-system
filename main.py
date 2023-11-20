import pandas as pd

# Assuming df is your DataFrame
# Replace 'df' with the actual variable name of your DataFrame if it's different
df = pd.read_csv('diabetes.csv') 

def fuzzify_pregnancies(value):
    # Define linguistic terms for 'Pregnancies'
    low = max(0, min((0 - value) / (0 - 3), (6 - value) / (6 - 3)))
    
    # Handle the case where the denominator is zero
    medium_denominator = 12 - 6 if (12 - 6) != 0 else 1
    high_denominator = value - 12 if (value - 12) != 0 else 1
    
    medium = max(0, min((value - 3) / (6 - 3), medium_denominator))
    high = max(0, min((value - 6) / (12 - 6), high_denominator))

    return {'Low': low, 'Medium': medium, 'High': high}


def fuzzify_glucose(value):
    # Define linguistic terms for 'Glucose'
    low = max(0, min((70 - value) / (70 - 0), (0 - value) / (0 - 70)))
    
    # Handle the case where the denominator is zero
    medium_denominator = 140 - 70 if (140 - 70) != 0 else 1
    high_denominator = value - 140 if (value - 140) != 0 else 1
    
    medium = max(0, min((value - 0) / (70 - 0), medium_denominator))
    high = max(0, min((value - 70) / (140 - 70), high_denominator))

    return {'Low': low, 'Medium': medium, 'High': high}

def fuzzify_blood_pressure(value):
    # Define linguistic terms for 'BloodPressure'
    low = max(0, min((40 - value) / (40 - 0), (0 - value) / (0 - 40)))

    # Handle the case where the denominator is zero
    medium_denominator = 80 - 40 if (80 - 40) != 0 else 1
    high_denominator = value - 80 if (value - 80) != 0 else 1
    
    medium = max(0, min((value - 0) / (40 - 0), medium_denominator))
    high = max(0, min((value - 40) / (80 - 40), high_denominator))

    return {'Low': low, 'Medium': medium, 'High': high}


# Repeat similar fuzzyfication functions for other features

# Apply fuzzification to the DataFrame
df['Pregnancies_Low'] = df['Pregnancies'].apply(lambda x: fuzzify_pregnancies(x)['Low'])
df['Pregnancies_Medium'] = df['Pregnancies'].apply(lambda x: fuzzify_pregnancies(x)['Medium'])
df['Pregnancies_High'] = df['Pregnancies'].apply(lambda x: fuzzify_pregnancies(x)['High'])

df['Glucose_Low'] = df['Glucose'].apply(lambda x: fuzzify_glucose(x)['Low'])
df['Glucose_Medium'] = df['Glucose'].apply(lambda x: fuzzify_glucose(x)['Medium'])
df['Glucose_High'] = df['Glucose'].apply(lambda x: fuzzify_glucose(x)['High'])

df['BloodPressure_Low'] = df['BloodPressure'].apply(lambda x: fuzzify_blood_pressure(x)['Low'])
df['BloodPressure_Medium'] = df['BloodPressure'].apply(lambda x: fuzzify_blood_pressure(x)['Medium'])
df['BloodPressure_High'] = df['BloodPressure'].apply(lambda x: fuzzify_blood_pressure(x)['High'])

# Repeat similar lines for other features

# Display the DataFrame with fuzzified columns
print(df.head())
