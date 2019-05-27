# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import uuid


# WHY: 这里不能体现uuid3的作用？
# 基于名字的MD5散列值。通过计算名字和命名空间的MD5散列值得到，
# 保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，
# 但同一命名空间的同一名字生成相同的uuid

def uniqid():
    return uuid.uuid3(
        uuid.uuid1(),
        uuid.uuid4().hex
    ).hex


def node_uniqid():
    uid = uniqid()
    node_uid = 'node%s' % uid
    return node_uid[:-4]


def line_uniqid():
    uid = uniqid()
    node_uid = 'line%s' % uid
    return node_uid[:-4]
