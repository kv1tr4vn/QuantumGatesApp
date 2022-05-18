from gates import *

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


def apply_scheme(scheme_string, input_array):
    gates_list = scheme_string.replace(' ', '').split('_')
    result_array = input_array
    for gate in gates_list:
        if gate == '':
            continue

        elif gate.startswith(SIGMA_X_NAME + '('):
            args_list = gate.replace(SIGMA_X_NAME + '(', '').replace(')', '').split(',')
            result_array = apply_sigma_x(result_array, int(args_list[0]) - 1)

        elif gate.startswith(SIGMA_Y_NAME + '('):
            args_list = gate.replace(SIGMA_Y_NAME + '(', '').replace(')', '').split(',')
            result_array = apply_sigma_y(result_array, int(args_list[0]) - 1)

        elif gate.startswith(SIGMA_Z_NAME + '('):
            args_list = gate.replace(SIGMA_Z_NAME + '(', '').replace(')', '').split(',')
            result_array = apply_sigma_z(result_array, int(args_list[0]) - 1)

    return result_array
