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


class FilterTrackPropertyCondition(Model):
    """The class to specify one track property condition.

    All required parameters must be populated in order to send to Azure.

    :param property: Required. The track property type. Possible values
     include: 'Unknown', 'Type', 'Name', 'Language', 'FourCC', 'Bitrate'
    :type property: str or ~azure.mgmt.media.models.FilterTrackPropertyType
    :param value: Required. The track proprty value.
    :type value: str
    :param operation: Required. The track property condition operation.
     Possible values include: 'Equal', 'NotEqual'
    :type operation: str or
     ~azure.mgmt.media.models.FilterTrackPropertyCompareOperation
    """

    _validation = {
        'property': {'required': True},
        'value': {'required': True},
        'operation': {'required': True},
    }

    _attribute_map = {
        'property': {'key': 'property', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FilterTrackPropertyCondition, self).__init__(**kwargs)
        self.property = kwargs.get('property', None)
        self.value = kwargs.get('value', None)
        self.operation = kwargs.get('operation', None)
