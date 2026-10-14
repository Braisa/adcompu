import numpy as np
from scipy.special import gamma

rng = np.random.default_rng(2664)

L, N = 10., 1_000

r = rng.uniform(0, L, (N, 3))

def dist_box(r, L, pbc=True):
    dr = r[np.newaxis, :] - r[:, np.newaxis]
    if pbc:
        dr -= L * np.round(dr/L)
    ds = np.sqrt(np.sum(dr**2, axis=-1))
    return ds

ds = dist_box(r, L)

print("Checking:")
print(f"ds shape: {ds.shape}")
print(f"ds symmetric: {np.all(ds == ds.T)}")
print(f"no distance over sqrt(3)/2 L: {np.all(ds < np.sqrt(3)/2*L)}")

ds_nopbc = dist_box(r, L, pbc=False)
strs = ("with", "without")

expected_mean_nnd = gamma(4/3) * np.power(4*np.pi/3*N/L**3, -1/3)
print(f"\nExpected mean nearest neighbor distance: {expected_mean_nnd}")
for d, st in zip((ds, ds_nopbc), strs):
    nearest_neighbor_distance = np.sort(d, axis=0)[1]
    mean_nnd = np.mean(nearest_neighbor_distance)
    dev_nnd = np.power(N*(N-1), -1/2) * np.sqrt(np.sum((nearest_neighbor_distance - mean_nnd)**2))
    within_error = mean_nnd - dev_nnd <= expected_mean_nnd <= mean_nnd + dev_nnd

    print(f"Computing {st} pbc:")
    print(f"- Mean nearest neighbor distance {st} pbc: {mean_nnd}")
    print(f"- Statistical error {st} pbc: {dev_nnd}")
    print(f"- Is expected within error: {within_error}")

