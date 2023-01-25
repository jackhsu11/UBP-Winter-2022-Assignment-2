# split IP address by '.'
# Calculation: (256^3*IP1) + (256^2*IP2) + (256^1*IP3) + (256^0*IP4)

class NumericIP:

    ip_split = []

    def __init__(self, ip):
        self.split_ip(ip)

    def split_ip(self, ip):
        self.ip_split = ip.split('.')

    def get_numeric_ip(self):
        numeric_ip = (256**3 * int(self.ip_split[0])) + (256**2 * int(self.ip_split[1])) + (256 * int(self.ip_split[2])) + int(self.ip_split[3])
        return numeric_ip


class FindGeolocation:

    def __init__(self, ip_dataset):
        self.ip_dataset = ip_dataset
        self.length = 1000

    def iterate_section(self, ip_num, n, length):
        for x in range(n, length):
            if self.ip_dataset[x][0] <= ip_num <= self.ip_dataset[x][1]:
                return self.ip_dataset[x][6]

    # first loop
    # increments of 1,000
    # n = 0, self.length = 1000
    def get_ip_geolocation(self, ip_num, n):
        if (len(self.ip_dataset) - self.length) < 1000:
            clength = len(self.ip_dataset) - self.length
            return self.iterate_section(ip_num, n, self.length + clength)
        else:
            if ip_num > self.ip_dataset[self.length - 1][1]:
                self.length += 1000
                return self.get_ip_geolocation(ip_num, n + 1000)
            else:
                return self.iterate_section(ip_num, n, self.length)

