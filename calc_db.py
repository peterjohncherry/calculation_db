from cinfo import CalcInfo
from calc_info_reader import CalcInfoReader as reader


class CalcDB:

    def __init__(self, connection, cursor):
        self.c = cursor
        self.conn = connection

    def initialize_table(self):
        print ("initializing table")

        with self.conn:
            self.c.execute("""DROP TABLE IF EXISTS base;""")
            self.c.execute("""DROP TABLE IF EXISTS inp;""")
            self.c.execute( """ CREATE EXTENSION "uuid-ossp";""")
            self.c.execute("""
                            create table inp(   
                                            inp_uid UUID NOT NULL PRIMARY KEY,
                                            method VARCHAR(100) NOT NULL,            
                                            nucleus_model VARCHAR(100),
                                            initialization VARCHAR(100),
                                            multiplicity NUMERIC(1),
                                            charge NUMERIC(2, 1),
                                            UNIQUE(inp_uid)
                                            );
                            create table base(
                                                base_uid UUID NOT NULL PRIMARY KEY,
                                                name VARCHAR(50) NOT NULL,
                                                system_name VARCHAR(50) NOT NULL,
                                                calc_type VARCHAR(50) NOT NULL,
                                                inp_uid UUID REFERENCES inp(inp_uid),
                                                UNIQUE(inp_uid),
                                                UNIQUE(base_uid)
                                                );
            """)

    def initial_test(self):
        print("into initial test")
        calcinfo_list = [CalcInfo('H2O', 'Free Energy', 'ReSpect-mDKS', 'DFT'),
                         CalcInfo('H2O+', 'Free Energy', 'ReSpect-mDKS', 'DFT'),
                         CalcInfo('H3', 'Free Energy', 'ReSpect-mDKS', 'DFT')]

        cinfo_test = reader('CalcExample')
        calcinfo_list.append(cinfo_test.get_cinfo())

        for ci in calcinfo_list:
            self.insert_calc_info(ci)

        print(self.get_all_calcs())

    def insert_calc_info(self, ci):
        with self.conn:
            self.c.execute("""DELETE FROM calcs ;""")
            self.c.execute("INSERT INTO inp (inp_uid, method, nucleus_model, initialization, multiplicity, charge) "
                           "VALUES ( uuid_generate_v4(), %s, %s, %s, %s, %s);",
                           (ci.system_name, ci.calc_type, ci.program, ci.method, ci.name))
            #self.c.execute("INSERT INTO calcs VALUES (:system_name, :calc_type, :program, :method, :name )",
                           #{'system_name': ci.system_name, 'calc_type': ci.calc_type, 'program': ci.program, 'method': ci.method, 'name': ci.name})

    def get_all_calcs(self):
        self.c.execute("SELECT * FROM calcs")
        return self.c.fetchall()



