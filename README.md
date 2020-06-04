# Create two files

## matt.py

```python
#!/usr/bin/python3

from mattermostdriver import Driver

matt = Driver({
    'url': '<baseurl>',
    'login_id': '<login>',
    'password': '<password>',
    'scheme': 'https',
    'port': 443,
    'basepath': '/api/v4',
    'verify': True,
    'debug': False
})

matt.login()

```
## channel.py

```python
#!/usr/bin/python3
from matt import matt
from awesomepost.awesomematt import AwesomePost

my_channel = matt.channels.get_channel(channel_id='<channel_id>')
post = AwesomePost(matt, my_channel)

```
