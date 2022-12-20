#////////////////Begin_Header///////////////////////////////////////////////////
#================================================================================
# This Python code was written by Behrooz Jadidi
# The first version was generated on 14_12_2022
# This code was written as a part of Movie_Maker project
# This code writes the trends search on google in a txt file
#================================================================================
#///////////////End_Header//////////////////////////////////////////////////////

# import libraries which we will use in our code

import pandas as pd                        
from pytrends.request import TrendReq

#Connecting to Google

pytrend = TrendReq()

# Interest By Region
# Let us see the terms which are popular in the region worldwide. 
# I will choose, the term to be searched as “Taylor Swift”

pytrend.build_payload(kw_list=["How to"])
df = pytrend.interest_by_region()
#print(df.head(20))

#df.reset_index().plot(x="geoName", y="Taylor_Swift", figsize=(120, 10), kind ="bar")


# Get Google Hot Trends data
df = pytrend.trending_searches(pn="canada")
#print(df.head())

df = pytrend.today_searches(pn="CA")
#print(df)

# Get Google Top Charts
# Let was see what was trending in 2019. 
# With the help of top_charts method we can get the top trending searches yearly.
df = pytrend.top_charts(2019, hl='en-US', tz=300, geo='GLOBAL')
print(df.head())

# Get Google Keyword Suggestions
keywords = pytrend.suggestions(keyword='Mercedes Benz')
df = pd.DataFrame(keywords)
#print(df.head())
#print(df.drop(columns= 'mid') )  # This column makes no sense


#Related Queries
#It's a common thing that when a user searches for a topic, they would also search for something related. 
# These are called related queries. Let us see what are the related queries for the topic “Coronavirus”. 
# Always remember when you want to change the topic name just 
# run the following code again with the new name as the parameter.


pytrend.build_payload(kw_list=['Coronavirus'])

# Related Queries, returns a dictionary of dataframes
related_queries = pytrend.related_queries()
#print(related_queries.values())

