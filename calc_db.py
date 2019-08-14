from cinfo import BaseInfo, InpInfo
from uuid import uuid4
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
                                            multiplicity INTEGER,
                                            charge DOUBLE PRECISION,
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


        base_info_list = [BaseInfo('H2O', 'Free_Energy', 'ReSpect-mDKS')]
        base_info_list.append(BaseInfo.buildfromfile('CO_base'))

        uuid_list = []
        for ci in base_info_list:
            uuid_list.append(uuid4())
            self.insert_base_info(ci, uuid_list[-1])



        print(self.get_all_info_from_table('base'))

    def insert_base_info(self, binfo, uid):
        with self.conn:
            self.c.execute("INSERT INTO base VALUES ( %s , %s, %s, %s )",
                           (str(uid), binfo.name, binfo.system_name, binfo.calc_type))


    def insert_inp_info(self, bi):
        with self.conn:
            self.c.execute("INSERT INTO base VALUES ( uuid_generate_v4(), %s, %s, %s, %d, %f )",
                           (bi.method, bi.nucleus_model, bi.initialization, bi.multiplicity, bi.charge))

    def get_all_info_from_table(self, table_name):
        self.c.execute("SELECT * FROM "+str(table_name)+";")
        return self.c.fetchall()

