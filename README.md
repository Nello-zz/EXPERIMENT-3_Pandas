# Experiment 3: Use of Pandas Library

## Introduction

The Pandas library is a powerful tool for data manipulation and analysis in Python. This experiment focuses on using Pandas to work with data in a DataFrame, specifically by extracting and analyzing data from a CSV file. It consists of two problems: the first involves loading a CSV file into a DataFrame and inspecting the data, while the second focuses on performing data operations such as subsetting, slicing, and indexing. This document outlines the objectives for these tasks to guide you through the experiment.

## Prerequisites

- **Software Used:**
  - Jupyter Notebook for coding
  - GitHub for repository sharing
- Pandas library installed (`pip install pandas`)

## Installation and Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Nello-zz/EXPERIMENT-3_Pandas
2. Navigate to the project directory: `cd your-project`
3. Install the necessary Python packages:
   - If you are using Jupyter Notebook, run the following command in a notebook cell:
     ```python
     !pip install pandas
     ```

4. Ensure the `cars.csv` file is in the project directory.

5. Load the CSV file into a DataFrame using the following code:
   ```python
   import pandas as pd

   cars_file = pd.read_csv('cars.csv')

## Problem 1

**Objective:**

1. Load a file into a DataFrame named `cars` using pandas.
2. Display the first five and last five rows of the `cars` DataFrame.

## Problem 2

**Objective:**

1. Perform subsetting, slicing, and indexing operations on the cars DataFrame to extract specific data.

*Additional information*

1. **Subsetting**: Extract data based on specified conditions.
2. **Slicing**: Getting a specific range of rows or columns.
3. **Indexing**: Given set conditions and set a particular column as the DataFrame’s index.

## Expected Results
For Problem 1, you should see the first and last five rows of the cars DataFrame displayed to the console.

For Problem 2, you should be able to extract and display specific portion of data or perform set of conditions and then extract that data from the DataFrame.

## Troubleshooting

- Verify that the CSV file is loaded properly and is located in the same directory as the notebook or script you are using to run the code.
- Ensure that column names in your code match those in the CSV file.

