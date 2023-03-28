import re
import math


def ip_input_and_validation(ip):
    ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    match = re.match(ValidIpAddressRegex, ip)
    if bool(match):
        print("Valid IP given")
        return bool(match)
    else:
        print("Invalid IP given, retry")
        return bool(match)

def CIDR_input():
    cidr = input("Give CIDR: ")
    ip = "192.168.0.1"
    octets = ip.split('.')

    first_octet = octets[0]
    second_octet = octets[1]
    third_octet = octets[2]
    forth_octet = octets[3]

    #print(first_octet)
    if cidr == '':
        if 0 < int(first_octet) < 128:
            cidr = 8
            return cidr
        elif 128 <= int(first_octet) < 191:
            cidr = 16
            return cidr
        elif 192 <= int(first_octet) < 224:
            cidr = 24
            return cidr
        else:
            return False

    elif int(cidr) > 0 and int(cidr) <= 32:
        return int(cidr)
    else:
        return False


def get_subnet_mask(cidr):
    if cidr >= 25:
        pow = 32 - cidr
        subnet_mask = f"255.255.255.{256 - (2 ** pow)}"
    elif cidr >= 17:
        pow = 24 - cidr
        subnet_mask = f"255.255.{256 - (2 ** pow)}.0"
    elif cidr >= 9:
        pow = 16 - cidr
        subnet_mask = f"255.{256 - (2 ** pow)}.0.0"
    else:
        pow = 8 - cidr
        subnet_mask = f"{256 - (2 ** pow)}.0.0.0"
    return subnet_mask


def get_default_CIDR(ip):
    split_ip = ip.split('.')
    print(split_ip[0])
    return 0


def get_host_amount(amount):
    return ((2 ** (math.ceil(math.log(amount + 2, 2)))) - 2)


def get_nub_of_subnets(amount, cidr):
    x = ((math.ceil(math.log(amount + 2, 2))))
    y = 2 ** ((32 - x) - cidr )
    return y

def get_subnet_amount(amount, cidr):
    z = (int(math.log(amount, 2)))
    return (2 ** (32-cidr-z)-2)



def to_binary(str):
    binary_ip = '.'.join([bin(int(x) + 256)[3:] for x in str.split('.')])  # ip to binary ip
    return binary_ip


def main():
    # ip = input("Give IP: ")
    ip = "127.0.0.1"
    octets = ip.split('.')

    first_octet = octets[0]
    second_octet = octets[1]
    third_octet = octets[2]
    forth_octet = octets[3]


    if ip_input_and_validation(ip):
        cidr = CIDR_input()

        print(get_subnet_mask(cidr))
        print(to_binary(get_subnet_mask(cidr)))
        choise = input("Will the partitioning be according to number of hosts or number of subnets? (H/S)")
        amount = int(input("How many? "))
        if choise == 'H':
            if amount>2**(32-cidr):
                print("too many hosts for given subnet")
                print(cidr)
            else:
                print("number of hosts", get_host_amount(amount))
                print("number of subnets", get_nub_of_subnets(amount, cidr))
        elif choise == 'S':
            if amount > 1 and cidr == 32:
                print("too many subnets required")
            else:
                print("number of hosts", get_subnet_amount(amount, cidr))
                print("number of subnets", amount)
        # 2^(choise +2 => log(2))


if __name__ == "__main__":
    main()
