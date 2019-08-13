import yaml
import cinfo

class CalcInfoReader:

    def __init__(self, seedname, attribute_list=None):

        # Done like this as python evaluates default arguments when function is defined, not every time it is called
        if attribute_list is None:
            self.attribute_list = []

        self.seedname = seedname
        self.base_data = None
        self.inp_data = None
        self.program_data = None

        base_file_name = seedname+'_base'
        with open(base_file_name) as f:
            self.base_data = yaml.load(f, Loader=yaml.Loader)

        if attribute_list is not None:
            for attribute in attribute_list:
                file_name = seedname+attribute

    def get_cinfo(self):
        return cinfo.BaseInfo(self.base_data['system_name'], self.base_data['calc_type'],
                              self.base_data['program'])
