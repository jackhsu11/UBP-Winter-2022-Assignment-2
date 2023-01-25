from FileRW import *
from App import *


def main():

    # initialize file reader via filepath
    ip_reader = IPReader("___.xlsx")
    ip_db_reader = IPDBReader("___.xlsx")

    # get list of ip addresses
    ip_list = ip_reader.get_ip_list()

    # set list (type: int): numeric values of ip addresses
    numeric_ip_list = []
    for ip in ip_list:
        x = NumericIP(ip)
        numeric_ip = x.get_numeric_ip()
        numeric_ip_list.append(numeric_ip)

    # set list (type: list): ip location datasets
    ip_dataset_list = []
    for ip_num in numeric_ip_list:
        # get database range from IP DB
        db_range = ip_db_reader.get_db_range(ip_num)
        ip_dataset = ip_db_reader.get_ip_dataset(db_range)
        ip_dataset_list.append(ip_dataset)

    # set list (type: str): geolocation of ip addresses
    # ip_geolocation_list = []
    # input numeric ip for each ip_dataset_list:
    geolocation_list = []
    for n in range(len(numeric_ip_list)):
        app = FindGeolocation(ip_dataset_list[n])
        geolocation_list.append(app.get_ip_geolocation(numeric_ip_list[n], 0))

    # create new sheet in original file
    writer = IPWriter("___.xlsx")
    writer.to_excel(ip_list, geolocation_list)


main()
