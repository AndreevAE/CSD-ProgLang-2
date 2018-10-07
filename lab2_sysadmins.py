"""
Необходимо написать скрипт, обрабатывающий лог файл Nginx и выводящий список IP
адресов, с которых производились запросы. Адреса из общей подсети \24 необходимо
группировать при выводе(напр. 10.40.0.4 и 10.40.0.231 относятся к одной подсети).

Базовый язык - Python 2.7 или Python 3.5. Требуется использовать библиотеку re
для RegEx.

Задание на языке python требуется сдать до 23:59 (UTC+7) 8 Ноября.
"""

import re

file_path = './access.log'

class IpList:
    def __init__(self):
        self.ip_list = []

    def sort(self):
        self.ip_list.sort()

    def add(self, ip_string):
        ip_address = IpAddress(ip_string)
        if ip_address in self.ip_list:
            #print("passed")
            pass
        else:
            self.ip_list.append(ip_address)

    def group_by_mask(self, mask):
        previous = IpAddress("0.0.0.0")
        for ip_address in self.ip_list:
            current = ip_address
            if current.mask(mask) == previous.mask(mask):
                pass
            else:
                net_address = IpAddress(str(current.mask(mask) >> 24) + "." + str(current.mask(mask) >> 16 & 255) + "." + str(current.mask(mask) >> 8 & 255) + "." + str(current.mask(mask) & 255))
                print()
                #print("{0}:".format(bin(current.mask(mask))))
                net_address.print(":")
            ip_address.print()
            previous = current

    def len(self):
        len(self.ip_list)

class IpAddress:
    def __init__(self, ip_string):
        ip_splitted = ip_string.split('.')
        self.byte1 = int(ip_splitted[0])
        self.byte2 = int(ip_splitted[1])
        self.byte3 = int(ip_splitted[2])
        self.byte4 = int(ip_splitted[3])

    def __lt__(self, other): # <
        if self.byte1 < other.byte1:
            return True
        elif self.byte1 == other.byte1:
            if self.byte2 < other.byte2:
                return True
            elif self.byte2 == other.byte2:
                if self.byte3 < other.byte3:
                    return True
                elif self.byte3 == other.byte3:
                    if self.byte4 < other.byte4:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, other): # <=
        if self.byte1 <= other.byte1:
            return True
        else:
            if self.byte2 <= other.byte2:
                return True
            else:
                if self.byte3 <= other.byte3:
                    return True
                else:
                    if self.byte4 <= other.byte4:
                        return True

    def __eq__(self, other): # ==
        return self.byte1 == other.byte1 and self.byte2 == other.byte2 and self.byte3 == other.byte3 and self.byte4 == other.byte4

    def __ne__(self, other): # !=
        return self.byte1 != other.byte1 or self.byte2 != other.byte2 or self.byte3 != other.byte3 or self.byte4 != other.byte4

    def __gt__(self,other): # >
        if self.byte1 > other.byte1:
            return True
        elif self.byte1 == other.byte1:
            if self.byte2 > other.byte2:
                return True
            elif self.byte2 == other.byte2:
                if self.byte3 > other.byte3:
                    return True
                elif self.byte3 == other.byte3:
                    if self.byte4 > other.byte4:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, other): # >=
        if self.byte1 >= other.byte1:
            return True
        else:
            if self.byte2 >= other.byte2:
                return True
            else:
                if self.byte3 >= other.byte3:
                    return True
                else:
                    if self.byte4 >= other.byte4:
                        return True
                    else:
                        return False

    def mask(self, mask):
        binary_address = self.byte1 << 24 | self.byte2 << 16 | self.byte3 << 8 | self.byte4
        net_mask = 4294967295 >> (32 - mask) << (32 - mask)
        net_address = binary_address & net_mask
        return net_address

    def print(self, string = ""):
        print("{0}.{1}.{2}.{3}{4}".format(self.byte1, self.byte2, self.byte3, self.byte4, string))

def main():
    ipList = IpList()

    with open(file_path, 'r') as file:
        for row in file:
            row
            result = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", row)
            result
            for one_element in result:
                ipList.add(one_element)

    ipList.sort()
    ipList.group_by_mask(24)

if __name__ == '__main__':
    main()
