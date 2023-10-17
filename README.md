# All Specialties Doctors Count - Bar Chart Race

This Python script utilizes the pandas, bar_chart_race, and matplotlib libraries to create an animated "Bar Chart Race" graph, illustrating the change in the count of doctors across all specialties over time.

## Usage Instructions

1. **Install Dependencies**

   Make sure you have all the required libraries installed by running:

    ```bash
    pip install pandas bar_chart_race matplotlib
    ```

2. **Run the Script**

   Replace `'Arzte.csv'` with the actual path to your CSV file, then run the script:

    ```bash
    python your_script_name.py
    ```

3. **View the Result**

   After the script execution, a video file named `arzte_race.mp4` will be created, depicting the change in the count of doctors over time.

## Script Parameters

- `title`: The title of the graph.
- `orientation`: The orientation of the graph (`'h'` for horizontal, `'v'` for vertical).
- `sort`: Sorting order of the columns (`'asc'` for ascending, `'desc'` for descending).
- `n_bars`: Number of bars to display.
- `steps_per_period`: Number of steps (frames) of animation per period.
- `period_length`: Duration of each period in milliseconds.
- `filename`: Path to save the video.
- `figsize`: Figure dimensions.
- `cmap`: Color map for the graph.
- `bar_kwargs`: Additional parameters for the graph bars.
- `filter_column_colors`: Filter column colors.

## License

This project is distributed under the MIT License - see the [LICENSE](LICENSE) file for details.
