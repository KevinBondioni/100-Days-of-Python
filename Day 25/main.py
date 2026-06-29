import pandas

data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260620.csv")

gray_squirrel_counts=len(data[data.Primary_Fur_Color=="Gray"])
cinnamon_squirrel_counts=len(data[data.Primary_Fur_Color=="Cinnamon"])
black_squirrel_counts=len(data[data.Primary_Fur_Color=="Black"])

new_dict={
    "fur color":["grey","cinnamon","black"],
    "count":[gray_squirrel_counts,cinnamon_squirrel_counts,black_squirrel_counts]
}

new_table=pandas.DataFrame(new_dict)
new_table.to_csv("color_count.csv")