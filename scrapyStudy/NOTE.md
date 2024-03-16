# scrapy

## 新建工程

```bash
scrapy startproject tutorial
```

工程文件如下

```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

在tutorial/spiders文件下放入爬虫文件，定义一个类继承 `scrapy.Spider`，其中预定的属性和方法包括：

```python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

* name：爬虫文件的唯一标识
* start_requests( )：必须返回请求，当只写一个url列表也可以不写这个方法，scrapy会自动调用该方法
* parse( )：解析请求

运行爬虫

```bash
scrapy crawl quote
```

此时就会生成爬取的两个HTML文件



你也可以直接不进行保存而直接返回一个可迭代对象：

```py
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
```

之后通过命令以json保存结果：

```bash
scrapy crawl quotes2 -o quotes.json
```

但注意scrapy不会清空已有json文件再写入，多次操作会导致得到错误的json文件

## 选择器

可以通过浏览器自带的开发者工具来定位元素，但是这里推荐使用SelectorGadget这个扩展来定位元素，这个扩展可以在点击选中元素后自动高亮所有相同的类型的元素，并给出最小css选择器和对应的xpath路径

### CSS选择器

此命令可以获取给定url内容

```bash
scrapy shell "http://quotes.toscrape.com/page/1/"
```

通过CSS选择器选择元素

```bash
# 1. 通过调用响应的CSS方法获取整个元素
>>>response.css('title')
[<Selector xpath='descendant-or-self::title'data='<title>Quotes to Scrape</title>'>]
# 2. 通过getall返回符合元素的列表
>>>response.css('title::text').getall() 
['Quotes to Scrape']
# 3. 如果没有::text则返回整个元素标签
>>>response.css('title').getall() 
['<title>Quotes to Scrape</title>']
# 4. get方法默认返回符合条件的第一个元素
>>>response.css('title::text').get() 
'Quotes to Scrape'
# 5. 也可以通过索引指定返回第几个符合的元素
>>>response.css('title::text')[0].get() 
'Quotes to Scrape'
# 6. 最后返回的内容也可以通过正则表达式处理
>>>response.css('title::text').re(r'(\w+)to(\w+)') 
['Quotes','Scrape']
```

### xpath选择器

尽管css已经能完成大部分元素选择，但是xpath拥有更多的功能，在爬虫中也更加推荐使用xpath来查找元素：

```bash
>>>response.xpath('//title')
[<Selector xpath='//title'data='<title>Quotes to Scrape</title>'>] 

>>>response.xpath('//title/text()').get() 
'Quotes to Scrape'
```

下面将通过一些举例来快速学习xpath语法：

#### 选取节点

| 路径表达式      | 结果                                                         |
| --------------- | ------------------------------------------------------------ |
| bookstore       | 选取 bookstore 元素的所有子节点                              |
| /bookstore      | 选取根元素 bookstore                                         |
| bookstore/book  | 选取属于 bookstore 的子元素的所有 book 元素                  |
| //book          | 选取所有 book 子元素，而不管它们在文档中的位置               |
| bookstore//book | 选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置 |
| //@lang         | 选取名为 lang 的所有属性                                     |
| /..             | 选择父节点                                                   |

#### 属性和位置

| 路径表达式                    | 结果                                                                    |
| ----------------------------- | ----------------------------------------------------------------------- |
| /bookstore/book[1]            | 选取属于 bookstore 子元素的第一个 book 元素。                           |
| /bookstore/book[last()]       | 选取属于 bookstore 子元素的最后一个 book 元素。                         |
| /bookstore/book[last()-1]     | 选取属于 bookstore 子元素的倒数第二个 book 元素。                       |
| /bookstore/book[position()<3] | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。               |
| //title[@lang]                | 选取所有拥有名为 lang 的属性的 title 元素。                             |
| //title[@lang='eng']          | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。              |
| /bookstore/book[@price>35.00] | 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.0 |

#### 未知节点

| 路径表达式   | 结果                            |
| ------------ | ------------------------------- |
| /bookstore/* | 选取 bookstore 元素的所有子元素 |
| //*          | 选取文档中的所有元素            |
| //title[@*]  | 选取所有带有属性的 title 元素   |

#### 同时选择

| 路径表达式                       | 结果                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| //book/title \| //book/price     | 选取 book 元素的所有 title 和 price 元素                     |
| //title \| //price               | 选取文档中的所有 title 和 price 元素                         |
| /bookstore/book/title \| //price | 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素 |

## 获取链接

可以通过两种方式获取元素中的链接：

```py
response.css('li.next a::attr(href)').get()
response.css('li.next a').attrib['href']
```

通过返回Request请求达到多次调用的目的：

```py
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # 这个方法是将相对路径拼接成绝对路径
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
```

response.follow()可以直接拼接地址

```py
for href in response.css('li.next a::attr(href)'):
    yield response.follow(href, callback=self.parse)
```

其实直接传入a标签也能直接解析

```py
for a in response.css('li.next a'):
    yield response.follow(a, callback=self.parse)
```

## 分页爬取

```py
import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
```

1. parse函数第一个循环获取当前页面的作者信息并且进行提取，传递给parse_author解析
2. 当该页完成后，找到下一页的元素并且进行点击，然后递归调用parse解析

### 自定义参数

运行scrapy时可以传递参数给爬虫进行使用

```py
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        # 接收传递过来的参数
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
```

之后运行下面的命令即可

```bash
scrapy crawl quotes -o quotes-humor.json -a tag=humor
```





