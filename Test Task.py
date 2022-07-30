import pandas as pd
import sqlalchemy as db
import pymongo
import json

# Creating MySQL connection
engine = db.create_engine("mysql+pymysql://root:User21@localhost:3306/Dress_Data?charset=utf8mb4", pool_pre_ping=True, pool_size=5, pool_recycle=3600)
c = engine.connect()

# Reading the Excel Files
t1 = pd.ExcelFile("D:\\task\\AttributeDataSet.xlsx")
t2 = pd.ExcelFile("D:\\task\\DressSales.xlsx")

# Creating Dataframes and Parsing it to prepare for load
df1 = t1.parse(sheet_name="Sheet1")
df2 = t2.parse(sheet_name="Sheet1")

# Loading the Excel Files as Tables in Dress_Data Database
d = df1.to_sql("attribute_ds", c, if_exists="append")
e = df2.to_sql("dress_sales", c, if_exists="append")

# Left Join Operation using MySQL
q4 = '''Select * from attribute_ds as a left join dress_sales ON a.Dress_ID = dress_sales.Dress_ID;'''
lj = pd.read_sql_query(q4, engine)
print(lj)

# No. of unique dress based on Dress_ID
q3 = '''select count(distinct Dress_ID) as Unique_DressID_Count from attribute_ds'''
ud = pd.read_sql_query(q3, engine)
print(ud)

# No. of dress with 0 Recommendations
q0 = '''select count(*) as Count_of_Zero_Recommendation from attribute_ds where Recommendation=0'''
zr = pd.read_sql_query(q0, engine)
print(zr)

# Total Dress Sales based on Dress ID
q1 = '''SELECT DISTINCT Dress_ID,SUM(COALESCE(`29/8/2013`, 0) + COALESCE(`31/8/2013`, 0) + COALESCE(`2013-02-09 00:00:00`, 0) + COALESCE(`2013-04-09 00:00:00`, 0) + COALESCE(`2013-06-09 00:00:00`, 0) + COALESCE(`2013-08-09 00:00:00`, 0) + COALESCE(`2013-10-09 00:00:00`, 0) + COALESCE(`2013-12-09 00:00:00`, 0) + COALESCE(`14/9/2013`, 0) + COALESCE(`16/9/2013`, 0) + COALESCE(`18/9/2013`, 0) + COALESCE(`20/9/2013`, 0) + COALESCE(`22/9/2013`, 0) + COALESCE(`24/9/2013`, 0) + COALESCE(`26/9/2013`, 0) + COALESCE(`28/9/2013`, 0) + COALESCE(`30/9/2013`, 0) + COALESCE(`2013-02-10 00:00:00`, 0) + COALESCE(`2013-04-10 00:00:00`, 0) + COALESCE(`2013-06-10 00:00:00`, 0) + COALESCE(`2010-08-10 00:00:00`, 0) + COALESCE(`2013-10-10 00:00:00`, 0) + COALESCE(`2013-12-10 00:00:00`, 0)) AS Total_Sales FROM dress_sales AS s GROUP BY s.Dress_ID Order by Total_Sales desc;'''
tds = pd.read_sql_query(q1, engine)
print(tds)

# Third most Selling Dress based on Dress_ID
q2 = '''SELECT DISTINCT Dress_ID,SUM(COALESCE(`29/8/2013`, 0) + COALESCE(`31/8/2013`, 0) + COALESCE(`2013-02-09 00:00:00`, 0) + COALESCE(`2013-04-09 00:00:00`, 0) + COALESCE(`2013-06-09 00:00:00`, 0) + COALESCE(`2013-08-09 00:00:00`, 0) + COALESCE(`2013-10-09 00:00:00`, 0) + COALESCE(`2013-12-09 00:00:00`, 0) + COALESCE(`14/9/2013`, 0) + COALESCE(`16/9/2013`, 0) + COALESCE(`18/9/2013`, 0) + COALESCE(`20/9/2013`, 0) + COALESCE(`22/9/2013`, 0) + COALESCE(`24/9/2013`, 0) + COALESCE(`26/9/2013`, 0) + COALESCE(`28/9/2013`, 0) + COALESCE(`30/9/2013`, 0) + COALESCE(`2013-02-10 00:00:00`, 0) + COALESCE(`2013-04-10 00:00:00`, 0) + COALESCE(`2013-06-10 00:00:00`, 0) + COALESCE(`2010-08-10 00:00:00`, 0) + COALESCE(`2013-10-10 00:00:00`, 0) + COALESCE(`2013-12-10 00:00:00`, 0)) AS Total_Sales FROM dress_sales AS s Group by s.Dress_ID ORDER BY Total_Sales desc limit 2,1'''
Third_hsd = pd.read_sql_query(q2, engine)
print("Third Highest Selling Dress")
print(Third_hsd)

# Converting Attribute DS to json format
df1.to_json("AttributeDS.json")

# Creating MongoDB Connection
client = pymongo.MongoClient("mongodb+srv://reema:Kathiran21@cluster0.gh4hl.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# Creating a database and table in Mongo DB
database = client['Dress_Data']
collection = database["Attribute_DS"]

# Loading the json file in MongoDB
with open('AttributeDS.json') as file:
    file1 = json.load(file)
collection.insert_one(file1)

# Printing the records found in the uploaded Database in MongoDB
record = collection.find()
for i in record:
    print("Find the records uploaded in MongoDB")
    print(i)
    