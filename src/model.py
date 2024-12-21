from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

class VirtualGaugeModel:
    def __init__(self):
        self.model = LinearRegression()
        self.is_trained = False

    def train(self, X, y):
        """
        Train the model on the given dataset.
        """
        self.model.fit(X, y)
        self.is_trained = True

    def predict(self, X):
        """
        Infer output variable from input data.
        """
        if not self.is_trained:
            raise Exception("Model must be trained before predictions can be made.")
        return self.model.predict(X)

    def run_inference(self, data, input_vars, output_var):
        """
        Full pipeline: Train, predict, and output results.
        """
        X = data[input_vars]
        y = data[output_var] if output_var in data.columns else None

        if y is not None:
            self.train(X, y)
        
        predictions = self.predict(X)
        result = pd.DataFrame({
            "input_data": X.to_dict(orient='records'),
            output_var: predictions
        })
        return result
