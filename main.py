import re
import math


def ip_input_and_validation(ip):
    #ip address validation
    ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    match = re.match(ValidIpAddressRegex, ip)
    if bool(match):
        print("Valid IP given")
        return bool(match)
    else:
        print("Invalid IP given, retry")
        return bool(match)

def CIDR_input(ip):
    #getting cidr from user or use defualt cidr according to classes
    cidr = input("enter CIDR: ")

    octets = ip.split('.')

    first_octet = octets[0]
    second_octet = octets[1]
    third_octet = octets[2]
    forth_octet = octets[3]

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
    #change cidr to subnet mask
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

def get_hosts_H(amount, cidr):
    #number of hosts as power of 2 minus 2
    bitsForHosts = (math.ceil(math.log(amount + 2, 2)))
    return ((2 **bitsForHosts) - 2)


def get_subnets_H(amount, cidr):
    bitsForHosts = (math.ceil(math.log(amount + 2, 2)))
    bitsForSubnets= 32 - cidr - bitsForHosts
    return (2 ** bitsForSubnets)


def get_subnets_S(amount, cidr):
    #number of subnets: for example if chosing 5 subnets there will be 8 subnets (power of 2)
    bitsForSubnets = ((math.ceil(math.log(amount, 2))))
    y = 2 ** bitsForSubnets
    return y

def get_hosts_S(amount, cidr):
    #number of hosts for calculated number of subnets
    bitsForSubnets = ((math.ceil(math.log(amount, 2))))
    bitsForHosts = 32 - cidr - bitsForSubnets
    w = (2 ** (bitsForHosts)-2)
    return w

#def to_binary(str):
#    binary_ip = '.'.join([bin(int(x) + 256)[3:] for x in str.split('.')])  # ip to binary ip
#    return binary_ip

#def class_c():
#    network=octets[0],octets[1],octets[2],

def new_cidr(choise, amount, cidr):
    if choise == 'H':
        bitsForHosts = (math.ceil(math.log(amount + 2, 2)))
        bitsForSubnets = 32 - cidr - bitsForHosts
    if choise == 'S':
        bitsForSubnets = ((math.ceil(math.log(amount, 2))))
    new_cidr=cidr+bitsForSubnets
    return new_cidr


def get_network(choise, amount, cidr):
    #change cidr to subnet mask
    if choise == 'H':
        bitsForHosts = (math.ceil(math.log(amount + 2, 2)))
        bitsForSubnets = 32 - cidr - bitsForHosts
    if choise == 'S':
        bitsForSubnets = ((math.ceil(math.log(amount, 2))))
    new_cidr=cidr+bitsForSubnets
    if new_cidr >= 25:
        pow = 32 - new_cidr
        network = f"octets[0].octets[1].octets[2].{256 - (2 ** pow)}"
    elif new_cidr >= 17:
        pow = 24 - new_cidr
        network = f"octets[0].octets[1].{256 - (2 ** pow)}.0"
    elif new_cidr >= 9:
        pow = 16 - new_cidr
        network = f"octets[0].{256 - (2 ** pow)}.0.0"
    else:
        pow = 8 - new_cidr
        network = f"{256 - (2 ** pow)}.0.0.0"
    return network

def main():
    ip=input("enter ip address ")
    #print (ip)
    octets = ip.split('.')

    first_octet = octets[0]
    second_octet = octets[1]
    third_octet = octets[2]
    forth_octet = octets[3]

    if ip_input_and_validation(ip):
        cidr = CIDR_input(ip)
        #print("Subnet mask (binary format):", to_binary(get_subnet_mask(cidr)))
        print("Output #1 - Subnet mask (decimal format):", get_subnet_mask(cidr))
        print("Output #2 - cidr: /",cidr)

        choise = input("Will the partitioning be according to number of hosts or number of subnets? (H/S)")
        if choise == 'H':
            amount = int(input("How many hosts? "))
            if amount>2**(32-cidr)-2:
                print("too many hosts for given subnet")
            else:
                print("Output #3 - number of hosts", get_hosts_H(amount, cidr))
                print("Output #4 - number of subnets", get_subnets_H(amount, cidr))
        elif choise == 'S':
            amount = int(input("How many subnets? "))
            if cidr == 32:
                print("Can't split the network")
            elif amount > get_hosts_S(amount, cidr):
                print("subnet can't be splited to ",amount, "networks")
            else:
                print("Output #3 - number of hosts", get_hosts_S(amount, cidr))
                print("Output #4 - number of subnets", get_subnets_S(amount, cidr))
        else:
                print("wrong value was entered")
    print("network",get_network(choise, amount, cidr)))


if __name__ == "__main__":
    main()
