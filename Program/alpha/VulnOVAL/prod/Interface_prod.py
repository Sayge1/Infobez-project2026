import sys
from PySide6 import QtWidgets as qtw
from prod.untitled import Ui_Form
from parse_functions import parse_oval, parse_xccdf
from download_scap_content_functions import apt_install, download_SCAP_content
class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_OVALcheck.clicked.connect(self.OVAL_check)
        self.bt_XCCDFcheck.clicked.connect(self.XCCDF_check)
        self.bt_OVAL_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.OVAL_page))
        self.bt_XCCDF_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.XCCDF_page))

    def OVAL_check(self):
        download_SCAP_content(self.Cb_chooseos.currentText())
        file_name = "cve-results.xml"
        results = parse_oval(file_name)
        for v in results:
            row_position = self.table_OVAL_results.rowCount()
            self.table_OVAL_results.insertRow(row_position)
            self.table_OVAL_results.setItem(row_position, 0, qtw.QTableWidgetItem(v['cve']))
            self.table_OVAL_results.setItem(row_position, 1, qtw.QTableWidgetItem(v['result']))
            self.table_OVAL_results.setItem(row_position, 2, qtw.QTableWidgetItem(v['description']))

    def XCCDF_check(self):
        download_SCAP_content(self.Cb_chooseos_2.currentText())

        file_name = "results.xml"
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
