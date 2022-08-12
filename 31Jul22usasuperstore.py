import pandas as pd
import sqlalchemy as db


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Creating MySQL connection
engine = db.create_engine("mysql+pymysql://root:User21@localhost:3306/ss_usa?", pool_pre_ping=True, pool_size=5, pool_recycle=3600)
c = engine.connect()

# Reading the Excel Files
t1 = pd.ExcelFile("Superstore_USA.xlsx")

# Creating Dataframes and Parsing it to prepare for load
df1 = t1.parse(sheet_name="Orders")
df2 = t1.parse(sheet_name="Returns")
df3 = t1.parse(sheet_name="Users")

# Loading the Excel Files as Tables in Dress_Data Database
tab1 = df1.to_sql("orders", c, if_exists="replace")
tab2 = df2.to_sql("returns", c, if_exists="replace")
tab3 = df3.to_sql("users", c, if_exists="replace")

# Merge Orders and Returns in Pandas
df4 = pd.merge(df1, df2, how='left', on='Order ID')

# Total Returns with Product Name
Ret = df4[(df4['Status'] == 'Returned')][['Order ID', 'Product Name']]
print('\n Returns with Product Details : ', Ret, '\n Total No. of returns : ', Ret['Order ID'].count())

# Merge Orders and Returns in SQL

q0 = '''SELECT * FROM `orders` o LEFT JOIN `returns` r ON o.`Order ID` = r.`Order ID`'''
q0s = pd.read_sql_query(q0, engine)
print("Merged Dataset : ", q0s)

# No.of unique customers
print('\n No. of unique customers : ', df4['Customer Name'].nunique())

# No.of regions where we are selling products
print('\n No.of regions :', df4['Region'].nunique())

# Regions and Respective Managers
print('\n Regions and Respective Managers :', df3)

# No. of Different Shipment Modes and percentage usability of them
print('\n No.of Different Shipment Modes : ', df4['Ship Mode'].value_counts())
print('\n Percentage Usability of Shipment Modes : ',
      (df4['Ship Mode'].value_counts()) * 100 / (df4['Ship Mode'].count()))

# Difference between order date and Shipment Date
df4['Order_to_ship_time'] = df4['Ship Date'] - df4['Order Date']
print('\n Order to Shipment Time : ', df4['Order_to_ship_time'])

# Order ID's having Order to Shipment time more than 10 Days
print('\n Order IDs having Order to Shipment time of more than 10 days : ', df4[(df4['Order_to_ship_time'] > '10 days')][['Order ID', 'Order_to_ship_time']])

# Order ID's and Respective Managers having Order to Shipment time more than 15 Days
df4['Manager'] = pd.merge(df1, df3, on='Region', how='left')['Manager']
print('\n Order IDs and Respective Managers having Order to Shipment time of more than 15 days :', df4[(df4['Order_to_ship_time'] > '15 days')][['Order ID', 'Manager']])

# No.of Order to Shipment time more than 15 Days with Status as rejected
df5 = df4[(df4['Order_to_ship_time'] > '15 days')][['Order ID', 'Manager', 'Status']]
print('\n No. of orders with more than 15 days shipment time that were rejected :', df5[(df5['Status'] == 'Rejected')]['Order ID'].count())

# Most Profitable Region
RP = pd.DataFrame(df4.groupby(['Region'])[['Profit']].sum()).reset_index()
print('\n Most Profitable Region : ', RP.nlargest(1, 'Profit'))

# City which is given most discount
MD = df4[['City', 'Discount']].groupby(['City'])['Discount'].sum().to_frame().reset_index()
print('\n City which is given most discount : ', MD.nlargest(1, 'Discount'))

# List of unique Postal Code
print('\n List of unique postal Code : ', df4['Postal Code'].drop_duplicates())

# Most Profitable Customer Segment
PCS = df4.groupby(['Customer Segment'])['Profit'].sum().to_frame().reset_index()
print('\n Most Profitable Customer Segment : ', PCS.nlargest(1, 'Profit'))

# 10th Loss Making Product
PP = df4.groupby(['Product Name'])['Profit'].sum().to_frame().reset_index().sort_values('Profit', ascending=True)
PP['Rank'] = PP['Profit'].rank(ascending=True)
print('\n 10th Most Loss Making product: ', PP[PP['Rank'] == 10])

# Top 10 products with The Highest Margin
PM = df4.groupby(['Product Name'])['Product Base Margin'].sum().to_frame().reset_index().sort_values('Product Base Margin', ascending=False)
print('\n Top 10 products with highest Margin: ', PM.head(10))
