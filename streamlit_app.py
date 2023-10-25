import pandas as pd
import numpy as np
# import plotly.graph_objects as go
# import plotly.express as px
import streamlit as st
# from datetime import datetime
import altair as alt

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.table(df2)

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
#
# st.table(df)
#
# fig = px.line(data_frame=df, x="col 0", y="col 1")
#
# fig.show()

# # dataframe of a wide format
# np.random.seed(123)
# X = np.random.randn(100,3)
# df= pd.DataFrame(X, columns=['a', 'b', 'c'])
# df= df.cumsum()
# df['id']= df.index
#
# # dataframe of a long format
# df = pd.melt(df, id_vars='id', value_vars=df.columns[:-1])
#
# # plotly express
# fig = px.line(df, x='id', y='value', color='variable')
# fig.show()

# # Load data
# df_agg = pd.read_csv("archive/Aggregated_Metrics_By_Video.csv").iloc[1:,:]
# df_agg.columns = ['Video', 'Video title', 'Video publish time', 'Comments added', 'Shares', 'Dislikes', 'Likes',
#                   'Subscribers lost', 'Subscribers gained', 'RPM(USD)', 'CPM(USD)', 'Average percentage viewed (%)',
#                   'Average view duration', 'Views', 'Watch time(hours)', 'Subscribers', 'Your estimated revenue(USD)',
#                   'Impressions', 'Impressions click-through rate(%)']
# df_agg["Video publish time"] = pd.to_datetime(df_agg["Video publish time"])
# df_agg["Average view duration"] = df_agg["Average view duration"].apply(lambda x: datetime.strptime(x, "%H:%M:%S"))
# df_agg["Average duration sec"] = df_agg["Average view duration"].apply(lambda x: x.second + x.minute*60 + x.hour*3600)
# # df_agg_sub = pd.read_csv("archive/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv")
# # df_comments = pd.read_csv("archive/All_Comments_Final.csv")
# # df_time = pd.read_csv("archive/Video_Performance_Over_Time.csv")
#
# print(list(df_agg.columns))
