class BaseInfo:

    def __init__(self, system_name, calc_type, program, name="auto gen name"):

        self.system_name = system_name
        self.calc_type = calc_type
        self.program = program

        if name == "auto gen name":
            self.name = str(self.system_name + '_' + self.calc_type + '_' + self.program )
        else:
            self.name = name

    def __repr__(self):
        return "CalcInfo(\n name ='{}'\n system_name = {}'\n calc_type = '{}'\n  program = '{}'".format(
            self.name, self.system_name, self.calc_type, self.program, self.method, self.id)


class InpInfo:

    def __init__(self, method, nucleus_model="not_defined", initialization="not_defined",
                 multiplicity=None, charge=None):

        self.method = method
        self.nucleus_model = nucleus_model
        self.initialization = initialization
        self.multiplicity = multiplicity
        self.charge = charge

    def __repr__(self):
        return "CalcInfo(\n method ='{}'\n nucleus_model = {}'\n initialization = '{}'\n  multiplicity = '{}'\n " \
               "charge ='{}'".format(self.method, self.nucleus_model, self.initialization, self.multiplicity,
                                     self.multiplicity, self.charge)


#    @property
#    def get_calc_type(self):
#        return '{}'.format(self.calc_type)

#    @property
#    def method(self):
#        return '{}'.format(self.method)


