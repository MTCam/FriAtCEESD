def inviscid_flux(discr, eos, cv):
    dim = cv.dim
    p = eos.pressure(cv)
    mom = cv.momentum
    return make_conserved(
        dim, mass=mom, energy=mom * (cv.energy + p) / cv.mass,
        momentum=np.outer(mom, mom) / cv.mass + np.eye(dim)*p,
        species_mass=(  # reshaped: (nspecies, dim)
            (mom / cv.mass) * cv.species_mass.reshape(-1, 1)))
