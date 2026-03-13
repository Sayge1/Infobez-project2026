import sys
from PySide6 import QtWidgets as qtw
from untitled import Ui_Form
from parse_functions import parse_oval, parse_xccdf
from download_scap_content_functions import apt_install, download_SCAP_content
from patch_scap_content import patch_SCAP_content
from scan_scap_functions import do_xccdf_scan, do_oval_scan
class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_OVALcheck.clicked.connect(self.OVAL_check)
        self.bt_XCCDFcheck.clicked.connect(self.XCCDF_check)
        self.bt_OVAL_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.OVAL_page))
        self.bt_XCCDF_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.XCCDF_page))
        self.first_encounter = 0

    def OVAL_check(self):
        if self.first_encounter == 0:
	    self.first_encounter = 1
            download_SCAP_content(self.Cb_chooseos.currentText())
            patch_SCAP_content(self.Cb_chooseos.currentText())
        do_oval_scan(self.Cb_chooseos.currentText())
        file_name = "results_oval.xml"
        results = parse_oval(file_name)
        for v in results:
            row_position = self.table_OVAL_results.rowCount()
            self.table_OVAL_results.insertRow(row_position)
            self.table_OVAL_results.setItem(row_position, 0, qtw.QTableWidgetItem(v['cve']))
            self.table_OVAL_results.setItem(row_position, 1, qtw.QTableWidgetItem(v['result']))
            self.table_OVAL_results.setItem(row_position, 2, qtw.QTableWidgetItem(v['description']))

    def XCCDF_check(self):
        if self.first_encounter == 0:
	    self.first_encounter = 1
            download_SCAP_content(self.Cb_chooseos_2.currentText())
            patch_SCAP_content(self.Cb_chooseos_2.currentText())
        do_xccdf_scan(self.Cb_chooseos_2.currentText(), self.checkb_remediation.isChecked())
        file_name = "results_xccdf.xml"
        results = parse_xccdf(file_name)
        for v in results:
            row_position = self.table_XCCDF_results.rowCount()
            self.table_XCCDF_results.insertRow(row_position)
            self.table_XCCDF_results.setItem(row_position, 0, qtw.QTableWidgetItem(v['title']))
            self.table_XCCDF_results.setItem(row_position, 1, qtw.QTableWidgetItem(v['result']))
            self.table_XCCDF_results.setItem(row_position, 2, qtw.QTableWidgetItem(v['severity']))
            self.table_XCCDF_results.setItem(row_position, 3, qtw.QTableWidgetItem(v['description']))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
