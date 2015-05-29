#uses genemap 
import csv

class MonogenicDiseaseManager:
    def __init__(self, fileName, path):
        self.fileName = fileName
        self.path = path
        self.diseases2genes = {} # Maps from diseaseName::String to {geneName::string}


    def load_data_from_csv(self):
        read_file = open(self.fileName)
        reader = csv.reader(read_file, delimiter='|')
        fieldnames = reader.next()
        for row in reader:
            if not row:
                continue
            diseaseName = row[13]
            reported_genes = row[5]
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
                    write_file.write('%s' %x)
                    write_file.write("\n")
        write_file.close()

def main():
    fileName = "/Users/mtchavez/plab/yeast_replaceable_genes/OMIM/genemap.txt" #location of GWAS catalog in computer
    path = "/Users/mtchavez/plab/yeast_replaceable_genes/monogenicDiseasesOMIMg.txt" #location where you want to store file
    mdm = MonogenicDiseaseManager(fileName, path)
    mdm.load_data_from_csv()
    mdm.write_data_to_csv()

main()
