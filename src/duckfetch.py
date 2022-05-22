"""
                GNU GENERAL PUBLIC LICENSE
                    Version 2, June 1991
                Copyright Matteo Krstic 2022

Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
Everyone is permitted to copy and distribute verbatim copies
"""

import rich
import uptime
import socket
import rich 
import subprocess
import psutil

from rich import *


# Uptime
uptime_         = uptime.uptime()
uptime_days     = int(uptime_ / 86400)
uptime_hours    = int((uptime_ / 3600) - (uptime_days * 24))
uptime_minutes  = int((uptime_ / 60) - (uptime_days * 1440) - (uptime_hours * 60))
uptime_seconds  = int(uptime_ - (uptime_days * 86400) - (uptime_hours * 3600) - (uptime_minutes * 60))
uptime_concat   = f" {uptime_hours}h {uptime_minutes}m {uptime_seconds}s"

# Hostname and username
hostname        = socket.gethostname()
username        = subprocess.check_output(["whoami"],stdin=subprocess.PIPE, shell=True).decode("utf-8").strip()
username_concat = f"{username}@{hostname}"
responsive_bar  = f"".join(['-' for i in range(len(username_concat))])

# Shell
shell_path      = subprocess.check_output(["echo $SHELL"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('\n')[0]
shell_version   = subprocess.check_output([f"{shell_path} --version"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('\n')[0]
distribution    = subprocess.check_output(["cat /etc/os-release"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('"')[1]

# Hardware stats
cpu             = psutil.cpu_percent()
ram             = subprocess.check_output(["free -m"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('\n')[1].split()
ram_used        = int(ram[2])
ram_total       = int(ram[1])
ram_concat      = f"{ram_used}MB/{ram_total}MB"

duck = f"""
                     [red][bold]{username_concat}[reset]
                     {responsive_bar}
[yellow]      ,~~. [reset]         [while][bold] Distribution: [reset][green][bold]{distribution}[reset]
[yellow] ,   (  - )>[reset]        [while][bold] Shell: [reset][green][bold]  {shell_version}[reset]
[yellow] )`~~'   ([reset]          [while][bold] Uptime: [reset][green][bold]{uptime_concat}[reset]
[yellow](  .__)   )[reset]         [while][bold] RAM: [reset][green][bold]{ram_concat}[reset]
[yellow] `-.____,'[reset]          [white][bold] CPU: [reset][green][bold]{cpu}%[reset]
"""

print(duck)
print("[bold red]██████[/bold red]", "[bold green]██████[/bold green]", "[bold yellow]██████[/bold yellow]", "[bold blue]██████[/bold blue]", "[bold magenta]██████[/bold magenta]", "[bold cyan]██████[/bold cyan]", "[bold white]██████[/bold white]", sep="")
print("[red]██████[/red]", "[green]██████[/green]", "[yellow]██████[/yellow]", "[blue]██████[/blue]", "[magenta]██████[/magenta]", "[cyan]██████[/cyan]", "[white]██████[/white]", sep="")
