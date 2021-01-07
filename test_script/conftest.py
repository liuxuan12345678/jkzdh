'''
脚本层的一些公共方法
'''
#################################
'''
python导包时，搜索包的规则：
1.如果使用IDE：从当前工程路径、当前执行文件路径、python安装目录找包。
2.命令行执行时：从当前执行文件路径、python安装目录找包。
 执行命令为：先到test_script文件的上一级目录，然后在上面地之栏输入:cmd->回车，最好在命令行输入：pytest zonghe\test_script  ->  回车
 命令行执行时，报错找不到包。解决办法：把工程路径，放到sys.path中。
'''
import sys
import os
print(sys.path)  #  sys.path：当前的环境变量
cp = os.path.realpath(__file__)  # 获取当前文件的绝对路径
print(cp)
cd = os.path.dirname(cp)  # 获取当前文件的绝对路径的上一级目录
# print(cd)
cd = os.path.dirname(cd)  # 在前一次的基础上在上一级目录
# print(cd)
cd = os.path.dirname(cd)  # 在前一次的基础上在上一级目录
# print(cd)
sys.path.append(cd)
############################
import pytest
from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests

env_path = r"data_env\env.ini"

# 读取env.ini中的url,设置session级别的，整个执行过程读一次。
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path,"url")

@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path,"db"))

# 创建一个BaseRequests的实例,设置session级别，整个执行过程只有一个实例，自动管理Cookie
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()