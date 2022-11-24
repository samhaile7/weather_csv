# # DIFFERENT WAYS OF READING A CSV/EXCEL FILE
#
# # USING BUILT IN READLINES
# # with open('weather_data.csv') as data_file:
# #     data_list = weather_data_file.readlines()
#
# # USING CSV MODULE
# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# # USING PANDAS
import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# #data_dict = data.to_dict()
# #print(data_dict)
# #print(type(data["temp"]))
# # # The type above is series object or column
# #
# #
# #temp_list = data["temp"].to_list()
# #print(temp_list)
# #
# # average_temp = sum(temp_list)/len(temp_list)
# # print(average_temp)
#
# # mean_temp = data["temp"].mean()
# # print(mean_temp)
# # max_temp = data["temp"].max()
# # print(max_temp, 'fdge')
#
# print(data[data.temp == data.temp.max()])
# # print(data)
#
# monday_row = data[data.day == "Monday"]
# print(monday_row)
# print(int(monday_row.temp))

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]
COLORS = ["Gray", "Cinnamon", "Black"]
count_list = []
data_dict = {"Fur color": COLORS, "Count": count_list}
for color in COLORS:
    all_rows = data[data["Primary Fur Color"] == color]

    num_rows = len(all_rows.index)
    count_list.append(num_rows)
    print(num_rows)

final_dataframe = pandas.DataFrame.from_dict(data_dict)
print(final_dataframe)
final_dataframe.to_csv('./final.csv')