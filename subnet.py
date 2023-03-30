import re


def validate_ip_address(ip_address):
    # Validate the IP address using regular expressions
    ip_regex = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(ip_regex, ip_address):
        raise ValueError('Invalid IP address format')

    octets = ip_address.split('.')
    for octet in octets:
        if int(octet) > 255:
            raise ValueError('Invalid IP address')


def validate_subnet_mask(subnet_mask):
    # Validate the subnet mask is a valid integer
    if not subnet_mask.isdigit() or int(subnet_mask) < 0 or int(subnet_mask) > 32:
        raise ValueError('Invalid subnet mask')


def validate_partitioning_type(partitioning_type):
    # Validate the partitioning type is either "hosts" or "subnets"
    if partitioning_type.lower() not in ['hosts', 'subnets']:
        raise ValueError('Invalid partitioning type')


def validate_number(number):
    # Validate the number is a valid integer
    if not number.isdigit() or int(number) <= 0:
        raise ValueError('Invalid number')


def infer_subnet_mask(ip_address):
    # Infer the subnet mask based on the class of the IP address
    first_octet = int(ip_address.split('.')[0])
    if first_octet < 128:
        return 8
    elif first_octet < 192:
        return 16
    elif first_octet < 224:
        return 24
    else:
        raise ValueError('Invalid IP address')


def calculate_subnet(ip_address, subnet_mask, partitioning_type, number):
    # Calculate the subnet
    validate_ip_address(ip_address)

    if subnet_mask:
        validate_subnet_mask(subnet_mask)
    else:
        subnet_mask = infer_subnet_mask(ip_address)

    validate_partitioning_type(partitioning_type)
    validate_number(number)

    subnet_mask_binary = '1' * subnet_mask + '0' * (32 - subnet_mask)
    subnet_mask_decimal = [str(int(subnet_mask_binary[i:i + 8], 2)) for i in range(0, 32, 8)]
    subnet_mask_decimal = '.'.join(subnet_mask_decimal)

    cidr_notation = str(subnet_mask)

    if partitioning_type.lower() == 'hosts':
        # Calculate the number of subnets
        subnets = 2 ** (32 - subnet_mask)

        # Calculate the number of hosts per subnet
        hosts_per_subnet = 2 ** (32 - subnet_mask - number)

        return subnet_mask_decimal, cidr_notation, hosts_per_subnet, subnets

    elif partitioning_type.lower() == 'subnets':
        # Calculate the number of hosts
        hosts = 2 ** number

        # Calculate the number of subnets
        subnets = 2 ** (subnet_mask - number)

        return subnet_mask_decimal, cidr_notation, hosts, subnets


def calculate_network_address(ip_address, subnet_mask, subnet_number):
    # Calculate the network address
    validate_ip_address(ip_address)
    validate_subnet_mask(subnet_mask)
    validate_number(subnet_number)

    subnet_mask_binary = '1' * subnet_mask + '0' * (32 - subnet_mask)
    subnet_mask_decimal = [str(int(subnet_mask_binary[i:i + 8], 2)) for i in range(0, 32, 8)]

    ip_address_binary = ''.join([bin(int(octet))[2:].zfill(8)])