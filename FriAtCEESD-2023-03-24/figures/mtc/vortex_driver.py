def main(ctx_factory=cl.create_some_context):
    ( ... )
    eos = IdealSingleGas()
    initializer = Vortex2D(center=orig, velocity=vel)
    casename = "vortex"
    boundaries = {BTAG_ALL: PrescribedBoundary(initializer)}

    generate_grid = ( ... )
    local_mesh, global_nelements = create_parallel_grid(comm, generate_grid)
    local_nelements = local_mesh.nelements

    discr = EagerDGDiscretization(actx, local_mesh, order=order, mpi_communicator=comm)
    current_state = initializer(0, nodes)

    def my_rhs(t, state):
        return inviscid_operator(discr, q=state, t=t, boundaries=boundaries,eos=eos)

    final_state = advance_state(rhs=my_rhs,state=current_state, t=current_t, t_final=t_final)
