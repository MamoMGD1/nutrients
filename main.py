import foods
import pandas as pd, matplotlib.pyplot as plt

df = pd.read_csv('foods_dataset.csv')

# you can change these values
tests = foods.avocado
k_value = 5

def predict(test,h_real):
    expected_features = []
    dif_features = []
    updated_df = df.copy()
    for col in updated_df:
        if test[col]!='':
            updated_df[f'dif_{col}'] = abs(updated_df[col]-test[col])
            dif_features.append(f'dif_{col}')
        else:
            expected_features.append(col)

    results = []
    for feature in dif_features:
        nearest_samples = updated_df.nsmallest(k_value,feature)
        for exp in expected_features:
            results.append({'exp': exp, 'val': float(nearest_samples[exp].mean())})
    print(results)

    # show false predictions only
    df_results = pd.DataFrame(results)
    mean_values = df_results.groupby('exp')['val']
    for exp,group in mean_values:
        value = float(group.mean())
        test[exp] = f'{'healthy' if value>=0.5 else 'unhealthy'}'
        test['accuracy'] = 100*abs(value-0.5)+50
    if test['healthiness']!=h_real:
        print(test)

# Fill all the null values with median (for numeric features) or mode (for categoric features)
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
categoric_cols = df.select_dtypes(include='object').columns
for col in categoric_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Bring original data for tasting the algorithm
# tests = [df.iloc[i].to_dict() for i in range(100)]

# Change str to float
for col in categoric_cols:
    df[col] = df[col].map({'healthy':1,'unhealthy':0})

# Predict testing samples
for test in tests:
    h_real = test['healthiness']
    test['healthiness'] = ''
    predict(test,h_real)

# Check the correlation of the dataset's features
# print(df.corr())
# print(f"{df['vitamin'].max()} ==== {df['vitamin'].min()}")

x_axis = 'fat'
y_axis = 'sugar'
colors = ['green' if h == 1 else 'red' for h in df['healthiness']]
plt.scatter(df[x_axis],df[y_axis],color=colors,alpha=0.75)
plt.scatter(tests[0][x_axis],tests[0][y_axis],color='blue',linewidths=2,label=f'Sample is {tests[0]['healthiness']}')
plt.xlabel(f'{x_axis} (g/100g)')
plt.ylabel(f'{y_axis} (g/100g)')
plt.legend()
plt.show()