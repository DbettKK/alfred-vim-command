# -*- coding:utf-8 -*-
import sys
from workflow import Workflow
import key_map


def init():
    reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
    sys.setdefaultencoding('utf-8')
    key_map.init()


def main(workflow):
    args = workflow.args[0]
    keys = key_map.key_map.keys()
    for key in keys:
        if args in key:
            workflow.add_item(title=key, subtitle=key_map.key_map.get(key))
    for v in key_map.value_map.keys():
        if args in v:
            workflow.add_item(title=v, subtitle=key_map.value_map.get(v))
    workflow.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    init()
    sys.exit(wf.run(main))
