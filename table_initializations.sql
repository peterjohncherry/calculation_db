create table inp (
        inp_uid UUID NOT NULL PRIMARY KEY,
        method VARCHAR(100) NOT NULL,
        nucleus_model VARCHAR(100),
        initialization VARCHAR(100),
        multiplicity NUMERIC(1),
        charge NUMERIC(2, 1)
);

create table base (
    base_uid UUID NOT NULL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        system_name VARCHAR(50) NOT NULL,
        calc_type VARCHAR(50) NOT NULL,
        inp_uid UUID REFERENCES inp(inp_uid),
        UNIQUE(inp_uid),
        UNIQUE(base_uid)
);

