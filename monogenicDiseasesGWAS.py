#program to find monogenic diseases on the GWAS catalog

import csv

class MonogenicDiseaseManager:
    def __init__(self, fileName, path):
        self.fileName = fileName
        self.path = path
        self.diseases2genes = {} # Maps from diseaseName::String to {geneName::string}


    def load_data_from_csv(self):
        read_file = open(self.fileName)
        reader = csv.reader(read_file, delimiter='\t')
        fieldnames = reader.next()
        for row in reader:
            if not row:
                continue
            diseaseName = row[7]
            reported_genes = row[13]
            if reported_genes == 'NR' or reported_genes == 'Intergenic':
                reported_genes == row[14]
            if reported_genes == ' - ' or reported_genes == 'Pending':
                continue
            reported_genes = set(reported_genes.split(','))
            group = self.diseases2genes.setdefault(diseaseName, set())
            group.update(reported_genes)
        read_file.close()


    def write_data_to_csv(self):
        write_file = open(self.path, 'w')
        for key in self.diseases2genes:
            if sum(1 for x in self.diseases2genes[key]) == 1:
                #print key, self.diseases2genes[key]
                write_file.write('%s, ' %key)
                for x in self.diseases2genes[key]:
                    if x == 'NR' or x == 'Intergenic':
                        continue
                    write_file.write('%s' %x)
                    write_file.write("\n")
        write_file.close()

def main():
    fileName = "/Users/mtchavez/Documents/ALS/Diseasome/GWAS.txt" #location of GWAS catalog in computer
    path = "/users/mtchavez/Documents/monogenicDiseases.txt" #location where you want to store file
    mdm = MonogenicDiseaseManager(fileName, path)
    mdm.load_data_from_csv()
    mdm.write_data_to_csv()

main()
