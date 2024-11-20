# Class is a Blueprint for the system utilities that will be used in the program

import os

class Utils:

    def show_disk_space(self):
        print('Disk Space: ', os.system('df -h'))

    def show_ram(self):
        print('RAM: ', os.system('free -m'))

    def show_system_info(self):
        print('System Info: ', os.system('uname -a'))
        print('System Info: ', os.uname().sysname)

machine_a = Utils()
machine_a.show_disk_space()
machine_a.show_ram()
machine_a.show_system_info()
machine_b = Utils()