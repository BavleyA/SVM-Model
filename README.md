# Employee Leave or Not Leave Prediction using SVM

## Project Overview

This project uses a **Support Vector Machine (SVM)** model to predict whether an employee will leave the company based on various features such as age, payment tier, gender, city, work experience, and other factors. The goal of this project is to build a machine learning model that can predict employee attrition and help HR teams take proactive steps to retain valuable talent.

### Problem Statement

Employee attrition is a critical issue for companies as it involves recruitment and operational costs. By predicting which employees are at risk of leaving, companies can take preventive measures to improve retention. This project builds an SVM classifier to predict whether an employee will leave the company or stay based on their personal and professional attributes.

## Dataset

### Dataset Name

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

- **Predict**: Whether an employee will leave the company (`1`) or stay (`0`).

## Installation

To get started with this project, clone the repository to your local machine.

```bash
  git clone https://github.com/yourusername/employee-attrition-prediction.git
```
# Project Requirements

This project requires several Python libraries to run smoothly. Below are the necessary dependencies:

### Required Libraries

- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations and handling arrays.
- **matplotlib**: For creating static, animated, and interactive visualizations.
- **seaborn**: For statistical data visualization built on top of matplotlib.
- **scikit-learn**: For machine learning algorithms and tools.
- **joblib**: For serializing Python objects, especially used to save and load the trained model.

### Installation

To install all the required dependencies for this project, you can use the following `pip` command:

```bash
pip install -r requirements.txt
```

# Additional Notes for Setting Up a Virtual Environment

If you're using a virtual environment (which is **recommended** for project-specific package management), make sure to activate it before running the `pip install` command.

## Creating a Virtual Environment

To create a virtual environment, run the following command:

```bash
python -m venv myenv
```
# Activating a Virtual Environment

Once you have created a virtual environment, you need to activate it to start using it for your project. Below are the instructions for activating the virtual environment on different operating systems:

## On Windows

To activate the virtual environment on Windows, run the following command in your terminal:

```bash
myenv\Scripts\activate
```

## On Mac/Linux

To activate the virtual environment on Windows, run the following command in your terminal:

```bash
source myenv/bin/activate
```
Once activated, your terminal prompt should change, and you'll see the environment name (e.g., (myenv)) at the beginning of the line, indicating that the virtual environment is active.

# Setting Up the Environment

After setting up the environment and installing the necessary dependencies, you’re ready to run the project!

## Installation Steps Recap

1. **Create a Virtual Environment**:
   - Run the following command to create a virtual environment:
     ```bash
     python -m venv myenv
     ```
   
2. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source myenv/bin/activate
     ```

3. **Install Dependencies**:
   - After activating the virtual environment, install the dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

Once these steps are completed, you are now ready to run the project!

## Running the Project

1. Ensure the virtual environment is activated.
2. Run the project scripts as per the instructions in the README or as required.

---

You can save this content in a file named `requirements.md`. This file provides the necessary details to install dependencies and set up the environment before running the project.


