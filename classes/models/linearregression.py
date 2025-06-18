import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class Model:
    def __init__(self):
        self.model = LinearRegression()
        self.data = None
        self.x = None
        self.y = None
        self.trained = False

    def get_data(self, data: pd.DataFrame, target_column: str):
        if target_column not in data.columns:
            raise ValueError(f"Target column '{target_column}' not found in dataframe.")

        self.data = data
        self.y = data[target_column]
        self.x = data.drop(columns=[target_column])

    def train_model(self, test_size=0.2, random_state=42):
        if self.x is None or self.y is None:
            raise ValueError("Data's not been loaded yet. Use get_data() first.")

        x_train, x_test, y_train, y_test = train_test_split(
            self.x, self.y, test_size=test_size, random_state=random_state
        )
        self.model.fit(x_train, y_train)
        self.trained = True

    def predict(self, new_data: pd.DataFrame):
        if not self.trained:
            raise RuntimeError("Model's not been trained yet. Use train_model() first.")

        return self.model.predict(new_data)
