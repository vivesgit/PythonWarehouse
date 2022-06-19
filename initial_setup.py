
import os
import fileinput

class Stock:
    def __init__(self):
        '''
        This function will create two warehouses databses with a predefined default stock.
        '''
        Warehouse1File = open('Warehouse1.txt', 'a')
        Warehouse1File.write('Shoes' + '\n')
        Warehouse1File.write('10' + '\n')
        Warehouse1File.write('Jackets' + '\n')
        Warehouse1File.write('7' + '\n')
        Warehouse1File.write('Trousers' + '\n')
        Warehouse1File.write('23' + '\n')

        Warehouse2File = open('Warehouse2.txt', 'a')
        Warehouse2File.write('Shoes' + '\n')
        Warehouse2File.write('3' + '\n')
        Warehouse2File.write('Jackets' + '\n')
        Warehouse2File.write('10' + '\n')
        Warehouse2File.write('Trousers' + '\n')
        Warehouse2File.write('23' + '\n')

Stock()