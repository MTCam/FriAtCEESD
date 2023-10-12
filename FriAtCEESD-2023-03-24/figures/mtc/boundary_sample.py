def boundary_pair(
        self, discr, q, btag, eos, t=0.0
):
    actx = q[0].array_context    
    boundary_discr = discr.discr_from_dd(btag)
    nodes = thaw(actx, boundary_discr.nodes())

    ext_soln = self._userfunc(t, nodes)
    int_soln = discr.project("vol", btag, q)

    return TracePair(btag, interior=int_soln,
                     exterior=ext_soln)
