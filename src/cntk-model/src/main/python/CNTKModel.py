# Copyright (C) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.

import sys

if sys.version >= '3':
    basestring = str

from mmlspark._CNTKModel import _CNTKModel
from pyspark.ml.common import inherit_doc

@inherit_doc
class CNTKModel(_CNTKModel):
    """
    :param SparkSession SparkSession: The SparkSession that will be used to find the model
    :param str location: The location of the model, either on local or HDFS
    """
    def setModel(self, sparkSession, location):
        jSpark = sparkSession._jsparkSession
        self._java_obj = self._java_obj.setModel(jSpark, location)
        return self
