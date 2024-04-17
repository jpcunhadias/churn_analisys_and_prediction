import os
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

def save_figures(figs, path):
    """
    Save multiple matplotlib figures to a file.
    
    Parameters
    ----------
    figs : list of matplotlib.figure.Figure
        The figures to save.
    path : str
        The directory to save the figures in.
    
    Returns
    -------
    None
    """
    if not os.path.exists(path):
        os.makedirs(path)
    
    for i, fig in enumerate(figs):
        fig.savefig(os.path.join(path, f'figure{i+1}.png'))

def demographic_analysis(data):
    """
    Perform demographic analysis and save the figures.
    
    Parameters
    ----------
    data : DataFrame
        The data to analyze.
    
    Returns
    -------
    None
    """
    figs = []

    # Analysis 1: Gender
    fig1, ax1 = plt.subplots()
    gender_counts = data['gender'].value_counts(normalize=True)
    gender_counts.plot(kind='bar', ax=ax1)
    ax1.set_title('Gender Distribution')
    figs.append(fig1)

    # Analysis 2: Senior Citizen
    fig2, ax2 = plt.subplots()
    senior_counts = data['SeniorCitizen'].value_counts(normalize=True)
    senior_counts.plot(kind='bar', ax=ax2)
    ax2.set_title('Senior Citizen Distribution')
    figs.append(fig2)

    # Analysis 3: Partner and Dependents
    fig3, ax3 = plt.subplots()
    partner_counts = data['Partner'].value_counts(normalize=True)
    dependents_counts = data['Dependents'].value_counts(normalize=True)
    partner_counts.plot(kind='bar', ax=ax3, position=0, width=0.4, color='b', label='Partner')
    dependents_counts.plot(kind='bar', ax=ax3, position=1, width=0.4, color='r', label='Dependents')
    ax3.set_title('Partner and Dependents Distribution')
    ax3.legend()
    figs.append(fig3)

    # Save all figures
    save_figures(figs, 'reports/figures/analise_demografica')

def service_analysis(data):
    """
    Perform service analysis and save the figures.
    
    Parameters
    ----------
    data : DataFrame
        The data to analyze.
    
    Returns
    -------
    None
    """
    data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})
    
    service_columns = ['PhoneService', 'MultipleLines', 'InternetService', 
                   'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                   'TechSupport', 'StreamingTV', 'StreamingMovies']
    
    figs = []
    for service in service_columns:
        # Calculating the churn rate for each service
        churn_rate = data.groupby(service)['Churn'].mean()
        # Visualization of the churn rate for each service
        fig, ax = plt.subplots(figsize=(10, 4))
        churn_rate.plot(kind='bar', ax=ax)
        ax.set_title(f'Taxa de Churn por {service}')
        ax.set_ylabel('Taxa de Churn')
        figs.append(fig)
    
    # Save all figures
    save_figures(figs, 'reports/figures/analise_servicos')

def contract_gain_analysis(data):
    """
    Perform contract gain analysis and save the figures.
    
    Parameters
    ----------
    data : DataFrame
        The data to analyze.
    
    Returns
    -------
    None
    """
    figs = []

    # Analysis 1: Contract Churn Rates
    contract_churn_rates = data.groupby('Contract')['Churn'].mean()
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    contract_churn_rates.plot(kind='bar', ax=ax1)
    ax1.set_title('Taxa de Churn por Tipo de Contrato')
    ax1.set_ylabel('Taxa de Churn')
    figs.append(fig1)

    # Analysis 2: Paperless Billing Churn Rates
    paperless_churn_rates = data.groupby('PaperlessBilling')['Churn'].mean()
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    paperless_churn_rates.plot(kind='bar', ax=ax2)
    ax2.set_title('Taxa de Churn por Faturamento Sem Papel')
    ax2.set_ylabel('Taxa de Churn')
    figs.append(fig2)

    # Analysis 3: Payment Method Churn Rates
    payment_method_churn_rates = data.groupby('PaymentMethod')['Churn'].mean()
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    payment_method_churn_rates.plot(kind='bar', ax=ax3)
    ax3.set_title('Taxa de Churn por Método de Pagamento')
    ax3.set_ylabel('Taxa de Churn')
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
    figs.append(fig3)

    # Save all figures
    save_figures(figs, 'reports/figures/analise_contrato_faturamento')
    

def financial_analysis(data):
    """
    Perform financial analysis and save the figures.
    
    Parameters
    ----------
    data : DataFrame
        The data to analyze.
    
    Returns
    -------
    None
    """
    figs = []

    # Histograms of MonthlyCharges and TotalCharges
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    sns.histplot(data['MonthlyCharges'], kde=True, ax=ax1)
    ax1.set_title('Distribuição de MonthlyCharges')
    sns.histplot(data['TotalCharges'], kde=True, ax=ax2)
    ax2.set_title('Distribuição de TotalCharges')
    figs.append(fig1)

    # Scatter plot between Tenure and TotalCharges
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='tenure', y='TotalCharges', data=data, ax=ax3)
    ax3.set_title('Relação entre Tenure e TotalCharges')
    figs.append(fig2)

    # Save all figures
    save_figures(figs, 'reports/figures/analise_financeira')


def churn_analysis(data):
    """
    Perform churn analysis and save the figures.
    
    Parameters
    ----------
    data : DataFrame
        The data to analyze.
    
    Returns
    -------
    None
    """
    figs = []

    # Setting the style
    sns.set(style="whitegrid")

    # Creating figures for MonthlyCharges
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(x='Churn', y='MonthlyCharges', data=data, ax=ax1)
    ax1.set_title('Box Plot of Monthly Charges by Churn Status')
    sns.violinplot(x='Churn', y='MonthlyCharges', data=data, ax=ax2)
    ax2.set_title('Violin Plot of Monthly Charges by Churn Status')
    figs.append(fig1)

    # Creating figures for TotalCharges
    fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(x='Churn', y='TotalCharges', data=data, ax=ax3)
    ax3.set_title('Box Plot of Total Charges by Churn Status')
    sns.violinplot(x='Churn', y='TotalCharges', data=data, ax=ax4)
    ax4.set_title('Violin Plot of Total Charges by Churn Status')
    figs.append(fig2)

    # Save all figures
    save_figures(figs, 'reports/figures/analise_churn')


def roc_curve(y_test, y_pred_prob, model_name=''):
    """
    Plot the ROC curve.
    
    Parameters
    ----------
    y_test : array-like
        True labels.
    y_pred_prob : array-like
        Predicted probabilities.
    
    Returns
    -------
    None
    """
    from sklearn.metrics import roc_curve, roc_auc_score
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    auc = roc_auc_score(y_test, y_pred_prob)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()
    
    save_figures([plt.gcf()], f'models/{model_name}/roc_curve')

if __name__ == "__main__":
    # Load your data
    data = pd.read_excel('data/raw/customer-churn.xlsx')

    # Perform each analysis
    demographic_analysis(data)
    service_analysis(data)
    contract_gain_analysis(data)
    financial_analysis(data)
    churn_analysis(data)
    # Call more functions as needed
