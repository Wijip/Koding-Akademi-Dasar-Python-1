import ipaddress

def calculate_subnet_info(ip_str, subnet_mask_str):
    ip = ipaddress.IPv4Address(ip_str)
    subnet = ipaddress.IPv4Network(f'{ip_str}/{subnet_mask_str}', strict=False)

    usable_ips = list(subnet.hosts())
    network_ip = subnet.network_address
    broadcast_ip = subnet.broadcast_address

    return usable_ips, subnet_mask_str, network_ip, broadcast_ip

def main():
    ip = input("Masukkan alamat IP: ")
    subnet_mask = input("Masukkan subnet mask: ")

    usable_ips, subnet_mask_str, network_ip, broadcast_ip = calculate_subnet_info(ip, subnet_mask)

    print(f"\nAlamat IP yang dapat digunakan dalam subnet {subnet_mask_str} adalah:")
    for usable_ip in usable_ips:
        print(usable_ip)

    print(f"\nSubnet mask: {subnet_mask_str}")
    print(f"IP network: {network_ip}")
    print(f"IP broadcast: {broadcast_ip}")

    host_count = len(usable_ips)
    print(f"\nJumlah host yang dapat mendapatkan IP: {host_count}")

if __name__ == "__main__":
    main()
