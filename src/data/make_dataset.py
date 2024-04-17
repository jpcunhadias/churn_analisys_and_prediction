import pandas as pd

def load_data(file_path='data/raw/customer-churn.xlsx'):
    data = pd.read_excel(file_path)
    return data

def preprocess_data(data):
    data = data.drop(columns=['customerID'])
    data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})
    data['TotalCharges'] = data['TotalCharges'].fillna(0)
    data['gender'] = data['gender'].map({'Male': 0, 'Female': 1})
    
    binary_columns = ['Partner', 'Dependents']
    for column in binary_columns:
        data[column] = data[column].map({'No': 0, 'Yes': 1})
    
    return data
    

def save_data(data, file_path=""):
    data.to_excel(file_path, index=False)
    return None

if __name__ == '__main__':
    data = load_data('data/raw/customer-churn.xlsx')
    data = preprocess_data(data)
    save_data(data, file_path='data/processed/customer_churn_processed.xlsx')
    print('Data processed and saved successfully.')