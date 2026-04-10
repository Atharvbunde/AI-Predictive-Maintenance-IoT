def preprocess_data(data):
    data = data.dropna()

    X = data[['temperature', 'vibration', 'current']]
    y = data['failure']

    return X, y