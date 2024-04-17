import sys
import os

from sklearn.model_selection import train_test_split

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.features.build_features import build_features
from src.visualization.visualize import save_figures, roc_curve

def train_test_split_data(data, target='Churn', test_size=0.2, random_state=42):
    """
    Split data into training and test sets.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataframe containing features and target.
    target : str, default='Churn'
        Name of target column.
    test_size : float, default=0.2
        Fraction of data to include in the test split.
    random_state : int, default=42
        Seed for random number generator.
    
    Returns
    -------
    tuple
        Tuple containing training and test sets.
    """
    X = data.drop(columns=[target])
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a machine learning model.
    
    Parameters
    ----------
    X_train : pd.DataFrame
        Dataframe containing training features.
    y_train : pd.Series
        Series containing training target.
    
    Returns
    -------
    object
        Trained machine learning model.
    """
    import lightgbm as lgb
    
    model = lgb.LGBMClassifier(random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)
    
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate a machine learning model.
    
    Parameters
    ----------
    model : object
        Trained machine learning model.
    X_test : pd.DataFrame
        Dataframe containing test features.
    y_test : pd.Series
        Series containing test target.
    
    Returns
    -------
    dict
        Dictionary containing evaluation metrics.
    """
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }
    
    roc_curve(y_test, model.predict_proba(X_test)[:, 1], model_name=f"{type(model).__name__}_roc_curve")
    
    return metrics

def export_model(model, directory='models/'):
    """
    Export a trained model to a file.
    
    Parameters
    ----------
    model : object
        Trained machine learning model.
    directory : str, default='src/models/'
        Directory to save the model file.
    
    Returns
    -------
    None
    """
    import joblib
    import os
    
    # Get the name of the model's class
    model_name = type(model).__name__
    
    # Create the file path
    file_path = os.path.join(directory, f'{model_name}.pkl')
    
    joblib.dump(model, file_path)
    
    return None



if __name__ == '__main__':
    data = build_features('data/raw/customer-churn.xlsx')
    X_train, X_test, y_train, y_test = train_test_split_data(data)
    model = train_model(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)
    
    y_pred_prob = model.predict_proba(X_test)[:, 1]
    roc_curve(y_test, y_pred_prob, model_name=f"{type(model).__name__}_roc_curve")
    
    export_model(model)
    
    print(metrics)
    
    print('Model trained and saved successfully.')