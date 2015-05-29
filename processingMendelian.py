import csv

class ReplaceableGenesManager:
    def __init__(self, fileName):
        self.fileName = fileName
        self.yeastGenes = {} # Maps from id::int to {geneName::string}
        self.allYeastGenes = [] #list containing all yeast replaceable genes
        self.mendelianGenes = []

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
            read_file = open(path, 'rU')
            reader = csv.reader(read_file, delimiter='\t')
            for row in reader:
                self.mendelianGenes.append(row)
            print self.mendelianGenes
            read_file.close()

    def write_data_to_csv(self, path):
        write_file = open(path, 'w')
        write_file.write("Gene Symbol(s), ID")
        write_file.write("\n")
        for item in self.mendelianGenes:
            for gene in item:
                if gene in self.allYeastGenes:
                    print gene
                    for ID, value in self.yeastGenes.items():
                        if gene in value:
                            print ID, value
                            for x in value:
                                write_file.write('%s ' %x)
                            write_file.write(",")
                            write_file.write('%s' %ID)
                            write_file.write("\n")
        write_file.close()

def main():
    fileName = "/Users/mtchavez/plab/yeast_replaceable_genes/replaceable_genes.csv"
    path1r = "/Users/mtchavez/plab/yeast_replaceable_genes/mendelian_genes.txt"
    pathw = "/Users/mtchavez/plab/yeast_replaceable_genes/genescomparedtoyeastmendelian.txt"
    rgm = ReplaceableGenesManager(fileName)
    rgm.load_data_from_csv()
    rgm.process_data([path1r])
    rgm.write_data_to_csv(pathw)

main()
