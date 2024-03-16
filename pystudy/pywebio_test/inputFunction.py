from pywebio.input import *
from pywebio.output import *


put_image('http://example.com/some-image.png') # internet image
# Markdown Output
put_markdown('~~Strikethrough~~')
# File Output
put_file('hello_word.txt', b'hello word!')
# Show a PopUp
popup('popup title', 'popup text content')
# Show a notification message
toast('New message')





