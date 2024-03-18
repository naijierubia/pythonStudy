import re

article01 = "2006年播放的《凉宫春日的忧郁》，2007年播放的《幸运☆星》，同样掀起了热潮。基本来说京都动画虽然曾经以Key" \
            "社作品闻名，但如今主要是把角川书店的轻小说或漫画作品动画化，同时也在摸索原创动画的道路，但其原创动画反倒难以得到成功的评价。" \
            "与《全金属狂潮》的作者贺东招二有很深的关系，《凉宫春日的忧郁》第11" \
            "话“射手座之日”，《幸运☆星》第5、12、22话的剧本都是由他担当的。原定2009年制作《隔壁的801腐女》，" \
            "因为诸般的事情被迫制作中止。2009年春季播出原创动画《Munto" \
            "》第三部，但因剧情等原因销量惨淡，是京都原创动画的一大失败。2009年将四格漫画《轻音少女》动画化，" \
            "这部以小成本制作的动画却再次在日本掀起热潮，发售的音乐CD创造了日本Oricon" \
            "公信榜动漫歌曲新的纪录，并于2010年推出第二季。2009年4月《凉宫春日的忧郁》重制为28集动画并用重播的名义播出，" \
            "同年12月18日剧场版《凉宫春日的消失》公映，取得8.5亿日元票房，并获得第15" \
            "届“动画神户赏”的剧场部门作品赏。2011年上旬，KA ESUMA文库正式建立，主要收录出版京都动画大赏得奖的作品。 "
print("测试")
print(re.search('《\w+?》', article01).group())  # 用列表存储符合规则的字符

"""
正则表达式
"""
print("\n普通字符值只寻找完全匹配的")
print(re.findall('ab', "abcdeacab"))

print('\n或关系|')
# 或的书写不能有空格，否则识别会加上空格
print(re.findall('cm|cn', "www.baidu.cm www.cm.cn"))

print("\n.匹配除了换行(\\n)之外的任意一个字符")
print(re.findall('张.丰', "张三丰 张四丰 张N丰"))

"""
字符区间[ ]
字符区间[0-9]|[a-z][A-Z]，[-a-z]非转义
^表示取反
可混合书写
"""
print('\n区间查找')
print(re.findall('[aeiou]', "How are you"))
print(re.findall('[a-u]', "How are you"))
print(re.findall('[^a-u]', "How are you"))

print("\n单独的^表示字符串的开头才能识别")
print("\n单独的$表示字符串的结尾才能识别")
# 可同时运用两种形成完全匹配
print(re.findall('^jarry', "jarry,oh,jarry"))
print(re.findall('jarry$', "jarry,oh,jarry"))

print("\n*匹配前面的字符出现0次或者多次")
print("+匹配前面的字符出现1次或者多次")
print(re.findall('wo*', "wooooooo-w!"))
print(re.findall('wo+', "wooooooo-w!"))
print(re.findall('[A-Z]+[a-z]*', "Hello, Are you OK?"))
print(re.findall('[0-9]+', "2022年10月4号"))
print(re.findall('.+', "2022年10月4号"))

print("\n?匹配前面的内容出现1/0次")
print(re.findall('-?[0-9]+', "今日南昌的气温为-2到8摄氏度"))

print("\n{m,n}匹配前面的内容出现m-n次")
print(re.findall('o{1,2}', "Are you ok? oooh, my good"))

print("\n\\d匹配数字字符\D匹配非数字字符，相当于[(^)0-9]")
print("\n\\w匹配普通字符\W匹配非普通字符")  # utf8，数字、字母、汉字、下划线
print(re.findall('-?\d+', "今日南昌的气温为-2到8摄氏度"))
print(re.findall('《\w+?》', article01))

print("\n\s匹配空字符\S匹配非空字符")  # 空字符表示\n \t \r \v \f
print(r"\b\B表示(非)单词边界")  # \b是退格

"""
test
"""
# 匹配邮箱格式
mail = "asdg sadg werq 2199646410@qq.com"
print(re.findall('\w+@[a-z]+\.com', mail))
# 匹配大写开头字母
string01 = "Hello I A CBD iPython"
print(re.findall(r'\b[A-Z]+[a-z]*', string01))

"""
默认为贪婪模式、非贪婪模式用？
"""
print(re.findall('《.+》', "《凉宫春日》和《轻音少女》都是京都动画的作品"))
print(re.findall('《.+?》', "《凉宫春日》和《轻音少女》都是京都动画的作品"))

"""
test02
"""
numbers = "1/2 1.6 11.5 -5 46.8% 1/3"
print(re.findall(r'-?\d+\.?/?\d*%?', numbers))
