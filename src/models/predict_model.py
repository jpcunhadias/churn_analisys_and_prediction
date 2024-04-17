import joblib

def load_model(model_path):
    """
    Load a trained model from a file.
    
    Parameters
    ----------
    model_path : str
        Path to the model file.
    
    Returns
    -------
    model : object
        Trained machine learning model.
    """
    model = joblib.load(model_path)
    return model

def predict(model, data):
    """
    Make a prediction using a trained model.
    
    Parameters
    ----------
    model : object
        Trained machine learning model.
    data : array-like
        Data to make predictions on.
    
    Returns
    -------
    predictions : array-like
        Predictions made by the model.
    """
    predictions = model.predict(data)
    return predictions

if __name__ == "__main__":
    # Load the model
    model = load_model('src/models/YourModelName.pkl')

    # Example data to make predictions on
    data = [[5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]]

    # Make a prediction
    predictions = predict(model, data)

    print(predictions)