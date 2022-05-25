import unittest
from gates import *


class TestGates(unittest.TestCase):
    def test_apply_phase_1(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        phase = 0.0
        control_qubit_ind = 0
        target_qubit_ind = 1

        result_array = apply_phase(input_array, control_qubit_ind, target_qubit_ind, phase)
        expected_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_phase_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        phase = 10.0
        control_qubit_ind = 0
        target_qubit_ind = 1

        result_array = apply_phase(input_array, control_qubit_ind, target_qubit_ind, phase)
        expected_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            '(1 - 1.2246467991473533e-15*I)*(c4 + I*c4)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_sigma_x_1(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 0

        result_array = apply_sigma_x(input_array, target_qubit_ind)

        expected_array = np.array([
            'c3 + c3 * j',
            'c4 + c4 * j',
            'c1 + c1 * j',
            'c2 + c2 * j'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_sigma_x_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 1

        result_array = apply_sigma_x(input_array, target_qubit_ind)

        expected_array = np.array([
            'c2 + c2 * j',
            'c1 + c1 * j',
            'c4 + c4 * j',
            'c3 + c3 * j'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_sigma_x_3_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I',
            'c5 + c5 * I',
            'c6 + c6 * I',
            'c7 + c7 * I',
            'c8 + c8 * I'], dtype='U1000')

        target_qubit_ind = 1

        result_array = apply_sigma_x(input_array, target_qubit_ind)

        expected_array = np.array([
            'c3 + c3 * j',
            'c4 + c4 * j',
            'c1 + c1 * j',
            'c2 + c2 * j',
            'c7 + c7 * j',
            'c8 + c8 * j',
            'c5 + c5 * j',
            'c6 + c6 * j'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_sigma_y_1(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 0

        result_array = apply_sigma_y(input_array, target_qubit_ind)

        expected_array = np.array([
            'I*(c3 + c3 * j)',
            'I*(c4 + c4 * j)',
            '-I*(c1 + c1 * j)',
            '-I*(c2 + c2 * j)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_sigma_y_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 1

        result_array = apply_sigma_y(input_array, target_qubit_ind)

        expected_array = np.array([
            'I*(c2 + c2 * j)',
            '-I*(c1 + c1 * j)',
            'I*(c4 + c4 * j)',
            '-I*(c3 + c3 * j)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_sigma_z_1(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 0

        result_array = apply_sigma_z(input_array, target_qubit_ind)

        expected_array = np.array([
            'c1 + c1 * j',
            'c2 + c2 * j',
            '-1*(c3 + c3 * j)',
            '-1*(c4 + c4 * j)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_sigma_z_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 1

        result_array = apply_sigma_z(input_array, target_qubit_ind)

        expected_array = np.array([
            'c1 + c1 * j',
            '-1*(c2 + c2 * j)',
            'c3 + c3 * j',
            '-1*(c4 + c4 * j)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_hadamard_one_qubit(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I'], dtype='U1000')

        target_qubit_ind = 0

        result_array = apply_hadamard(input_array, target_qubit_ind)

        expected_array = np.array([
            '(c1 + c1*j + c2 + c2*j) / sqrt(2)',
            '(c1 + c1*j - c2 - c2*j) / sqrt(2)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_hadamard_1(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 0

        result_array = apply_hadamard(input_array, target_qubit_ind)

        expected_array = np.array([
            '(c1 + c3 + c1 * j + c3 * j) / sqrt(2)',
            '(c2 + c4 + c2 * j + c4 * j) / sqrt(2)',
            '(c1 - c3 + c1 * j - c3 * j) / sqrt(2)',
            '(c2 - c4 + c2 * j - c4 * j) / sqrt(2)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_hadamard_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        target_qubit_ind = 1

        result_array = apply_hadamard(input_array, target_qubit_ind)

        expected_array = np.array([
            '(c1 + c2 + c1 * j + c2 * j) / sqrt(2)',
            '(c1 - c2 + c1 * j - c2 * j) / sqrt(2)',
            '(c3 + c4 + c3 * j + c4 * j) / sqrt(2)',
            '(c3 - c4 + c3 * j - c4 * j) / sqrt(2)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_walsh_hadamard_one_qubit(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I'], dtype='U1000')

        result_array = apply_walsh_hadamard(input_array)

        expected_array = np.array([
            '(c1 + c1*j + c2 + c2*j) / sqrt(2)',
            '(c1 + c1*j - c2 - c2*j) / sqrt(2)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_walsh_hadamard_two_qubit(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        result_array = apply_walsh_hadamard(input_array)

        expected_array = np.array([
            '(c1 + c1*j + c2 + c2*j + c3 + c3*j + c4 + c4*j) / sqrt(4)',
            '(c1 + c1*j - c2 - c2*j + c3 + c3*j - c4 - c4*j) / sqrt(4)',
            '(c1 + c1*j + c2 + c2*j - c3 - c3*j - c4 - c4*j) / sqrt(4)',
            '(c1 + c1*j - c2 - c2*j - c3 - c3*j + c4 + c4*j) / sqrt(4)'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_cnot_2_1_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        control_qubit_ind = 0
        target_qubit_ind = 1

        result_array = apply_cnot(input_array, control_qubit_ind, target_qubit_ind)
        #print(result_array)
        expected_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c4 + c4 * I',
            'c3 + c3 * I'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_cnot_2_2_1(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        control_qubit_ind = 1
        target_qubit_ind = 0

        result_array = apply_cnot(input_array, control_qubit_ind, target_qubit_ind)
        expected_array = np.array([
            'c1 + c1 * I',
            'c4 + c4 * I',
            'c3 + c3 * I',
            'c2 + c2 * I'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_cnot_3_1_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I',
            'c5 + c5 * I',
            'c6 + c6 * I',
            'c7 + c7 * I',
            'c8 + c8 * I'], dtype='U1000')

        control_qubit_ind = 0
        target_qubit_ind = 1

        result_array = apply_cnot(input_array, control_qubit_ind, target_qubit_ind)
        expected_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I',
            'c7 + c7 * I',
            'c8 + c8 * I',
            'c5 + c5 * I',
            'c6 + c6 * I'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_ccnot_1_2_3(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I',
            'c5 + c5 * I',
            'c6 + c6 * I',
            'c7 + c7 * I',
            'c8 + c8 * I'], dtype='U1000')

        first_control_qubit_ind = 0
        second_control_qubit_ind = 1
        target_qubit_ind = 2

        result_array = apply_ccnot(input_array, first_control_qubit_ind, second_control_qubit_ind, target_qubit_ind)
        expected_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I',
            'c5 + c5 * I',
            'c6 + c6 * I',
            'c8 + c8 * I',
            'c7 + c7 * I'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))

    def test_apply_ccnot_1_3_2(self):
        input_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I',
            'c5 + c5 * I',
            'c6 + c6 * I',
            'c7 + c7 * I',
            'c8 + c8 * I'], dtype='U1000')

        first_control_qubit_ind = 0
        second_control_qubit_ind = 2
        target_qubit_ind = 1

        result_array = apply_ccnot(input_array, first_control_qubit_ind, second_control_qubit_ind, target_qubit_ind)
        expected_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I',
            'c5 + c5 * I',
            'c8 + c8 * I',
            'c7 + c7 * I',
            'c6 + c6 * I'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))


if __name__ == '__main__':
    unittest.main()
