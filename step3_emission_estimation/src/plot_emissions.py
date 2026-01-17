import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure results folder exists
os.makedirs("../results", exist_ok=True)

# Load data
#data = pd.read_csv("../data/traffic_data.csv")

BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "../data/traffic_data.csv")

data = pd.read_csv(csv_path)


EMISSION_RATE = 2.3

data["emission_fixed"] = data["waiting_time_fixed"] * EMISSION_RATE
data["emission_ai"] = data["waiting_time_ai"] * EMISSION_RATE

# ----- BAR CHART -----
total_fixed = data["emission_fixed"].sum()
total_ai = data["emission_ai"].sum()

plt.figure()
plt.bar(["Fixed Signal", "AI Signal"], [total_fixed, total_ai])
plt.xlabel("Traffic Signal Type")
plt.ylabel("Total CO₂ Emission (grams)")
plt.title("CO₂ Emission Comparison")
plt.savefig("../results/emission_comparison.png")
plt.show()

# ----- LINE CHART -----
plt.figure()
plt.plot(data["episode"], data["emission_fixed"], label="Fixed Signal")
plt.plot(data["episode"], data["emission_ai"], label="AI Signal")
plt.xlabel("Episode")
plt.ylabel("CO₂ Emission (grams)")
plt.title("Emission Trend Over Episodes")
plt.legend()
plt.show()
