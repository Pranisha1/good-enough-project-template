# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:38:29 2023

@author: Pokhr002
"""
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime

def funct(pp):
    """
    This script read all the flow components from .tss files and plot them as figures.
    Frist all the .tss files are read and stored in seperate DataFrame in which the first column is a Datetime and second is the value.
    Now using date time as index the data is combined into monthly avaerages and plotted.

    Also make the comment clear and asthetically pleasing

    """
    return

help(funct)

start_year = "1991"
start_date = "01/01/" + start_year
date_1 = datetime.datetime.strptime(start_date, "%m/%d/%Y")
data_dir = "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results"

# Get list of all .tss files in the directory
tss_files = [f for f in os.listdir(data_dir) if f.endswith(".tss")]

list260 = []
list270 = []
list280 = []

print(tss_files)

for file in tss_files:
    path = os.path.join(data_dir, file)
    # print(path)
    value1 = []
    value2 = []
    value3 = []
    days = []

    with open(path, "r") as f:
        for line_number, line in enumerate(f, 1):
            if line_number > 6:
                data = line.split()
                x = int(data[0])
                y1 = float(data[1])
                y2 = float(data[2])
                y3 = float(data[3])
                value1.append(round(y1, 0))
                value2.append(round(y2, 0))
                value3.append(round(y3, 0))
                days.append(
                    date_1 + datetime.timedelta(days=int(x))
                )  # check the dates, might be wrong

        df_260 = pd.DataFrame(value1, columns=["Discharge at 260"])
        df_270 = pd.DataFrame(value2, columns=["Discharge at 270"])
        df_280 = pd.DataFrame(value3, columns=["Discharge at 280"])
        dt_time = pd.DataFrame(days, columns=["Date"])
        # dt_time['Date'] = pd.to_datetime(dt_time['Date'])
        df_stn260 = pd.concat([dt_time, df_260], axis=1)
        df_stn270 = pd.concat([dt_time, df_270], axis=1)
        df_stn280 = pd.concat([dt_time, df_280], axis=1)
        list260.append(df_stn260)
        list270.append(df_stn270)
        list280.append(df_stn280)

### SETI
# combining the dataframes in the list to one dataframe with multiple columns
Seti = pd.concat([df.set_index(df.columns[0]) for df in list260], axis=1).reset_index()
Seti.columns = ["Date", "BtoDTS", "GtotDTS", "QallDTS", "RtotDTS", "StotDTS"]
# convert the 'date' column to a datetime object
Seti["Date"] = pd.to_datetime(Seti["Date"])
# set the 'date' column as the index
Seti.set_index("Date", inplace=True)
# for a sub years
df_sub260 = Seti.loc["1991":"2022"]
# Group the data by the month and calculate the mean for each month
Monthly_average_260 = df_sub260.groupby(df_sub260.index.month).mean()
Monthly_average_260.reset_index(inplace=True)

### BHERI
# combining the dataframes in the list to one dataframe with multiple columns
Bheri = pd.concat([df.set_index(df.columns[0]) for df in list270], axis=1).reset_index()
Bheri.columns = ["Date", "BtoDTS", "GtotDTS", "QallDTS", "RtotDTS", "StotDTS"]
# convert the 'date' column to a datetime object
Bheri["Date"] = pd.to_datetime(Bheri["Date"])
# set the 'date' column as the index
Bheri.set_index("Date", inplace=True)
# for a sub years
df_sub270 = Bheri.loc["1991":"2022"]
# Group the data by the month and calculate the mean for each month
Monthly_average_270 = df_sub270.groupby(df_sub270.index.month).mean()
Monthly_average_270.reset_index(inplace=True)

### KARNALI
# combining the dataframes in the list to one dataframe with multiple columns
Karnali = pd.concat(
    [df.set_index(df.columns[0]) for df in list280], axis=1
).reset_index()
Karnali.columns = ["Date", "BtoDTS", "GtotDTS", "QallDTS", "RtotDTS", "StotDTS"]
# convert the 'date' column to a datetime object
Karnali["Date"] = pd.to_datetime(Karnali["Date"])
# set the 'date' column as the index
Karnali.set_index("Date", inplace=True)
# for a sub years
df_sub280 = Karnali.loc["1991":"2022"]
# Group the data by the month and calculate the mean for each month
Monthly_average_280 = df_sub280.groupby(df_sub280.index.month).mean()
Monthly_average_280.reset_index(inplace=True)

# code to plot values
# label and variable names
month_dict = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}
labels = ["Date", "BtoDTS", "GtotDTS", "QallDTS", "RtotDTS", "StotDTS"]
figtitle_260 = "Seti"
figtitle_270 = "Bheri"
figtitle_280 = "Karnali"
savefilename_280 = "Hydrographs combined(280)"  # name of figure when saved
savefilename_260 = "Hydrographs combined(260)"  # name of figure when saved
savefilename_270 = "Hydrographs combined(270)"  # name of figure when saved
figdir = "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Figures/"  # directory to save figure
plt.close("all")

### KARNALI PLOT

x = Monthly_average_280["Date"]
y1 = Monthly_average_280["BtoDTS"]
y2 = Monthly_average_280["GtotDTS"]
y3 = Monthly_average_280["QallDTS"]
y4 = Monthly_average_280["RtotDTS"]
y5 = Monthly_average_280["StotDTS"]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the obs data
ax.plot(x, y3, linewidth=2, ls="--", label="Total Runoff", color="black")
ax.plot(x, y4, label="Rain Runoff", color="crimson")
ax.plot(x, y5, label="Snow Runoff", color="slategray")
ax.plot(x, y1, label="Baseflow Runoff", color="lightseagreen")
ax.plot(x, y2, label="Glacier Runoff", color="olive")

# plot the data and fill the area under the curves
ax.fill_between(x, y1, alpha=0.2, color="lightseagreen")
ax.fill_between(x, y2, alpha=0.2, color="olive")
# ax.fill_between(x, y3, alpha=0.2, color='green')
ax.fill_between(x, y4, alpha=0.2, color="crimson")
ax.fill_between(x, y5, alpha=0.2, color="slategray")

# Set x-axis limits
ax.set_xlim(1, 12)
ax.set_ylim([0, 4000])
ax.set_xticks(list(month_dict.keys()))
ax.set_xticklabels([month_dict[m] for m in Monthly_average_280["Date"]])

# plot and save
plt.title(figtitle_280, fontsize=13, fontweight="bold")
plt.legend()
# plt.tight_layout()
plt.xlabel("Month")
plt.ylabel("Average Monthly Discharge($m^3$/s)")
plt.savefig(figdir + savefilename_280 + ".png", dpi=300)
plt.show()


# For SETI PLOT
x = Monthly_average_260["Date"]
y1 = Monthly_average_260["BtoDTS"]
y2 = Monthly_average_260["GtotDTS"]
y3 = Monthly_average_260["QallDTS"]
y4 = Monthly_average_260["RtotDTS"]
y5 = Monthly_average_260["StotDTS"]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the obs data
ax.plot(x, y3, linewidth=2, ls="--", label="Total Runoff", color="black")
ax.plot(x, y4, label="Rain Runoff", color="crimson")
ax.plot(x, y5, label="Snow Runoff", color="slategray")
ax.plot(x, y1, label="Baseflow Runoff", color="lightseagreen")
ax.plot(x, y2, label="Glacier Runoff", color="olive")

# plot the data and fill the area under the curves
ax.fill_between(x, y1, alpha=0.2, color="lightseagreen")
ax.fill_between(x, y2, alpha=0.2, color="olive")
# ax.fill_between(x, y3, alpha=0.2, color='green')
ax.fill_between(x, y4, alpha=0.2, color="crimson")
ax.fill_between(x, y5, alpha=0.2, color="slategray")

# Set x-axis limits
ax.set_xlim(1, 12)
ax.set_ylim([0, 3000])
ax.set_xticks(list(month_dict.keys()))
ax.set_xticklabels([month_dict[m] for m in Monthly_average_260["Date"]])
plt.title(figtitle_260, fontsize=13, fontweight="bold")
plt.legend()
# plt.tight_layout()
plt.xlabel("Month")
plt.ylabel("Average Monthly Discharge($m^3$/s)")
plt.savefig(figdir + savefilename_260 + ".png", dpi=300)
plt.show()


# For BHERI PLOT
x = Monthly_average_270["Date"]
y1 = Monthly_average_270["BtoDTS"]
y2 = Monthly_average_270["GtotDTS"]
y3 = Monthly_average_270["QallDTS"]
y4 = Monthly_average_270["RtotDTS"]
y5 = Monthly_average_270["StotDTS"]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the obs data
ax.plot(x, y3, linewidth=2, ls="--", label="Total Runoff", color="black")
ax.plot(x, y4, label="Rain Runoff", color="crimson")
ax.plot(x, y5, label="Snow Runoff", color="slategray")
ax.plot(x, y1, label="Baseflow Runoff", color="lightseagreen")
ax.plot(x, y2, label="Glacier Runoff", color="olive")

# plot the data and fill the area under the curves
ax.fill_between(x, y1, alpha=0.2, color="lightseagreen")
ax.fill_between(x, y2, alpha=0.2, color="olive")
# ax.fill_between(x, y3, alpha=0.2, color='green')
ax.fill_between(x, y4, alpha=0.2, color="crimson")
ax.fill_between(x, y5, alpha=0.2, color="slategray")

# Set x-axis limits
ax.set_xlim(1, 12)
ax.set_ylim([0, 3000])
ax.set_xticks(list(month_dict.keys()))
ax.set_xticklabels([month_dict[m] for m in Monthly_average_270["Date"]])
plt.title(figtitle_270, fontsize=13, fontweight="bold")
plt.legend()
# plt.tight_layout()
plt.xlabel("Month")
plt.ylabel("Average Monthly Discharge($m^3$/s)")
plt.savefig(figdir + savefilename_270 + ".png", dpi=300)
plt.show()


# =============================================================================
## OLD _SCRIPT

# xmin = Monthly_average_280['Date'][0]
# xmax = Monthly_average_280['Date'][10]
# ax.set_xlim(xmin, xmax)
# plt.show()
#
#
# plt.ioff()
# # Create a figure and axis object
# fig, ax = plt.subplots()
# for i in range(len(Monthly_average_280)):
#     df_simulated = Monthly_average_280[i]
#     label = labels[i]
#     # Plot the obs data
#     ax.plot(df_simulated['Date'], df_simulated['Discharge at 280'], label= label)
#     plt.legend()
#     print(label)

# plt.savefig(figdir + savefilename1 + '.png', dpi = 300)
# plt.show()
# =============================================================================

# # creating error bars
# max_value = Karnali.groupby(Karnali.index.month).max()
# min_value = Karnali.groupby(Karnali.index.month).min()
# mean_value = Karnali.groupby(Karnali.index.month).mean()
# error_pos = np.abs(max_value-mean_value)
# error_neg = np.abs(mean_value-min_value)

# # Plot the line graph with error bars
# plt.errorbar(x, y1, yerr=[error_pos['BtoDTS'], error_neg['BtoDTS']], fmt='ko-', capsize=3, linewidth=1, markersize=3.5)
# plt.errorbar(x, y2, yerr=[error_pos['GtotDTS'], error_neg['GtotDTS']], fmt='ko-', capsize=3, linewidth=1, markersize=3.5)
# plt.errorbar(x, y3, yerr=[error_pos['QallDTS'], error_neg['QallDTS']], fmt='ko-', capsize=3, linewidth=1, markersize=3.5)
# plt.errorbar(x, y4, yerr=[error_pos['RtotDTS'], error_neg['RtotDTS']], fmt='ko-', capsize=3, linewidth=1, markersize=3.5)
# plt.errorbar(x, y5, yerr=[error_pos['StotDTS'], error_neg['StotDTS']], fmt='ko-', capsize=3, linewidth=1, markersize=3.5)