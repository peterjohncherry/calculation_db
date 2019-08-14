from cinfo import BaseInfo, InpInfo
from uuid import uuid4
from calc_info_reader import CalcInfoReader as reader


class CalcDB:

    def __init__(self, connection, cursor):
        self.c = cursor
        self.conn = connection
        self.base_info_list = []
        self.inp_info_list = []
        self.inp_uuid_dict = {}
        self.base_uuid_list = []


    def initialize_table(self):
        print("initializing table")

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
        self.base_info_list = [BaseInfo('H2O', 'Free_Energy', 'ReSpect-mDKS'), BaseInfo.buildfromfile('CO_base')]
        self.inp_info_list = [InpInfo('DFT', 'finite_gaussian', 'atomic', 3, 1.0), InpInfo.buildfromfile('CO_inp')]

        self.enter_base_info()
        self.enter_inp_info()

        print(self.get_all_info_from_table('base'))
        print(self.get_all_info_from_table('inp'))

    def enter_base_info(self):
        for bi in self.base_info_list:
            self.base_uuid_list.append(uuid4())
            self.insert_base_info(bi, self.base_uuid_list[-1])

    def enter_inp_info(self):
        for ii in range(len(self.inp_info_list)):
            new_inp_uid = uuid4()
            self.insert_inp_info(self.inp_info_list[ii], new_inp_uid)
            self.add_foreign_id_in_base(str(self.base_uuid_list[ii]), new_inp_uid, "inp_uid")
            self.inp_uuid_dict[self.base_uuid_list[ii]] = new_inp_uid

    def insert_base_info(self, binfo, uid):
        with self.conn:
            self.c.execute("INSERT INTO base VALUES ( %s , %s, %s, %s );",
                           (str(uid), binfo.name, binfo.system_name, binfo.calc_type))

    def add_foreign_id_in_base(self, base_key, foreign_key, foreign_key_name):
        with self.conn:
            self.c.execute("UPDATE base SET " + foreign_key_name + " = %s  WHERE base_uid = %s",
                           (str(foreign_key), str(base_key)))

    def insert_inp_info(self, ii, uid):
        with self.conn:
            self.c.execute("INSERT INTO inp VALUES ( %s, %s, %s, %s, %s, %s);",
                           (str(uid), ii.method, ii.nucleus_model, ii.initialization, ii.multiplicity, ii.charge))

    def get_all_info_from_table(self, table_name):
        self.c.execute("SELECT * FROM "+str(table_name)+";")
        return self.c.fetchall()
