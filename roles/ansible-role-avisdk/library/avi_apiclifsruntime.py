#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.1
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_apiclifsruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of APICLifsRuntime Avi RESTful Object
description:
    - This module is used to configure APICLifsRuntime object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    auto_allocated:
        description:
            - Boolean flag to set auto_allocated.
    cifs:
        description:
            - List of cif.
    lif_label:
        description:
            - Lif_label of apiclifsruntime.
        required: true
    multi_vrf:
        description:
            - Boolean flag to set multi_vrf.
    name:
        description:
            - Name of the object.
        required: true
    network:
        description:
            - Network of apiclifsruntime.
    se_uuid:
        description:
            - Unique object identifier of se.
    subnet:
        description:
            - Subnet of apiclifsruntime.
    tenant_name:
        description:
            - Tenant_name of apiclifsruntime.
        required: true
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    transaction_uuid:
        description:
            - Unique object identifier of transaction.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
    vs_uuid:
        description:
            - Unique object identifier of vs.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create APICLifsRuntime object
  avi_apiclifsruntime:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_apiclifsruntime
"""

RETURN = '''
obj:
    description: APICLifsRuntime (api/apiclifsruntime) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or (sdk_version and
            (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        auto_allocated=dict(type='bool',),
        cifs=dict(type='list',),
        lif_label=dict(type='str', required=True),
        multi_vrf=dict(type='bool',),
        name=dict(type='str', required=True),
        network=dict(type='str',),
        se_uuid=dict(type='list',),
        subnet=dict(type='str',),
        tenant_name=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        transaction_uuid=dict(type='list',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vs_uuid=dict(type='list',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'apiclifsruntime',
                           set([]))

if __name__ == '__main__':
    main()
