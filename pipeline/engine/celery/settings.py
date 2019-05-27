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

"""
配置说明：
    任务队列：2个
        pipeline: pipeline相关任务（进程启动，状态转移等）
        service_schedule: service调度任务
    工作进程启动参考：
    pworker: python manage.py celery worker -Q pipeline -n pipeline_worker@%h -c 6 -l info --maxtasksperchild=50
    sworker: celery worker -A blueapps.core.celery -P gevent -Q service_schedule -c 6 -l info -n schedule_worker@%h --maxtasksperchild=50
    
"""

from kombu import Exchange, Queue

default_exchange = Exchange('default', type='direct')

PIPELINE_ROUTING = {
    'queue': 'pipeline',
    'routing_key': 'pipeline_push'
}

CELERY_ROUTES = {
    # schedule
    'pipeline.engine.tasks.service_schedule': {
        'queue': 'service_schedule',
        'routing_key': 'schedule_service'
    },
    # pipeline
    'pipeline.engine.tasks.batch_wake_up': PIPELINE_ROUTING,
    'pipeline.engine.tasks.dispatch': PIPELINE_ROUTING,
    'pipeline.engine.tasks.process_wake_up': PIPELINE_ROUTING,
    'pipeline.engine.tasks.start': PIPELINE_ROUTING,
    'pipeline.engine.tasks.wake_from_schedule': PIPELINE_ROUTING,
    'pipeline.engine.tasks.wake_up': PIPELINE_ROUTING
}

CELERY_QUEUES = (
    Queue('pipeline', default_exchange, routing_key='pipeline_push'),
    Queue('service_schedule', default_exchange, routing_key='schedule_service'),
)

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'
