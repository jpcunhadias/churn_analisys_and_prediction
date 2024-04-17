import pandas as pd
import sys
import os
from scipy.stats import chi2_contingency

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.data.make_dataset import load_data, preprocess_data, save_data

def chi_square_test(data, target, alpha=0.05):
    """
    Perform chi-square test for independence between target and each feature.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataframe containing features and target.
    target : str
        Name of target column.
    alpha : float, default=0.05
        Significance level for chi-square test.
    
    Returns
    -------
    pd.DataFrame
        Dataframe containing chi-square test results.
    """
    categorical_columns = ['PhoneService', 'MultipleLines', 'InternetService', 
                           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                           'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 
                           'PaperlessBilling', 'PaymentMethod']
    
    num_tests = len(categorical_columns)
    
    bonferroni_alpha = alpha / num_tests
    
    print(f'Nível de significância ajustado com Bonferroni: {bonferroni_alpha}')
    
    results = []
    for col in categorical_columns:
        table = pd.crosstab(data[col], data[target])
        chi2, p, dof, ex = chi2_contingency(table)
        results.append([col, p, chi2, dof])
        print(f"{col} - p-value: {p} - {'Significant' if p < bonferroni_alpha else 'Not significant'}")
    
    results_df = pd.DataFrame(results, columns=['feature', 'p_value', 'chi2', 'dof'])
    results_df['significant'] = results_df['p_value'] < alpha
    return results_df

def feature_engineering(data):
    standard_columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']
    chi_square_test_results = chi_square_test(data, 'Churn')
    significant_features = chi_square_test_results[chi_square_test_results['significant']]['feature'].tolist()
    data = data[standard_columns + significant_features]
    data['PaperlessBilling'] = data['PaperlessBilling'].map({'Yes': 1, 'No': 0})
    
    categorical_columns = data.select_dtypes(include='object').columns
    for column in categorical_columns:
        dummies = pd.get_dummies(data[column], prefix=column)
        data = pd.concat([data, dummies], axis=1)
        data = data.drop(columns=column)
    
    return data
    
def build_features(file_path=''):
    data = load_data(file_path)
    data = preprocess_data(data)
    data = feature_engineering(data)
    save_data(data, file_path='data/interim/customer_churn_processed_transformed.xlsx')
    return data

if __name__ == '__main__':
    build_features('data/raw/customer-churn.xlsx')