import pandas as pd

global_data = pd.read_csv("../data/road_accident_dataset.csv")
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
canadian_data = raw_canadian_data[[
    'Year', 'Month', 'Day of Week', 'Time of Day', 
    'Urban/Rural', 'Road Type', 'Weather Conditions', 'Visibility Level',
    'Number of Vehicles Involved', 'Speed Limit', 'Driver Age Group',
    'Driver Gender', 'Driver Alcohol Level', 'Driver Fatigue',
    'Vehicle Condition', 'Pedestrians Involved', 'Cyclists Involved',
    'Accident Severity', 'Number of Injuries', 'Number of Fatalities',
    'Emergency Response Time', 'Traffic Volume', 'Road Condition',
    'Accident Cause', 'Insurance Claims', 'Medical Cost', 'Economic Loss',
    'Population Density']]