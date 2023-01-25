import pandas as pd
import numpy as np


class IPReader:
    ip_list = []

    def __init__(self, filepath):
        excel_file = pd.ExcelFile(filepath)
        ip_df = pd.read_excel(excel_file, 'IP')
        ip_dict = ip_df.to_dict()
        dict_list = ip_dict["IP Address"].items()
        for ip in dict_list:
            self.ip_list.append(ip[1])

    def get_ip_list(self):
        return self.ip_list


class IPDBReader:

    # pre-set values to identify largest value in IPTO data set (among 20,000 values)
    ipto_cap_list = [774078463, 1495473151, 1733165055,
                     2181169151, 2891120639, 3116709887,
                     3231235583, 3271926271, 3354690815,
                     3432631807, 3758096383]

    def __init__(self, filepath):
        self.excel_file = pd.ExcelFile(filepath)

    # returns index of ipto cap
    def get_db_range(self, ip_num):
        for x in self.ipto_cap_list:
            if ip_num <= x:
                return self.ipto_cap_list.index(x)

    # returns list of 20,000 rows
    def get_ip_dataset(self, index):

        if index != 0:

            skiprows = 19999
            nrows = 20000

            for x in range(10):

                if x+1 == index:
                    ip_db_df = pd.read_excel(self.excel_file, 'IP_DB', skiprows=skiprows, nrows=nrows, usecols='A:G')
                    ip_db_list = ip_db_df.values.tolist()
                    return ip_db_list
                else:
                    skiprows += nrows

        # if index is 0
        else:
            ip_db_df = pd.read_excel(self.excel_file, 'IP_DB', skiprows=0, nrows=19999, usecols='A:G')
            ip_db_list = ip_db_df.values.tolist()
            return ip_db_list


class IPWriter:
    def __init__(self, filepath):
        self.filepath = filepath

    def to_excel(self, ip_list, geolocation_list):
        columns = ['IP Address', 'Country']
        df = pd.DataFrame(list(zip(ip_list, geolocation_list)), columns=columns)
        with pd.ExcelWriter(self.filepath,
                            engine='openpyxl', mode='a') as writer:
            df.to_excel(writer, sheet_name='Countries', index=False)
