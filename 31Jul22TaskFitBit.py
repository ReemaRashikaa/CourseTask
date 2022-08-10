import pandas as pd
import sqlalchemy as db
import pymongo
import json
from sqlalchemy import text
import sqlparse

pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# Reading the CSV file using Pandas
df1 = pd.read_csv("C:/Users/Administrator/Downloads/task_/FitBit data.csv")
print('\n FitBit Data')
print(df1)

# Creating MySQL connection
engine = db.create_engine("mysql+pymysql://root:User21@localhost:3306/fitbit?", pool_pre_ping=True, pool_size=5,
                          pool_recycle=3600)
c = engine.connect()

# Reading the Excel Files
t1 = pd.read_csv("FitBit data.csv")

# Loading the Excel Files as Tables in SQL
d = df1.to_sql("tracker", c, if_exists="append")

# Converting FitBit data to json format
df1.to_json("Fitbit.json")

# Creating MongoDB Connection
client = pymongo.MongoClient("mongodb+srv://reema:Kathiran21@cluster0.gh4hl.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# Creating a database and table in Mongo DB
database = client['FB']
collection = database["FB_DB"]

# Loading the json file in MongoDB
with open('Fitbit.json') as file:
    file1 = json.load(file)
collection.insert_one(file1)

# Converting ActivityDate to Date Time format using Pandas
df1['ActivityDate'] = pd.to_datetime(df1['ActivityDate'])
print("\n Data Type of ActivityDate", df1['ActivityDate'].dtype)
# Converting ActivityDate toDate format in MySQL

query = """
SET SQL_SAFE_UPDATES = 0;
update tracker set ActivityDate = str_to_date(ActivityDate, '%m/%d/%Y');
Alter table tracker modify column ActivityDate date ;
Select ActivityDate from tracker;
"""
s = sqlparse.split(sqlparse.format(query, strip_comments=True))
for q in s:
    result = c.execute(text(q))
print('Converted Activity Date to date type : ', result)

# Find out the number of unique ID's in this dataset using Pandas
a = df1['Id'].nunique()
print("\n No. of Unique ID in the dataset : ", a)
# Find out the number of unique ID's in this dataset using MySQL
q1 = '''select count(distinct id) from tracker'''
q1s = pd.read_sql_query(q1, engine)
print("\n No. of Unique ID in dataset : ", q1s)

# Most Active ID in the whole Dataset using Pandas
b = df1.groupby(['Id'])['Calories'].sum().idxmax()
print("\n Most Active ID : ", b)
# Most Active ID in the whole Dataset using MySQL
q2 = '''select Id , sum(calories) tot_sum from tracker group by ID order by tot_sum desc limit 1'''
q2s = pd.read_sql_query(q2, engine)
print("\n Most Active ID : ", q2s)

# No.of ID's who have not logged in their activities using Pandas
e = df1.groupby('Id')['LoggedActivitiesDistance'].sum().value_counts()[0]
print('\n No. of IDs who have not logged in their activities : ', e)

# No.of ID's who have not logged in their activities using MySQL
q3 = '''select count(id) from (select id, sum(LoggedActivitiesDistance) log_tot from tracker group by 1 having 
log_tot = 0.000000000000000) a '''
q3s = pd.read_sql_query(q3, engine)
print('\n No. of IDs who have not logged in their activities : ', q3s)

# Laziest Person ID using Pandas
f = df1.groupby(['Id'])['Calories'].sum().idxmin()
print("\n Most Lazy ID : ", f)
# Laziest Person ID using MySQL
q4 = '''select Id , sum(calories) tot_sum from tracker group by ID order by tot_sum  limit 1'''
q4s = pd.read_sql_query(q4, engine)
print("\n Most Active ID : ", q4s)

# Calories to be Burned per day = 2200
# No.of healthy persons in our dataset using Pandas
g = df1.groupby('Id')['Calories'].mean().apply(lambda x: x >= 2200).value_counts()[True]
print('\n No.of healthy persons in the dataset : ', g)

# No.of healthy persons in our dataset using MySQL
q5 = '''select count(id) from (select Id , avg(calories) cal_avg from tracker group by 1 having cal_avg >=2200) a'''
q5s = pd.read_sql_query(q5, engine)
print('\n No.of healthy persons in the dataset : ', q5s)

# No. of persons who are irregular in activities using Pandas
h = df1[df1['TotalSteps'] == 0]['Id'].drop_duplicates().count()
print('\n No. of people who are irregular in activities : ', h)

# No. of persons who are irregular in activities using MySQL
q6 = '''select count(distinct(id)) from tracker where TotalSteps=0'''
q6s = pd.read_sql_query(q6, engine)
print('\n No. of people who are irregular in activities : ', q6s)

# Third Most Active Person ID using Pandas
i = df1.groupby(['Id'])['Calories'].sum().sort_values(ascending=False).reset_index().iloc[2]['Id']
print('\n Third Most Active Person ID : ', i)

# Third Most Active Person ID using MySQL
q7 = '''select Id , sum(calories) tot_sum from tracker group by ID order by tot_sum desc limit 2,1'''
q7s = pd.read_sql_query(q7, engine)
print('\n Third Most Active Person ID : ', q7s)

# Fifth Most Laziest Person ID using Pandas
j = df1.groupby(['Id'])['Calories'].sum().sort_values(ascending=True).reset_index().iloc[4]['Id']
print('\n Fifth Most Laziest Person ID : ', j)

# Fifth Most Laziest Person ID using MySQL
q8 = '''select Id , sum(calories) tot_sum from tracker group by ID order by tot_sum  limit 4,1'''
q8s = pd.read_sql_query(q8, engine)
print('\n Fifth Most Laziest Person ID : ', q8s)

# Total Calories burnt by a person using Pandas
k = df1.groupby(['Id'])['Calories'].sum()

# Total Calories burnt by a person using MySQL
'''select Id , sum(calories) tot_cal from tracker group by ID order by tot_cal'''
