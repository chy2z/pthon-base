"""
演示导入模块使用
"""
import sys
sys.path.append("..")
# 导入根目录模块
# import module
# 导入其他目录模块
from module.print_module import *

print_fun("jack")

