#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis on US Accidents 

# ## Importing the data file 

# In[18]:


import pandas as pd
data_file = '/Users/swaroopkumarpalai/Desktop/data analysis/Untitled Folder/US_Accidents_March23.csv'



# In[19]:


df = pd.read_csv(data_file)
df


# ##  Ask & answer questions
# 
# 1. Are there more accidents in warmer or colder areas?
# 2. Which 5 states have the highest number of accidents? How about per capita?
# 3. Does New York show up in the data? If yes, why is the count lower if this the most populated city.
# 4. Among the top 100 cities in number of accidents, which states do they belong to most frequently.
# 5. What time of the day are accidents most frequent in? 
# 6. Which days of the week have the most accidents?
# 7. Which months have the most accidents?
# 8. What is the trend of accidents year over year (decreasing/increasing?)
# 9. When is accidents per unit of traffic the highest.

# ## Checking the datatype for each column index

# In[8]:


df.info()


# In[9]:


df.describe()


# ## few things to note:
# 1. start_Lat and Lng are more than End_lat and lng entries. maybe most of the accidents are point accidents and end_cooridnates are not a crucial entry.
# 2. Are there more accidents in warmer or colder temperatures?
# 3. which states have the highest/lowest accidents?
# 4. Which states have the highest/lowest accidents per capita?
# 5. which 5 states have the highest accidents? 
# 6. New York has the highest population, but doesnt come up in the top 10 cities arranged by accidents!!!

# In[13]:


numerics = ['int16' , 'int32', 'int64', 'float16', 'float32', 'float64' ]


# ## how many data columns we have ?

# In[22]:


num_df = df.select_dtypes(include = numerics)
print(num_df.shape[1])


# 
# ## how many missing values are there?
# 

# In[27]:


null_values = df.isna().sum()


# We want to know the percentage of missing values

# In[36]:


missing_percentages = (null_values/len(df)*100).sort_values(ascending = False)


# ## Plotting the percentage of missing values in the columns

# In[47]:


missing_percentages_filter = missing_percentages[missing_percentages != 0]


# In[48]:


missing_percentages_filter.plot(kind = 'barh')


# ## Remove the columns you dont want to display: Use .Drop() function

# ## We will use few columns to analyse
# 
# ### 1. City/State
# ### 2. Start Time
# ### 3. Start Lat/long
# ### 4. Temperature
# ### 5. Weather condition

# In[49]:


df.columns


# In[52]:


missing_percentages_filter.index


# In[55]:


df.columns


# # Analysing the City/State attributes

# In[57]:


df.City


# In[62]:


unique_cities = df.City.unique()
len(unique_cities)


# In[64]:


accidents_by_city = df.City.value_counts()
accidents_by_city


# ## data for New York is absent

# In[67]:


'New York'in df.City


# ## Accidents per state across the US

# In[68]:


accidents_by_state = df.State.value_counts()
accidents_by_state


# ## Plotting number of accidents by State (for the top 10)

# In[72]:


accidents_by_state[accidents_by_state != 0][0:10].plot(kind='barh')


# ## Ploting the number of accidents per city (for the top 10 cities)

# In[75]:


accidents_by_city[0:10].plot(kind = 'barh')


# ## Importing Seaborn

# In[78]:


import seaborn as sns
sns.set_style("darkgrid")
sns.distplot(accidents_by_state)


# ## how to know the type of pandas dataframe?

# In[79]:


type(accidents_by_city)


# In[80]:


sns.histplot(accidents_by_state)


# ## Creating buckets for categorising cities by number of accidents

# In[105]:


low_accident_cities = accidents_by_city[(accidents_by_city<1000)]
high_accident_cities = accidents_by_city[accidents_by_city >= 1000]


# In[106]:


len(high_accident_cities)/len(accidents_by_city)*100


# In[107]:


sns.distplot(high_accident_cities)


# ## Plot for the high accident cities presenting number of cities vs number of accidents

# In[112]:


sns.histplot(high_accident_cities)


# In[113]:


sns.histplot(low_accident_cities)


# In[114]:


sns.distplot(low_accident_cities)


# In[115]:


sns.distplot(high_accident_cities)


# ## Histogram plot showing number of accidents (in log. scale) vs number of cities 

# In[110]:


sns.histplot(high_accident_cities, log_scale = True)


# In[111]:


sns.histplot(low_accident_cities, log_scale = True)


# ## Number of cities with just 1 accident

# In[117]:


accidents_by_city[accidents_by_city == 1]


# # Analysing the Start time

# In[120]:


df.Start_Time


# ## Parsing date-time in pandas

# In[127]:


df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='mixed', errors='coerce')
df.Start_Time


# ## Time of the day

# In[130]:


df['Hour'] = df['Start_Time'].dt.hour
df['Hour']


# In[157]:


import matplotlib as plt
sns.histplot(df.Hour, bins = 24, stat = 'percent')


# #### 1.Most accidents happen during 7am-9am in the morning. Probably during the time when people are going to office.
# #### 2.Most accidents happen during 16pm-18pm in the evening. Probably during the time when the people are returing from the week.

# ## Day of the Week

# In[159]:


df['Day'] = df['Start_Time'].dt.dayofweek
df['Day']


# In[160]:


sns.histplot(df.Day, bins = 7, stat = 'percent')


# #### 1. On weekends, the number of accidents are lower.

# ###  Question- Is the distribution of time of accident same on weekends also as weekdays??

# ## Saturday distribution throughout the day

# In[167]:


df['Saturday'] = df['Start_Time'].dt.dayofweek == 5
df['Saturday']


# In[169]:


sns.histplot(df[df['Saturday']]['Start_Time'].dt.hour, bins=24, stat='percent')


# ## Sunday distribution throughout the day

# In[170]:


df['Sunday'] = df['Start_Time'].dt.dayofweek == 6
df['Sunday']


# In[172]:


sns.histplot(df[df['Sunday']]['Start_Time'].dt.hour, bins=24, stat='percent')


# ## Monday distribution throughout the day

# In[173]:


df['Monday'] = df['Start_Time'].dt.dayofweek == 0
df['Monday']


# In[175]:


sns.histplot(df[df['Monday']]['Start_Time'].dt.hour, bins=24, stat='percent')


# #### On Saturdays and Sundays the peak occurs between 12pm to 16pm, quite DIFFERENT than on Mondays

# In[178]:


sns.histplot(df['Start_Time'].dt.month, bins=12, stat='percent')


# ### The accidents are more common in winter months like November, December, January, February maybe due to snow.

# ## Data for 2021 year

# In[179]:


df['2021']= df['Start_Time'].dt.year == 2021
df['2021']


# In[182]:


sns.histplot(df[df['2021']]['Start_Time'].dt.month, bins=12, stat='percent')


# ## Data for 2022 year

# In[184]:


df['2022']= df['Start_Time'].dt.year == 2022
df['2022']


# In[185]:


sns.histplot(df[df['2022']]['Start_Time'].dt.month, bins=12, stat='percent')


# ## Knowing the Source of the data df.source

# In[190]:


df.columns


# In[194]:


df.Source


# In[198]:


df.Source.value_counts().plot(kind='pie',autopct='%1.1f%%')


# # Latitude and Longitude analysis

# In[199]:


df.Start_Lat


# In[200]:


df.Start_Lng


# In[219]:


sample_df = df.sample(frac=0.1)


# In[220]:


sns.scatterplot(x=sample_df.Start_Lng, y=sample_df.Start_Lat, size=0.001, alpha=0.1)


# In[28]:


import folium
from folium.plugins import HeatMap


# In[29]:


list(zip(list(df.Start_Lat),list(df.Start_Lng)))


# #### Marking a trial point on the folium Map

# In[27]:


lat, long = df.Start_Lat[0], df.Start_Lng[0]
map = folium.Map(location=[lat, long], zoom_start=10)

# Create a folium Marker
marker = folium.Marker(location=[lat, long])

# Add the Marker to the Map
marker.add_to(map)

map


# In[36]:


sample_df = df.sample(int(0.001*len(df)))
lat_long_pairs = list(zip(list(sample_df.Start_Lat),list(sample_df.Start_Lng)))


# In[37]:


map = folium.Map()
HeatMap(lat_long_pairs).add_to(map)
map


# # Number of accidents per capita

# In[38]:


accidents_by_state = df.State.value_counts()
accidents_by_state


# In[39]:


df.columns


# In[40]:


population_file = '/Users/swaroopkumarpalai/Desktop/data analysis/Untitled Folder/population_by_zip_2010.csv'
df_pop = pd.read_csv(population_file)
df_pop


# In[41]:


sorted_df_pop = df_pop.sort_values(by = 'zipcode')
sorted_df_pop


# In[42]:


sorted_df = df.sort_values(by = 'Zipcode')
sorted_df


# # insights and conclusions
# 
# ### 1. No Data from New York
# ### 2. High Accident (>1000 accidents) cities constitute about 8.9% of all the cities in the US.
# ### 3. About 1000 cities have just 1 accident reported for.
# ### 4. Number of accidents per city shows a gaussian trend (just eyeballing).

# In[ ]:




