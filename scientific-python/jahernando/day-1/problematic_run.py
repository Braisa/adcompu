import numpy as np

rng = np.random.default_rng(2664)

n = 6_000

time = rng.uniform(0, 120, n)
chan = rng.integers(0, 12, n)
energy = rng.exponential(1.5, n)

# Detector workings
hot = rng.random(n) < .08
chan[hot] = 7
energy[hot] = rng.exponential(.2, hot.sum())
off = (time > 61.3) & (time < 68.9)
time, chan, energy = time[~off], chan[~off], energy[~off]
energy[rng.random(time.size) < .03] = np.nan

time_order = np.argsort(time)
time, chan, energy = time[time_order], chan[time_order], energy[time_order]

failed_readouts = np.isnan(energy)
time, chan, energy = time[~failed_readouts], chan[~failed_readouts], energy[~failed_readouts]
print(f"Number of failed readouts: {sum(failed_readouts)}\n")

events_per_channel = np.bincount(chan)
mean_energy_per_channel = np.bincount(chan, weights=energy) / events_per_channel
for channel, (events, mean_energy) in enumerate(zip(events_per_channel, mean_energy_per_channel)):
    print(f"Channel {channel:02} with {events} events has mean energy: {mean_energy}")

time_cutoff = np.where(np.diff(time) > 1)[0][0]
print(f"\nDetector turned off from t = {time[time_cutoff]:.2f} s to t = {time[time_cutoff+1]:.2f} s")
