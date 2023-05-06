import numpy as np


def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'overall' and country == "overall":
        temp_df = medal_df
    if year == 'overall' and country != "overall":
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'overall' and country == "overall":
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'overall' and country != "overall":
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                    ascending=False).reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x
    # print(x)

def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])

    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',ascending=False).reset_index()

    medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['total'] = medal_tally['total'].astype('int')

    return medal_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'overall')

    return years,country

def data_over_time(df,col):
    nation_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('index')
    nation_over_time.rename(columns={'index': 'Edition', 'Year': col}, inplace=True)

    return nation_over_time


def most_success(df, sport):
    temp_df = df.dropna(subset=['Medal'])
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    temp_df = temp_df['Name'].value_counts().reset_index().head(15).merge(df, left_on='index', right_on='Name',
                                                                          how='left').drop_duplicates('index')
    temp = temp_df[['index', 'Name_x', 'Sport', 'region']].reset_index().drop(['level_0'], axis='columns')
    temp.rename(columns={'index': 'Name', 'Name_x': 'Medals'}, inplace=True)

    return temp


def most_wins(df, sport):
    if sport != 'Overall':
        temp = df[df['Sport'] == sport].groupby('Name').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',ascending=False).reset_index().head(10)
    else:
        temp = df.groupby('Name').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index().head(10)

    temp = temp.merge(df.drop(['Gold', 'Silver', 'Bronze'], axis='columns'), left_on='Name', right_on='Name',how='left').drop_duplicates('Name')

    temp['Total Medal'] = temp['Gold'] + temp['Silver'] + temp['Bronze']

    temp = temp[['Name', 'Gold', 'Silver', 'Bronze', 'Total Medal', 'Sport', 'region']].sort_values('Total Medal',ascending=False).reset_index().drop(['index'], axis='columns')

    return temp

def yearwise_medal_tally(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
    new_temp_df = temp_df[temp_df['region'] == country]
    final_df = new_temp_df.groupby('Year').count()['Medal'].reset_index()
    return final_df

def country_event_heatmap(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
    temp_df = temp_df[temp_df['region'] == country]
    y = temp_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0).astype(int)

    return y


def successfull_athelets(df, country):
    temp = df[df['region'] == country].groupby('Name').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',ascending=False).reset_index().head(10)

    temp = temp.merge(df.drop(['Gold', 'Silver', 'Bronze'], axis='columns'), left_on='Name', right_on='Name',how='left').drop_duplicates('Name')

    temp['Total Medal'] = temp['Gold'] + temp['Silver'] + temp['Bronze']

    temp = temp[['Name', 'Total Medal', 'Sport', 'Gold', 'Silver', 'Bronze']].sort_values('Total Medal',ascending=False).reset_index().drop(['index'], axis='columns')

    return temp

def men_vs_women(df):
    men = df[df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = df[df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()
    final = men.merge(women, on='Year', how='left').fillna(0).astype(int)
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    return final

