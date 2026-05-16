python
from statsmodels.tsa.arima.model import ARIMA
from .abstract_agent import AbstractAgent
import pandas as pd
class ForecastingAgent(AbstractAgent):
    def __init__(self):
        pass
    def process(self, input):
        return self.forecast(input["data"], input["n_steps"])
    def forecast(self, data, n_steps):
        model = ARIMA(data, order=(5,1,0))
        model_fit = model.fit()
        forecast_steps = model_fit.forecast(steps=n_steps)
        return forecast_steps
