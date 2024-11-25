import pandas

# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data)
#     for row in data:
#         temperature = int(row[1])
#         temperatures.append(temperature)
#     print(temperatures)


# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])
#
# # temp_list = data["temp"].to_list()
# # #print(len(temp_list))
# # # av_temp = int(sum(temp_list) / len(temp_list))
# # # print(av_temp)
# #
# # print(data["temp"].max())
#
# #print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)

# data_dict = {
#     "students": ["dave", "steve", "dan"],
#     "scores": [10, 20, 30]
# }
# some_data = pandas.DataFrame(data_dict)
# some_data.to_csv("someCsv.data")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# to create own data frame easiest to start with a dictionary

data_dict = {
    "Fur Colour": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")

# print(grey)
# print(len(red))
# print(len(black))