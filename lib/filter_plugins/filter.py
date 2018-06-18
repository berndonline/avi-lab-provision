#!/user/bin/python
# -*- coding: utf-8 -*-

def compile_node_ips(ip_list):
    return [{"ip": {"addr": x, "type": "V4"}, "name": x} for x in ip_list]

class FilterModule(object):
    def filters(self):
        return {
            'compile_node_ips'       : compile_node_ips
        }

