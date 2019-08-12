import yaml
import cinfo

class CalcInfoReader:

    def __init__(self, filename ):

        with open('CalcExample.yaml') as f:
            self.data = yaml.load(f, Loader=yaml.Loader)

    def get_cinfo(self):
            return cinfo.CalcInfo( self.data['system_name'], self.data['calc_type'], self.data['program'], self.data['method'])
