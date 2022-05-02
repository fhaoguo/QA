
'''
定义模板：
query attribute:
1. what is the cpu?
   - what kind of entity do you want to ask?
   - server
   - please tell me about the ip of the entity
   - 1.2.3.4
   - 4 cores
2. what is the cpu of the 1.1.1.1?
   - please tell me about the entity of the ip
   - server
   - 4 cores
3. what is the cpu of the server 1.2.3.1
   - 5 cores


query relation
1. list all the server host in ?
   - what kind of entity do you ask?(datacenter, cluster)
   - cluster
   - please tell me about the ip of entity
   - 1.1.1.1
   - dataframe of servers
2. list all the server host in datacenter?
   - please tell me about the ip of entity
   - 1.1.1.1
   - dataframe of servers
3. list all the server host in datacenter 1.1.1.1
   - dataframe of servers



'''


with open('cluster.csv','r',encoding='utf-8') as f1:
    cluster = f1.readlines()
with open('datacenter.csv','r',encoding='utf-8') as f2:
    datacenter = f2.readlines()
with open('server.csv','r',encoding='utf-8') as f3:
    server = f3.readlines()

entity2attribute = {}

entity2ip = {}
entity2ip['cluster'] = []
entity2ip['datacenter'] = []
entity2ip['server'] = []
for index,line in enumerate(cluster):
    if index == 0:
        line = line.strip()
        line = line.split(',')
        ip = line[0]
        name = line[1]
        business = line[2]
        city = line[3]
        datacenter_ip = line[4]
        entity2attribute['cluster'] = [name,business,city,datacenter_ip]

    else:
        line = line.strip()
        line = line.split(',')
        # print(line)
        ip = line[0]
        entity2ip['cluster'].append(ip)

for index,line in enumerate(datacenter):
    if index == 0:
        line = line.strip()
        line = line.split(',')
        ip = line[0]
        name = line[1]
        longitude = line[2]
        latitude = line[3]
        region = line[4]
        cpu = line[5]
        entity2attribute['datacenter'] = [name, longitude, latitude, region,cpu]
    else:
        line = line.strip()
        line = line.split(',')
        ip = line[0]
        entity2ip['datacenter'].append(ip)

for index,line in enumerate(server):
    if index == 0:
        line = line.strip()
        line = line.split(',')
        ip = line[0]
        name = line[1]
        cpu = line[2]
        memory = line[3]
        disk = line[4]
        server_ip = line[5]
        datacenter_ip = line[6]
        entity2attribute['server'] = [name, cpu, memory, disk,server_ip,datacenter_ip]
    else:
        line = line.strip()
        line = line.split(',')
        ip = line[0]
        entity2ip['server'].append(ip)


relation2entity = {
    'host in':{'server':['cluster','datacenter'],'cluster':['datacenter']},
    'configuration by':{'datacenter':['cluster','server'],'cluster':['server']}
}
def write_query_attribute(f):
    f.write('## intent: query_attribute' + '\n')
    for entity,value in entity2attribute.items():
        ips = entity2ip[entity]
        for attribute in value:
            for ip in ips:
                temp1 = '- what is the ['+attribute+'](attribute) ?'
                temp2 = '- what is the ['+attribute+'](attribute) of the ['+ip+'](ip) ?'
                temp3 = '- what is the ['+attribute+'](attribute) of the [' +entity+'](entity) ['+ip+'](ip) ?'
                f.write(temp1 + '\n')
                f.write(temp2 + '\n')
                f.write(temp3 + '\n')

def write_query_ralation(f):
    for relation,entities in relation2entity.items():
        relation_ = relation.replace(' ','_')
        f.write('## intent: query_'+relation_ + '\n')
        for s_entity,o_entities in entities.items():
            for o_entity in o_entities:
                ips = entity2ip[o_entity]
                for ip in ips:
                    temp1 = '- list all the ['+s_entity+'](s_entity) '+relation + ' ?'
                    temp2 = '- list all the ['+s_entity+'](s_entity) '+relation+' ['+o_entity+'](o_entity) ?'
                    temp3 = '- list all the ['+s_entity+'](s_entity) '+relation+' ['+o_entity+'](o_entity) ['+ip+'](ip) ?'
                    f.write(temp1 + '\n')
                    f.write(temp2 + '\n')
                    f.write(temp3 + '\n')
def write_lookup(f):
    f.write('## lookup:entity' + '\n')
    f.write('  data/lookup/entity.txt' + '\n')
    f.write('## lookup:attribute' + '\n')
    f.write('  data/lookup/attribute.txt' + '\n')
    f.write('## lookup:s_entity' + '\n')
    f.write('  data/lookup/s_entity.txt' + '\n')
    f.write('## lookup:o_entity' + '\n')
    f.write('  data/lookup/o_entity.txt' + '\n')
    f.write('## lookup:ip' + '\n')
    f.write('  data/lookup/ip.txt' + '\n')


if __name__ == '__main__':
    f = open('./nlu.md','a',encoding='utf-8')
    write_query_attribute(f)
    write_query_ralation(f)
    write_lookup(f)










