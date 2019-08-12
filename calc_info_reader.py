import yaml
import cinfo

class CalcInfoReader:

    def __init__(self, seedname, props =[] ):

        base_file_name = seedname+'.yaml'
        with open(base_file_name) as f:
            self.data = yaml.load(f, Loader=yaml.Loader)

        if data['program'] == 'ReSpect-mDKS':
            inp_file_name = seedname + '.inp'
            with open(prop_file_name) as f:
                self.data = yaml.load(f, Loader=yaml.Loader)

        if (props.len != 0):
            for prop_type in props :
                prop_file_name = seedname + '.yaml'
                with open(prop_file_name) as f:
                    self.data = yaml.load(f, Loader=yaml.Loader)


    def get_cinfo(self):
        return cinfo.CalcInfo(self.data['system_name'], self.data['calc_type'],
                              self.data['program'], self.data['method'])
