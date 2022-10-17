import pandas as pd
df_read = pd.read_excel(r'C:\Users\USER\Desktop\Students_data.xlsx')
print(df_read)
# --------------------------------------------------------------------
# use to write the file in csv format here we have to mention name
# df_read.to_csv("newstud123.csv")
# --------------------------------------------------------------------
# data1 = pd.read_csv(r"D:\Python Final Practice all imp work\pycharmcode\newstud123.csv")
# print(data)
# --------------------------------------------------------------------
print(df_read.loc[[1,3]])
df_read.fillna(0,inplace = True)
df_read.dropna()

df_read.insert(column="total",value = 100,loc = 1)
print(df_read.loc[[1,3]])
# df_read.rename(columns = {'RollNo':'RNO'},inplace = True)
# print(df_read)

# datahead=df_read.head(2)
# print(datahead)

# data =df_read.tail()
# print(data)

# x = df_read['EC'].max()
# print(x)

# x1 = df_read['EC'].min()
# print(x1)

# x3 = df_read['EC'].sum()
# print(x)

# x4 = df_read['EC'].apply(lambda x : x *2)
# print(x4)

# x5 =x = df_read['EC'].transform(lambda x : x * 3)
# print(x5)

# a =df_read.duplicated()
# print(a)

# a1 =df_read.info()
# print(a1)

# b = df_read.describe()
# print(b)


# -----------------
#Left-join longer columns with shorter ones
# newDataFrame = df1.join([df_shorter2, df_shorter3], how='left')
# print(newDataFrame)
#
#
# newDataFrame = df1.join([df2, rsuffix='_', how='outer')
# print(newDataFrame)
#
#
# newDataFrame = df.combine(df2, numpy.minimum)
# print(newDataFrame)
#
#
# newDataFrame = DataFrame.sort_values(by = "colmun_name", descending = True)
#
# DataFrame.count()
#
#
# DataFrame.where(DataFrame['Age'] < 30)