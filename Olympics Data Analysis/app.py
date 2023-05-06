import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympic Analysis")
# st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-Wise Analysis','Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)

    if selected_year == 'overall' and selected_country == "overall":
        st.title("Overall Tally")
    if selected_year == 'overall' and selected_country != "overall":
        st.title(selected_country + " Overall Performance")
    if selected_year != 'overall' and selected_country == "overall":
        st.title("Madel Tally in " + str(selected_year) + " Olympics")
    if selected_year != 'overall' and selected_country != "overall":
        st.title(selected_country + " Performance in " + str(selected_year) +" Olympics")

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    st.table(medal_tally)

if user_menu == "Overall Analysis":
    edition = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athelets = df['Name'].unique().shape[0]
    nation = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col,col2,col3 = st.columns(3)
    with col:
        st.header("Editions")
        st.title(edition)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col, col2, col3 = st.columns(3)
    with col:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nation")
        st.title(nation)
    with col3:
        st.header("Athelets")
        st.title(athelets)

    nation_over_time = helper.data_over_time(df,'region')
    st.title("Participating Nations Over The Years")
    fig_nation = px.line(nation_over_time, x='Edition', y='region')
    st.plotly_chart(fig_nation)

    event_over_time = helper.data_over_time(df, 'Event')
    st.title("Events Over The Years")
    fig_event = px.line(event_over_time, x='Edition', y='Event')
    st.plotly_chart(fig_event)

    atheletes_over_time = helper.data_over_time(df, 'Name')
    st.title("Atheletes Over The Years")
    fig_athelete = px.line(atheletes_over_time, x='Edition', y='Name')
    st.plotly_chart(fig_athelete)

    # st.title("No. of Event Over The Time")
    # x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    # fig,ax = plt.subplots(figsize=(25,35))
    # y = x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int)
    # # st.table(y)
    # ax = sn.heatmap(y,annot=True)
    # st.pyplot(fig)

    st.title("Top Most Succesfull Athelets")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    sport = st.selectbox("Select A Sport",sport_list)
    x = helper.most_wins(df,sport)
    st.table(x)

if user_menu == 'Country-Wise Analysis':

    st.sidebar.title('Country-Wise-Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    country_name = st.sidebar.selectbox("Select a country",country_list)
    country_df = helper.yearwise_medal_tally(df,country_name)

    st.title("Medal Tally Over The Years")
    fig_country_medal = px.line(country_df, x='Year', y='Medal')
    st.plotly_chart(fig_country_medal)

    # st.title(country_name+" excels in the folloing sports")
    # pt = helper.country_event_heatmap(df,country_name)
    # try:
    #     fig,ax = plt.subplots(figsize=(20, 20))
    #     ax = sn.heatmap(pt, annot=True)
    #     st.pyplot(fig)
    # except:
    #     st.header("\"This country isn't any kind of medal in any sports\"")

    st.title("Most Succesfull Athelets of "+country_name)
    athelets = helper.successfull_athelets(df,country_name)
    st.table(athelets)

if user_menu == 'Athlete wise Analysis':
    st.title('Men vs Women Participates')
    final = helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    st.plotly_chart(fig)
