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


def add_apply_phase(scheme_string, control_qubit_ind, target_qubit_ind, phase_in_fractions_of_pi):
    return scheme_string + TRANSITION_NAME + PHASE_NAME + '(' + str(control_qubit_ind + 1) + ',' + \
           str(target_qubit_ind + 1) + ',' + str(phase_in_fractions_of_pi) + ')'


def apply_scheme(scheme_string, input_array):
    gates_list = scheme_string.replace(' ', '').split('_')
    result_array = input_array
    for gate_string in gates_list:
        for array_ind in range(result_array.size):
            result_array[array_ind] = sp.simplify(result_array[array_ind])

        def is_gate(gate_name):
            return gate_string.startswith(gate_name + '(')

        def gate_args(gate_name):
            return gate_string.replace(gate_name + '(', '').replace(')', '').split(',')

        if gate_string == '':
            continue

        elif is_gate(SIGMA_X_NAME):
            args_list = gate_args(SIGMA_X_NAME)
            if len(args_list) != 1:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_sigma_x(result_array, int(args_list[0]) - 1)

        elif is_gate(SIGMA_Y_NAME):
            args_list = gate_args(SIGMA_Y_NAME)
            if len(args_list) != 1:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_sigma_y(result_array, int(args_list[0]) - 1)

        elif is_gate(SIGMA_Z_NAME):
            args_list = gate_args(SIGMA_Z_NAME)
            if len(args_list) != 1:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_sigma_z(result_array, int(args_list[0]) - 1)

        elif is_gate(HADAMARD_NAME):
            args_list = gate_args(HADAMARD_NAME)
            if len(args_list) != 1:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_hadamard(result_array, int(args_list[0]) - 1)

        elif is_gate(WALSH_HADAMARD_NAME):
            args_list = gate_args(WALSH_HADAMARD_NAME)
            print(args_list)
            if len(args_list) != 1:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_walsh_hadamard(result_array)

        elif is_gate(CNOT_NAME):
            args_list = gate_args(CNOT_NAME)
            if len(args_list) != 2:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_cnot(result_array, int(args_list[0]) - 1, int(args_list[1]) - 1)

        elif is_gate(CCNOT_NAME):
            args_list = gate_args(CCNOT_NAME)
            if len(args_list) != 3:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_ccnot(
                result_array, int(args_list[0]) - 1, int(args_list[1]) - 1, int(args_list[2]) - 1)

        elif is_gate(PHASE_NAME):
            args_list = gate_args(PHASE_NAME)
            if len(args_list) != 3:
                return result_array, 'Wrong number of args: ' + gate_string
            result_array = apply_phase(result_array, int(args_list[0]) - 1, int(args_list[1]) - 1, float(args_list[2]))

        else:
            return result_array, 'Unknown operator: ' + gate_string

    return result_array, ''
