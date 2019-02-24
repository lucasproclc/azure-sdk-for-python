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


try:
    from ._models_py3 import APIError
    from ._models_py3 import Address
    from ._models_py3 import Body
    from ._models_py3 import BodyModel
    from ._models_py3 import Candidate
    from ._models_py3 import Classification
    from ._models_py3 import ClassificationCategory1
    from ._models_py3 import ClassificationCategory2
    from ._models_py3 import ClassificationCategory3
    from ._models_py3 import Content
    from ._models_py3 import CreateReviewBodyItem
    from ._models_py3 import CreateReviewBodyItemMetadataItem
    from ._models_py3 import CreateVideoReviewsBodyItem
    from ._models_py3 import CreateVideoReviewsBodyItemMetadataItem
    from ._models_py3 import CreateVideoReviewsBodyItemVideoFramesItem
    from ._models_py3 import CreateVideoReviewsBodyItemVideoFramesItemMetadataItem
    from ._models_py3 import CreateVideoReviewsBodyItemVideoFramesItemReviewerResultTagsItem
    from ._models_py3 import DetectedLanguage
    from ._models_py3 import DetectedTerms
    from ._models_py3 import Email
    from ._models_py3 import Error
    from ._models_py3 import Evaluate
    from ._models_py3 import Face
    from ._models_py3 import FoundFaces
    from ._models_py3 import Frame
    from ._models_py3 import Frames
    from ._models_py3 import IPA
    from ._models_py3 import Image
    from ._models_py3 import ImageAdditionalInfoItem
    from ._models_py3 import ImageIds
    from ._models_py3 import ImageList
    from ._models_py3 import Job
    from ._models_py3 import JobExecutionReportDetails
    from ._models_py3 import JobId
    from ._models_py3 import JobListResult
    from ._models_py3 import KeyValuePair
    from ._models_py3 import Match
    from ._models_py3 import MatchResponse
    from ._models_py3 import OCR
    from ._models_py3 import PII
    from ._models_py3 import Phone
    from ._models_py3 import RefreshIndex
    from ._models_py3 import Review
    from ._models_py3 import SSN
    from ._models_py3 import Screen
    from ._models_py3 import Status
    from ._models_py3 import Tag
    from ._models_py3 import TermList
    from ._models_py3 import Terms
    from ._models_py3 import TermsData
    from ._models_py3 import TermsInList
    from ._models_py3 import TermsPaging
    from ._models_py3 import TranscriptModerationBodyItem
    from ._models_py3 import TranscriptModerationBodyItemTermsItem
    from ._models_py3 import VideoFrameBodyItem
    from ._models_py3 import VideoFrameBodyItemMetadataItem
    from ._models_py3 import VideoFrameBodyItemReviewerResultTagsItem
    from ._models_py3 import APIErrorException
except (SyntaxError, ImportError):
    from ._models import APIError
    from ._models import Address
    from ._models import Body
    from ._models import BodyModel
    from ._models import Candidate
    from ._models import Classification
    from ._models import ClassificationCategory1
    from ._models import ClassificationCategory2
    from ._models import ClassificationCategory3
    from ._models import Content
    from ._models import CreateReviewBodyItem
    from ._models import CreateReviewBodyItemMetadataItem
    from ._models import CreateVideoReviewsBodyItem
    from ._models import CreateVideoReviewsBodyItemMetadataItem
    from ._models import CreateVideoReviewsBodyItemVideoFramesItem
    from ._models import CreateVideoReviewsBodyItemVideoFramesItemMetadataItem
    from ._models import CreateVideoReviewsBodyItemVideoFramesItemReviewerResultTagsItem
    from ._models import DetectedLanguage
    from ._models import DetectedTerms
    from ._models import Email
    from ._models import Error
    from ._models import Evaluate
    from ._models import Face
    from ._models import FoundFaces
    from ._models import Frame
    from ._models import Frames
    from ._models import IPA
    from ._models import Image
    from ._models import ImageAdditionalInfoItem
    from ._models import ImageIds
    from ._models import ImageList
    from ._models import Job
    from ._models import JobExecutionReportDetails
    from ._models import JobId
    from ._models import JobListResult
    from ._models import KeyValuePair
    from ._models import Match
    from ._models import MatchResponse
    from ._models import OCR
    from ._models import PII
    from ._models import Phone
    from ._models import RefreshIndex
    from ._models import Review
    from ._models import SSN
    from ._models import Screen
    from ._models import Status
    from ._models import Tag
    from ._models import TermList
    from ._models import Terms
    from ._models import TermsData
    from ._models import TermsInList
    from ._models import TermsPaging
    from ._models import TranscriptModerationBodyItem
    from ._models import TranscriptModerationBodyItemTermsItem
    from ._models import VideoFrameBodyItem
    from ._models import VideoFrameBodyItemMetadataItem
    from ._models import VideoFrameBodyItemReviewerResultTagsItem
    from ._models import APIErrorException


__all__=[
    'APIError',
    'Address',
    'Body',
    'BodyModel',
    'Candidate',
    'Classification',
    'ClassificationCategory1',
    'ClassificationCategory2',
    'ClassificationCategory3',
    'Content',
    'CreateReviewBodyItem',
    'CreateReviewBodyItemMetadataItem',
    'CreateVideoReviewsBodyItem',
    'CreateVideoReviewsBodyItemMetadataItem',
    'CreateVideoReviewsBodyItemVideoFramesItem',
    'CreateVideoReviewsBodyItemVideoFramesItemMetadataItem',
    'CreateVideoReviewsBodyItemVideoFramesItemReviewerResultTagsItem',
    'DetectedLanguage',
    'DetectedTerms',
    'Email',
    'Error',
    'Evaluate',
    'Face',
    'FoundFaces',
    'Frame',
    'Frames',
    'IPA',
    'Image',
    'ImageAdditionalInfoItem',
    'ImageIds',
    'ImageList',
    'Job',
    'JobExecutionReportDetails',
    'JobId',
    'JobListResult',
    'KeyValuePair',
    'Match',
    'MatchResponse',
    'OCR',
    'PII',
    'Phone',
    'RefreshIndex',
    'Review',
    'SSN',
    'Screen',
    'Status',
    'Tag',
    'TermList',
    'Terms',
    'TermsData',
    'TermsInList',
    'TermsPaging',
    'TranscriptModerationBodyItem',
    'TranscriptModerationBodyItemTermsItem',
    'VideoFrameBodyItem',
    'VideoFrameBodyItemMetadataItem',
    'VideoFrameBodyItemReviewerResultTagsItem',
    'APIErrorException',
]
