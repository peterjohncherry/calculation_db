import yaml
import cinfo


class CalcInfoReader:

    def __init__(self, seedname, props=None):

        # Done like this as python evaluates default arguments when function is defined, not every time it is called
        if props is None:
            props = []

        self.data = None
        self.inp_data = None

        base_file_name = seedname+'.yaml'
        with open(base_file_name) as f:
            self.data = yaml.load(f, Loader=yaml.Loader)

        if self.data['program'] == 'ReSpect-mDKS':
            with open(seedname + '.inp') as f:
                self.inp_data = yaml.load(f, Loader=yaml.Loader)
                print("inp_data = ", self.inp_data)

        if len(props) != 0:
            for prop_type in props:
                prop_file_name = seedname + prop_type + '.yaml'
                with open(prop_file_name) as f:
                    self.data = yaml.load(f, Loader=yaml.Loader)

    def get_cinfo(self):
        return cinfo.CalcInfo(self.data['system_name'], self.data['calc_type'],
                              self.data['program'], self.data['method'])
