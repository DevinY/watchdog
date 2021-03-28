#!/bin/env python3
# -*- coding: utf-8 -*-
import time 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
from action import created, others, folder
  
class ObServer: 
    # 設定監控目錄
    watchDirectory = folder
  
    def __init__(self): 
        self.observer = Observer() 
  
    def run(self): 
        event_handler = Handler() 
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
  
 #處理事件 
class Handler(FileSystemEventHandler): 
  
    @staticmethod
    def on_any_event(event): 
        prefix = ""
        if event.is_directory: 
            return None
        elif event.event_type == 'created': 
            # 檔案已新增，在這裡建立要執行的動作
            created(event)
        else:
            others(event)

  
if __name__ == '__main__': 
    watch = ObServer() 
    watch.run() 
