# coding=utf-8
import logging

# 第一步，创建一个logger
logger = logging.getLogger()
# Log等级总开关
logger.setLevel(logging.DEBUG)

# 第二步，创建一个handler，用于写入日志文件
logfile = './logger/logger.txt'
fh = logging.FileHandler(logfile, mode='w',encoding='utf-8')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logger.debug('中文:this is a logger debug message')
logger.info('中文:this is a logger info message')
logger.warning('中文:this is a logger warning message')
logger.error('中文:this is a logger error message')
logger.critical('中文:this is a logger critical message')