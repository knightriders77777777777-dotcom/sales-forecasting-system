import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Create sample sales dataset
np.random.seed(42)

dates = pd.date_range(start="2026-01-01", periods=180)

sales = (
    500
    + np.arange(180) * 2
    + 50 * np.sin(np.arange(180) * 2 * np.pi / 7)
    + np.random.normal(0, 20, 180)
)

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})

# 2. Prepare data
df["Day"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Weekday"] = df["Date"].dt.dayofweek
df["Day_Number"] = np.arange(len(df))

X = df[["Day", "Month", "Weekday", "Day_Number"]]
y = df["Sales"]

# 3. Train and test model
X_train = X.iloc[:-30]
X_test = X.iloc[-30:]
y_train = y.iloc[:-30]
y_test = y.iloc[-30:]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# 4. Check model accuracy
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("SALES FORECASTING SYSTEM")
print("------------------------")
print("Mean Absolute Error:", round(mae, 2))

# 5. Forecast next 30 days
future_dates = pd.date_range(
    start=df["Date"].iloc[-1] + pd.Timedelta(days=1),
    periods=30
)

future = pd.DataFrame({
    "Date": future_dates
})

future["Day"] = future["Date"].dt.day
future["Month"] = future["Date"].dt.month
future["Weekday"] = future["Date"].dt.dayofweek
future["Day_Number"] = np.arange(180, 210)

future_X = future[["Day", "Month", "Weekday", "Day_Number"]]

future["Predicted_Sales"] = model.predict(future_X)

# 6. Display forecast
print("\nNEXT 30 DAYS SALES PREDICTION")
print(future[["Date", "Predicted_Sales"]].to_string(index=False))

# 7. Save results
df.to_csv("sales_data.csv", index=False)
future.to_csv("forecast_results.csv", index=False)

# 8. Display graph
plt.figure(figsize=(12, 6))

plt.plot(
    df["Date"],
    df["Sales"],
    label="Historical Sales"
)

plt.plot(
    future["Date"],
    future["Predicted_Sales"],
    label="Future Sales Prediction",
    linestyle="--"
)

plt.title("Sales Forecasting System")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("sales_forecast.png")
plt.show()

print("\nProject completed successfully!")
print("Files and graph saved successfully.")