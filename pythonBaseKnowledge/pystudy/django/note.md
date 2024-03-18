# Django项目结构
settings.py 配置文件

urls.py 路由文件

wsgi.py 正式启动文件

## settings.py 配置文件

```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 项目所在的路径，即setting.py所在的爷爷级绝对路径路径

BASE_DIR = Path(__file__).resolve().parent.parent
>>>F:\creation\std\python\pystudy\django\mysitel\mysitel\settings.py

# SECURITY WARNING: don't run with debug turned on in production!
# 修改文件后立即刷新，并且出错时会出现报错界面简单分析报错原因
DEBUG = True

# 允许访问的ip地址
ALLOWED_HOSTS = []

# 主路由位置
ROOT_URLCONF = 'mysitel.urls'

# 语言
LANGUAGE_CODE = 'zh-Hans'
# 时区
TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

```



## url.py

```py
# 由上到下，逐个匹配，符合退出
urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/001', views.page_001_view, name='page_001'),
    path('page/<int:pageNumbers>', views.pageN_view, name='pageN')
    path('/<int:NumberA>/')
]
```

