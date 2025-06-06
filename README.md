# DSCI 532 - Group 30: Canadian Road Accident Tracker

## Our Motivation and Purpose  

Road accidents are a major public safety concern, leading to significant loss of life, economic costs, and infrastructural damage. Understanding the factors contributing to accidents—such as weather conditions, vehicle types, and driver behaviors—can help policymakers and city planners design safer road systems. This dashboard provides interactive visualizations to explore Canadian accident trends, analyze accident severity across different regions, and identify key risk factors. By offering data-driven insights, it helps decision-makers implement targeted interventions to improve road safety.  

## Who are we?  

We are data analysts specializing in transportation safety. Our goal is to help the Canadian government transportation agencies and urban planners leverage data to make informed decisions that enhance road safety.  

## Dataset Attribution

This project uses data from the [Global Road Accidents Dataset](https://www.kaggle.com/datasets/ankushpanday1/global-road-accidents-dataset) available on Kaggle.  

## Usage

Navigate through the dashboard using the following interactive features:

- **Group By Options** – Aggregate data based on:
  - Accident Severity
  - Time of Accident
  - Settlement Type (Urban, Rural)
  - Season (Winter, Spring, Summer, Autumn)

- **Filter Options** – Select one or more:
  - Settlement Type
  - Season
  - Weather Condition
  - Road Condition
  - Time of Day (Morning, Afternoon, Evening, Night)
  - Year – Adjust using a range slider
  - Month – Select specific months (Jan–Dec)
  - Count Type (For Total Accidents by Age/Weather/Road Conditions charts only)
    - Raw Count – Displays the absolute count of accidents for each group
    - Normalized Count – Converts accident counts into fractions (relative proportions) instead of absolute values

- **Apply or Reset Filters**
  - Click “Apply Filters” to update visualizations.
  - Click “Reset Filters” to clear all selections.

- **Charts** – Dynamically update based on selected filters.
- **Hover Effects** – Display additional insights when hovering over charts and summary cards.

## Demo

![gif](https://raw.githubusercontent.com/UBC-MDS/DSCI-532_2025_30_road-accident-dashboard/refs/heads/main/img/demo.gif)

Try it out: [link](https://mds-2025-road-accident-dashboard.onrender.com/)

## Support

For any issues regarding running the dashboard or feature requests, please contact us using [GitHub Issues](https://github.com/UBC-MDS/DSCI-532_2025_30_road_accident_dashboard/issues).  

## Running the App Locally

1. Clone the repository:  

   ```shell
   git clone https://github.com/UBC-MDS/DSCI-532_2025_30_road_accident_dashboard.git
   ```  

2. Change directory to the project root:  

   ```shell
   cd DSCI-532_2025_30_road_accident_dashboard
   ```  

3. Create a conda environment:  

   ```shell
   conda env create -f environment.yml
   ```  

4. Activate the environment:  

   ```shell
   conda activate 532-group-30
   ```  

5. Run the application:

   ```shell
   python src/app.py
   ```  

6. Open your browser and navigate to `http://localhost:8050/` to view the dashboard.

## Contributing

We welcome contributions! Please refer to our [contributing guidelines](CONTRIBUTING.md) for details on how to get involved.  

## License

### Code

The code within this repository is licensed under the [MIT][mit] license.

[mit]: http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative"

### Content/Text

[![CC BY 4.0 license button][cc-by-png]][cc-by]

The non-code content within the project is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

[cc-by-png]: https://licensebuttons.net/l/by/4.0/88x31.png#floatleft "CC BY 4.0 license button"
[cc-by]: https://creativecommons.org/licenses/by/4.0/ "Creative Commons Attribution 4.0 International License"
