__author__ = 'agross'

import pandas as pd
import numpy as np
import scipy as sp

from scipy.stats import binom_test

from Helpers.LinAlg import frame_svd
from Helpers.Pandas import true_index
from Stats.Scipy import ttest_rel


def binomial_test_screen(df, fc=1.5, p=.5):
    """
    Run a binomial test on a DataFrame.

    df:
        DataFrame of measurements.  Should have a multi-index with
        subjects on the first level and tissue type ('01' or '11')
        on the second level.
    fc:
        Fold-chance cutoff to use
    """
    a, b = df.xs('01', 1, 1), df.xs('11', 1, 1)
    dx = a - b
    dx = dx[dx.abs() > np.log2(fc)]
    n = dx.count(1)
    counts = (dx > 0).sum(1)
    cn = pd.concat([counts, n], 1)
    cn = cn[cn.sum(1) > 0]
    b_test = cn.apply(lambda s: binom_test(s[0], s[1], p), axis=1)
    dist = (1.*cn[0] / cn[1])
    tab = pd.concat([cn[0], cn[1], dist, b_test],
                    keys=['num_ox', 'num_dx', 'frac', 'p'],
                    axis=1)
    return tab


def pull_out_tn(df, assoication_cutoff=.001):
    """
    Does a reconstruction of the data with on only eigenvectors
    associated with the tumor-normal axis.

    This is done by calculating the signular-value-decomposition
    of the matrix, searching for associations of each eigenvector
    with the tumor-normal change, and finally reconstructing the
    matrix with those not significantly associated zero-ed out.

    Returns a DataFrame of the reconstructed data matrix.

    df:
        DataFrame of measurements.  Should have a multi-index with
        subjects on the first level and tissue type ('01' or '11')
        on the second level.
    """
    df = pd.concat([df.xs('01',1,1), df.xs('11',1,1)],
                    keys=['01','11'], axis=1)
    df.columns = df.columns.swaplevel(0,1)

    svd = frame_svd(df)
    keep = svd[2].apply(ttest_rel).T.p < assoication_cutoff
    S = pd.Series(svd[1]) * 1.*keep
    S = pd.DataFrame(sp.linalg.diagsvd(S, len(S), len(S)), index=S.index,
                     columns=S.index)
    df_new = svd[0].dot(S).dot(svd[2].T)
    return df_new


def infer_normal_knn(df, r_curtoff=.4, k=5):
    """
    Preform imputation to predict normal expression levels.

    r_curtoff:
        Correlation cutoff to use for isolating genes to use for nearest
        neighbor calclulation.  The idea here is that we want to use those
        genes that are not differentially expressed between tumor and nornal
        tissue to find patients that are similar.  The goal of this operation
        is for the KNN to find patients that are similar in their normal
        tissue expression profiles rather than patients with similar tumor
        profiles.  The normal tissue can be influenced by a number of factors
        including specific tissue location, age and gender of patient, general
        health of patient, ect.
    k:
        K-nearest-neighbor parameter
    """
    df = df.dropna(axis=[0, 1])
    tumor = df.xs('01', 1, 1)
    normal = df.xs('11', 1, 1)
    tn_corr = tumor.corrwith(normal, axis=1).dropna()
    tumor_corr = tumor.ix[true_index(tn_corr > r_curtoff)].corr()

    pts = tumor_corr.index.intersection(normal.columns)
    nn = pd.Series({i: list(v.ix[pts].order().index[-1 * k:]) for i, v
                    in tumor_corr.iteritems()})
    nn = nn[nn.map(len) > 1]
    norm_inf = pd.DataFrame({i: normal.ix[:, n].mean(1) for i, n in
                             nn.iteritems()})
    tn_c = pd.concat([norm_inf, tumor.ix[:, norm_inf.columns]],
                     keys=['11', '01'], axis=1)
    tn_c.columns = tn_c.columns.swaplevel(0, 1)
    tn_c = tn_c.sortlevel(axis=1, level=0)
    return tn_c