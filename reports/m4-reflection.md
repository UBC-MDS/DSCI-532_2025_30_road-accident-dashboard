# Milestone 4 Reflection

## Performance Impovement via Flask-Caching

During Milestone 4, we implemented `Flask-Caching` in the dashboard to optimize performance by reducing redundant computations and improving response times. By using `cache.memoize()`, we efficiently cached the dataset, default filters, and frequently used user filters, ensuring that expensive data processing was not repeated unnecessarily. By making the app more responsive we have significantly improved load times which will enhanced the user experience.

## Tooltip for the Dashboard Summary Cards

We implemented tooltips to explain the percentage change for each summary card when hovering. The tooltip displays the difference between the earlier year and the latest year on the slider, as well as the selected months. Additionally, it provides the full meaning of each card if necessary. This feature helps users to better understand the data presented in the summary cards.

## Apply Filters Button

We added an "Apply Filters" button to the dashboard (top of the sidebar) to allow users to apply multiple filters at once. This feature enables users to select multiple filters and apply them all at once, rather than applying each filter individually. This enhancement improves the user experience by making the filtering process more efficient and user-friendly.

## Normalization of Bar Charts

We added a checkbox to normalize each bar chart to ensure that the data is displayed proportionally, regardless of the number of accidents. This enhancement provides a more accurate representation of the data and allows users to compare accident counts across different categories more effectively.

## Favicon

We added a favicon to the dashboard to improve the user experience by providing a visual representation of the application. The favicon appears in the browser tab and bookmarks, making it easier for users to identify and access the dashboard.
