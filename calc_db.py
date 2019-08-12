from cinfo import CalcInfo

class CalcDB:

    def __init__(self, connection, cursor):
        self.c = cursor
        self.conn = connection

    def initialize_table(self):
       # self.c.execute("""CREATE TABLE calcs(system_name TEXT, calc_type TEXT, program TEXT, method TEXT, name TEXT);""")

        calcinfo_list = [CalcInfo('H2O', 'Free Energy', 'ReSpect-mDKS', 'DFT'),
                         CalcInfo('H2O+', 'Free Energy', 'ReSpect-mDKS', 'DFT'),
                         CalcInfo('H3', 'Free Energy', 'ReSpect-mDKS', 'DFT')]

        for ci in calcinfo_list:
            self.insert_calc_info(ci)

        print(self.get_all_calcs())

    def insert_calc_info(self, ci):
        with self.conn:
            self.c.execute("INSERT INTO calcs VALUES (%s, %s, %s, %s, %s);",
                           (ci.system_name, ci.calc_type, ci.program, ci.method, ci.name))
            #self.c.execute("INSERT INTO calcs VALUES (:system_name, :calc_type, :program, :method, :name )",
                           #{'system_name': ci.system_name, 'calc_type': ci.calc_type, 'program': ci.program, 'method': ci.method, 'name': ci.name})

    def get_all_calcs(self):
        self.c.execute("SELECT * FROM calcs")
        return self.c.fetchall()


