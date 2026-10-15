import numpy as np
import pandas as pd
from fca_events import make_events

events = make_events(3_000, np.random.default_rng(2664), missing=.05)

measured_eta = ~np.isnan(events["eta"])
big_pt = events["pt"] > 5
central_eta = np.abs(events["eta"]) < 2.5
mask = measured_eta & big_pt & central_eta
cut_events = events[mask]

dfs = (events, cut_events)
sts = ("Before", "After")

print(f"Before the cut, there are {len(events)} particles in {events["event"].nunique()} events.")
print(f"After the cut, there are {len(cut_events)} particles in {cut_events["event"].nunique()} events.")

muon_events = cut_events[cut_events["ptype"] == "muon"]
opposite_dimuons = len(muon_events.groupby("event").agg(n=("pt", "size"), q=("charge", "sum")).query("n == 2 and q == 0"))

print(f"\nThere are {opposite_dimuons} events with exactly two muons of opposite charge.")

cut_events = cut_events.assign(pt_rel=cut_events["pt"] / cut_events.groupby("event")["pt"].transform("max"))
