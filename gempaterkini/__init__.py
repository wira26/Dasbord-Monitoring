def ekstraksi_data():
    """

tanggal: 21 juli 2021
waktu: 16:57:48 WIB
magnetudo: 4.3
kedalaman: 10 km
lokasi: 2.09 LS - 120.51 BT
pusat gempa: Pusat gempa berada di darat 62 Km Timur Laut Luwu Utara
dirasakan: Dirasakan (Skala MMI): II - III Malili
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '21 juli 2021'
    hasil['waktu'] = '16:57:48 WIB'
    hasil['magnetudo'] = 4.3
    hasil['lokasi'] = {'ls':2.09, 'bt': 120.51}
    hasil['pusat gempa'] = 'Pusat gempa berada di darat 62 Km Timur Laut Luwu Utara'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Malili'
    print(hasil)
    return hasil
    pass


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"magnetudo{result['magnetudo']}")
    print(f"lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"pusat gempa{result['pusat gempa']}")
    print(f"dirasakan{result['dirasakan']}")
    print(result)


#if __name__=__'main'__ :
 #   print('ini adalah pacage gempa terkini')