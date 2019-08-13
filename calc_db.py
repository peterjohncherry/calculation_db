from cinfo import BaseInfo, InpInfo
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
            self.c.execute("""DROP TABLE IF EXISTS program;""")
            self.c.execute("""CREATE EXTENSION IF NOT EXISTS "uuid-ossp";""")
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
                            create table program(
                                                program_uid UUID NOT NULL PRIMARY KEY,
                                                program_name VARCHAR(50),
                                                program_version VARCHAR(50),
                                                git_commit VARCHAR(50),
                                                UNIQUE(program_uid)
                                                );
                            create table base(
                                                base_uid UUID NOT NULL PRIMARY KEY,
                                                name VARCHAR(50) NOT NULL,
                                                system_name VARCHAR(50) NOT NULL,
                                                calc_type VARCHAR(50) NOT NULL,
                                                inp_uid UUID REFERENCES inp(inp_uid),
                                                program_uid UUID REFERENCES program(program_uid),
                                                UNIQUE(base_uid)
                                                );

            """)

    def initial_test(self):
        print("into initial test")
        calcinfo_list = [BaseInfo('H2O',  'Free Energy', 'ReSpect-mDKS')]
        cinfo_test = BaseInfo.buildfromfile('CO_base')
        calcinfo_list.append(cinfo_test.get_cinfo())

        print("len(calcinfo_list) = ", len(calcinfo_list))
        for ci in calcinfo_list:
            self.insert_calc_info(ci)

        print(self.get_all_info('base'))

    def insert_calc_info(self, ci):
        with self.conn:
            self.c.execute("INSERT INTO base VALUES ( uuid_generate_v4(), %s, %s, %s )",
                           (ci.name, ci.system_name, ci.calc_type))

    def get_all_info(self, table_name):
        self.c.execute("SELECT * FROM "+str(table_name)+";")
        return self.c.fetchall()

