import csv

prime_count = 0
region_count = 0
zone_count = 0
file_path = 'YOUR LOG FILE PATH GOES HERE'

with open(file_path,'r') as logs:
    for line in logs:
        if "ZONE" in line:
            zone_count += 1
        elif "REGION" in line:
            region_count += 1
        elif "PRIME" in line:
            prime_count += 1
        else:
            continue
    print("PRIME BLOCKS MINED: " + str(prime_count))
    print("REGION BLOCKS MINED: " + str(region_count))
    print("ZONE BLOCKS MINED: " + str(zone_count))
    total_blocks = prime_count + region_count + zone_count
    print("TOTAL BLOCKS MINED: " + str(total_blocks))
