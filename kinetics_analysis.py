import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Photocatalytic dye degradation data
kinetics_data = {
    "Time_min": [0, 10, 20, 30, 40, 50],
    "Run1_mol_L": [0.8, 0.54, 0.36, 0.24, 0.16, 0.11],
    "Run2_mol_L": [0.8, 0.44, 0.24, 0.13, 0.07, 0.04],
}

kinetics_df = pd.DataFrame(kinetics_data)
print("Kinetics data:")
print(kinetics_df)

kinetics_df.to_csv("kinetics.csv", index=False)
kinetics_df.to_json("kinetics.json", orient="records", indent=2)

# Read the CSV file back and inspect its shape and data types.
kinetics_from_csv = pd.read_csv("kinetics.csv")
print("\nCSV shape:", kinetics_from_csv.shape)
print("\nCSV data types:")
print(kinetics_from_csv.dtypes)

# Calculate and compare sample standard deviations.
run1_mean = kinetics_from_csv["Run1_mol_L"].mean()
run1_std = kinetics_from_csv["Run1_mol_L"].std()
run2_mean = kinetics_from_csv["Run2_mol_L"].mean()
run2_std = kinetics_from_csv["Run2_mol_L"].std()

print(f"\nRun 1 mean: {run1_mean:.4f} mol/L")
print(f"Run 1 standard deviation: {run1_std:.4f} mol/L")
print(f"Run 2 mean: {run2_mean:.4f} mol/L")
print(f"Run 2 standard deviation: {run2_std:.4f} mol/L")

if run1_std > run2_std:
    print("Run 1 shows more variation.")
elif run2_std > run1_std:
    print("Run 2 shows more variation.")
else:
    print("Both runs show the same variation.")

# Plot both photocatalytic degradation runs.
plt.figure()
plt.plot(
    kinetics_from_csv["Time_min"],
    kinetics_from_csv["Run1_mol_L"],
    marker="o",
    label="Run 1 (low UV)",
)
plt.plot(
    kinetics_from_csv["Time_min"],
    kinetics_from_csv["Run2_mol_L"],
    marker="s",
    label="Run 2 (high UV)",
)
plt.title("Photocatalytic Dye Degradation")
plt.xlabel("Time (min)")
plt.ylabel("Concentration (mol/L)")
plt.legend()
plt.grid(True)

# Isothermal compression data
pressure_volume_df = pd.DataFrame(
    {
        "Volume_L": [2, 3, 4, 5, 6],
        "Pressure_bar": [3.01, 1.98, 1.52, 1.19, 1.01],
    }
)

pressure_volume_df["PV_bar_L"] = (
    pressure_volume_df["Pressure_bar"] * pressure_volume_df["Volume_L"]
)
k = pressure_volume_df["PV_bar_L"].mean()
print(f"\nMean value of P*V (k): {k:.4f} bar L")

# Draw P = k/V over the measured volume range.
reference_volume = np.linspace(
    pressure_volume_df["Volume_L"].min(),
    pressure_volume_df["Volume_L"].max(),
    100,
)
reference_pressure = k / reference_volume

plt.figure()
plt.scatter(
    pressure_volume_df["Volume_L"],
    pressure_volume_df["Pressure_bar"],
    label="Measured data",
)
plt.plot(reference_volume, reference_pressure, label=f"Reference curve (k={k:.2f} bar L)")
plt.title("Pressure vs. Volume During Isothermal Compression")
plt.xlabel("Volume (L)")
plt.ylabel("Pressure (bar)")
plt.legend()
plt.grid(True)

plt.show()