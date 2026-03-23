
# Phishing URL Detection Using UI

A machine learning-based phishing URL detection system with a simple web interface built using Flask.

## Overview

This project is designed to detect whether a given URL is **phishing** or **legitimate**.  
It uses **machine learning** and **URL feature extraction** to classify URLs and display the result through a user-friendly web interface.

The system extracts important phishing-related features from the URL, passes them to a trained **Random Forest model**, and returns the prediction on the webpage.

## Features

- Detects phishing and legitimate URLs
- Flask-based user interface
- Machine learning-based classification
- URL feature extraction for phishing detection
- Random Forest model for prediction
- Simple and interactive web application

## Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **HTML/CSS**
- **WHOIS**

## Project Structure

```bash
Phishing website detection using UI/
│
├── templates/
│
├── .project
├── .pydevproject
├── Classifier2.py
├── legitimate-urls.csv
├── phishing-urls.csv
├── retrain.py
├── screenshot1.png
├── screenshot2.png
│
├── extracted_csv_files/
├── notebooks/
├── raw_datasets/
├── templates/
│
├── .gitignore
├── Classifier.py
├── FeatureExtraction.py
├── README.md
├── RandomForestModel.sav
├── _config.yml
└── app.py
