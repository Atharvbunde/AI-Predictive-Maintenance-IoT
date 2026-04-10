import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    
    print("Columns in dataset:", data.columns)  # 👈 ADD THIS
    
    return data