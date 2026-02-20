# Data Operations Pipeline

A production-style data pipeline simulating real-world workflows 
used by data engineering teams — built with Python and pandas.

## Overview

This project demonstrates core data operations skills including 
ingestion, validation, and transformation of raw data — mirroring 
workflows used in modern data platforms.

## Pipeline Stages

### 1. Data Ingestion (`ingest.py`)
- Loads data from CSV, JSON, or Parquet files
- Structured logging with timestamps
- Error handling for missing or unsupported files

### 2. Data Validation (`validate.py`)
- Detects and reports missing values with percentages
- Identifies and removes duplicate rows
- Logs data types and shape after validation

### 3. Data Processing (`process.py`)
- Normalizes column names
- Fills missing values using median/mode strategies
- Adds processing metadata timestamp

## Tech Stack
- Python 3.x
- Pandas
- Logging module

## How to Run
```bash
pip install pandas
python ingest.py
python validate.py
python process.py
```

## Skills Demonstrated
- ETL pipeline design
- Data quality checks
- Production-style logging
- Error handling best practices
