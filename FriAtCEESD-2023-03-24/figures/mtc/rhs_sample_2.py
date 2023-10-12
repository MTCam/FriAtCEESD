    # Flux across partition boundaries
    partition_boundary_flux = sum(
        _facial_flux(discr, eos=eos, q_tpair=part_pair)
        for part_pair in cross_rank_trace_pairs(discr, q)
    )

    return discr.inverse_mass(
        dflux - discr.face_mass(interior_face_flux + domain_boundary_flux
                                + partition_boundary_flux)
    )
