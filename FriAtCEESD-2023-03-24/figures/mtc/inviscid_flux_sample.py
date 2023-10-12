def inviscid_flux(discr, eos, q):
    dim = discr.dim
    cv = split_conserved(dim, q)
    p = eos.pressure(cv)
    mom = cv.momentum
    massfrac = \
        (mom * cv.massfractions.reshape(-1, 1) / cv.mass)

    return join_conserved(dim, mass=mom, energy=mom * (cv.energy + p) / cv.mass,
            momentum=(np.outer(mom, mom) / cv.mass + np.eye(dim) * p),
            massfractions=massfrac)
