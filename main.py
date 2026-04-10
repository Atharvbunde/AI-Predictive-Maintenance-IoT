from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.train_model import train_model
from src.visualize import plot_results

# Load data
data = load_data("data/iot_sensor_data.csv")

# Preprocess
X, y = preprocess_data(data)

# Train model
y_test, y_pred = train_model(X, y)
# Visualization
plot_results(y_test, y_pred)