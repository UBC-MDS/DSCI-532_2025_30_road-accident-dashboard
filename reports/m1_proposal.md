# Proposal

## Motivation and Purpose

Our role: Data analysts specializing in transportation safety being hired by the Canadian government

Target audience: Canadian government transportation agencies and urban planners

Road accidents are a major public safety concern, leading to significant loss of life, economic costs, and infrastructural damage. Understanding the factors contributing to accidents—such as weather conditions, vehicle types, and driver behaviors—can help policymakers and city planners design safer road systems. To address this issue, we propose building an interactive dashboard that allows stakeholders to explore Canadian road accident trends, analyze accident severity across different regions, and identify key risk factors. By providing visual insights and filtering capabilities, our dashboard will help decision-makers implement targeted interventions to improve road safety.

## Description of the data

The original dataset used in this study is the [Global Road Accidents Dataset](https://www.kaggle.com/datasets/ankushpanday1/global-road-accidents-dataset), which provides a comprehensive collection of road accident records from various countries. It contains approximately 132,000 rows and 30 features, capturing a range of accident-related factors including accident severity, environmental conditions, vehicle involvement, and driver characteristics.

This dataset enables exploratory data analysis (EDA), feature engineering, and predictive modeling to assess accident trends and severity levels. The variables included in the dataset are as follows:

1. **Country** *(string)* – The country where the accident occurred.
2. **Year** *(integer)* – The year in which the accident took place.
3. **Month** *(string)* – The month of the accident.
4. **Day of Week** *(string)* – The day of the week when the accident happened.
5. **Time of Day** *(string)* – The time period (morning, afternoon, evening, night) when the accident occurred.
6. **Urban/Rural** *(string)* – Whether the accident took place in an urban or rural area.
7. **Road Type** *(string)* – The classification of the road where the accident happened (e.g., highway, street).
8. **Weather Conditions** *(string)* – The weather at the time of the accident (e.g., clear, rainy, snowy, windy).
9. **Visibility Level** *(float)* – The level of visibility at the accident scene (measured or categorized level).
10. **Number of Vehicles Involved** *(integer)* – The total number of vehicles involved in the accident.
11. **Speed Limit** *(integer)* – The speed limit of the road where the accident occurred.
12. **Driver Age Group** *(string)* – The age category of the driver(s) involved.
13. **Driver Gender** *(string)* – The gender of the driver(s) involved.
14. **Driver Alcohol Level** *(float)* – The recorded alcohol level of the driver(s).
15. **Driver Fatigue** *(integer: 0 or 1)* – Indicator of whether driver fatigue was a contributing factor.
16. **Vehicle Condition** *(string)* – The condition of the vehicle(s) involved (e.g., poor, good).
17. **Pedestrians Involved** *(integer)* – The number of pedestrians involved in the accident.
18. **Cyclists Involved** *(integer)* – The number of cyclists involved in the accident.
19. **Accident Severity** *(string)* – The severity of the accident (e.g., minor, moderate, severe).
20. **Number of Injuries** *(integer)* – The number of injuries recorded in the accident.
21. **Number of Fatalities** *(integer)* – The number of fatalities resulting from the accident.
22. **Emergency Response Time** *(float)* – The response time of emergency services in minutes.
23. **Traffic Volume** *(float)* – The level of traffic at the time of the accident.
24. **Road Condition** *(string)* – The condition of the road surface (e.g., dry, wet, icy).
25. **Accident Cause** *(string)* – The identified cause of the accident (e.g., weather, human error).
26. **Insurance Claims** *(integer)* – The number of insurance claims filed as a result of the accident.
27. **Medical Cost** *(float)* – The estimated medical expenses related to the accident.
28. **Economic Loss** *(float)* – The total economic loss attributed to the accident, including damage costs.
29. **Region** *(string)* – The geographical region where the accident took place.
30. **Population Density** *(float)* – The population density of the region where the accident occurred.

This dataset provides a robust foundation for analyzing accident trends and understanding the impact of environmental and human factors on road safety. For this project, we will focus on filtering the data for Canada, which would reduced the number of observations to 13,349 rows.

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

![app sketch](../img/sketch.png)

TO BE FILLED BY TIEN
