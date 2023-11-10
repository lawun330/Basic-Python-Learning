#!/usr/bin/env python3

import shutil
import psutil

'''free space and CPU check'''

def has_free_space(disk):
	du = shutil.disk_usage(disk)
	return (du.free/du.total *100)>25

def is_cpu_safe():
	percent = psutil.cpu_percent(1)
	return percent < 75

if not is_cpu_safe() or not has_free_space("/"):
	print("ERROR!")
else :
	print("Everything is OK!")
