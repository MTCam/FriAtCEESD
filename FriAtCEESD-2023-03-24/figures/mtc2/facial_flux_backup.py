def _facial_flux(discr, eos, q_tpair, local=False):
    dim = discr.dim
    actx = q_tpair[0].int.array_context

    flux_int = inviscid_flux(discr, eos, q_tpair.int)
    flux_ext = inviscid_flux(discr, eos, q_tpair.ext)

    # Lax-Friedrichs/Rusanov after [Hesthaven_2008]_, Section 6.6
    flux_avg = 0.5*(flux_int + flux_ext)

    lam = actx.np.maximum(
        _get_wavespeed(dim, eos=eos, cv=split_conserved(dim, q_tpair.int)),
        _get_wavespeed(dim, eos=eos, cv=split_conserved(dim, q_tpair.ext))
    )

    normal = thaw(actx, discr.normal(q_tpair.dd))
    flux_weak = (
        flux_avg * normal
        - 0.5 * lam * (q_tpair.ext - q_tpair.int))

    return flux_weak
