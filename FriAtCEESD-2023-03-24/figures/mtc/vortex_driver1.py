eos = IdealSingleGas()
initializer = Vortex2D(center=orig, velocity=vel)
boundaries = { BTAG_ALL:
    PrescribedBoundary(initializer)
}

generate_grid = partial(
    generate_regular_rect_mesh,
    a=(box_ll,) * dim,
    b=(box_ur,) * dim, n=(nel_1d,) * dim
    )
mesh = create_parallel_grid(mpicomm,
                            generate_grid)

discr = EagerDGDiscretization(
    actx, mesh, order=order, mpicomm
)
