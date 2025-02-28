# Milestone 2 Reflection

Here are what we have implemented so far:

## User Filter Sidebar

We have implemented all the proposed filter widgets in the sidebar. The sidebar dynamically generates the unique options for each filter directly from the dataset by importing the `canadian_data` into `sidebar.py`. This ensures that any changes in the data are automatically reflected in the filter options. For example, the dropdown for `Time of Day` displays only the unique values present in the dataset.

The following filters were implemented:

- `Settlement Type`
  
A dropdown that allows the user to select one or more categories (e.g., Urban and Rural).

- `Season`
  
A dropdown with the four seasons (Summer, Autumn, Winter, and Spring). The Season column was computed by mapping full month names to their corresponding season.

- `Weather Condition`

A dropdown that includes options like Rainy, Foggy, Snowy, Windy, and Clear.

- `Road Condition`

A dropdown with options such as Icy, Snow-covered, Wet, and Dry.

- `Time of Day`

A dropdown offering options such as Morning, Afternoon, Evening, and Night.

- `Year Range Slider`

A double-ended slider was used for year selection. This slider is set up with its minimum and maximum values derived from the dataset (i.e., `min_year` and `max_year`). A tooltip is included to display the exact years when the slider handles are adjusted.

- `Month Checklist`
  
Since the dataset does not include day-level information, we could not implement a full calendar. Instead, we created a month checklist using a `dcc.Checklist` that displays a grid of month buttons (computed by slicing the month names to their first three letters, stored in the `MonthX` column). This allows users to filter the data by selecting one or more months in which accidents occurred.

Default Filtering Behavior

- All dropdown filters (`Settlement Type`, `Season`, `Weather Condition`, `Road Condition`, and `Time of Day`) start with no selection, which means that by default, the dashboard shows data for all available categories.

- The year slider is initially set to span from the earliest to the latest year in the dataset, thereby including all years by default.

- With no months selected by default, the month filter does not restrict the data. Hence, all months are shown until the user makes a selection.

## Summary Cards

The summary cards were implemented relatively closely to the proposed sketch. We ended up displaying these summary statistics in the dashboard:

- Total number of accidents
- Total fatalities
- Average emergency response time
- Total economic loss
- Leading cause of accident

The only deviation that we made was that we initially wanted an economic cost per capita stats. However, the dataset does not have population data but rather population density. We decided to pivot away from economic loss per capita to total economic lost instead!

## Visualization Board

The five charts that were implemented:

- Emergency Response Time box plot
- Accident Count by Weather Conditions
- Accident Count by Road Conditions
- Accident Count by Age Groups
- Accident Count by Year

Note that we have also implemented categories to group these charts, either by "Accident Severity" or by "Time of Accident". Since the number of rows of the dataframe is approximately only 10,000 rows, our app was able to be relatively performant. These charts were implemented exactly the same as our proposed Milestone 1 sketch. No deviations from the proposal was made!

Low Hanging Fruit: We added tooltips to each charts so that when user hovers over the charts, additional information can be provided!

Limitaton: When working on the data with no filters applied yet, there seem to be no visible trend in any of the charts. However, once some user filters are applied (through the UI), then some notable and visible trends can be seen.

## NavBar (CHALLENGING section)

We also implemented the navbar with GitHub and About buttons. The GitHub buttons will take the user to the GitHub repository while the About buttons will render an additional About section in the navbar that explains what the project is, who the target audience is, main contributors as well as the date of the last deployment.
