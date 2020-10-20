"""Quickstart Circuit Tutorial from https://strawberryfields.readthedocs.io/en/stable/introduction/circuits.html"""

import strawberryfields as sf
from strawberryfields import ops

def test_quickstart():
    # create a 3-mode quantum program
    prog = sf.Program(3)

    with prog.context as q:
        ops.Sgate(0.54) | q[0]
        ops.Sgate(0.54) | q[1]
        ops.Sgate(0.54) | q[2]
        ops.BSgate(0.43, 0.1) | (q[0], q[2])
        ops.BSgate(0.43, 0.1) | (q[1], q[2])
        ops.MeasureFock() | q

    # intialize the fock backend with a
    # Fock cutoff dimension (truncation) of 5
    eng = sf.Engine("fock", backend_options={"cutoff_dim": 5})

    # run the program
    result = eng.run(prog)

    # Really just making sure we get this far. We're assuming Strawberry Fields was tested on its own.
    assert result.state.num_modes == 3
    assert result.state.cutoff_dim == 5

    print(result.state)

def test_symbolic_parameters():
    # create a 2-mode quantum program
    prog = sf.Program(2)

    # create a free parameter named 'a'
    a = prog.params('a')

    # define the program
    with prog.context as q:
        ops.Dgate(a ** 2)    | q[0]  # free parameter
        ops.MeasureX         | q[0]  # measure qumode 0, the result is used in the next operation
        ops.Sgate(1 - sf.math.sin(q[0].par)) | q[1]  # measured parameter
        ops.MeasureFock()    | q[1]

    # intialize the Fock backend
    eng = sf.Engine('fock', backend_options={'cutoff_dim': 5})

    # run the program, with the free parameter 'a' bound to the value 0.9
    result = eng.run(prog, args={'a': 0.9})

    # Really just making sure we get this far. We're assuming Strawberry Fields was tested on its own.
    assert result.state.num_modes == 2
    assert result.state.cutoff_dim == 5

    print(result.state)