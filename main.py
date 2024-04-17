def main():
    from src.features.build_features import build_features
    from src.models.train_model import train_test_split_data, train_model, evaluate_model, export_model

    data = build_features('data/raw/customer-churn.xlsx')

    X_train, X_test, y_train, y_test = train_test_split_data(data)

    model = train_model(X_train, y_train)

    metrics = evaluate_model(model, X_test, y_test)

    export_model(model, directory='models/')
    print(metrics)

if __name__ == "__main__":
    main()