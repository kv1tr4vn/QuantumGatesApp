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

        result_array = apply_phase(input_array, phase, control_qubit_ind, target_qubit_ind)
        expected_array = np.array([
            'c1 + c1 * I',
            'c2 + c2 * I',
            'c3 + c3 * I',
            'c4 + c4 * I'], dtype='U1000')

        self.assertTrue(result_array.size == expected_array.size)
        for array_ind in range(expected_array.size):
            self.assertTrue((sp.simplify(result_array[array_ind] + ' - (' + expected_array[array_ind] + ')') == 0))


if __name__ == '__main__':
    unittest.main()
