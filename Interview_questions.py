[context]
#Below we have a header snippet of three tables: Google_ad_impression; Visits; Leads
#Google_ad_impressions: We pay Google to show ads to users interested in real estate.
#Vistis: A subset of people on google click on the ad and visit the realtor.com website. Other visitors can arrive organically or via other marketing channels.
#Leads: A subset of realtor.com visits complete a real estate lead form that earns realtor.com revenue.


[RDC.CLICKSTREAM.Google_ad_impression]
google_impression_id  timestamp             cost_usd    campaign_id     device
VgMyLFvuYj29          2021-11-08 19:10:05   0.08        156703080064    mobile
3DPLfoTrrzlm          2021-11-08 19:10:05   0.25        968930046248    desktop
YmObbQWN0uQ7          2021-11-08 19:10:05   0.12        156703080064    mobile
O1AIi5lV3iMq          2021-11-08 19:10:05   0.03        156703080064    mobile
O7hNpz6qgYrW          2021-11-08 19:10:06   0.55        968930046248    desktop
YKnVsBaeG6W6          2021-11-08 19:10:06   0.42        968930046248    desktop
mHUWNoH54Ow8          2021-11-08 19:10:08   0.18        156703080064    mobile


[RDC.CLICKSTREAM.Visits]
visit_id    timestamp             google_impression_id    lead_id
ssi60p79    2021-11-08 19:10:05
qta2s7fz    2021-11-08 19:10:06   O7hNpz6qgYrW
sm5qwkuu    2021-11-08 19:10:08
jj4m2uuc    2021-11-08 19:10:08   mHUWNoH54Ow8            as3nz9
gmsfeygh    2021-11-08 19:10:09


[RDC.ANLYTICS.Leads]      
lead_id   timestamp               lead_type   revenue_usd
as3nz9    2021-11-08 19:10:08     for_sale    50
w99czu    2021-11-08 19:10:43     for_rent    10
i7yyi2    2021-11-08 19:11:33     for_sale    1850
hksje3    2021-11-08 19:12:00     for_rent    3


#SQL questions:
#1. What are the costs and revenues by campaign for the month of October 2022?


#2. There are numerous insightful questions we could ask about the tables above. Can you describe a few?
  


#Coding Questions:
#1. Return a list that excludes integers below zero and remove duplicates from a list of integers.
list_of_integers = [1,-999,4,-1,4,5,5,9,5,4,3,0,9,9,33,4]
#Use base Python/R only without imports.


#2. Our tables are partitioned by a string 'YYYYMM' format. For example, '202109'.
#Create a function that increments the input string 'YYYYMM' by one month and returns a 'YYYYMM' string
#use base Python/R only without imports





----------------------------------------------
ANSWERS



[context]
#Below we have a header snippet of three tables: Google_ad_impression; Visits; Leads
#Google_ad_impressions: We pay Google to show ads to users interested in real estate.
#Vistis: A subset of people on google click on the ad and visit the realtor.com website. Other visitors can arrive organically or via other marketing channels.
#Leads: A subset of realtor.com visits complete a real estate lead form that earns realtor.com revenue.


[RDC.CLICKSTREAM.Google_ad_impression]
google_impression_id  timestamp             cost_usd    campaign_id     device
VgMyLFvuYj29          2021-11-08 19:10:05   0.08        156703080064    mobile
3DPLfoTrrzlm          2021-11-08 19:10:05   0.25        968930046248    desktop
YmObbQWN0uQ7          2021-11-08 19:10:05   0.12        156703080064    mobile
O1AIi5lV3iMq          2021-11-08 19:10:05   0.03        156703080064    mobile
O7hNpz6qgYrW          2021-11-08 19:10:06   0.55        968930046248    desktop
YKnVsBaeG6W6          2021-11-08 19:10:06   0.42        968930046248    desktop
mHUWNoH54Ow8          2021-11-08 19:10:08   0.18        156703080064    mobile


[RDC.CLICKSTREAM.Visits]
visit_id    timestamp             google_impression_id    lead_id
ssi60p79    2021-11-08 19:10:05
qta2s7fz    2021-11-08 19:10:06   O7hNpz6qgYrW
sm5qwkuu    2021-11-08 19:10:08
jj4m2uuc    2021-11-08 19:10:08   mHUWNoH54Ow8            as3nz9
gmsfeygh    2021-11-08 19:10:09


[RDC.ANLYTICS.Leads]      
lead_id   timestamp               lead_type   revenue_usd
as3nz9    2021-11-08 19:10:08     for_sale    50
w99czu    2021-11-08 19:10:43     for_rent    10
i7yyi2    2021-11-08 19:11:33     for_sale    1850
hksje3    2021-11-08 19:12:00     for_rent    3


#SQL questions:
#1. What are the costs and revenues by campaign for the month of October 2022?


       [Answer]

    SELECT 
    g.campaign_id, 
    SUM(g.cost_usd) AS total_cost,
    COALESCE(SUM(l.revenue_usd), 0) AS total_revenue
FROM 
    RDC_CLICKSTREAM_Google_ad_impression AS g
LEFT JOIN
    RDC_CLICKSTREAM_Visits AS v
ON 
    g.google_impression_id = v.google_impression_id
AND
    DATE(g.timestamp) BETWEEN '2022-10-01' AND '2022-10-31'
LEFT JOIN
    RDC_ANLYTICS_Leads AS l
ON
    v.lead_id = l.lead_id
AND
    DATE(l.timestamp) BETWEEN '2022-10-01' AND '2022-10-31'
GROUP BY
    g.campaign_id;


The COALESCE function is used to handle NULL values that might be present in the revenue_usd field due to the LEFT JOIN operation (which would include rows even if there is no matching lead). 
If a NULL value is found, it gets replaced by zero.


#2. There are numerous insightful questions we could ask about the tables above. Can you describe a few?
#User Conversion Analysis: What is the conversion rate (leads generated from impressions) per campaign_id? This will require linking all three tables and calculating the ratio of the count of leads to the count of impressions for each campaign.

#Device Analysis: What is the distribution of cost and revenue across different device types (mobile, desktop, etc.)?

#High-Performance Time Slots: During which hours of the day do we see the highest revenue generation? This will involve extracting the hour from the timestamp and grouping the revenue by it.

#Lead Type Performance: Which lead types (for_sale, for_rent, etc.) are generating the most revenue, and what's their cost?

#Efficiency of Campaigns: Calculate the return on investment (ROI) for each campaign (total revenue - total cost).

#Path Analysis: For each lead generated, what is the average number of impressions and visits leading up to the lead? This will require understanding the sequence of events leading to a lead conversion.

#Delayed Conversions: How long does it take on average from the first impression to lead conversion for each campaign? You'll need to calculate the time difference between related records in the impressions and leads tables.



Coding questions
1. Return a list that excludes integers below zero and remove duplicates from a list of integers
list_of_integers = [1,-999,4,-1,4,5,5,9,5,4,3,0,9,9,33,4]
use base Python/R only without imports.


   [Answer]
   def deduplicate(list_of_integers):
       output = []
       for i in list_of_integers:
           if i not in output and i != 0:
               output.append(i)
       return output


    [Answer]

set_list = set(list_of_integers)
final_list = [x for x in list(set_list) if x >= 0]


list_of_integers = [1,-999,4,-1,4,5,5,9,5,4,3,0,9,9,33,4]
# Use list comprehension and set to filter out negative numbers and remove duplicates
result = [integer for integer in set(list_of_integers) if integer >= 0]
print(result)


# Use list comprehension and set to filter out negative numbers and remove duplicates
unique_positive_list = list(set([i for i in list_of_integers if i >= 0]))
print(unique_positive_list)


    [Answer]
import pandas as pd
list_of_integers = [1,-999,4,-1,4,5,5,9,5,4,3,0,9,9,33,4]
# create a pandas Series from the list
series = pd.Series(list_of_integers)
# filter out negative numbers
positive_series = series[series >= 0]
# remove duplicates
unique_positive_series = positive_series.drop_duplicates()
# convert back to list
unique_positive_list = unique_positive_series.tolist()
print(unique_positive_list)




2. Our tables are partitioned by a string 'YYYYMM' format. For example, '202109'.
Create a function that increments the input string 'YYYYMM' by one month and returns a 'YYYYMM' string
use base Python/R only without imports


    [Answer]
    def add_one_month(dt):
        if dt[4:6] == '12':
            yr = str(int(dt[0:4]) + 1)
            mo = '01'
        else:
            yr = dt[0:4]
            if int(dt[4:6]) >= 9:
                mo = str(int(dt[4:6]) + 1)
            else:
                mo = '0' + str(int(dt[4:6]) + 1)
        return yr + mo


def add_month(my_string):
    year = int(my_string[0:4])
  month = int(my_string[4:6])
  if month == 12:
    year += 1
    month = 1
  else:
    month += 1
  return str(year) + lpad(month, 2)


  def incrementDate(dateString):
  yr = dateString[:4]
  mth = dateString[4:]
  mth = int(mth) + 1
  if mth>12:
    yr = int(yr) + 1
    mth = '01'
  res = str(yr)+str(mth)

  return res


    [Answer]

    def increment_month(yyyymm):
    year = int(yyyymm[:4])
    month = int(yyyymm[4:])

    if month == 12:
        year += 1
        month = 1
    else:
        month += 1

    return f"{year:04d}{month:02d}"
# Testing
print(increment_month("202109"))  # Output: 202110
print(increment_month("202112"))  # Output: 202201


    [Answer]
    import pandas as pd

def increment_month(yyyymm):
    date = pd.to_datetime(yyyymm, format='%Y%m')
    incremented_date = date + pd.DateOffset(months=1)
    return incremented_date.strftime('%Y%m')

# Testing
print(increment_month("202109"))  # Output: 202110
print(increment_month("202112"))  # Output: 202201
  






