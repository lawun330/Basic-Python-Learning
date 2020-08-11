import numpy as np 
import pandas as pd 

#creating a series from list
mylist=['m','h','n']
print(pd.Series(data=mylist))
print('\n')

#changing or assigning labels
labels =['bad', 'good', 'unknown']
print(pd.Series(data=mylist,index=labels))
print('\n')

#creating a series from np array
array=np.array([2,4,6])
print(pd.Series(array))
print('\n')

#from dictionary
Dict={'love':'spiritual','business':'creative'}
print(pd.Series(Dict)) #indexes are as same as dictionary's indexes
print('\n')

#####################

#operations on index
se1=pd.Series([1,2,3,4],index=['USA','UK','Russia','NK'])
se2=pd.Series([4,0,2,1],index=['USA','Myanmar','Russia','SK'])

print(se1,'\n',se2,'\n')
print(se1+se2) #values under the same labels can be added #opposite shows 'NaN'
print(se1['NK']) #indexing is like list


#####################

#building a data frame
np.random.seed(101) #define a seed(some_number) so that whenever some_number is called from seed, the same output will be achieved
df=pd.DataFrame(np.random.randn(4,5),index='a b c d'.split(),columns=['v','w','x','y','z'])
print(df)


#selecting columns
print(df[['x','y']]) #pass one parameter only #double brackets when a list pass in
print(type(df['w'])) #type should be series.Series under DataFrame

df['total']=df['v']+df['w']+df['x']+df['y']+df['z']
print(df,'\n')

#selecting rows
print(df.loc['a'])
print(df.iloc[0])  #by index
print('\n')

#selecting element
print('a,y has',df.loc['a','y'])
print('\n')

print(df.drop('d',axis=0)) #hide any column or row but not permanent

df.drop('total',axis=1,inplace=True)#delete row or column permanently
print(df)

####################

#conditions
print(df>0) #return booleans
print(df[df>0]) #return with numbers
print('\n\nonly rows allowed for y>0')
print(df[df['y']>0]) #returns 'y' column's non-zeros rows , define this as the whole row number
print(df[df['y']>0][['x','z']]) #in original Frame, y column has rows=2 when y>0, the frame rows=2 and now is choosing row=2,column under 'x' and 'z'
print(  df[ (df['v']>1) & (df['w']<0) ]  ) #rows under 'v' that has element value>1 and rows under 'w' that has element value <0
#return empty since the two conditions doesn't match in any condition
print('\n\n')

#reset index
print(df.reset_index()) 

#set or changes index
df['countries']=['US','UK','Ukarine','Urine'] #insert a new column
df.set_index('countries',inplace=True) #without inplace is temporary change
print(df,'\n')

#####################

#index hierarchy
outside	='A A B B'.split()
inside 	='1 2 1 2'.split()
hier_index = list(zip(outside,inside)) #match two lists
print(hier_index)

hier_index = pd.MultiIndex.from_tuples(hier_index) #make it index
print(hier_index)

df.set_index(hier_index,inplace=True)
print(df,'\n')

###################

#name the index
print('named')
df.index.names= ['Class','room'] 
print(df,'\n')

##################

#indexing

print(df.loc['A'].loc['1'] , '\n') #values of A,1

print(df.xs('A')) #values of A,all
print(df.xs(['A','1'])) #another way of values of A,1

#search 'this' under name >> level='this_name'
print(df.xs('1',level='room'))  #values of all,1

##################

#dealing with missing datas

df = df[df>0]
print(df)
print(df.isnull()) # check null values, opposite to print(df>0)
print(df.fillna(axis=1,value='FUCK')) #replace NaN values
print(df.dropna(axis=1)) #drop NaN values
print(df.dropna(axis=0,thresh=4)) #drop NaN values for no of non-Nans = thresh
print('\n')

dfw = df['w'].fillna(value=df['w'].mean())
print('w nan is filled with mean\n',dfw)
print('\n')

##################

#grouping

data = 	{
		'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
		'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
		'Sales':[200,120,340,124,243,350]
		}

df=pd.DataFrame(data)
print(df)
comp_gp = df.groupby("Company")

print(comp_gp.describe().transpose()) 
#mean()
#min()
#max()
#std()
#count() - returns the repeatation, count of the same unit 

#extracting a variable
fb = comp_gp.describe().transpose()['FB']
print(fb)
print('\n')
#################

#dataFrames merge, join, concatenation

#concatenation
df1= pd.DataFrame(
	{
	'A':'A0 A1 A2'.split(),
	'B':'B0 B1 B2'.split(),
	'C':'C0 C1 C2'.split()
	},index=[0,1,2])
df2= pd.DataFrame(
	{
	'A':'A3 A4 A5'.split(),
	'B':'B3 B4 B5'.split(),
	'C':'C3 C4 C5'.split()
	}, index=[3,4,5])
df3= pd.DataFrame(
	{
	'A':'A6 A7 A8'.split(),
	'B':'B6 B7 B8'.split(),
	'C':'C6 C7 C8'.split()
	},index=[6,7,8])

df = pd.concat([df1,df2,df3],axis=1)  #axis 0 concate rows when 1 concates columns, index matters 
print(df)

#merging
df1= pd.DataFrame(
	{
	'A':'A0 A1 A2'.split(),
	'B':'B0 B1 B2'.split(),
	'C':'C0 C1 C2'.split()
	},index=[0,1,2])
df2= pd.DataFrame(
	{
	'C':'C0 C1 C2'.split(),
	'D':'D0 D1 D2'.split(),
	'E':'E0 E1 E2'.split()
	}, index=[0,1,2])

#to be merged, there has to be common
df = pd.merge(df1,df2,how='inner',on='C')
print(df)
#merge(df1,df2,on=['key1','key2'])
#merge(df1,df2,how='outer',on=['key1','key2'])
#merge(df1,df2,how='right',on=['key1','key2'])
#merge(df1,df2,how='left',on=['key1','key2'])
#more complicated methods of merging

left = pd.DataFrame(
	{
	'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
    },index=['K0', 'K1', 'K2']) 

right = pd.DataFrame(
	{
	'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
    },index=['K0', 'K2', 'K3'])

print(left.join(right)) #how=inner gives no nan rows #outer gives all nans rows
#no how parameter gives no nan rows in left, right rows are adjusted to left
print('\n')
###################

#operations

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head()) #get the first n rows (no of rows)

print('unique af',df['col2'].unique())  #return the unique elements of array
print('index',df['col2'].nunique()) #return the indexes of unique elements of array
print('counts are-\n',df['col2'].value_counts()) #return the repeatations of numbers

#indexing or selecting
print ( df[(df['col1']>2) & (df['col2']==444)]  )
#########################
#applying function
#.apply(func)
def times2(x):
	return x*2

df['col1*2'] = df['col1'].apply(times2)
print(df)

print('col3 has strings their lengths are-')
print(df['col3'].apply(len))
#.sum() adds every thing under column

#########################

#deleting column value
print('we don\'t need them we delete')
del df['col3']
print(df)

#########################

#Getting index and column
#df.index  - for index
#df.columns- for column

#########################

#Sorting
df.sort_values(by='col2',ascending=True,inplace=True) #False for descending
print('sorted df')
print(df,'\n')

#########################

#pivot_table or reshaping
data = {'A':['foo','foo','foo','bar','bar','bar'],
     	'B':['one','one','two','two','one','one'],
       	'C':['x','y','x','y','x','y'],
       	'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
print('\nchanged\n')
df = df.pivot_table(values='D',index=['A','B'],columns=['C'])
print(df)

#######################

#data read, inputs, outputs

# df = pd.read_csv('file.csv') #read csv file
# df.to_csv('example1',index=False) #write csv file
# df = pd.read_excel('file.xlsx',sheetname='Sheet1') #read excel file
# df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1') #write excel file

#read html datas 
# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
