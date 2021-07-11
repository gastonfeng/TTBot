from component.user import TTUser

user = TTUser('5787290902')

def print_data(data_item,sec_param):
    '''
    回调函数的第一个参数永远都是 获取到的单条json数据 get_published函数
    已经默认传入，所以在 cb_args 中需要传入的参数 只能从第二个参数开始
    当前函数 的 sec_param 值为:'This is the sec param' 即为cb_args
    的第一个值。
    返回值提醒:
        返回 None:回调函数处理后继续进行后续的数据库保存、格式清理等工作
        返回 True:回调函数处理后 忽略此条数据，进行下一条数据的获取处理
    '''
    print(data_item,sec_param)

# 对单条数据使用print_data回调函数处理
articles = user.get_published(count=100,data_cb=print_data,cb_args=('This is the sec param',))

#使用lambda 来表示上面的 回调处理
results =  user.get_published(count=100,data_cb=lambda x,y:print(x,y),cb_args=('This is the sec param',))