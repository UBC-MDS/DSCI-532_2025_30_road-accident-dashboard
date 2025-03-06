import pandas as pd

global_data = pd.read_csv("data/raw/road_accident_dataset.csv")
raw_canadian_data = global_data[global_data["Country"] == "Canada"]

# List of columns
# ['Country', 'Year', 'Month', 'Day of Week', 'Time of Day', 'Urban/Rural',
#   'Road Type', 'Weather Conditions', 'Visibility Level',
#   'Number of Vehicles Involved', 'Speed Limit', 'Driver Age Group',
#   'Driver Gender', 'Driver Alcohol Level', 'Driver Fatigue',
#   'Vehicle Condition', 'Pedestrians Involved', 'Cyclists Involved',
#   'Accident Severity', 'Number of Injuries', 'Number of Fatalities',
#   'Emergency Response Time', 'Traffic Volume', 'Road Condition',
#   'Accident Cause', 'Insurance Claims', 'Medical Cost', 'Economic Loss',
#   'Region', 'Population Density']

# TODO: Remove some of the unused columns below such that the DataFrame can be lighter :)
# Final output
canadian_data = raw_canadian_data[
    [
        "Year",
        "Month",
        "Day of Week",
        "Time of Day",
        "Urban/Rural",
        "Road Type",
        "Weather Conditions",
        "Visibility Level",
        "Number of Vehicles Involved",
        "Speed Limit",
        "Driver Age Group",
        "Driver Gender",
        "Driver Alcohol Level",
        "Driver Fatigue",
        "Vehicle Condition",
        "Pedestrians Involved",
        "Cyclists Involved",
        "Accident Severity",
        "Number of Injuries",
        "Number of Fatalities",
        "Emergency Response Time",
        "Traffic Volume",
        "Road Condition",
        "Accident Cause",
        "Insurance Claims",
        "Medical Cost",
        "Economic Loss",
        "Population Density",
    ]
].copy()

season_dict = {
    "December": "Winter",
    "January": "Winter",
    "February": "Winter",
    "March": "Spring",
    "April": "Spring",
    "May": "Spring",
    "June": "Summer",
    "July": "Summer",
    "August": "Summer",
    "September": "Autumn",
    "October": "Autumn",
    "November": "Autumn",
}

# Create Seasons based on Month
canadian_data["Season"] = canadian_data["Month"].map(season_dict)

# Create shortnames for Months
canadian_data["MonthX"] = canadian_data["Month"].str[:3]

canadian_data = canadian_data.rename(columns={"Urban/Rural": "Settlement Type"})