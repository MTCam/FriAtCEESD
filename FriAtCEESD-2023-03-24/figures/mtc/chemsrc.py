def my_chem_sources(discr, q, eos):
  cv = split_conserved(dim, q)

  omega = eos.get_production_rates(cv)
  w = eos.get_species_molecular_weights()

  spec_src = w * omega
  rho_src = 0 * cv.mass
  mom_src = 0 * cv.momentum
  e_src = 0 * cv.energy

  return join_conserved(dim,
                  mass=rho_src,
                  energy=energy_src,
                  momentum=mom_src,
                  massfractions=spec_src)
