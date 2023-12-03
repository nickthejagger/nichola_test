import sys
import ipaddress

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must insert the ip number")
    raise SystemExit(2)

def validate_ip(ip_string):
   try:
       is_ip_valid = ipaddress.ip_address(ip_string)
       print("The IP address "+ ip_string +" is valid.")
   except ValueError:
       print("The IP address "+ ip_string +" is not valid")

validate_ip(sys.argv[1])