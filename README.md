# imapnotes

stickyimapnotes is a Python / PySide2 application to read and write notes stored on an IMAPS server. It expects that your notes reside in the folder _Notes_ in your mailbox.
It looks like the Notes App from Microsoft, but can sync notes with the IOS note app

It is still being developed.



# Requirements

* Python 3.9
* PySide2
* html2text
* sqlalchemy
* PIL
* io
* uuid
* datetime


# Configuration

Create a file called _.imapnotes.ini_ in your home directory:

```
[connection]
host = _hostname of your IMAPS server_
# port = _optional port number if not 993_
user = _username to log into your mailbox_
pass = _your password_
```


