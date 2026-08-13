import pandas as pd

data = {
    "Tid": [1,2,3,4,5,6,7,8,9,10],
    "Refund": ["Yes","No","No","Yes","No","No","Yes","No","No","No"],
    "Marital Status": ["Single","Married","Single","Married","Divorced",
                       "Married","Divorced","Single","Married","Single"],
    "Taxable Income": ["125K","100K","70K","120K","95K","60K","220K","85K","75K","90K"],
    "Cheat": ["No","No","No","No","Yes","No","No","Yes","No","Yes"],
}
df = pd.DataFrame(data)
print(df)
print(df.iloc[[0, 4, 7, 8]])
print(df.iloc[3:8])
print(df.iloc[4:9, 2:5])
print(df.loc[1:3])
dp=pd.read_csv("/Users/m0ta_b1lla/work/thapar_assigments/cogni/Assigment 3/employees.csv")
print(dp.head())
print(dp.shape)
dp.info()
print(dp.describe())
print(" avg salary:", dp["Salary"].mean(), "| total bonus:", dp["Bonus"].sum(),"| min age:", dp["Age"].min(), "| max rating:", dp["Rating"].max())
print(dp.sort_values("Salary", ascending=False))
print(dp.isnull().sum())
dp = dp.rename(columns={"Employee_ID":"ID"})
print(dp.head())
print(dp[(dp["Years_of_Experience"]>5) & (dp["Department"]=="IT")][["ID","Name","Department","Years_of_Experience"]])
dp["Tax"] = dp["Salary"]*0.10
print(dp)
dp["Performance_Category"] = pd.cut(dp["Rating"], bins=[0,4.0,4.5,5.0],labels=["Average","Good","Excellent"], right=False)
    
dp.to_csv("modified_employees.csv", index=False)