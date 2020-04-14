import numpy as np
class Perceptron(object):

    def __init__(ident, urutinput, nilaitresh=100, ratapembelajaran=0.01):
        ident.nilaitresh = nilaitresh
        ident.ratapembelajaran = ratapembelajaran
        ident.berat = np.zeros(urutinput + 1)

    def prediksi(ident, masukan):
        jumlah = np.dot(masukan, ident.berat[1:]) + ident.berat[0]
        if jumlah > 0:
            aktivasi = 1
        else :
            aktivasi = 0
        return aktivasi

    def train(ident, datalatih, lebel):
        for _ in range(ident.nilaitresh):
            for input, lebel in zip (datalatih, output):
                x = ident.prediksi(input)
                ident.berat[1:] += ident.ratapembelajaran * (lebel - x) * input
                ident.berat[0] += ident.ratapembelajaran * (lebel - x)

datalatih = []
datalatih.append(np.array([-1, -1]))
datalatih.append(np.array([-1, 1]))
datalatih.append(np.array([1, -1]))
datalatih.append(np.array([1, 1]))

output = np.array([-1, 1, 1, 1])

a = Perceptron(2)
a.train(datalatih, output)

masukan = np.array([1, 1])
a.prediksi(masukan)
    # -> 1

input = np.array([0, 1])
a.prediksi(input)
 # ->0

#hasil= def prediksi(ident, masukan)
