# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CostAllocationTag(Model):
    """The cost allocation tag.

    :param key_name: Cost allocation tag key name.
    :type key_name: str
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(self, key_name=None):
        super(CostAllocationTag, self).__init__()
        self.key_name = key_name
