def inviscid_operator(discr, eos, boundaries, q, t=0.0, sources=None):
    # volume term: flux divergence
    vol_flux = inviscid_flux(discr, eos, q)
    dflux = discr.weak_div(vol_flux)

    # inter-element fluxes
    interior_face_flux=_facial_flux(discr,eos=eos,q_tpair=interior_trace_pair(discr,q))

    # Domain boundaries
    domain_boundary_flux=sum(
        _facial_flux(discr,q_tpair=boundary_pair(discr,eos=eos,btag=btag,t=t,q=q),
                     eos=eos) for btag in boundaries)

    # inter-element fluxes on partition boundaries
    partition_boundary_flux = sum(_facial_flux(discr, eos=eos, q_tpair=part_pair)
                                  for part_pair in cross_rank_trace_pairs(discr, q))

    facial_fluxes = interior_face_flux + domain_boundary_flux + partition_boundary_flux
    source_terms = sum(source(discr, q=q, eos=eos) for source in sources)

    return (source_terms + discr.inverse_mass(dflux - discr.face_mass(facial_fluxes)))
