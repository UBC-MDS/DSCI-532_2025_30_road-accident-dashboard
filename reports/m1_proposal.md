# Proposal

## Motivation and Purpose

Our role: Data analysts specializing in transportation safety being hired by the Canadian government

Target audience: Canadian government transportation agencies and urban planners

Road accidents are a major public safety concern, leading to significant loss of life, economic costs, and infrastructural damage. Understanding the factors contributing to accidents—such as weather conditions, vehicle types, and driver behaviors—can help policymakers and city planners design safer road systems. To address this issue, we propose building an interactive dashboard that allows stakeholders to explore Canadian road accident trends, analyze accident severity across different regions, and identify key risk factors. By providing visual insights and filtering capabilities, our dashboard will help decision-makers implement targeted interventions to improve road safety.

## Description of the data

The original dataset used in this study is the [Global Road Accidents Dataset](https://www.kaggle.com/datasets/ankushpanday1/global-road-accidents-dataset). The dataset contains approximately 132,000 recorded road accidents from various countries. Each accident is characterized by 30 variables that describe factors potentially influencing accident severity and outcomes. These variables fall into the following key categories:

- **Geographic and temporal attributes**: These include the country, year, month, day of the week, time of day, and whether the accident occurred in an urban or rural area.
- **Environmental conditions**: Weather conditions, visibility level, and road condition provide insight into how external factors contribute to accidents.
- **Accident details**: Information on the road type, number of vehicles involved, speed limit, and accident cause helps in identifying patterns and risk factors.
- **Driver and vehicle characteristics**: Variables such as driver age group, gender, alcohol level, fatigue, and vehicle condition allow us to assess human and mechanical contributions to accidents.
- **Accident severity and outcomes**: This includes accident severity (minor, moderate, severe), number of injuries, number of fatalities, and emergency response time.
- **Economic impact**: Variables such as insurance claims, medical cost, and economic loss help estimate the financial burden of road accidents.
- **Additional contextual information**: Region, traffic volume, and population density contribute to understanding how location-based factors influence accident trends.

Using this data, we will also derive new variables, such as:

- **Season**: Based on the month of the accident, we will categorize accidents into winter, spring, summer, or fall to analyze seasonal trends in accident severity.
- **Economic Cost Per Capita**: By dividing the total economic loss by the population density in the affected region, we can estimate the financial impact of accidents on a per-capita basis.

For this project, we will focus on filtering the data for Canada, which will reduce the number of observations to 13,349 rows.

By leveraging these features, we aim to explore accident trends, identify high-risk conditions, and support policymakers in making data-driven decisions to improve road safety in Canada.

## Research Questions

- Which weather conditions lead to the most severe accidents?
- Are certain times of day or days of the week more prone to high-severity accidents?
- Do driver factors such as alcohol level, fatigue, or age group correlate with accident severity and fatalities?
- How do geographic differences (urban vs rural) influence accident trends and outcomes?
- Which road conditions, such as icy or wet surfaces, are most frequently associated with severe or fatal outcomes?

In summary, analyzing how weather and road conditions, geographic differences, and driver behaviors contribute to road accidents can guide the strategic allocation of resources to reduce risk and fatalities.

## Usage Scenarios

Daniel’s main goal is to create a policy brief for regional authorities. He hopes to show how accidents in rural areas differ from those in urban centers and needs concrete data to support recommendations for resource allocation and new safety measures.

To achieve this goal, he plans to:

1. Analyze accident trends across both urban and rural areas to compare key differences.

2. Filter for severe accidents in both settings to pinpoint high-risk areas that need attention.

3. Compare driver characteristics, including age, alcohol level, and fatigue, to assess their correlation with accident severity.

4. Examine emergency response times across urban and rural regions to determine if delays contribute to higher fatality rates.

5. Identify patterns that could inform targeted safety measures, such as traffic regulations or infrastructure improvements.

When Daniel logs into the dashboard, he sees an overview of accidents across Canada. To compare `Rural` and `Urban` areas, he selects both categories in the Urban or Rural filter. The dashboard updates with summary statistics, showing a higher frequency of severe accidents in rural regions. To understand contributing factors, he applies additional filters to analyze accidents during commuting hours (`Morning` and `Afternoon`).

Next, Daniel examines weather conditions and notices that rainy weather significantly increases accidents in rural areas during weekday mornings, while urban areas see higher accident rates in congested evening hours. He further filters the data for `Rainy` conditions and discovers that rural accidents often occur on roads with speed limits over 80 km/h and poor visibility, with driver fatigue and alcohol use as recurring factors.

Equipped with these insights, Daniel drafts a policy recommendation that includes installing weather-warning signboards on high-speed rural highways, increasing law enforcement presence during identified high-risk hours, and developing designated rest stops on long routes to reduce fatigue-related accidents. He also presents findings on emergency response delays in rural areas, proposing improved resource distribution to reduce fatality risks.

This policy brief is shared with authorities, who begin discussions on implementing these recommendations. Additionally, Daniel suggests a follow-up study focused on the impact of road infrastructure on accident severity, as early insights indicate that road quality and maintenance may also play a critical role in accident preventions.

## App sketch & brief description

![app sketch](../img/app-sketch.png)

### Dashboard Overview

The Road Accident Analytics Dashboard provides an interactive interface to explore trends in road accidents across Canada. The dashboard allows users to filter accident data by key factors such as settlement type (urban/rural), season, weather conditions, road conditions, time of day, and year range. The visualizations are designed to provide insights into accident severity, emergency response time, and economic impact.

### Key Metrics Display

At the top of the dashboard, four key statistics provide a quick overview of accident data:

- Total Accidents: Displays the total number of recorded accidents in the selected dataset.
- Total Fatalities: Shows the number of fatalities resulting from these accidents.
- Average Emergency Response Time: Indicates the average time emergency services took to respond.
- Economic Cost per Capita: Estimates the financial burden of accidents per person in the affected region.

### Interactive Filters

Users can dynamically filter the data using the following controls:

- Settlement Type (Dropdown): Toggle between Urban and Rural accidents.
- Season (Dropdown): Filter accidents by season (Winter, Summer, etc.).
- Weather Condition (Dropdown): Select specific weather conditions like Clear, Snowy, Foggy, etc..
- Road Condition (Dropdown): Choose road conditions such as Wet, Icy, or Dry.
- Time of Day (Dropdown): Filter accidents occurring in Morning, Afternoon, Evening, or Night.
- Year Range Slider: Adjust the time window for analysis (2001 - 2022).
- Calendar View: Provides an alternative way to select specific dates.

### Visualizations

1. Emergency Response Time vs. Accident Severity (Boxplot)

  This boxplot compares emergency response times across different accident severities (minor, moderate, and severe). The visualization highlights whether severe accidents tend to have longer response times than minor ones.

2. Weather Conditions and Accident Severity (Stacked Bar Chart)

  This chart categorizes accidents based on weather conditions (windy, snowy, rainy, foggy, clear), with bars color-coded to indicate minor, moderate, and severe accidents. It helps analyze which weather conditions are linked to more severe accidents.

3. Age Group and Accident Severity (Stacked Horizontal Bar Chart)

    This chart shows the distribution of accident severity for different driver age groups (e.g., 18-25, 26-40, 41-60, etc.). The color-coded bars allow users to observe whether younger or older drivers are more likely to be involved in severe accidents.

4. Accident Trends Over Time (Line Chart)

    This line chart illustrates how the number of minor, moderate, and severe accidents has changed over time (2001-2024). It allows users to detect trends, such as increasing accident severity in recent years.

### Interactivity Features

Users can hover over charts to see detailed tooltips with exact data values.
Filters dynamically update all charts, allowing users to explore specific conditions.

This dashboard provides an intuitive and insightful way to analyze road accidents, helping policymakers and researchers identify risk factors and potential safety improvements.
