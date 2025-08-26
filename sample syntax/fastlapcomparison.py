# F1 Data Analysis: F1 Ferrari Drivers

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fastf1
from fastf1.core import Laps

# Creating / Enabling Caching
fastf1.Cache.enable_cache('cache')  # 'cache' is the folder name

# Load the Qualifying Session
session = fastf1.get_session(2024, 'Monaco', 'Q') # get_session(year, 'gran prix', 'Q = Qualifyer or R = Race')
session.load()

# Select Drivers
ferrari_one = 'LEC' # Charles Leclerc
ferrari_two = 'HAM' # Lewis Hamilton

# Get all laps and filter for fastest lap
laps_driver1 = session.laps.pick_driver(ferrari_one).sort_values('LapTime').iloc[0]
laps_driver2 = session.laps.pick_driver(ferrari_two).sort_values('LapTime').iloc[0]

# Merge lap data for comparison
fastest_laps = pd.DataFrame([laps_driver1, laps_driver2])

# Plot lap times
plt.figure(figsize=(8, 4))
plt.bar([ferrari_one, ferrari_two], fastest_laps['LapTime'].dt.total_seconds(), color=['blue', 'red'])
plt.ylabel('Lap Time (seconds)')
plt.title('Fastest Lap Comparison')
plt.show()

# Plot Telemetry Data
tel1 = laps_driver1.get_telemetry()
tel2 = laps_driver2.get_telemetry()

plt.figure(figsize=(10, 5))
plt.plot(tel1['Distance'], tel1['Speed'], label=ferrari_one)
plt.plot(tel2['Distance'], tel2['Speed'], label=ferrari_two)
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.title('Speed Comparison')
plt.legend()
plt.show()
