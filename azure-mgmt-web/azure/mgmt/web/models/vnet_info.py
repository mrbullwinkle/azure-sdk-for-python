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

from .proxy_only_resource import ProxyOnlyResource


class VnetInfo(ProxyOnlyResource):
    """Virtual Network information contract.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param vnet_resource_id: The Virtual Network's resource ID.
    :type vnet_resource_id: str
    :ivar cert_thumbprint: The client certificate thumbprint.
    :vartype cert_thumbprint: str
    :param cert_blob: A certificate file (.cer) blob containing the public key
     of the private key used to authenticate a
     Point-To-Site VPN connection.
    :type cert_blob: bytearray
    :ivar routes: The routes that this Virtual Network connection uses.
    :vartype routes: list[~azure.mgmt.web.models.VnetRoute]
    :ivar resync_required: <code>true</code> if a resync is required;
     otherwise, <code>false</code>.
    :vartype resync_required: bool
    :param dns_servers: DNS servers to be used by this Virtual Network. This
     should be a comma-separated list of IP addresses.
    :type dns_servers: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'cert_thumbprint': {'readonly': True},
        'routes': {'readonly': True},
        'resync_required': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'vnet_resource_id': {'key': 'properties.vnetResourceId', 'type': 'str'},
        'cert_thumbprint': {'key': 'properties.certThumbprint', 'type': 'str'},
        'cert_blob': {'key': 'properties.certBlob', 'type': 'bytearray'},
        'routes': {'key': 'properties.routes', 'type': '[VnetRoute]'},
        'resync_required': {'key': 'properties.resyncRequired', 'type': 'bool'},
        'dns_servers': {'key': 'properties.dnsServers', 'type': 'str'},
    }

    def __init__(self, kind=None, vnet_resource_id=None, cert_blob=None, dns_servers=None):
        super(VnetInfo, self).__init__(kind=kind)
        self.vnet_resource_id = vnet_resource_id
        self.cert_thumbprint = None
        self.cert_blob = cert_blob
        self.routes = None
        self.resync_required = None
        self.dns_servers = dns_servers
