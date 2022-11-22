# DIFFERENT WAYS OF READING A CSV/EXCEL FILE

# USING BUILT IN READLINES
# with open('weather_data.csv') as data_file:
#     data_list = weather_data_file.readlines()

# USING CSV MODULE
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# USING PANDAS
import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
# #print(data_dict)
# print(type(data["temp"]))
# # The type above is series object or column
#
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
#
# mean_temp = data["temp"].mean()
# print(mean_temp)
max_temp = data["temp"].max()
# print(max_temp)
#
# print(data)

mon_temp_row = data[data.day == 'Monday']
print(mon_temp_row)
mon_temp = mon_temp_row['temp']
print((mon_temp * 1.8) + 32 , "F")