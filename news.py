from component.toutiao import TTBot

bot = TTBot()
# 新闻爬虫
spider = bot.news_spider

#获取首页推荐新闻,ALL置真表示获取所有，MDB置真表示存入数据库
# recommend_news = spider.get_recommend_news(ALL=True)
#获取首页推荐新闻,ALL置False,count=100表示只获取前100条数据，MDB置真表示存入数据库
recommend_100 = spider.get_recommend_news(ALL=False,count=100)
#获取 2019-07-07 12:00:00 以后的所有 首页推荐新闻，时间之前的数据忽略
recommend_by_dtime = spider.get_recommend_news(ALL=True,last_time='2019-07-07 12:00:00')