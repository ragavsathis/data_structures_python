def validate_ip_addr(ip_addr):
    print("the Validation fucntion")
    if len(ip_addr.split('.')) > 4:
        print("Ipv4 addr is not in the valid format")
    if all([True if int(x) in range(0,256) else False for x in ip_addr.split('.')]):
        print "Ipv4 address is in the valid format "
    else:
        print "Ipv4 address is not valid as it's not in the range"

if __name__ == "__main__":
    N = int(input())
    ip_addr = [str(input()) for i in range(N)]
    map(lambda x:validate_ip_addr(x), ip_addr)
       