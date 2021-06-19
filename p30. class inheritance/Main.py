class Ojek():
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_driver(self):
        print('nama:', self.nama, '\nmotor',
              self.transmisi, '\ndaerah', self.daerah)


# Inheritance
class Gojek(Ojek):

    # Overide
    def cek_id_driver(self):
        print('cek aplikasi gojek')


ojek1 = Ojek('mario', 'manual', 'bandung selatan')
ojek2 = Gojek('jackson', 'automatic', 'tasikmalaya')

ojek1.cek_id_driver()
ojek2.cek_id_driver()

# Di dalam programming jangan lakukan DRY (Dont Repeat Yourself)
