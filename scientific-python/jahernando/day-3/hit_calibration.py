import numpy as np
import pandas as pd

rng = np.random.default_rng(2664)
n = 2000
hits = pd.DataFrame({'channel': rng.integers(0, 16, n),
                     'adc': rng.normal(500, 80, n).round()})
hits.loc[rng.random(n) < 0.03, 'channel'] = np.nan    # channel not decoded
gain = pd.Series(rng.normal(0.020, 0.002, 16).round(4), index=range(16))
gain = gain.drop([5, 11])

hits["channel"] = hits["channel"].astype("Int64")
hits_without_channel = sum(hits["channel"].isna())
print(f"There are {hits_without_channel} hits without channel.")

hits = hits.assign(energy=hits["channel"].map(gain))
hits_without_energy = sum(hits["energy"].isna())
because_no_calibration = sum(hits["channel"].isin([5, 11]))
print(f"\nThere are {hits_without_energy} hits with no energy; {hits_without_channel} because they have no channel and {because_no_calibration} because they have no calibration.")

saturation_mask = hits["adc"] > 700
hits.loc[saturation_mask, "energy"] = np.nan
grouped_by_channel = hits.groupby("channel").agg(number=("adc", "size"), mean_energy=("energy", "mean"))
print(f"\nPer channel, number of hits and mean energy:\n{grouped_by_channel}")
