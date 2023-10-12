    def my_rhs(t, state):
        return (
            ns_operator(discr, cv=state, t=t, boundaries=boundaries, eos=eos)
            + av_operator(discr, q=state.join(), boundaries=boundaries,
                          boundary_kwargs={"time": t, "eos": eos}, alpha=alpha_av,
                          s0=s0_av, kappa=kappa_av)
            + sponge(cv=state, cv_ref=ref_state, sigma=sponge_sigma)
        )

