"""
<Analysis of Bank Campaign - Group C>

This script contains functions for analyzing customer age distribution, job success rates, and the impact of loans on the success of subscribing to a term deposit.

Copyright (c) 2024
Licensed
Written by <Racheal Ezeja, Lishan Wang, Abiodun Wale-Adebowale, Ebiere Adegbesan>
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(bank_campaign):
    """
    Plot the distribution of customer ages.

    :param df: pandas DataFrame containing the dataset
    :return: None, displays the plot
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(bank_campaign['age'], bins=30, kde=True, color='skyblue')
    plt.title('Age Distribution of Customers')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

def plot_job_success_rates(df, job_column='job', target_column='y'):
    """
    This function calculates the success rates of a marketing campaign by job type and plots the results.
    
    :param df: pandas DataFrame containing the dataset
    :param job_column: string, the name of the column representing job types
    :param target_column: string, the name of the column representing the target variable ('yes' or 'no')
    :return: None, displays the plots
    """
    # Grouping by job type and target variable to count the occurrences of "yes" and "no"
    job_response = df.groupby([job_column, target_column]).size().unstack().fillna(0)

    # Renaming columns to 'No' and 'Yes' for clarity
    job_response.columns = ['No', 'Yes']

    # Calculating the success rate for each job type
    job_response['Success Rate'] = job_response['Yes'] / (job_response['Yes'] + job_response['No'])

    # Display the job response counts and success rates
    print(job_response)

    # Plotting the stacked bar chart for response distribution by job type
    plt.figure(figsize=(14, 8))
    job_response[['No', 'Yes']].plot(kind='bar', stacked=True, color=['salmon', 'skyblue'], figsize=(14, 8))

    plt.title('Term Deposit Response by Job Type')
    plt.xlabel('Job Type')
    plt.ylabel('Count of Responses')
    plt.xticks(rotation=45)
    plt.legend(title='Response')
    plt.show()

    # Plotting the success rate by job type
    plt.figure(figsize=(14, 8))
    sns.barplot(x=job_response.index, y=job_response['Success Rate'], palette='viridis')

    plt.title('Success Rate by Job Type')
    plt.xlabel('Job Type')
    plt.ylabel('Success Rate')
    plt.xticks(rotation=45)
    plt.show()

def plot_loan_success_rates(df, housing_column='housing', loan_column='loan', target_column='y'):
    """
    Analyze and plot the impact of having a housing or personal loan on the success rate of subscribing to a term deposit.

    :param df: pandas DataFrame containing the dataset
    :param housing_column: string, the name of the column representing housing loan status
    :param loan_column: string, the name of the column representing personal loan status
    :param target_column: string, the name of the column representing the target variable ('yes' or 'no')
    :return: None, displays the plots
    """
    # Analyzing the impact of having a housing loan on the success rate
    housing_response = df.groupby([housing_column, target_column]).size().unstack().fillna(0)
    housing_response.columns = ['No', 'Yes']
    housing_response['Success Rate'] = housing_response['Yes'] / (housing_response['Yes'] + housing_response['No'])

    # Analyzing the impact of having a personal loan on the success rate
    loan_response = df.groupby([loan_column, target_column]).size().unstack().fillna(0)
    loan_response.columns = ['No', 'Yes']
    loan_response['Success Rate'] = loan_response['Yes'] / (loan_response['Yes'] + loan_response['No'])

    # Plotting the success rate by housing loan status
    plt.figure(figsize=(12, 6))
    sns.barplot(x=housing_response.index, y=housing_response['Success Rate'], palette='viridis')
    plt.title('Success Rate by Housing Loan Status')
    plt.xlabel('Housing Loan')
    plt.ylabel('Success Rate')
    plt.show()

    # Plotting the success rate by personal loan status
    plt.figure(figsize=(12, 6))
    sns.barplot(x=loan_response.index, y=loan_response['Success Rate'], palette='viridis')
    plt.title('Success Rate by Personal Loan Status')
    plt.xlabel('Personal Loan')
    plt.ylabel('Success Rate')
    plt.show()

if __name__ == "__main__":
    
    plot_age_distribution(bank_campaign)
    plot_job_success_rates(bank_campaign)
    plot_loan_success_rates(bank_campaign)
