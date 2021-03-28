#pip install watchdog
import os
# 設定監控目錄
folder = os.path.dirname(os.path.abspath(__file__))

#動作
def created(event):
    print(event.event_type)
    print("Watchdog 收到建立事件 - % s." % event.src_path) 

#其他事件
def others(event):
    print(event.event_type)
    print("%s" % event.src_path) 
