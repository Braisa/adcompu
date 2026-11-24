import numpy as np
import pandas as pd
from matplotlib.pyplot import subplot_mosaic, subplots
import seaborn as sns
from cmasher import get_sub_cmap

mean = lambda z : sum(z) / len(z)
var = lambda z : sum((z - mean(z))**2) / len(z)
cov = lambda x, y : mean(x*y) - mean(x)*mean(y)
def cov_matrix(x, y):
    cov_matrix = np.zeros((2,2))
    cov_matrix[0, 0] = cov(x, x)
    cov_matrix[0, 1] = cov(x, y)
    cov_matrix[1, 0] = cov(y, x)
    cov_matrix[1, 1] = cov(y, y)
    return cov_matrix

df = pd.read_csv("multivariate-methods/juan/pca/NBA.csv")

fig, axs = subplot_mosaic([["sc", "scree", "vec"], ["sc_m", "scree_m", "vec_m"], ["sc_st", "scree_st", "vec_st"]], figsize=(18, 18))

ppg_or, apg_or = df["PPG"], df["APG"]
ppg_min, apg_min = df["PPG"]/df["MPG"], df["APG"]/df["MPG"]
st_ppg_min, st_apg_min = (ppg_min - mean(ppg_min))/var(ppg_min), (apg_min - mean(apg_min))/var(apg_min)

ppgs = (ppg_or, ppg_min, st_ppg_min)
apgs = (apg_or, apg_min, st_apg_min)
axns = ("", "_m", "_st")
xlabs = ("PPG", "PPG/MPG", "Standardized PPG/MPG")
ylabs = ("APG", "APG/MPG", "Standardized APG/MPG")

for axn, xlab, ylab, ppg, apg in zip(axns, xlabs, ylabs, ppgs, apgs):
    data_cov = cov_matrix(ppg, apg)
    eig_values, eig_vectors = np.linalg.eig(data_cov)

    axs[f"sc{axn}"].plot(ppg, apg, ".", color="tab:purple", alpha=.2)

    axs[f"sc{axn}"].set_xlabel(xlab)
    axs[f"sc{axn}"].set_ylabel(ylab)

    axs[f"scree{axn}"].plot(np.arange(len(eig_values)), sorted(np.real(eig_values))[::-1], "o", color="tab:orange")

    axs[f"scree{axn}"].set_xticks((0, 1))

    axs[f"scree{axn}"].set_xlabel(r"Index")
    axs[f"scree{axn}"].set_ylabel(r"Eigenvalue")

    for vec in eig_vectors.T:
        axs[f"vec{axn}"].quiver(0, 0, vec[0], vec[1])

    axs[f"vec{axn}"].set_xlim(left=-1, right=1)
    axs[f"vec{axn}"].set_ylim(bottom=-1, top=1)

fig.savefig("multivariate-methods/juan/pca/nba_small_pcas.pdf", bbox_inches="tight")

df_big = df[["PPG", "APG", "RPG", "TPG", "SPG", "BPG", "3PA", "2PA", "3P%", "2P%"]]
st_df_big = df_big.copy()
for col in df_big.columns:
    st_df_big[col] = (df_big[col] - mean(df_big[col])) / var(df_big[col])

big_cov_matrix = np.cov(st_df_big.T)
big_eig_values, big_eig_vectors = np.linalg.eig(big_cov_matrix)

sorted_big_eig_values, sorted_big_eig_vectors = [list(t) for t in zip(*sorted(zip(big_eig_values, big_eig_vectors), reverse=True))]

bfig, bax = subplots()

bax.plot(np.arange(len(sorted_big_eig_values)), np.real(sorted_big_eig_values), "o", color="tab:orange")

bax.set_xticks(np.arange(len(sorted_big_eig_values)))

bax.set_xlabel("Index")
bax.set_ylabel("Eigenvalue")

bfig.savefig("multivariate-methods/juan/pca/nba_big_pca.pdf", bbox_inches="tight")

sfig, sax = subplots(figsize=(10,10))

sns.heatmap(np.real(sorted_big_eig_vectors), ax=sax, annot=True, cmap=get_sub_cmap("viridis", .2, .8))

column_names = list(st_df_big.columns)
sax.set_yticklabels(column_names)

sfig.savefig("multivariate-methods/juan/pca/nba_big_pca_heatmap.pdf", bbox_inches="tight")
