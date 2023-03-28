import re


def ip_input_and_validation(ip):
    ValidIpAddressRegex = "^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$";
    match = re.match(ValidIpAddressRegex, ip)
    if bool(match):
        print("Valid IP given")
    else:
        print("Invalid IP given, retry")


def CIDR_input():
    cidr = int(input("Give CIDR: "))
    while cidr < 0 or cidr > 32:
        cidr = int(input("Give a valid CIDR: "))


# 3. Will the partitioning be according to number of hosts or number of subnets
# • Verify the input


# 4. Number of hosts/subnets (according to previous question)
# • Verify that an integer legit valid number was inpu


def main():
    ip = input("Give IP: ")
    if ip_input_and_validation(ip):
        CIDR_input()


if __name__ == "__main__":
    main()
