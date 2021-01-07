'''
断言
'''
import pytest_check as ck
# check(r.json(),login_data['expect'],"code,msg,status")
def check(r_json,expect,keys):
    '''
    校验r_json与expect中，响应的key对应的value是否相同
    :param r_json:  实际的响应结果：r.json()
    :param expect:  预期结果
    :param keys:   校验的key列表，用逗号分隔：code,msg,status
    :return:
    '''
    ks = keys.split(",")  # 用逗号分隔
    for k in ks:
        real = r_json[k]  # 根据key取r_json中的value
        exp = expect[k]  # 根据key取expect中的value
        try:
            # assert str(real) == str(exp)
            ck.equal(str(real),str(exp))
        except Exception as e:
            print(f"响应信息：{r_json},预期结果：{expect},校验结果：{k}失败")