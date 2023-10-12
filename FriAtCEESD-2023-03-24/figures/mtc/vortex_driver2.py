nodes = thaw(actx, discr.nodes())
current_state = initializer(0, nodes)

def my_rhs(t, state):
    return inviscid_operator(
        discr, q=state, t=t,
        boundaries=boundaries,eos=eos)

final_state = advance_state(rhs=my_rhs,
               timestepper=timestepper,
               checkpoint=sim_checkpoint,
               get_timestep=get_timestep,
               state=current_state,
               t=current_t, t_final=t_final)
