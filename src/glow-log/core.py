import os
import sys
import time

class glow_log:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.log_file = open(log_file_path, 'a')

    def info(self, message):
        self.log(message, 'INFO')

    def warning(self, message):
        self.log(message, 'WARNING')

    def log(self, message, log_level):
        current_time = time.ctime()
        log_message = f'{current_time} - {log_level}: {message}\n'
        self.log_file.write(log_message)
        self.log_file.flush()
