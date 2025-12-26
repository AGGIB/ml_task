import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
import logging

logging.getLogger("cmdstanpy").setLevel(logging.WARNING)

np.random.seed(42)
df = pd.DataFrame({
    'ds': pd.date_range(start='2025-12-26', periods=30),
    'y': np.random.randint(50, 100, size=30)
})

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=5)
forecast = model.predict(future)

print(forecast[['ds', 'yhat']].tail(5))

plt.plot(df['ds'], df['y'], label='Исходные', marker='o')
plt.plot(forecast['ds'][-5:], forecast['yhat'][-5:], label='Прогноз', marker='x', color='red')
plt.title("Прогноз временного ряда на 5 дней")
plt.xlabel("Дата")
plt.ylabel("Значение")
plt.legend()
plt.show()
