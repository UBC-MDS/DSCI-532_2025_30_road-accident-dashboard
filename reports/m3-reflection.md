# Milestone 2 Reflection

We have significantly enhanced the dashboard by implementing several key features from our proposal and sketch. The following improvements have been made:

1. **Summary Cards Enhancements**

We refined the summary cards to align properly with the sidebar and charts, ensuring a uniform layout. The cards now display relevant accident statistics, formatted for clarity (e.g., using K, M, and B suffixes for large numbers). Additionally, we improved the visual hierarchy by adjusting fonts, spacing, and card styling to enhance readability.

As part of the summary card enhancements, we also implemented a robust logic for computing percentage changes between the earliest and latest years. The percentage change follows these improved rules:

- If a range of years is selected, the calculation compares the earliest and latest year in the selection, aggregating data across all months within those years to ensure a comprehensive comparison.
- If only one year is selected, the percentage change returns “N/A”, as there is no other year available for comparison.
- If specific months are selected within a year range, the data is aggregated only for those months within the earliest and latest years. This ensures that comparisons are made within the same timeframe across years.
- If, after aggregation, there is no data available for either the earliest or latest year, the percentage change also returns “N/A” to indicate missing data.

2. **Sidebar Enhancements**

We added a reset button that resets all filters to default values. This ensures that users can easily revert their selections without refreshing the page.

3. **Dynamic Last Deployment Date**

We included a dynamically updated “Last Deployment Date” in the About section using Python’s datetime module. This ensures users always see the most recent deployment date without manual updates.

4. **Code Modularization**

This was implemeted in Milestone 2.

## Inspiration (Challenging)

- **Summary Cards Layout (Inspired by Group 16)**
We adopted Group 16’s structured approach to summary cards, where they organized content into header, body, and footer. This helped improve the visual clarity and readability of key accident statistics. However, we chose to omit the footer, as it was not necessary for our data presentation.

- **Reset Filter Functionality (Inspired by Group 18)**
We implemented a reset filter button based on the approach taken by Group 18. While their implementation had issues, we refined the logic to ensure our reset functionality worked correctly and efficiently, resetting all filters to their default states.

- **Chart Loading Animation (Inspired by Group 17)**
For a more polished user experience, we implemented a loading animation for the chart area, inspired by Group 17. We specifically used a red cube loading animation, which aligns well with our dashboard’s theme and provides clear feedback to users while data is being processed.

## Future Improvements

To enhance the percentage change calculation, we aim to improve how it handles single-year selections:

- If a single year is selected, compare January to December instead of returning “N/A.”
- If specific months are selected, compare the earliest to latest month within that year.
- Only return “N/A” if there is no data after filtering or only one month within a single year is selected .
