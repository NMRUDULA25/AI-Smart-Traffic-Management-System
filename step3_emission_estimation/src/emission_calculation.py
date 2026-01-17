import pandas as pd

# Load traffic data
data = pd.read_csv("../data/traffic_data.csv")

EMISSION_RATE = 2.3  # grams CO2 per second per vehicle

data["emission_fixed"] = data["waiting_time_fixed"] * EMISSION_RATE
data["emission_ai"] = data["waiting_time_ai"] * EMISSION_RATE

data["reduction"] = data["emission_fixed"] - data["emission_ai"]

print("\n=== CO₂ EMISSION ANALYSIS ===\n")
print(data)

total_fixed = data["emission_fixed"].sum()
total_ai = data["emission_ai"].sum()

print("\nTotal Emission (Fixed Signal):", total_fixed, "grams")
print("Total Emission (AI Signal):", total_ai, "grams")
print("Total CO₂ Reduction:", total_fixed - total_ai, "grams")
