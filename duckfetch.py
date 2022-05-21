import os
import sys
import rich
import uptime
import socket
import rich 
import psutil
from rich.console import *

# print the hostname 

hostname = socket.gethostname()
uptime = uptime.uptime()
duck = f"""
      ,~~.          hostname: {hostname}
     (  9 )-_,      uptime: {uptime}
(\___ )=='-'
 \ .   ) )
  \ `-' /
   `~j-' 
     "=:
"""
print(duck)