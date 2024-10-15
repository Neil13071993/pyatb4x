class Excelreader:


    def read_excel_file(self):
        print("reading from excel")

class MySQLDBConncetion:

    def read_MySQL_file(self):
                print("reading from MySQL")


class TC1:
    def runTC(self):
        Excelreader().read_excel_file()
        MySQLDBConncetion.read_MySQL_file()


tc1 = TC1()
tc1.runTC()
