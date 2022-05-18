import math
import numpy as np
import sympy as sp
from bin_tools import dec_to_bin_list, bin_list_to_dec, bin_register

sigma_x_matrix = np.array([[0, 1], [1, 0]])
sigma_y_matrix = np.array([[0, 0 - 1j], [0 + 1j, 0]])
sigma_z_matrix = np.array([[1, 0], [0, -1]])
hadamard_matrix = np.array([[1, 1], [1, -1]])


def apply_matrix(input_array, matrix, qubit_ind):
    length = int(np.log2(input_array.size))
    result = np.zeros(input_array.size, input_array.dtype)
    for array_ind in range(input_array.size):
        bin_array_ind = dec_to_bin_list(array_ind, length)
        register = bin_register(bin_array_ind[qubit_ind])
        output = np.ravel(np.dot(matrix, register))

        if bin_array_ind[qubit_ind] == 1:
            output = output[::-1]

        result[array_ind] += "+((" + str(output[0]) + ")*(" + input_array[array_ind] + "))"
        bin_array_ind[qubit_ind] = not bin_array_ind[qubit_ind]
        result[array_ind] += "+((" + str(output[1]) + ")*(" + input_array[bin_list_to_dec(bin_array_ind)] + "))"
        result[array_ind] = sp.sympify(result[array_ind].replace('I', 'j'))
    return result


def apply_sigma_x(input_array, qubit_ind):
    return apply_matrix(input_array, sigma_x_matrix, qubit_ind)


def apply_sigma_y(input_array, qubit_ind):
    return apply_matrix(input_array, sigma_y_matrix, qubit_ind)


def apply_sigma_z(input_array, qubit_ind):
    return apply_matrix(input_array, sigma_z_matrix, qubit_ind)


def apply_hadamard(input_array, qubit_ind):
    result = apply_matrix(input_array, hadamard_matrix, qubit_ind)
    for row in range(0, len(result)):
        result[row] = "1/sqrt(2)*(" + str(result[row]).replace('I', 'j') + ")"
    return result


def apply_walsh_hadamard(input_array):
    length = int(np.log2(input_array.size))
    result = input_array
    for array_ind in range(length):
        result = apply_matrix(result, hadamard_matrix, array_ind)
    for row in range(0, len(result)):
        result[row] = "(1/sqrt(2))**" + str(length) + " *(" + str(result[row]).replace('I', 'j') + ")"
    return result


def apply_cnot(input_array, control_qubit_ind, target_qubit_ind):
    length = int(np.log2(input_array.size))
    result = np.zeros(input_array.size, input_array.dtype)
    for array_ind in range(input_array.size):
        bin_array_ind = dec_to_bin_list(array_ind, length)
        if bin_array_ind[control_qubit_ind] == 1:
            bin_array_ind[target_qubit_ind] = not bin_array_ind[target_qubit_ind]
        bin_array_ind = bin_list_to_dec(bin_array_ind)
        result[array_ind] = input_array[bin_array_ind]
    return result


def apply_ccnot(input_array, first_control_qubit_ind, second_control_qubit_ind, target_qubit_ind):
    length = int(np.log2(input_array.size))
    result = np.zeros(input_array.size, input_array.dtype)
    for array_ind in range(input_array.size):
        bin_array_ind = dec_to_bin_list(array_ind, length)
        if bin_array_ind[first_control_qubit_ind] == 1 and bin_array_ind[second_control_qubit_ind] == 1:
            bin_array_ind[target_qubit_ind] = not bin_array_ind[target_qubit_ind]
        bin_array_ind = bin_list_to_dec(bin_array_ind)
        result[array_ind] = input_array[bin_array_ind]
    return result


def apply_phase(input_array, control_qubit_ind, target_qubit_ind, phase_in_fractions_of_pi):
    real_phase = math.pi * phase_in_fractions_of_pi
    length = int(np.log2(input_array.size))
    result = input_array
    for array_ind in range(input_array.size):
        if dec_to_bin_list(array_ind, length)[control_qubit_ind] == 1 and \
                dec_to_bin_list(array_ind, length)[target_qubit_ind] == 1:
            result[array_ind] = sp.sympify("(" + str(np.exp(real_phase * 1j)) + ")*(" + input_array[array_ind] + ")")
    return result
