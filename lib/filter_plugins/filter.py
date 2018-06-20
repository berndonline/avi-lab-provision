#!/user/bin/python
# -*- coding: utf-8 -*-

def compile_node_ips(ip_list):
    return [{"ip": {"addr": x, "type": "V4"}, "name": x} for x in ip_list]

def compile_node_dns(dns_list):
    return [ {"addr": x, "type": "V4"} for x in dns_list]

def compile_node_ntp(ntp_list):
    return [{"server": {"addr": x, "type": "DNS"}} for x in ntp_list]

class FilterModule(object):
    def filters(self):
        return {
            'compile_node_ips'       : compile_node_ips,
            'compile_node_dns'       : compile_node_dns,
            'compile_node_ntp'       : compile_node_ntp
        }

