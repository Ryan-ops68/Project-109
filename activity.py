import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv("Data.csv")
writing_list = df["writing score"].to_list()
writing_mean = statistics.mean(writing_list)
writing_median = statistics.median(writing_list)
writing_mode = statistics.mode(writing_list)
print("Mean, Median, Mode of Writing Scores is {}, {}, {} Respectively".format(writing_mean, writing_median, writing_mode))
writing_std_deviation = statistics.stdev(writing_list)
writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)
writing_list_of_data_within_1_std_deviation = [result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]
print("{}% of data for writing scores lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing scores lies within 2 standard deviation".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing scores lies within 3 standard deviation".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_list)))
fig = ff.create_distplot([writing_list], ["Writing Scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [writing_mean, writing_mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [writing_first_std_deviation_start, writing_first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [writing_first_std_deviation_end, writing_first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [writing_second_std_deviation_start, writing_second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [writing_second_std_deviation_end, writing_second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))

fig.show()