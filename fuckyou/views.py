# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from pipeline import builder
from pipeline.builder import EmptyStartEvent, ServiceActivity, EmptyEndEvent
from pipeline.parser import PipelineParser
from pipeline.service import task_service


def test(request):
    # 使用 builder 构造出流程描述结构
    start = EmptyStartEvent()
    act = ServiceActivity(component_code='example_component')
    end = EmptyEndEvent()

    start.extend(act).extend(end)

    tree = builder.build_tree(start)

    # 根据流程描述结构创建流程对象
    parser = PipelineParser(pipeline_tree=tree)
    pipeline = parser.parse()

    # 执行流程对象
    task_service.run_pipeline(pipeline)

    return HttpResponse('hello')
