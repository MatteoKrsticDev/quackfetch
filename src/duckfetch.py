"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

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

Uptime = uptime.uptime()
UptimeDays = int(Uptime / 86400)
UptimeHours = int((Uptime / 3600) - (UptimeDays * 24))
UptimeMinutes = int((Uptime / 60) - (UptimeDays * 1440) - (UptimeHours * 60))
UptimeSeconds = int(Uptime - (UptimeDays * 86400) - (UptimeHours * 3600) - (UptimeMinutes * 60))
UptimeConcat = f" {UptimeHours}h {UptimeMinutes}m {UptimeSeconds}s"
hostname = socket.gethostname()
username = subprocess.check_output(["whoami"],stdin=subprocess.PIPE, shell=True).decode("utf-8").strip()
usernameConcat = f"{username}@{hostname}"
responsivebar = f"".join(['-' for i in range(len(usernameConcat))])
ShellPath = subprocess.check_output(["echo $SHELL"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('\n')[0]
ShellVersion = subprocess.check_output([f"{ShellPath} --version"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('\n')[0]
distribution = subprocess.check_output(["cat /etc/os-release"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('"')[1]
cpu = psutil.cpu_percent()
ram = subprocess.check_output(["free -m"],stdin=subprocess.PIPE, shell=True).decode("utf-8").split('\n')[1].split()
ram_used = int(ram[2])
ram_total = int(ram[1])
RAMConcat = f"{ram_used}MB/{ram_total}MB"

duck = f"""
                     [red][bold]{usernameConcat}[reset]
                     {responsivebar}
[yellow]      ,~~. [reset]         [while][bold] Distribution: [reset][green][bold]{distribution}[reset]
[yellow] ,   (  - )>[reset]        [while][bold] Shell: [reset][green][bold]  {ShellVersion}[reset]
[yellow] )`~~'   ([reset]          [while][bold] Uptime: [reset][green][bold]{UptimeConcat}[reset]
[yellow](  .__)   )[reset]         [while][bold] RAM: [reset][green][bold]{RAMConcat}[reset]
[yellow] `-.____,'[reset]          [white][bold] CPU: [reset][green][bold]{cpu}%[reset]
"""                              
print(duck)
print("[bold red]██████[/bold red]", "[bold green]██████[/bold green]", "[bold yellow]██████[/bold yellow]", "[bold blue]██████[/bold blue]", "[bold magenta]██████[/bold magenta]", "[bold cyan]██████[/bold cyan]", "[bold white]██████[/bold white]", sep="")
print("[red]██████[/red]", "[green]██████[/green]", "[yellow]██████[/yellow]", "[blue]██████[/blue]", "[magenta]██████[/magenta]", "[cyan]██████[/cyan]", "[white]██████[/white]", sep="")