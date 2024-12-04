# Employee Leave or Not Leave Prediction using SVM

## Project Overview

This project uses a **Support Vector Machine (SVM)** model to predict whether an employee will leave the company based on various features such as age, payment tier, gender, city, work experience, and other factors. The goal of this project is to build a machine learning model that can predict employee attrition and help HR teams take proactive steps to retain valuable talent.

### Problem Statement

Employee attrition is a critical issue for companies as it involves recruitment and operational costs. By predicting which employees are at risk of leaving, companies can take preventive measures to improve retention. This project builds an SVM classifier to predict whether an employee will leave the company or stay based on their personal and professional attributes.

### Dataset

# Dataset Name

- **Employee.csv**

The dataset used in this project contains the following features:

- `ever_benched`: Whether the employee has ever been benched (0: No, 1: Yes)
- `age`: Age of the employee
- `payment_tier`: The payment tier assigned to the employee (categorical: Tier 1, Tier 2, Tier 3)
- `gender`: Gender of the employee (Male, Female, Other)
- `city`: The city where the employee is located
- `experience`: Number of years of professional experience
- `started_work_year`: The year the employee started working at the company
- `attrition`: Whether the employee left the company (1: Left, 0: Stayed) (target variable)

### Objective

- **Predict**: Whether an employee will leave the company (`attrition = 1`) or stay (`attrition = 0`).
- **Analyze**: Identify which features have the most significant impact on employee attrition.

## Installation

To get started with this project, clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/employee-attrition-prediction.git
