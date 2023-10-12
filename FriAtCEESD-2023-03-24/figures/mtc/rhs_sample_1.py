def inviscid_operator(discr, eos, boundaries, q, t=0.0):
    vol_flux = inviscid_flux(discr, eos, q)
    dflux = discr.weak_div(vol_flux)

    interior_face_flux = _facial_flux(
        discr, eos=eos, q_tpair=interior_trace_pair(discr, q))

    # Domain boundaries
    domain_boundary_flux = sum(
        _facial_flux(
            discr,
            q_tpair=\
            boundaries[btag].boundary_pair(
                discr, eos=eos, btag=btag,
                t=t, q=q), eos=eos
        )
        for btag in boundaries
    )
