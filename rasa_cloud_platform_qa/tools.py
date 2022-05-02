
import pandas as pd


class DataBase:

    def __init__(self):
        self.cluster = pd.read_csv('./database/cluster.csv')
        self.datacenter = pd.read_csv('./database/datacenter.csv')
        self.server = pd.read_csv('./database/server.csv')

    def get_attribute(self,attribute,ip,entity):
        if entity == 'cluster':
            return self.cluster[self.cluster['ip'] == ip][attribute].values[0]
        elif entity == 'server':
            return self.server[self.server['ip'] == ip][attribute].values[0]
        else:
            return self.datacenter[self.datacenter['ip']==ip][attribute].values[0]

    relation2entity = {
        'host in': {'server': ['cluster', 'datacenter'], 'cluster': ['datacenter']},
        'configuration by': {'datacenter': ['cluster', 'server'], 'cluster': ['server']}
    }

    def get_relation_has_in(self,s_entity,o_entity,ip):
        if s_entity == 'server':
            if o_entity == 'cluster':
                return self.server[self.server['server_ip']==ip]
            else:
                return self.server[self.server['datacenter_ip']==ip]
        else:
            return self.cluster[self.cluster['datacenter_ip']==ip]

    def get_relation_configuration(self,s_entity,o_entity,ip):
        if s_entity == 'datacenter':
            if o_entity == 'cluster':
                return self.datacenter[self.datacenter['ip']==self.cluster[self.cluster['ip']==ip]['datacenter_ip'].values[0]]
            else:
                # print(self.server[self.server['ip']==ip]['datacenter_ip'].values[0])
                return self.datacenter[self.datacenter['ip']==self.server[self.server['ip']==ip]['datacenter_ip'].values[0]]
        else:
            return self.cluster[self.cluster['ip']==self.server[self.server['ip']==ip]['server_ip'].values[0]]

    def get_sameAttributeEntities(self,attribute_name):
        if attribute_name == 'cpu':
            return ['datacenter','server']
        elif attribute_name == 'name':
            return ['cluster','datacenter','server']
        elif attribute_name == 'memory':
            return ['server']
        elif attribute_name == 'disk':
            return ['server']
        elif attribute_name == 'business':
            return ['cluster']
        elif attribute_name == 'region':
            return ['cluster','datacenter']
        elif attribute_name == 'longitude':
            return ['datacenter']
        elif attribute_name == 'latitude':
            return ['datacenter']

    def getEntityIp(self):
        return ['cluster','datacenter','server']


if __name__ == '__main__':
    d = DataBase()
    # print(d.get_attribute('cpu','1.2.1.4','server'))
    print(d.get_relation_configuration('datacenter','server','1.2.1.5'))
    print(d.get_relation_has_in('cluster','datacenter','1.8.9.8'))
