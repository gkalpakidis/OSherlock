import os, platform, psutil


class Colors:
    DEFAULT = "\033[0m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREY = "\033[30m"
    CYAN = "\033[36m"
    PINK = "\033[35m"

def banner():
    print(Colors.RED + """
   ___     ______   __                    __                 __       
 .'   `. .' ____ \ [  |                  [  |               [  |  _   
/  .-.  \| (___ \_| | |--.  .---.  _ .--. | |  .--.   .---.  | | / ]  
| |   |  | _.____`. | .-. |/ /__\\ [ `/'`\]| |/ .'`\ \/ /'`\] | '' <   
\  `-'  /| \____) | | | | || \__., | |    | || \__. || \__.  | |`\ \  
 `.___.'  \______.'[___]|__]'.__.'[___]  [___]'.__.' '.___.'[__|  \_] v1.0

Provided to you by H@d3s. <3
""" + Colors.DEFAULT)

def seperator():
    print(Colors.GREY + "---------------------------------------------------------------------------\n")

#Sinartiseis leitourgion
def osInfo():
    os_info = platform.uname()
    print(f"{Colors.BLUE}System: {os_info.system}")
    print(f"{Colors.BLUE}System Name: {os_info.node}")
    print(f"{Colors.BLUE}Release: {os_info.release}")
    print(f"{Colors.BLUE}Version: {os_info.version}")
    #print(f"{Colors.BLUE}Machine: {os_info.machine}")
    print(f"{Colors.BLUE}Processor: {os_info.processor}{Colors.DEFAULT}")
    print()

def cpuInfo():
    print(f"{Colors.BLUE}Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"{Colors.BLUE}Total cores: {psutil.cpu_count(logical=True)}")
    cpuFreq = psutil.cpu_freq()
    print(f"{Colors.BLUE}Max Frequency: {cpuFreq.max:.2f}Mhz")
    #print(f"{Colors.BLUE}Min Frequency: {cpuFreq.min:.2f}Mhz")
    print(f"{Colors.BLUE}Current Frequency: {cpuFreq.current:.2f}Mhz")
    print(f"{Colors.BLUE}CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"{Colors.BLUE}Core {i}: {percentage}%")
    print(f"{Colors.BLUE}Total CPU Usage: {psutil.cpu_percent()}%{Colors.DEFAULT}")
    print()

def memInfo():
    svmem = psutil.virtual_memory()
    print(f"{Colors.BLUE}Total Memory: {sizeAdj(svmem.total)}")
    print(f"{Colors.BLUE}Available Memory: {sizeAdj(svmem.available)}")
    print(f"{Colors.BLUE}Used Memory: {sizeAdj(svmem.used)}")
    print(f"{Colors.BLUE}Percentage: {svmem.percent}%{Colors.DEFAULT}")
    print()

def diskInfo():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"{Colors.BLUE}Device: {partition.device}")
        print(f"{Colors.BLUE}Mountpoint: {partition.mountpoint}")
        print(f"{Colors.BLUE}File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"{Colors.BLUE}Total Size: {sizeAdj(partition_usage.total)}")
        print(f"{Colors.BLUE}Used: {sizeAdj(partition_usage.used)}")
        print(f"{Colors.BLUE}Free: {sizeAdj(partition_usage.free)}")
        print(f"{Colors.BLUE}Percentage: {partition_usage.percent}%{Colors.DEFAULT}")
    print()

def netInfo():
    interface_addr = psutil.net_if_addrs()
    for if_name, if_addr in interface_addr.items():
        for addr in if_addr:
            print(f"{Colors.BLUE}Interface: {if_name}")
            if str(addr.family) == "AddressFamily.AF_INET":
                print(f"{Colors.BLUE}IP Address: {addr.address}")
                print(f"{Colors.BLUE}Netmask: {addr.netmask}")
                print(f"{Colors.BLUE}Broadcast: {addr.broadcast}")
            elif str(addr.family) == "AddressFamily.AF_PACKET":
                print(f"{Colors.BLUE}MAC Address: {addr.address}")
                print(f"{Colors.BLUE}Netmask: {addr.netmask}")
                print(f"{Colors.BLUE}Broadcast: {addr.broadcast}")
    print()

#Leitourgikes sinartiseis
def sizeAdj(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return(
                f"{bytes:.2f}{unit}{suffix}"
            )
        bytes /= factor

def menu():
    print(Colors.RED + """Select one of the following options:
0. Exit
1. Display all available info
2. Display OS info
3. Display CPU info
4. Display Memory info
5. Display Disk info
6. Display Network info
""" + Colors.DEFAULT)

def main():
    banner()
    seperator()
    while True:
        menu()
        epilogi = input(Colors.PINK + "Enter your choice: " + Colors.DEFAULT)
        seperator()
        if epilogi == "0":
            print(Colors.PINK + "Quiting OSherlock..." + Colors.DEFAULT)
            break
        elif epilogi == "1":
            osInfo()
            seperator()
            cpuInfo()
            seperator()
            memInfo()
            seperator()
            diskInfo()
            seperator()
            netInfo()
        elif epilogi == "2":
            osInfo()
        elif epilogi == "3":
            cpuInfo()
        elif epilogi == "4":
            memInfo()
        elif epilogi == "5":
            diskInfo()
        elif epilogi == "6":
            netInfo()
        else:
            print(Colors.PINK + "Invalid choice, choose another option." + Colors.DEFAULT)
        seperator()

if __name__ == "__main__":
    main()