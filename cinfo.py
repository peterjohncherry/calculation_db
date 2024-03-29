import yaml
import numpy as np

class BaseInfo:

    def __init__(self, system_name, calc_type, program, name="auto gen name"):

        self.system_name = system_name
        self.calc_type = calc_type
        self.program = program

        if name == "auto gen name":
            self.name = str(self.system_name + '_' + self.calc_type + '_' + self.program )
        else:
            self.name = name

    @classmethod
    def buildfromfile(cls, filename):
        with open(filename) as f:
            base_data = yaml.load(f, Loader=yaml.Loader)
        return cls(base_data['system_name'], base_data['calc_type'], base_data['program'])

    def __repr__(self):
        return "CalcInfo(\n name ='{}'\n system_name = {}'\n calc_type = '{}'\n  program = '{}'".format(
            self.name, self.system_name, self.calc_type, self.program)


class InpInfo:

    def __init__(self, method=None, nucleus_model=None, initialization=None, multiplicity=None, charge=None):

        self.method = method
        self.nucleus_model = nucleus_model
        self.initialization = initialization
        if multiplicity is not None:
            self.multiplicity = int(multiplicity)

        if charge is not None:
            self.charge = float(charge)

    @classmethod
    def buildfromfile(cls, filename):
        with open(filename) as f:
            inp_data = yaml.load(f, Loader=yaml.Loader)

        return cls(inp_data['method'], inp_data['nucleus_model'], inp_data['initialization'], inp_data['multiplicity'],
                   inp_data['charge'])

    def __repr__(self):
        return "InpInfo(\n method ='{}'\n nucleus_model = {}'\n initialization = '{}'\n  multiplicity = {}\n " \
               "charge ={}".format(self.method, self.nucleus_model, self.initialization, self.multiplicity,
                                     self.multiplicity, self.charge)

