import pandas as pd
import plotly.express as px

def plot_photos_by_weather(df):
    fig = px.bar(df.groupby('weather')['photos'].mean().reset_index(),
                 x='weather', y='photos',
                 title='Average Photos by Weather')
    fig.show(renderer="browser")

def plot_mood_distribution(df):
    fig = px.pie(df, names='mood', title='Mood Distribution')
    fig.show(renderer="browser")

def plot_photos_over_time(df):
    df['date'] = pd.to_datetime(df['date'])
    fig = px.line(df, x='date', y='photos', title='Photos Over Time')
    fig.show(renderer="browser")