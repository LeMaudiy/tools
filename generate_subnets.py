def generate_subnets(base_network="10", subnet_length=16):
    for i in range(256):
        print(f"{base_network}.{i}.0.0/{subnet_length}")

if __name__ == "__main__":
    generate_subnets()
