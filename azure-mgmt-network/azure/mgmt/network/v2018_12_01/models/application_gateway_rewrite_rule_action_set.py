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


class ApplicationGatewayRewriteRuleActionSet(Model):
    """Set of actions in the Rewrite Rule in Application Gateway.

    :param request_header_configurations: Request Header Actions in the Action
     Set
    :type request_header_configurations:
     list[~azure.mgmt.network.v2018_12_01.models.ApplicationGatewayHeaderConfiguration]
    :param response_header_configurations: Response Header Actions in the
     Action Set
    :type response_header_configurations:
     list[~azure.mgmt.network.v2018_12_01.models.ApplicationGatewayHeaderConfiguration]
    """

    _attribute_map = {
        'request_header_configurations': {'key': 'requestHeaderConfigurations', 'type': '[ApplicationGatewayHeaderConfiguration]'},
        'response_header_configurations': {'key': 'responseHeaderConfigurations', 'type': '[ApplicationGatewayHeaderConfiguration]'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayRewriteRuleActionSet, self).__init__(**kwargs)
        self.request_header_configurations = kwargs.get('request_header_configurations', None)
        self.response_header_configurations = kwargs.get('response_header_configurations', None)
