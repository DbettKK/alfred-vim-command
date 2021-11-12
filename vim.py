# -*- coding:utf-8 -*-
import sys
from workflow import Workflow
import key_map

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')


def main(workflow):
    key_map.init()
    for k in key_map.key_map:
        workflow.add_item(title=k, subtitle=key_map.key_map.get(k))
    workflow.add_item(title="this is test", subtitle="this is a test")
    workflow.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
