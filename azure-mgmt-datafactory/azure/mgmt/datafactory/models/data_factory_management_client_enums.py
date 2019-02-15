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

from enum import Enum


class IntegrationRuntimeState(str, Enum):

    initial = "Initial"
    stopped = "Stopped"
    started = "Started"
    starting = "Starting"
    stopping = "Stopping"
    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    access_denied = "AccessDenied"


class IntegrationRuntimeAutoUpdate(str, Enum):

    on = "On"
    off = "Off"


class ParameterType(str, Enum):

    object_enum = "Object"
    string = "String"
    int_enum = "Int"
    float_enum = "Float"
    bool_enum = "Bool"
    array = "Array"
    secure_string = "SecureString"


class DependencyCondition(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    skipped = "Skipped"
    completed = "Completed"


class VariableType(str, Enum):

    string = "String"
    bool_enum = "Bool"
    array = "Array"


class TriggerRuntimeState(str, Enum):

    started = "Started"
    stopped = "Stopped"
    disabled = "Disabled"


class RunQueryFilterOperand(str, Enum):

    pipeline_name = "PipelineName"
    status = "Status"
    run_start = "RunStart"
    run_end = "RunEnd"
    activity_name = "ActivityName"
    activity_run_start = "ActivityRunStart"
    activity_run_end = "ActivityRunEnd"
    activity_type = "ActivityType"
    trigger_name = "TriggerName"
    trigger_run_timestamp = "TriggerRunTimestamp"


class RunQueryFilterOperator(str, Enum):

    equals = "Equals"
    not_equals = "NotEquals"
    in_enum = "In"
    not_in = "NotIn"


class RunQueryOrderByField(str, Enum):

    run_start = "RunStart"
    run_end = "RunEnd"
    pipeline_name = "PipelineName"
    status = "Status"
    activity_name = "ActivityName"
    activity_run_start = "ActivityRunStart"
    activity_run_end = "ActivityRunEnd"
    trigger_name = "TriggerName"
    trigger_run_timestamp = "TriggerRunTimestamp"


class RunQueryOrder(str, Enum):

    asc = "ASC"
    desc = "DESC"


class TriggerRunStatus(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    inprogress = "Inprogress"


class TumblingWindowFrequency(str, Enum):

    minute = "Minute"
    hour = "Hour"


class BlobEventTypes(str, Enum):

    microsoft_storage_blob_created = "Microsoft.Storage.BlobCreated"
    microsoft_storage_blob_deleted = "Microsoft.Storage.BlobDeleted"


class DayOfWeek(str, Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class DaysOfWeek(str, Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class RecurrenceFrequency(str, Enum):

    not_specified = "NotSpecified"
    minute = "Minute"
    hour = "Hour"
    day = "Day"
    week = "Week"
    month = "Month"
    year = "Year"


class SparkServerType(str, Enum):

    shark_server = "SharkServer"
    shark_server2 = "SharkServer2"
    spark_thrift_server = "SparkThriftServer"


class SparkThriftTransportProtocol(str, Enum):

    binary = "Binary"
    sasl = "SASL"
    http = "HTTP "


class SparkAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    username = "Username"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"


class ServiceNowAuthenticationType(str, Enum):

    basic = "Basic"
    oauth2 = "OAuth2"


class PrestoAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    ldap = "LDAP"


class PhoenixAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"


class ImpalaAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    sasl_username = "SASLUsername"
    username_and_password = "UsernameAndPassword"


class HiveServerType(str, Enum):

    hive_server1 = "HiveServer1"
    hive_server2 = "HiveServer2"
    hive_thrift_server = "HiveThriftServer"


class HiveThriftTransportProtocol(str, Enum):

    binary = "Binary"
    sasl = "SASL"
    http = "HTTP "


class HiveAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    username = "Username"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"


class HBaseAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    basic = "Basic"


class GoogleBigQueryAuthenticationType(str, Enum):

    service_authentication = "ServiceAuthentication"
    user_authentication = "UserAuthentication"


class SapHanaAuthenticationType(str, Enum):

    basic = "Basic"
    windows = "Windows"


class SftpAuthenticationType(str, Enum):

    basic = "Basic"
    ssh_public_key = "SshPublicKey"


class FtpAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class HttpAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"
    digest = "Digest"
    windows = "Windows"
    client_certificate = "ClientCertificate"


class MongoDbAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class ODataAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class TeradataAuthenticationType(str, Enum):

    basic = "Basic"
    windows = "Windows"


class Db2AuthenticationType(str, Enum):

    basic = "Basic"


class SybaseAuthenticationType(str, Enum):

    basic = "Basic"
    windows = "Windows"


class DatasetCompressionLevel(str, Enum):

    optimal = "Optimal"
    fastest = "Fastest"


class JsonFormatFilePattern(str, Enum):

    set_of_objects = "setOfObjects"
    array_of_objects = "arrayOfObjects"


class AzureFunctionActivityMethod(str, Enum):

    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"
    options = "OPTIONS"
    head = "HEAD"
    trace = "TRACE"


class WebActivityMethod(str, Enum):

    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"


class CassandraSourceReadConsistencyLevels(str, Enum):

    all = "ALL"
    each_quorum = "EACH_QUORUM"
    quorum = "QUORUM"
    local_quorum = "LOCAL_QUORUM"
    one = "ONE"
    two = "TWO"
    three = "THREE"
    local_one = "LOCAL_ONE"
    serial = "SERIAL"
    local_serial = "LOCAL_SERIAL"


class StoredProcedureParameterType(str, Enum):

    string = "String"
    int_enum = "Int"
    decimal_enum = "Decimal"
    guid = "Guid"
    boolean = "Boolean"
    date_enum = "Date"


class SalesforceSourceReadBehavior(str, Enum):

    query = "Query"
    query_all = "QueryAll"


class HDInsightActivityDebugInfoOption(str, Enum):

    none = "None"
    always = "Always"
    failure = "Failure"


class SalesforceSinkWriteBehavior(str, Enum):

    insert = "Insert"
    upsert = "Upsert"


class AzureSearchIndexWriteBehaviorType(str, Enum):

    merge = "Merge"
    upload = "Upload"


class CopyBehaviorType(str, Enum):

    preserve_hierarchy = "PreserveHierarchy"
    flatten_hierarchy = "FlattenHierarchy"
    merge_files = "MergeFiles"


class PolybaseSettingsRejectType(str, Enum):

    value = "value"
    percentage = "percentage"


class SapCloudForCustomerSinkWriteBehavior(str, Enum):

    insert = "Insert"
    update = "Update"


class IntegrationRuntimeType(str, Enum):

    managed = "Managed"
    self_hosted = "SelfHosted"


class SelfHostedIntegrationRuntimeNodeStatus(str, Enum):

    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    upgrading = "Upgrading"
    initializing = "Initializing"
    initialize_failed = "InitializeFailed"


class IntegrationRuntimeUpdateResult(str, Enum):

    none = "None"
    succeed = "Succeed"
    fail = "Fail"


class IntegrationRuntimeInternalChannelEncryptionMode(str, Enum):

    not_set = "NotSet"
    ssl_encrypted = "SslEncrypted"
    not_encrypted = "NotEncrypted"


class ManagedIntegrationRuntimeNodeStatus(str, Enum):

    starting = "Starting"
    available = "Available"
    recycling = "Recycling"
    unavailable = "Unavailable"


class IntegrationRuntimeSsisCatalogPricingTier(str, Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    premium_rs = "PremiumRS"


class IntegrationRuntimeLicenseType(str, Enum):

    base_price = "BasePrice"
    license_included = "LicenseIncluded"


class IntegrationRuntimeEdition(str, Enum):

    standard = "Standard"
    enterprise = "Enterprise"


class SsisObjectMetadataType(str, Enum):

    folder = "Folder"
    project = "Project"
    package = "Package"
    environment = "Environment"


class IntegrationRuntimeAuthKeyName(str, Enum):

    auth_key1 = "authKey1"
    auth_key2 = "authKey2"
