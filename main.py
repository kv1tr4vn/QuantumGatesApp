import sys

import numpy as np

from mainwindow import *
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QMessageBox, QFileDialog
from scheme_builder import *


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    n_cols = 2
    n_qubits = 3
    n_rows = 2 ** n_qubits
    for col in range(0, n_cols):
        ui.inputTableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)
        ui.outputTableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

        for row in range(0, n_rows):
            item = QTableWidgetItem(str(0))
            item.setTextAlignment(132)
            ui.inputTableWidget.setItem(row, col, item)
            ui.outputTableWidget.setItem(row, col, item.clone())


    def input_array_from_table(table_widget):
        result = np.zeros(0, dtype='U1000')
        for row in range(0, n_rows):
            item_real = table_widget.item(row, 0).text()
            item_imag = table_widget.item(row, 1).text()
            item_real = '0' if item_real == '' else item_real
            item_imag = '0' if item_imag == '' else item_imag
            result_row = '(' + item_real + ') + (' + item_imag + ') * I'
            result = np.append(result, result_row)
        return result


    def output_array_to_table(output_array, table_widget):
        for row in range(0, n_rows):
            row_data = sp.expand(str(output_array[row]).replace('j', 'I'))

            row_data_real = str(sp.re(row_data))
            row_data_imag = str(sp.im(row_data))
            row_data_real = str(row_data_real.replace('re', '').replace('im', '0*'))
            row_data_imag = str(row_data_imag.replace('re', '').replace('im', '0*'))
            row_data_real = str(sp.simplify(row_data_real))
            row_data_imag = str(sp.simplify(row_data_imag))

            item_real = QTableWidgetItem(row_data_real)
            item_real.setTextAlignment(132)
            table_widget.setItem(row, 0, item_real)

            item_imag = QTableWidgetItem(row_data_imag)
            item_imag.setTextAlignment(132)
            table_widget.setItem(row, 1, item_imag)


    def qubit_number_from_spin_box(spin_box):
        qubit_ind = spin_box.value() - 1
        if qubit_ind >= n_qubits:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                'Cannot select qubit with number ' + str(spin_box.value()) + '! '
                'Current number of qubits is ' + str(n_qubits) + '.')
            msg.setWindowTitle('Qubit number error')
            msg.exec_()
            return -1
        return qubit_ind


    def number_of_qubits_spin_box_value_changed():
        global n_qubits, n_rows
        n_qubits = ui.numberOfQubitsSpinBox.value()
        n_old_rows = n_rows
        n_rows = 2 ** n_qubits

        ui.inputTableWidget.setRowCount(n_rows)
        ui.outputTableWidget.setRowCount(n_rows)

        for col in range(0, n_cols):
            for row in range(n_old_rows, n_rows):
                item = QTableWidgetItem(str(0))
                item.setTextAlignment(132)
                ui.inputTableWidget.setItem(row, col, item)
                ui.outputTableWidget.setItem(row, col, item.clone())
    ui.numberOfQubitsSpinBox.valueChanged.connect(lambda: number_of_qubits_spin_box_value_changed())


    def set_zero_table_widget(table_widget):
        for col in range(0, n_cols):
            for row in range(0, n_rows):
                item = QTableWidgetItem(str(0))
                item.setTextAlignment(132)
                table_widget.setItem(row, col, item)

    def set_zero_input_push_button_clicked():
        set_zero_table_widget(ui.inputTableWidget)
    ui.setZeroInputPushButton.clicked.connect(set_zero_input_push_button_clicked)

    def set_zero_output_push_button_clicked():
        set_zero_table_widget(ui.outputTableWidget)
    ui.setZeroOutputPushButton.clicked.connect(set_zero_output_push_button_clicked)


    def set_symbolic_table_widget(table_widget):
        for col in range(0, n_cols):
            for row in range(0, n_rows):
                item = QTableWidgetItem('c' + str(row))
                item.setTextAlignment(132)
                table_widget.setItem(row, col, item)

    def set_symbolic_input_push_button_clicked():
        set_symbolic_table_widget(ui.inputTableWidget)
    ui.setSymbolicInputPushButton.clicked.connect(set_symbolic_input_push_button_clicked)

    def set_symbolic_output_push_button_clicked():
        set_symbolic_table_widget(ui.outputTableWidget)
    ui.setSymbolicOutputPushButton.clicked.connect(set_symbolic_output_push_button_clicked)


    def set_symbolic_by_re_and_im_table_widget(table_widget):
        for row in range(0, n_rows):
            item_real = QTableWidgetItem('r' + str(row))
            item_real.setTextAlignment(132)
            table_widget.setItem(row, 0, item_real)

            item_imag = QTableWidgetItem('i' + str(row))
            item_imag.setTextAlignment(132)
            table_widget.setItem(row, 1, item_imag)

    def set_symbolic_by_re_and_im_input_push_button_clicked():
        set_symbolic_by_re_and_im_table_widget(ui.inputTableWidget)
    ui.setSymbolicByReAndImInputPushButton.clicked.connect(set_symbolic_by_re_and_im_input_push_button_clicked)

    def set_symbolic_by_re_and_im_output_push_button_clicked():
        set_symbolic_by_re_and_im_table_widget(ui.outputTableWidget)
    ui.setSymbolicByReAndImOutputPushButton.clicked.connect(set_symbolic_by_re_and_im_output_push_button_clicked)


    def copy_result_to_input_push_button_clicked():
        for col in range(0, n_cols):
            for row in range(0, n_rows):
                ui.inputTableWidget.setItem(row, col, ui.outputTableWidget.item(row, col).clone())
    ui.copyResultToInputPushButton.clicked.connect(copy_result_to_input_push_button_clicked)

    def main_message_error(string):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(string)
        msg.setWindowTitle('Input error')
        msg.exec_()


    def normalize_input_if_needed(input_array):
        if not is_numeric(input_array):
            return input_array

        input_length = length(input_array)
        if input_length == 1:
            return input_array

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Question")
        msg.setText("Input is not normalized. Normalize?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()

        if retval == QMessageBox.No:
            return input_array
        return normalize(input_array)


    def pauli_matrices_sigma_x_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        qubit_ind = qubit_number_from_spin_box(ui.pauliMatricesSpinBox)
        if qubit_ind == -1:
            return
        try:
            output_array_to_table(
                apply_sigma_x(input_array, qubit_ind), ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_sigma_x(ui.lineEdit.text(), qubit_ind))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.pauliMatricesSigmaXPushButton.clicked.connect(pauli_matrices_sigma_x_push_button_clicked)


    def pauli_matrices_sigma_y_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        qubit_ind = qubit_number_from_spin_box(ui.pauliMatricesSpinBox)
        if qubit_ind == -1:
            return
        try:
            output_array_to_table(
                apply_sigma_y(input_array, qubit_ind), ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_sigma_y(ui.lineEdit.text(), qubit_ind))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.pauliMatricesSigmaYPushButton.clicked.connect(pauli_matrices_sigma_y_push_button_clicked)


    def pauli_matrices_sigma_z_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        qubit_ind = qubit_number_from_spin_box(ui.pauliMatricesSpinBox)
        if qubit_ind == -1:
            return
        try:
            output_array_to_table(
                apply_sigma_z(input_array, qubit_ind), ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_sigma_z(ui.lineEdit.text(), qubit_ind))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.pauliMatricesSigmaZPushButton.clicked.connect(pauli_matrices_sigma_z_push_button_clicked)


    def hadamard_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        qubit_ind = qubit_number_from_spin_box(ui.hadamardSpinBox)
        if qubit_ind == -1:
            return
        try:
            output_array_to_table(
                apply_hadamard(input_array, qubit_ind), ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_hadamard(ui.lineEdit.text(), qubit_ind))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.hadamardPushButton.clicked.connect(hadamard_push_button_clicked)


    def walsh_hadamard_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        try:
            output_array_to_table(
                apply_walsh_hadamard(input_array), ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_walsh_hadamard(ui.lineEdit.text()))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.walshHadamardPushButton.clicked.connect(walsh_hadamard_push_button_clicked)


    def controlled_not_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        control_qubit_ind = qubit_number_from_spin_box(ui.controlledNotControlSpinBox)
        target_qubit_ind = qubit_number_from_spin_box(ui.controlledNotTargetSpinBox)
        if control_qubit_ind == -1 or target_qubit_ind == -1:
            return
        try:
            output_array_to_table(
                apply_cnot(input_array, control_qubit_ind, target_qubit_ind),
                ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_cnot(ui.lineEdit.text(), control_qubit_ind, target_qubit_ind))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.controlledNotPushButton.clicked.connect(controlled_not_push_button_clicked)


    def controlled_controlled_not_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        first_control_qubit_ind = qubit_number_from_spin_box(ui.controlledControlledNotFirstControlSpinBox)
        second_control_qubit_ind = qubit_number_from_spin_box(ui.controlledControlledNotSecondControlSpinBox)
        target_qubit_ind = qubit_number_from_spin_box(ui.controlledControlledNotTargetSpinBox)
        if first_control_qubit_ind == -1 or second_control_qubit_ind == -1 or target_qubit_ind == -1:
            return
        try:
            output_array_to_table(apply_ccnot(
                input_array,
                first_control_qubit_ind, second_control_qubit_ind, target_qubit_ind), ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_ccnot(
                ui.lineEdit.text(), first_control_qubit_ind, second_control_qubit_ind, target_qubit_ind))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.controlledControlledNotPushButton.clicked.connect(controlled_controlled_not_push_button_clicked)


    def phase_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        phase_control_qubit_ind = qubit_number_from_spin_box(ui.phaseControlSpinBox)
        phase_target_qubit_ind = qubit_number_from_spin_box(ui.phaseTargetSpinBox)
        if phase_control_qubit_ind == -1 or phase_target_qubit_ind == -1:
            return
        try:
            phase_in_fractions_of_pi = ui.phaseDoubleSpinBox.value()
            output_array_to_table(apply_phase(
                input_array,
                phase_control_qubit_ind, phase_target_qubit_ind, phase_in_fractions_of_pi), ui.outputTableWidget)
            ui.lineEdit.setText(add_apply_phase(
                ui.lineEdit.text(), phase_control_qubit_ind, phase_target_qubit_ind, phase_in_fractions_of_pi))
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.phasePushButton.clicked.connect(phase_push_button_clicked)


    def clear_line_push_button_clicked():
        ui.lineEdit.clear()
    ui.clearLinePushButton.clicked.connect(clear_line_push_button_clicked)


    def apply_line_push_button_clicked():
        input_array = input_array_from_table(ui.inputTableWidget)
        input_array = normalize_input_if_needed(input_array)
        output_array_to_table(input_array, ui.inputTableWidget)

        try:
            result_array, error_message = apply_scheme(ui.lineEdit.text(), input_array)
            if error_message == '':
                output_array_to_table(result_array, ui.outputTableWidget)
                return
            main_message_error(error_message)
        except sp.SympifyError as error:
            main_message_error(str(error))
    ui.applyLinePushButton.clicked.connect(apply_line_push_button_clicked)


    def import_txt_to_table(table_widget):
        try:
            filename, _ = QFileDialog.getOpenFileName(None, "Select File", "", "Text Files (*.txt)")
            if filename == '':
                return
            with open(filename) as file:
                import_array = file.read().splitlines()
                n_qubits = 0 if len(import_array) == 0 else math.floor(math.log(len(import_array), 2))
                if n_qubits == 0:
                    n_qubits = 1
                    import_array = np.array(['0', '0'])
                ui.numberOfQubitsSpinBox.setValue(n_qubits)
                number_of_qubits_spin_box_value_changed()
                output_array_to_table(import_array, table_widget)
        except sp.SympifyError as error:
            main_message_error(str(error))

    def input_import_txt_push_button_clicked():
        import_txt_to_table(ui.inputTableWidget)
    ui.inputImportTxtPushButton.clicked.connect(input_import_txt_push_button_clicked)

    def output_import_txt_push_button_clicked():
        import_txt_to_table(ui.outputTableWidget)
    ui.outputImportTxtPushButton.clicked.connect(output_import_txt_push_button_clicked)


    def export_txt_from_file(table_widget):
        try:
            export_array = sp.simplify(input_array_from_table(table_widget))
            export_str = '\n'.join('{}'.format(item) for item in export_array)
            filename, _ = QFileDialog.getSaveFileName(None, 'Export File', "", 'Text Files (*.txt)')
            if filename == '':
                return
            with open(filename, 'w') as file:
                file.write(export_str)
        except sp.SympifyError as error:
            main_message_error(str(error))

    def input_export_txt_push_button_clicked():
        export_txt_from_file(ui.inputTableWidget)
    ui.inputExportTxtPushButton.clicked.connect(input_export_txt_push_button_clicked)

    def output_export_txt_push_button_clicked():
        export_txt_from_file(ui.outputTableWidget)
    ui.outputExportTxtPushButton.clicked.connect(output_export_txt_push_button_clicked)

    MainWindow.show()
    sys.exit(app.exec_())
