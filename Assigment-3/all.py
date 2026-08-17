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
print("Q2")
print(df.iloc[[0, 4, 7, 8]])
print("Q3  1")

print(df.iloc[3:8]) #Q3 1)
print("Q3  2")

print(df.iloc[4:9, 2:5]) #3 2)
print("Q3  3")

print(df.loc[1:3]) #3 3)
print("Q6")

dp=pd.read_csv("/Users/m0ta_b1lla/work/thapar_assigments/cogni/Assigment 3/employees.csv") #Q6
print(dp.head())
print("a")

print(dp.shape)
print("b")

dp.info()
print("c")

print(dp.describe())
print("e")

print(" avg salary:", dp["Salary"].mean(), "| total bonus:", dp["Bonus"].sum(),"| min age:", dp["Age"].min(), "| max rating:", dp["Rating"].max())
print("f")

print(dp.sort_values("Salary", ascending=False))
print("g")

dp["Performance_Category"] = pd.cut(dp["Rating"], bins=[0,4.0,4.5,5.0],labels=["Average","Good","Excellent"], right=False)

print("h")

print(dp.isnull().sum())
print("i")

dp = dp.rename(columns={"Employee_ID":"ID"})
print(dp.head())
print("j")

print(dp[(dp["Years_of_Experience"]>5) & (dp["Department"]=="IT")][["ID","Name","Department","Years_of_Experience"]])
print("k")

dp["Tax"] = dp["Salary"]*0.10
print(dp)
dp["Performance_Category"] = pd.cut(dp["Rating"], bins=[0,4.0,4.5,5.0],labels=["Average","Good","Excellent"], right=False)
print("l")

dp.to_csv("modified_employees.csv", index=False)