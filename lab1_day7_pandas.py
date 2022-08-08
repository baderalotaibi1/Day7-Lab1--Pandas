import pandas as pd
lst=["bader","ali","anwar"]
ds=pd.Series(lst,index=[1,2,3])
print("Q1: Create a Series with indexes = 1, 2, 3 and has three names.\n",ds,"\n")
ds.index=[11,12,13]
print("Q2: Change indexes to 11, 12, 13.\n",ds,"\n")
print("Q3: Retrieve First and second elements.\n",ds[0:2],"\n")
add=pd.Series(["bader"])
ds=ds.append(add)
print("Q4:Add duplicate elements\n",ds,"\n")

print("Q4:then remove the duplication\n",ds.drop_duplicates(),"\n")
ds_frame={'ID':[1,2,3,4],
           'Name':["bader","ahmed","ali","salem"],
           'Salary':[1000,2000,3000,4000] }
ds_frame=pd.DataFrame(ds_frame,columns=["ID","Name","Salary"])
print("Q5: Create a Students DataFrame has three columns (ID, Name)\n",ds_frame,"\n")
data=pd.read_csv('C:/Users/bader/OneDrive/gitlesson/Lectures/Day#7/educ_figdp_1_Data.csv')
print("Q6: Read educ_figdp_1_Data.csv file\n",data.head())
print("Q7: What is the difference between loc and slicing?","\nloc:includes the last element of the range passed in it,\nSlicing:does not include the last element of the range passed in it")




