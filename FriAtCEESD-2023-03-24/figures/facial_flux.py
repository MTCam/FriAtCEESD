def flux_lfr(cv_tpair, f_tpair, normal, lam):
    return make_conserved(
        dim=cv_tpair.int.dim,
        q=(f_tpair.avg.join() - lam*np.outer(cv_tpair.diff.join(), normal)/2)
    )
