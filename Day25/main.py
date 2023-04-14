# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparatures = []
#     for row in data:
#         if row[1] != "temp":
#             temparatures.append(int(row[1]))
#     print(temparatures)

#use pandas simply
import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)
# print(data["temp"])

#convert data to dictionary. 
# data_dict = data.to_dict()
# print(data_dict)

#to get series into list
temp_list = data["temp"].to_list()
print(temp_list)

# print(sum(temp_list)/len(temp_list))
#or
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())

#get data in columns.
# print(data["condition"])
#or
# print(data.condition)

#get data in row
# print(data[data.Day == "Monday"])
#to get row data which have max temp.
# print(data[data.temp == data.temp.max()])

#to get particular row column.
#temp of row
# monday = data[data.Day == "Monday"]
# print(monday.condition)

#temp im faranite
# monday_temp = int(monday.temp[0])
# monday_temp_f = monday_temp*9/5 + 32
# print(monday_temp_f)


#Create a dataframe from scratch.
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("new_data.csv") #creating new csv file.