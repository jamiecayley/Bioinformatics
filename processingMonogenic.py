import csv

class ReplaceableGenesManager:
    def __init__(self, fileName):
        self.fileName = fileName
        self.yeastGenes = {} # Maps from id::int to {geneName::string}
        self.genes2diseases = {} # Maps from geneName::String to {diseaseName::string}
        self.allYeastGenes = [] #list containing all yeast replaceable genes

    def load_data_from_csv(self):
        read_file = open(self.fileName)
        reader = csv.reader(read_file, delimiter=',')
        fieldnames = reader.next()
        for row in reader:
            if not row:
                continue
            ID = row[5]
            genes = row[0]
            genes = set(genes.split('; '))
            group = self.yeastGenes.setdefault(ID, set())
            group.update(genes)
            for gene in genes:
                self.allYeastGenes.append(gene)
        read_file.close()


    def process_data(self, paths):
        for path in paths:
            read_file = open(path)
            fieldnames = read_file.readline()
            for row in read_file:
                if not row:
                    continue
                data = row.rsplit(",", 1)
                diseaseName = data[0]
                reported_gene = data[1]
                group = self.genes2diseases.setdefault(reported_gene, set())
                group.update(diseaseName)
            read_file.close()

    def write_data_to_csv(self, path):
        write_file = open(path, 'w')
        write_file.write("Disease, Gene, ID")
        write_file.write("\n")
        for key in self.genes2diseases:
            if key in self.allYeastGenes:
                print key
                write_file.write('%s, ' %self.genes2diseases[key])
                for ID, genes in self.yeastGenes.items():
                    if key in genes:
                        write_file.write('%s,' %ID)
                        write_file.write('%s' %key)
                        write_file.write("\n")
        write_file.close()

def main():
    fileName = "/Users/mtchavez/plab/yeast_replaceable_genes/replaceable_genes.csv"
    path1r = "/Users/mtchavez/plab/yeast_replaceable_genes/monogenicDiseasesGWAS.txt"
    path2r = "/Users/mtchavez/plab/yeast_replaceable_genes/monogenicDiseasesOMIM.txt"
    path3r = "/Users/mtchavez/plab/yeast_replaceable_genes/monogenicDiseasesOMIMg.txt"
    #path4r = "/Users/mtchavez/plab/yeast_replaceable_genes/monogenicDiseasesKEGG.txt"
    pathw = "/Users/mtchavez/plab/yeast_replaceable_genes/genescomparedtoyeast.txt"
    rgm = ReplaceableGenesManager(fileName)
    rgm.load_data_from_csv()
    rgm.process_data([path1r, path2r, path3r])
    rgm.write_data_to_csv(pathw)

main()
