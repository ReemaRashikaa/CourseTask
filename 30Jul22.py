import pandas as pd
import openpyxl
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# Reading the Excel Files
df1 = pd.read_excel("C:/Users/Administrator/Downloads/AgentLogin.xls", header=2)
df2 = pd.read_excel("C:/Users/Administrator/Downloads/AgentPerformance.xlsx", header=1)

# Creating a Column 'Week' that captures the week details
df2['Week'] = pd.to_datetime(df2['Date']).dt.isocalendar().week

# Finding the Weekly Average Rating on the Agents
WAR = pd.DataFrame(df2[(df2['Total Chats'] > 0)][['Agent Name', 'Average Rating', 'Week']].groupby(['Agent Name', 'Week'])['Average Rating'].mean())
print('\n Weekly Average Rating')
print(WAR)

# Total Working Day for Each Agent
TWD = df2[(df2['Total Chats'] > 0)][['Agent Name','Date']].groupby(['Agent Name'])['Date'].count().to_frame().reset_index()
print('\n Total Working Days')
print(TWD)

# Total queries taken by each agent
TQ = pd.DataFrame(df2[(df2['Total Chats'] > 0)].groupby(['Agent Name'])['Total Chats'].sum())
print('\n Total Queries Taken by the Agent')
print(TQ)

# Total Feedback Received
TF = pd.DataFrame(df2[(df2['Total Chats'] > 0)].groupby(['Agent Name'])['Total Feedback'].sum())
print('\n Total Feedback for Agents')
print(TF)

# Creating a column 'Month' to capture the month number
df2['Month'] = pd.to_datetime(df2['Date']).dt.month

# Creating a Dataframe to store Overall Average Rating of Agents
df3 = (df2[(df2['Total Chats'] > 0)][['Agent Name', 'Average Rating', 'Month']].groupby(['Agent Name'])['Average Rating'].mean()).to_frame().reset_index()

# Performing left join operation on Agent Name
df2 = df2.merge(df3, on='Agent Name', how='left')

# Renaming the columns
df2.rename(columns={'Average Rating_x': 'Daily_Avg', 'Average Rating_y': 'Overall_Avg'}, inplace=True)

# Removing Nan Values and replacing with 0
df2['Overall_Avg'] = df2['Overall_Avg'].fillna(0)

# Agents with Overall Average between 3.5 to 4
OA = pd.DataFrame(df2[df2['Overall_Avg'].between(3.5, 4, inclusive=True)][['Agent Name', 'Overall_Avg']].sort_values(by=['Overall_Avg'], ascending=False).drop_duplicates())
print('\n Agents with Overall Avg between 3.5 to 4')
print(OA)

# Agents with Overall Average less than 3.5
OA1 = pd.DataFrame(df2[(df2['Overall_Avg'] < 3.5)][['Agent Name', 'Overall_Avg']].sort_values(by=['Overall_Avg'], ascending=False).drop_duplicates())
print('\n Agents with Overall Avg less than 3.5')
print(OA1)

# Agents with Overall Average more than 4.5
OA2 = pd.DataFrame(df2[(df2['Overall_Avg'] > 4.5)][['Agent Name', 'Overall_Avg']].sort_values(by=['Overall_Avg'], ascending=False).drop_duplicates())
print('\n Agents with Overall Avg more than 4.5')
print(OA2)

# Count of Feedback received by agents with Overall Average of more than 4.5
OA3 = pd.DataFrame(df2[(df2['Overall_Avg'] > 4.5)].groupby(['Agent Name'])['Total Feedback'].sum())
print('\n No.of Feedbacks received by agents with Overall Avg more than 4.5')
print(OA3)

# Convert Required Columns to Date Time
df2['Date'] = pd.to_datetime(df2['Date'])
df2['Average Response Time'] = pd.to_datetime(df2['Average Response Time'], infer_datetime_format=True)
df2['Average Resolution Time'] = pd.to_datetime(df2['Average Resolution Time'], infer_datetime_format=True)

# Average Weekly Response Time for each agent
WART = pd.DataFrame(pd.to_datetime(df2[(df2['Total Chats'] > 0)][['Agent Name', 'Average Response Time', 'Week']].groupby(['Agent Name', 'Week'])['Average Response Time'].mean()).dt.time)
print("\n Avg. Weekly Response Time for each Agent")
print(WART)

# Average Weekly Resolution Time for Each Agent
WART1 = pd.DataFrame(pd.to_datetime(df2[(df2['Total Chats'] > 0)][['Agent Name', 'Average Resolution Time', 'Week']].groupby(['Agent Name', 'Week'])['Average Resolution Time'].mean()).dt.time)
print("\n Avg. Weekly Resolution Time for each Agent")
print(WART1)

# List of All Agents Name
AN = pd.DataFrame(df2['Agent Name'].drop_duplicates())
print('\n List of Agents')
print(AN)

# Creating New column ' Feedback %'
df2['Feedback %'] = (df2['Total Feedback']*100/df2['Total Chats']).fillna(0)

# Finding the Feedback % for all agents
FB = pd.DataFrame(df2[(df2['Total Feedback'] > 0)][['Agent Name', 'Feedback %']].groupby(['Agent Name'])['Feedback %'].mean())
print('\n Feedback Percentage of Agents')
print(FB)

# Converting the required columns to datetime format and timedelta format
df1['Week'] = pd.to_datetime(df1['Date']).dt.isocalendar().week
df1['Date'] = pd.to_datetime(df1['Date'])
df1['Login Time'] = pd.to_datetime(df1['Login Time'])
df1['Logout Time'] = pd.to_datetime(df1['Logout Time'])
df1['Duration'] = pd.to_timedelta(df1['Duration'])

# Total Hours of Contribution of Agents on Weekly Basis
THC = pd.DataFrame(df1[['Agent', 'Week', 'Duration']].groupby(['Agent', 'Week'])['Duration'].sum())
print('\n Total Hours of Contribution of Agents on Weekly Basis')
print(THC)

# Creating New Column Month
df1['Month'] = pd.to_datetime(df1['Date']).dt.month

# Computing Total Duration
TDn = (df1[['Agent', 'Month', 'Duration']].groupby(['Agent', 'Month'])['Duration'].sum()).to_frame().reset_index()
df1 = df1.merge(TDn, on='Agent', how='left')
df1.drop(['Month_y'], axis=1, inplace=True)
df1.rename(columns={'Duration_x': 'Duration', 'Duration_y': 'Total Duration', 'Month_x': 'Month'}, inplace=True)

# Capturing the date components from Total Duration
td = df1['Total Duration'].dt.components

# Computing the Active Hours Percentage
df2.rename(columns={'Agent Name':'Agent'},inplace=True)
TWD1 = df2[(df2['Total Chats'] > 0)][['Agent','Date']].groupby(['Agent'])['Date'].count().to_frame().reset_index()
df1 = pd.merge(TWD1,df1,on='Agent',how='inner')
df1.rename(columns={'Date_x':'TWD','Date_y':'Date'},inplace=True)
df1['ActiveHours'] = ((td.days*24) + td.hours + (td.minutes/60) + (td.seconds/3600))

""" Considering 9 hours of work a day """
df1['TWH'] = ((df1['TWD'])*9)
df1['ActiveHours %'] = (((df1['ActiveHours'])*100)/df1['TWH'])
AHP = pd.DataFrame(df1.groupby(['Agent'],sort=True)['ActiveHours %'].mean())
print('\n Active Hour Percentage of Agents')
print(AHP)

