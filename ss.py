from urllib.request import urlopen

import execjs
import gne
import requests
from requests import request

from component.toutiao import TTBot

headers = {
    #    'cookie': 'tt_webid=6731181496139384324; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6731181496139384324; csrftoken=c73ecbc9df06a4ae0d23e05d37fb8b03; UM_distinctid=16ce5e8d711901-077cddbf26490d-f353163-144000-16ce5e8d712443; uuid="w:0eab1ab0084845a18c7108ace948c421"; __tasessionId=ejvfe2fta1567265113476; CNZZDATA1272960458=693129193-1567223451-https%253A%252F%252Fwww.baidu.com%252F%7C1567266006',
       'referer': 'https://www.toutiao.com/ch/news_tech/',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
   }



def get_cp_as():
    with open('cp_as.js', 'r') as f:
        js = f.read()
        context = execjs.compile(js)
        cp_as = context.call('getHoney')
        return cp_as

def get_signature():

    with open('sign.js', 'r') as f:
        js = f.read()
        context = execjs.compile(js)
        signature = context.call('tac')
        return signature

def get_url(behot_time):

    # 注意最后一个/要写，否则报错
    url = 'https://www.toutiao.com/api/pc/feed/'

    params = {
        'category': 'news_tech',
        'utm_source': 'toutiao',
        'widen': '1',
        'max_behot_time': behot_time,
        'max_behot_time_tmp': behot_time,
        'tadrequire': 'true',
        'as': get_cp_as().get('as'),
        'cp': get_cp_as().get('cp'),
        '_signature': get_signature()
    }

    return (url,params)

# url='http://toutiao.com/group/6720499469701349899/'
# # url=a['article_url']
# with urlopen(url) as res:
# # response = requests.get(url)
#     text=res.read()
#     extractor = gne.GeneralNewsExtractor()
#     result = extractor.extract(text, noise_node_list=['//div[@class="comment-list"]'])



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
bot = TTBot()
# 搜索 关键词 Gucci 的文章类头条结果，ALL置真表示获取所有结果，MDB置真表示使用数据库保存
# results_all = bot.search('Gucci',ALL=True,MDB=True)
# 搜索 关键词 Gucci 的文章类头条结果，ALL置False,count=100表示只获取100条结果，MDB置真表示使用数据库保存
results_100 = bot.search('LOra', ALL=False, MDB=False, count=10)

print(results_100)