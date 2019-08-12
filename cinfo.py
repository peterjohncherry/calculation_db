import hashlib

class CalcInfo:

    def __init__(self, system_name, calc_type, program, method, name = "auto gen name"):

        self.system_name = system_name
        self.calc_type = calc_type
        self.program = program
        self.method = method

        if name == "auto gen name":
            self.name = str(self.system_name+'_'+self.calc_type+'_'+self.program+'_'+self.method)
            self.id = int(hashlib.md5(self.name.encode('utf-8')).hexdigest(), 16)
            print("self.id = ", self.id)
        else:
            self.name = name
            self.id = int(hashlib.md5(self.name.encode('utf-8')).hexdigest(), 16)
            print("self.id = ", self.id)

#    @property
#    def get_calc_type(self):
#        return '{}'.format(self.calc_type)

#    @property
#    def method(self):
#        return '{}'.format(self.method)

    def __repr__(self):
        return "CalcInfo(\n name ='{}'\n system_name = {}'\n calc_type = '{}'\n program = '{}'" \
               "\n database_id = {})".format(self.name, self.system_name, self.calc_type,
                                             self.program, self.method, self.id)
