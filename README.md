# Newspaper Articles Analysis Repository

This repository contains Python scripts designed to analyze newspaper articles, focusing on relevance assessment and inter-rater reliability measurement using Krippendorff's alpha. The scripts process data from various sources to enhance the understanding and quality of information related to Cabo Delgado.

## Contents

- **Relevance Analysis Script**: Evaluates the relevance of newspaper articles based on specific keywords and criteria.
- **Krippendorff's Alpha Calculation Script**: Computes inter-rater reliability using Krippendorff's alpha for different measurement levels.

## Features

### Relevance Analysis

- **Data Import**: Loads article datasets from Excel files.
- **Keyword Filtering**: Identifies articles that contain specific keywords such as "publicidade" and marks them as irrelevant.
- **Confidence Scoring**: Assigns a confidence score to articles deemed irrelevant.
- **Data Export**: Saves the updated dataset back to the original Excel file for further analysis.

### Krippendorff's Alpha Calculation

- **Inter-Rater Reliability Assessment**: Calculates Krippendorff's alpha for relevance ratings across multiple datasets, providing a measure of agreement between different raters.
- **Multiple Measurement Levels**: Supports nominal, ordinal, interval, and ratio metrics for comprehensive reliability analysis.
- **Data Import**: Reads data from CSV files containing relevance and confidence ratings.

## Requirements

To run the scripts, ensure you have the following libraries installed:

```bash
pip install pandas openpyxl krippendorff
