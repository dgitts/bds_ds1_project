#!/usr/bin/env python
# coding: utf-8

# In[4]:


import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_csv("C:\\Users\\oscer\\Downloads\\Airbnb_texas_rental_data.csv")
df.head()
Texas = df[df.city.str.contains('Dallas', case=False)
          |df.city.str.contains('Carrollton', case=False)
          | df.city.str.contains('Grapevine', case=False)
          | df.city.str.contains('Addison', case=False)
          | df.city.str.contains('Lewisville', case=False)
          | df.city.str.contains('Plano', case=False)
          | df.city.str.contains('Arlington', case=False)
          | df.city.str.contains('Irving', case=False)
          | df.city.str.contains('Farmers Branch', case=False)
          | df.city.str.contains('Coppell', case=False)
          | df.city.str.contains('Fort Worth', case=False)
          | df.city.str.contains('Grand Prairie', case=False)]
Texas

fig = px.density_mapbox(Texas, lat='latitude', lon='longitude', z='bedrooms_count', radius=10,
                        hover_name="city", hover_data=["average_rate_per_night"],
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="open-street-map")


fig.update_layout(autosize=False,
    width=2000,
    height=1000,margin={"r":0.5,"t":0.5,"l":0.5,"b":0.5})
fig.show()


# In[5]:


df = pd.read_csv("C:\\Users\\oscer\\Downloads\\Airbnb_texas_rental_data.csv")
df.head()
Texas = df[df.city=='Dallas']

import matplotlib.pyplot as plt
import plotly.graph_objects as go

freq = Texas['bedrooms_count']. value_counts().sort_values(ascending=True)
freq.plot.barh(figsize=(15, 3), width=1, color = ["g","b","r","yellow","black","turquoise"])
plt.title('Rental Type')
plt.xlabel('Number of Listings')
plt.ylabel('Accommodates')

plt.show()


# In[6]:


import pandas as pd
import plotly.express as px
import plotly.offline as ofl
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\oscer\\Downloads\\airbnb_dfw_market\\airbnb_dfw_market.csv")

x = df['Market']
y = df['Occupancy Rate %']
y1 = df['Entire Home Rentals']
y2 = df['Q1 19']
y3 = df['Q2 19']
y4 = df['Q3 19']
y5 = df['Q4 19']
y6 = df['Q1 20']
y7 = df['Q2 20']

# Create trace 1 for Corp_A

trace1 = go.Bar(
    x=x,
    y=y2,
    name='2019 Q1'
)
trace2 = go.Bar(
    x=x,
    y=y3,
    name='2019 Q2'
)


trace3= go.Bar(
    x=x,
    y=y6,
    name='2020 Q1'
)

trace4= go.Bar(
    x=x,
    y=y7,
    name='2020 Q2'
)

data = [trace1,trace3,trace2,trace4]

# Create layout object with barmode set to group
layout = go.Layout(
    barmode='group'
)

# Create figure object and visualize plot
fig = go.Figure(data=data, layout=layout)
ofl.iplot(fig, filename='grouped-bar')


# In[ ]:




