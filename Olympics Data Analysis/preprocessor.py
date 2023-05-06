import pandas as pd

def preprocess(df,region_df):
    #filtering for summer olympics
    df = df[df['Season'] == 'Summer']

    #merge with region_df
    df = df.merge(region_df, on='NOC', how='left')

    #drooping Duplicates
    df.drop_duplicates(inplace=True)

    #one hot encoding medals
    dummies = pd.get_dummies(df['Medal'])
    df = pd.concat([df, dummies], axis='columns')

    return df