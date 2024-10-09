# Relevance Analysis for Cabo Delgado Articles

This Python script automates the analysis of newspaper articles, calculating the relevance of each article based on specific criteria such as relevance scores and confidence levels. The goal is to identify and filter articles related to Cabo Delgado, Mozambique, that meet certain thresholds for significance and reliability.

## Key Features

- **Data Cleaning**: Automatically processes datasets by handling missing values and converting key columns (`Relevance` and `Confidence`) into a usable format for analysis.
  
- **Relevance Calculation**: The script evaluates each article's relevance based on two main criteria:
  - Relevance score: Articles marked with a relevance score of `1` are considered important.
  - Confidence score: Only articles with a confidence score of 5 or higher are included in the final results.
  
  It calculates the percentage of relevant articles in each dataset and provides an overall summary.

- **Data Aggregation**: Combines multiple datasets to calculate overall relevance scores across various time periods and publications, giving a broader view of article significance.

- **Filtering**: After relevance calculations, the script filters out articles that don't meet the predefined relevance and confidence thresholds. This creates a dataset that only includes articles with both high relevance and sufficient confidence.

- **Results Export**: The final analysis is saved to two output files:
  - A file summarizing the percentage of relevant articles for each dataset.
  - A comprehensive file that contains only the relevant, high-confidence articles.

## Benefits

- **Automated Analysis**: This script streamlines the analysis process, removing the need for manual data handling or relevance calculations.
- **Consistent Criteria**: Ensures consistent, objective filtering of articles across multiple datasets.
- **Comprehensive Output**: Provides a clear summary of relevant content, making it easier to focus on the most significant articles without sifting through irrelevant data.

## Requirements

- Python 3.x
- pandas (`pip install pandas`)
- openpyxl (`pip install openpyxl`)

## Usage

1. Install the required dependencies:
    ```bash
    pip install pandas openpyxl
    ```

2. Run the script to process the datasets and generate the results:
    ```bash
    python relevance_analysis_cabo_delgado.py
    ```



