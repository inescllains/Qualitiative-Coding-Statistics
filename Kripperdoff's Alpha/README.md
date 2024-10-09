# Krippendorff's Alpha Calculation for Relevance Data

This Python script calculates Krippendorff's alpha, a statistic used to measure the reliability of agreement between multiple raters for categorical, ordinal, interval, and ratio data. It utilizes two datasets containing relevance and confidence ratings.

## Key Features

- **Data Import**: Reads two CSV files containing relevance and confidence ratings from different sources. The data is loaded into pandas DataFrames for further processing.

- **Relevance Extraction**: Extracts the `Relevance` column from both datasets to create lists of relevance ratings for analysis.

- **Confidence Extraction**: Extracts the `Confidence` column from the second dataset for potential use in further analysis.

- **Krippendorff's Alpha Calculation**: Computes Krippendorff's alpha for various levels of measurement:
  - **Nominal**: For categorical data where no ordering is implied.
  - **Ordinal**: For data with a clear order but no consistent scale.
  - **Interval**: For data with a meaningful scale but no true zero.
  - **Ratio**: For data with a meaningful scale and a true zero point.

## Usage

1. Ensure you have the necessary libraries installed:
   ```bash
   pip install pandas krippendorff
