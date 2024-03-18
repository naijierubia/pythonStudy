import re

regex = '</span><a title="(.*?)".*?' \
                     'href="//www.bilibili.com/video/(.*?)\?.*?' \
                     '<div class="des hide">(.*?)</div>.*?' \
                     '<i class="icon-playtime"></i>(.*?)</span>.*?' \
                     '<i class="icon-date"></i>(.*?)</span>.*?' \
                     'class="up-name">(.*?)</a>'

html = """
href="//www.bilibili.com/video/BV1m8411j7EH?from=search" title="【碧蓝航线】11月18日莱莎联动生放送总结，联动角色4金2紫，睡衣主题皮肤登场" target="_blank" class="img-anchor"><div class="img"><div class="lazy-img"><img alt="" src=""></div><span class="so-imgTag_rb">02:38</span><div class="watch-later-trigger watch-later"></div><span class="mask-video"></span></div><!----></a><div class="info"><div class="headline clearfix"><!----><!----><span class="type hide">手机游戏</span><a title="【碧蓝航线】11月18日莱莎联动生放送总结，联动角色4金2紫，睡衣主题皮肤登场" href="//www.bilibili.com/video/BV1m8411j7EH?from=search" target="_blank" class="title">【<em class="keyword">碧蓝航线</em>】11月18日莱莎联动生放送总结，联动角色4金2紫，睡衣主题皮肤登场</a></div><div class="des hide">
      生放送原图请去碧蓝航线wiki欣赏喵
bgm：Machico - 願いのカタチ
    </div><div class="tags"><span title="观看" class="so-icon watch-num"><i class="icon-playtime"></i>
        7.7万
      </span><span title="弹幕" class="so-icon hide"><i class="icon-subtitle"></i>
        247
      </span><span title="上传时间" class="so-icon time"><i class="icon-date"></i>
        2022-11-18
      </span><span title="up主" class="so-icon"><i class="icon-uper"></i><a href="//space.bilibili.com/41377819?from=search" target="_blank" class="up-name">猫姐姐nya</a></span></div></div></li><li class="video-item matrix"><a 

"""
p = re.compile(regex, re.S)
print(p.findall(html))
