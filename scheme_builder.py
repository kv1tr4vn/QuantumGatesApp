SIGMA_X_NAME = 'sigX'
SIGMA_Y_NAME = 'sigY'
SIGMA_Z_NAME = 'sigZ'
HADAMARD_NAME = 'H'
WALSH_HADAMARD_NAME = 'WH'
CNOT_NAME = 'CN'
CCNOT_NAME = 'CCN'
PHASE_NAME = 'PH'
TRANSITION_NAME = '_'


def add_apply_sigma_x(scheme_string, qubit_ind):
    return scheme_string + TRANSITION_NAME + SIGMA_X_NAME + '(' + str(qubit_ind + 1) + ')'


def add_apply_sigma_y(scheme_string, qubit_ind):
    return scheme_string + TRANSITION_NAME + SIGMA_Y_NAME + '(' + str(qubit_ind + 1) + ')'


def add_apply_sigma_z(scheme_string, qubit_ind):
    return scheme_string + TRANSITION_NAME + SIGMA_Z_NAME + '(' + str(qubit_ind + 1) + ')'


def add_apply_hadamard(scheme_string, qubit_ind):
    return scheme_string + TRANSITION_NAME + HADAMARD_NAME + '(' + str(qubit_ind + 1) + ')'


def add_apply_walsh_hadamard(scheme_string):
    return scheme_string + TRANSITION_NAME + WALSH_HADAMARD_NAME + '()'


def add_apply_cnot(scheme_string, control_qubit_ind, target_qubit_ind):
    return scheme_string + TRANSITION_NAME + CNOT_NAME + '(' + \
           str(control_qubit_ind + 1) + ',' + str(target_qubit_ind + 1) + ')'


def add_apply_ccnot(scheme_string, first_control_qubit_ind, second_control_qubit_ind, target_qubit_ind):
    return scheme_string + TRANSITION_NAME + CCNOT_NAME + '(' + str(first_control_qubit_ind + 1) + ',' + \
           str(second_control_qubit_ind + 1) + ',' + str(target_qubit_ind + 1) + ')'


def add_apply_phase(scheme_string, control_qubit_ind, target_qubit_ind, phase):
    return scheme_string + TRANSITION_NAME + PHASE_NAME + '(' + str(control_qubit_ind + 1) + ',' + \
           str(target_qubit_ind + 1) + ',' + str(phase) + ')'
