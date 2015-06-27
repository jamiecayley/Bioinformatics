import xlsxwriter
import csv
import numpy

humanSequence = "MAEEQGRERDSVPKPSVLFLHPDLGVGGAERLVLDAALALQARGCSVKIWTAHYDPGHCFAESR--ELPVRCAGDWLPRGLGWGGRGAAVCAYVRMVFLALYVLFLA--DEEFDVVVCDQVSACIPVFRLARRRKKILFYCHFPDLLLTKRDSFLKRLYRAPIDWIEEYTTGMADCILVNSQFTAAVFKETFKSLSHIDPDVLYPSLNVTSFDSVVP--EKLDDLVPKGKK-------FLLLSINRYERKKNLTLALEALVQLRGRLTSQDWERVHLIVAGGYDERVLENVEHYQELKKMVQQSDL----------------------GQYVTFLRSFSDKQKISLLHSCTCVLYTPSNEHFGIVPLEAMYMQCPVIAVNSGGPLESID--------HSVTGFLCEPDPVHFSEAIEKFIREPS-LKATMGLAGRARVKEKFSPEAFTEQLYRYVTKLLV--------------------------------------------------------------------"
mouseSequence =  "MAENLYRARSRVYSPSVLFLHPDMGIGGAERLVLDAALALQEYGCDVKIWTAHYDPNHCFIETR--ELSVQCAGDWLPRSLGWGGRGAAICSYVRMVFLALYVLFLS--GEEFDVVVCDQVSACIPVFKLARRRKRVLFYCHFPDLLLTQRNSALKKFYRAPIDWIEEYTTGMADRILVNSQYTASVFKETFKTLSHRNPDVLYPSLNIGSFDLAIP--EKIDDLVPKGKQ-------FLFLSINRYERKKNLPLALRSLVQLRNRLPSQEWDKVHLFMAGGYDDRIPENVEHYKELKKMVQESDL----------------------ERHVTFLRSFSDRQKISLLHGCLCVLYTPSNEHFGIVPLEAMYMQCPVIAVNNGGPLESIV--------HKVTGFLCEPDPVHFSEAMEKFIHKPS-LKATMGLAGKARVAEKFSADAFADQLYQYVTKLV---------------------------------------------------------------------"
zebrafishSequence = "MVR-------------VVFLHPDLGIGGAERLVVDAAVALRSRGCSVQIWTAHYDPQHCFSETLSPDLPVVCVGDWLPTSV--FGYFHALCAYLRMIYLTIYLVLFS--GEEFDVVFCDQVSACIPFLRLARQRKKVLFYCHFPDQLLTQRRSALKRLYRGPIDWFEELTTGMADRILVNSQFTAKVFKQTFPKLSEIHTDVLYPSLNSSAFDDEV---EGLGGLLPEGRS-------FIYLSINRYERKKNLPLALQALANLKDRLSVGEWERVHLVMAGGYDERVVENVEHYEELRSLVTSLGL----------------------EDHVTFLRSFSDKQKLSLLHNSTCVLYTPSNEHFGIVPIESMYLRCPVIAVNSGGPLESVA--------HEETGFLCEPTPERFSEAMQNFVSDPK-LKQRMGQAGRERVQQRFSMQAFTEQLYSHIASLTQ--------------------------------------------------------------------"
drosophilaSequence = "MVR-------------VLFLHPDLGIGGAERLVVDAALALKERGHQVSFLTNHHDSTHCFKETADGTFPVHVVGDWLPRGL--FGRFYAICAYLRMLYAAIYASFFMPQREQVDVVVCDLISVCIPVLRFAPHRPKVLFYCHFPDQLLSSREGLLKRLYRLPINWLEEHTIGLADKVLVNSKFTLRVFQDTFRRLSTV-PDVLYPSLHTQYFDQMQKKLEQRSALLDEPVHPRVPLNAFIYLDINRYERKKNHALALHSLRLLGDMLPATDFKRCRLIIAGGYDTRCMENVEHFAELEHLTEELKL----------------------QDHVVLLRSPTDEEKCRLLFAAHCLLYTPENEHFGIVPLEGMYCSKPVVALNSGGPTETVV--------STSTGFLCEKTEKSFGGAMLQLFRDEQ-LRVKMGDQGHKRVQQKFSFQAFADRLNGIIRDLVPISRESSAKKNK---------------------------------------------------------"
celegansSequence = "MVR-------------VTILHPDLGIGGAERLIVDAAVGLQDRGHSVRIFTNQYSRSHCFQETL--DLDICTVVPWIPRSI--FGKGHALCAYLKMIIAALYIVIYH---KDTDVILSDSVSASQFVLRHFS-KAKLVFYCHFPDRLLTKRDGNLKAFYRNIIDWIEEYTTGLADVICVNSNFTKNVVRETFKSLASQELTVLYPSLNTEFFDSIEAS-DDFGEEIPRGTK-------YVFTSLNRFERKKNIVLALDAFEKLKSNLPADEFSQCHLVIAGGYDLKNPENIEHYDELVEHMKKLELP---------------------ADQIVFLHSPSDTQKVNLIRRSRAVLYTPDREHFGIVPVEAMYLGTPVIAVNTGGPCESVR--------NNETGFLVDQTAEAFAEKMIDLMKDEE-MYRRMSEEGPKWVQKVFAFEAFARKLDEIIQSTL---------------------------------------------------------------------"
yeastSequence = "MIEKDKR--------TIAFIHPDLGIGGAERLVVDAALGLQQQGHSVIIYTSHCDKSHCFEEVKNGQLKVEVYGDFLPTNF--LGRFFIVFATIRQLYLVIQLILQK-KVNAYQLIIIDQLSTCIPLLHIFS-SATLMFYCHFPDQLLAQRAGLLKKIYRLPFDLIEQFSVSAADTVVVNSNFTKNTFHQTFKYLSND-PDVIYPCVDLSTIEIEDIDKKFFKTVFNEGDR--------FYLSINRFEKKKDVALAIKAFALSEDQIN----DNVKLVICGGYDERVAENVEYLKELQSLADEYELSHTTIYYQEIKRVSDLESFKTNNSKIIFLTSISSSLKELLLERTEMLLYTPAYEHFGIVPLEAMKLGKPVLAVNNGGPLETIKSYVAGENESSATGWLKPAVPIQWATAIDESRKILQNGSVNFERNGPLRVKKYFSREAMTQSFEENVEKVIWKEKKYYPWEIFGISFSNFILHMAFIKILPNNPWPFLFMATFMVLYFKNYLWGIYWAFVFALSYPYEEI"
pathogenic_mutations = "V367A,V68G,K131N"
pathogenic_mutations = map(str, pathogenic_mutations.split(","))
benign_mutations = "G6A,S11P"
benign_mutations = map(str, benign_mutations.split(","))
gene = "ALG2"
fileName = "/Users/mtchavez/Documents/Plab/yeast_replaceable_genes/sequences/non_replaceable_mendelian/ALG2/ALG2mutationConservationData.xlsx"
jsdivergencePath = "/Users/mtchavez/Documents/Plab/yeast_replaceable_genes/sequences/non_replaceable_mendelian/ALG2/jsDivergenceALG2.csv"
sentropyPath = "/Users/mtchavez/Documents/Plab/yeast_replaceable_genes/sequences/non_replaceable_mendelian/ALG2/sEntropyALG2.csv"
sumofpairsPath = "/Users/mtchavez/Documents/Plab/yeast_replaceable_genes/sequences/non_replaceable_mendelian/ALG2/sumOfPairsALG2.csv"


polarAA = ["N", "Q", "S", "T", "K", "R", "H", "D", "E"]
nonPolarAA = ["A", "V", "L", "I", "P", "Y", "F", "M", "W", "C"]
hBondingAA = ["C", "W", "N", "Q", "S", "T", "Y", "K", "R", "H", "D", "E"]
sulfurContainingAA = ["C", "M"]
acidicAA = ["D", "E"]
basicAA = ["K", "R"]
ionizableAA = ["D", "E", "H", "C", "Y", "K", "R"]
aromaticAA = ["F", "W", "Y"]
aliphaticAA = ["G", "A", "V", "L", "I", "P"]
fullyConservedMutations = 0
fullyConserved = 0
fullyConservedMouse = 0
fullyConservedZebrafish = 0
fullyConservedDrosophila = 0
fullyConservedCelegans = 0
fullyConservedYeast = 0
jsDivergenceScores = []
pathogenicJS = []
benignJS = []
mutationsJS = []
sEntropyScores = []
pathogenicSE = []
benignSE = []
mutationsSE = []
sumOfPairsScores = []
pathogenicSOP = []
benignSOP = []
mutationsSOP = []

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

empty_positions = findOccurences(humanSequence, "-")

def clean_sequences(humanSequence, mouseSequence, zebrafishSequence, drosophilaSequence, celegansSequence, yeastSequence, empty_positions):
  i = 0
  for x in empty_positions:
    x = x-i
    humanSequence = humanSequence[:x] + humanSequence[(x+1):]
    mouseSequence = mouseSequence[:x] + mouseSequence[(x+1):]
    zebrafishSequence = zebrafishSequence[:x] + zebrafishSequence[(x+1):]
    drosophilaSequence = drosophilaSequence[:x] + drosophilaSequence[(x+1):]
    celegansSequence = celegansSequence[:x] + celegansSequence[(x+1):]
    yeastSequence = yeastSequence[:x] + yeastSequence[(x+1):]
    i += 1
  return humanSequence, mouseSequence, zebrafishSequence, drosophilaSequence, celegansSequence, yeastSequence

humanSequence, mouseSequence, zebrafishSequence, drosophilaSequence, celegansSequence, yeastSequence = clean_sequences(humanSequence, mouseSequence, zebrafishSequence, drosophilaSequence, celegansSequence, yeastSequence, empty_positions)

def process_jsdivergence(jsdivergencePath, jsDivergenceScores, empty_positions):
  read_file = open(jsdivergencePath, 'rU')
  reader = csv.reader(read_file, delimiter=',')
  for row in reader:
      if not row:
          continue
      score = row[1]
      jsDivergenceScores.append(score)
  read_file.close()
  i = 0
  for x in empty_positions:
      x = x-i
      jsDivergenceScores = jsDivergenceScores[:x] + jsDivergenceScores[(x+1):]
      i += 1
  return jsDivergenceScores

jsDivergenceScores = process_jsdivergence(jsdivergencePath, jsDivergenceScores, empty_positions)

def process_sentropy(sentropyPath, sEntropyScores, empty_positions):
  read_file = open(sentropyPath, 'rU')
  reader = csv.reader(read_file, delimiter=',')
  for row in reader:
      if not row:
          continue
      score = row[1]
      sEntropyScores.append(score)
  read_file.close()
  i = 0
  for x in empty_positions:
      x = x-i
      sEntropyScores = sEntropyScores[:x] + sEntropyScores[(x+1):]
      i += 1
  return sEntropyScores

sEntropyScores = process_sentropy(sentropyPath, sEntropyScores, empty_positions)

def process_sumofpairs(sumofpairsPath, sumOfPairsScores, empty_positions):
  read_file = open(sumofpairsPath, 'rU')
  reader = csv.reader(read_file, delimiter=',')
  for row in reader:
      if not row:
          continue
      score = row[1]
      sumOfPairsScores.append(score)
  read_file.close()
  i = 0
  for x in empty_positions:
      x = x-i
      sumOfPairsScores = sumOfPairsScores[:x] + sumOfPairsScores[(x+1):]
      i += 1
  return sumOfPairsScores

sumOfPairsScores = process_sumofpairs(sumofpairsPath, sumOfPairsScores, empty_positions)


def create_spreadsheet(humanSequence, mouseSequence, zebrafishSequence, drosophilaSequence, celegansSequence, yeastSequence, pathogenic_mutations, benign_mutations, gene, fileName, polarAA, nonPolarAA, hBondingAA, sulfurContainingAA, acidicAA, basicAA, ionizableAA, aromaticAA, aliphaticAA, fullyConservedMutations, fullyConserved, fullyConservedMouse, fullyConservedZebrafish, fullyConservedDrosophila, fullyConservedCelegans, fullyConservedYeast, jsDivergenceScores, pathogenicJS, benignJS, mutationsJS, sEntropyScores, pathogenicSE, benignSE, mutationsSE, sumOfPairsScores, pathogenicSOP, benignSOP, mutationsSOP):
   workbook = xlsxwriter.Workbook(fileName)
   mutationData = workbook.add_worksheet(gene + "mutationConservationData")
   jsDivergence = workbook.add_worksheet("JS Divergence")
   sEntropy = workbook.add_worksheet("Shannon Entropy")
   sumOfPairs = workbook.add_worksheet("Sum of Pairs")
   number = 1
   for x in jsDivergenceScores:
        jsDivergence.write(number-1, 0, number)
        jsDivergence.write(number-1, 1, x)
        number +=1
   number = 1
   for x in sEntropyScores:
        sEntropy.write(number-1, 0, number)
        sEntropy.write(number-1, 1, x)
        number +=1
   number = 1
   for x in sumOfPairsScores:
        sumOfPairs.write(number-1, 0, number)
        sumOfPairs.write(number-1, 1, x)
        number +=1
   mutationData.write(1, 1, "Mouse")
   mutationData.write(1, 2, "Zebrafish")
   mutationData.write(1, 3, "Drosophila")
   mutationData.write(1, 4, "C. Elegans")
   mutationData.write(1, 5, "Yeast")
   mutationData.write(1, 6, "JS Divergence")
   mutationData.write(1, 7, "S Entropy")
   mutationData.write(1, 8, "Sum of Pairs")
   mutationData.merge_range('K2:L2', 'Summary')
   mutationData.write(2, 10, "% fully conserved mice")
   mutationData.write(3, 10, "% fully conserved zebrafish")
   mutationData.write(4, 10, "% fully conserved drosophila")
   mutationData.write(5, 10, "% fully conserved c elegans")
   mutationData.write(6, 10, "% fully conserved yeast")
   mutationData.write(7, 10, "% fully conserved mutations")
   mutationData.write(8, 10, "# fully conserved mutations (fcm)")
   mutationData.write(9, 10, "# fully conserved amino acids (fca)")
   mutationData.write(10, 10, "fcm/faa (percentage)")
   mutationData.write(11, 10, "# pathogenic mutations analyzed")
   mutationData.write(12, 10, "# benign mutations analyzed")
   mutationData.write(13, 10, "# total mutations analyzed")
   mutationData.write(14, 10, "JS divergence average")
   mutationData.write(15, 10, "JS divergence average pathogenic")
   mutationData.write(16, 10, "JS divergence average benign")
   mutationData.write(17, 10, "Shannon entropy average")
   mutationData.write(18, 10, "Shannon entropy average pathogenic")
   mutationData.write(19, 10, "Shannon entropy average benign")
   mutationData.write(20, 10, "Sum of pairs average")
   mutationData.write(21, 10, "Sum of pairs average pathogenic")
   mutationData.write(22, 10, "Sum of pairs average benign")
   mutationData.merge_range('K25:L25', 'Standard deviation')
   mutationData.write(25, 10, "JS divergence SD")
   mutationData.write(26, 10, "JS divergence pathogenic SD")
   mutationData.write(27, 10, "JS divergence benign SD")
   mutationData.write(28, 10, "Shannon entropy SD")
   mutationData.write(29, 10, "Shannon entropy pathogenic SD")
   mutationData.write(30, 10, "Shannon entropy benign SD")
   mutationData.write(31, 10, "Sum of pairs SD")
   mutationData.write(32, 10, "Sum of pairs pathogenic SD")
   mutationData.write(33, 10, "Sum of pairs benign SD")
   mutationData.merge_range('K36:L36', 'p Values')
   mutationData.write(36, 10, "JS div. path. and JS div.")
   mutationData.write(37, 10, "JS div. path. and JS div. benign")
   mutationData.write(38, 10, "S. ent. path. and S. ent.")
   mutationData.write(39, 10, "S. ent. path. and S. ent. benign")
   mutationData.write(40, 10, "S. of pairs path. and S. of pairs")
   mutationData.write(41, 10, "S. of pairs path. and S. of pairs benign")
   redformat = workbook.add_format()
   redformat.set_bg_color('red')
   yellowformat = workbook.add_format()
   yellowformat.set_bg_color('yellow')
   greenformat = workbook.add_format()
   greenformat.set_bg_color('green')
   grayformat = workbook.add_format()
   grayformat.set_bg_color('gray')
   row = 2
   for mutation in benign_mutations:
       oAA = mutation[0]
       pos = int(mutation[1:-1])
       mAA = mouseSequence[pos-1]
       zAA = zebrafishSequence[pos-1]
       dAA = drosophilaSequence[pos-1]
       cAA = celegansSequence[pos-1]
       yAA = yeastSequence[pos-1]
       mutationData.write(row, 6, jsDivergenceScores[pos-1])
       mutationsJS.append(jsDivergenceScores[pos-1])
       mutationData.write(row, 7, sEntropyScores[pos-1])
       mutationsSE.append(sEntropyScores[pos-1])
       mutationData.write(row, 8, sumOfPairsScores[pos-1])
       mutationsSOP.append(sumOfPairsScores[pos-1])
       if oAA != humanSequence[pos-1]:
           mutationData.write(row, 0, mutation, redformat)
       else:
           mutationData.write(row, 0, mutation, greenformat)
           benignSOP.append(sumOfPairsScores[pos-1])
           benignSE.append(sEntropyScores[pos-1])
           benignJS.append(jsDivergenceScores[pos-1])
       if oAA == mAA:
           mutationData.write(row, 1, mAA, greenformat)
           fullyConservedMouse += 1
       elif (oAA and mAA in polarAA) or (oAA and mAA in nonPolarAA) or (oAA and mAA in hBondingAA) or (oAA and mAA in sulfurContainingAA) or (oAA and mAA in acidicAA) or (oAA and mAA in basicAA) or (oAA and mAA in ionizableAA) or (oAA and mAA in aromaticAA) or (oAA and mAA in aliphaticAA):
           mutationData.write(row, 1, mAA, yellowformat)
       elif mAA == '-':
           mutationData.write(row, 1, mAA)
       else:
           mutationData.write(row, 1, mAA, redformat)
       if oAA == zAA:
           mutationData.write(row, 2, zAA, greenformat)
           fullyConservedZebrafish += 1
       elif (oAA and zAA in polarAA) or (oAA and zAA in nonPolarAA) or (oAA and zAA in hBondingAA) or (oAA and zAA in sulfurContainingAA) or (oAA and zAA in acidicAA) or (oAA and zAA in basicAA) or (oAA and zAA in ionizableAA) or (oAA and zAA in aromaticAA) or (oAA and zAA in aliphaticAA):
           mutationData.write(row, 2, zAA, yellowformat)
       elif zAA == '-':
           mutationData.write(row, 2, zAA)
       else:
           mutationData.write(row, 2, zAA, redformat)
       if oAA == dAA:
           mutationData.write(row, 3, dAA, greenformat)
           fullyConservedDrosophila += 1
       elif (oAA and dAA in polarAA) or (oAA and dAA in nonPolarAA) or (oAA and dAA in hBondingAA) or (oAA and dAA in sulfurContainingAA) or (oAA and dAA in acidicAA) or (oAA and dAA in basicAA) or (oAA and dAA in ionizableAA) or (oAA and dAA in aromaticAA) or (oAA and dAA in aliphaticAA):
           mutationData.write(row, 3, dAA, yellowformat)
       elif dAA == '-':
           mutationData.write(row, 3, dAA)
       else:
           mutationData.write(row, 3, dAA, redformat)
       if oAA == cAA:
           mutationData.write(row, 4, cAA, greenformat)
           fullyConservedCelegans += 1
       elif (oAA and cAA in polarAA) or (oAA and cAA in nonPolarAA) or (oAA and cAA in hBondingAA) or (oAA and cAA in sulfurContainingAA) or (oAA and cAA in acidicAA) or (oAA and cAA in basicAA) or (oAA and cAA in ionizableAA) or (oAA and cAA in aromaticAA) or (oAA and cAA in aliphaticAA):
           mutationData.write(row, 4, cAA, yellowformat)
       elif cAA == '-':
           mutationData.write(row, 4, cAA)
       else:
           mutationData.write(row, 4, cAA, redformat)
       if oAA == yAA:
           mutationData.write(row, 5, yAA, greenformat)
           fullyConservedYeast += 1
       elif (oAA and yAA in polarAA) or (oAA and yAA in nonPolarAA) or (oAA and yAA in hBondingAA) or (oAA and yAA in sulfurContainingAA) or (oAA and yAA in acidicAA) or (oAA and yAA in basicAA) or (oAA and yAA in ionizableAA) or (oAA and yAA in aromaticAA) or (oAA and yAA in aliphaticAA):
           mutationData.write(row, 5, yAA, yellowformat)
       elif yAA == '-':
           mutationData.write(row, 5, yAA)
       else:
           mutationData.write(row, 5, yAA, redformat)
       if oAA == mAA == zAA == dAA == cAA == yAA:
           fullyConservedMutations += 1
       row += 1
   for mutation in pathogenic_mutations or mutation in benign_mutations:
       oAA = mutation[0]
       pos = int(mutation[1:-1])
       mAA = mouseSequence[pos-1]
       zAA = zebrafishSequence[pos-1]
       dAA = drosophilaSequence[pos-1]
       cAA = celegansSequence[pos-1]
       yAA = yeastSequence[pos-1]
       mutationData.write(row, 6, jsDivergenceScores[pos-1])
       mutationsJS.append(jsDivergenceScores[pos-1])
       mutationData.write(row, 7, sEntropyScores[pos-1])
       mutationsSE.append(sEntropyScores[pos-1])
       mutationData.write(row, 8, sumOfPairsScores[pos-1])
       mutationsSOP.append(sumOfPairsScores[pos-1])
       if oAA != humanSequence[pos-1]:
           mutationData.write(row, 0, mutation, redformat)
       else:
           mutationData.write(row, 0, mutation)
           pathogenicSOP.append(sumOfPairsScores[pos-1])
           pathogenicSE.append(sEntropyScores[pos-1])
           pathogenicJS.append(jsDivergenceScores[pos-1])
       if oAA == mAA:
           mutationData.write(row, 1, mAA, greenformat)
           fullyConservedMouse += 1
       elif (oAA and mAA in polarAA) or (oAA and mAA in nonPolarAA) or (oAA and mAA in hBondingAA) or (oAA and mAA in sulfurContainingAA) or (oAA and mAA in acidicAA) or (oAA and mAA in basicAA) or (oAA and mAA in ionizableAA) or (oAA and mAA in aromaticAA) or (oAA and mAA in aliphaticAA):
           mutationData.write(row, 1, mAA, yellowformat)
       elif mAA == '-':
           mutationData.write(row, 1, mAA)
       else:
           mutationData.write(row, 1, mAA, redformat)
       if oAA == zAA:
           mutationData.write(row, 2, zAA, greenformat)
           fullyConservedZebrafish += 1
       elif (oAA and zAA in polarAA) or (oAA and zAA in nonPolarAA) or (oAA and zAA in hBondingAA) or (oAA and zAA in sulfurContainingAA) or (oAA and zAA in acidicAA) or (oAA and zAA in basicAA) or (oAA and zAA in ionizableAA) or (oAA and zAA in aromaticAA) or (oAA and zAA in aliphaticAA):
           mutationData.write(row, 2, zAA, yellowformat)
       elif zAA == '-':
           mutationData.write(row, 2, zAA)
       else:
           mutationData.write(row, 2, zAA, redformat)
       if oAA == dAA:
           mutationData.write(row, 3, dAA, greenformat)
           fullyConservedDrosophila += 1
       elif (oAA and dAA in polarAA) or (oAA and dAA in nonPolarAA) or (oAA and dAA in hBondingAA) or (oAA and dAA in sulfurContainingAA) or (oAA and dAA in acidicAA) or (oAA and dAA in basicAA) or (oAA and dAA in ionizableAA) or (oAA and dAA in aromaticAA) or (oAA and dAA in aliphaticAA):
           mutationData.write(row, 3, dAA, yellowformat)
       elif dAA == '-':
           mutationData.write(row, 3, dAA)
       else:
           mutationData.write(row, 3, dAA, redformat)
       if oAA == cAA:
           mutationData.write(row, 4, cAA, greenformat)
           fullyConservedCelegans += 1
       elif (oAA and cAA in polarAA) or (oAA and cAA in nonPolarAA) or (oAA and cAA in hBondingAA) or (oAA and cAA in sulfurContainingAA) or (oAA and cAA in acidicAA) or (oAA and cAA in basicAA) or (oAA and cAA in ionizableAA) or (oAA and cAA in aromaticAA) or (oAA and cAA in aliphaticAA):
           mutationData.write(row, 4, cAA, yellowformat)
       elif cAA == '-':
           mutationData.write(row, 4, cAA)
       else:
           mutationData.write(row, 4, cAA, redformat)
       if oAA == yAA:
           mutationData.write(row, 5, yAA, greenformat)
           fullyConservedYeast += 1
       elif (oAA and yAA in polarAA) or (oAA and yAA in nonPolarAA) or (oAA and yAA in hBondingAA) or (oAA and yAA in sulfurContainingAA) or (oAA and yAA in acidicAA) or (oAA and yAA in basicAA) or (oAA and yAA in ionizableAA) or (oAA and yAA in aromaticAA) or (oAA and yAA in aliphaticAA):
           mutationData.write(row, 5, yAA, yellowformat)
       elif yAA == '-':
           mutationData.write(row, 5, yAA)
       else:
           mutationData.write(row, 5, yAA, redformat)
       if oAA == mAA == zAA == dAA == cAA == yAA:
           fullyConservedMutations += 1
       row += 1
   mutationData.write(row, 0, "Summary", grayformat)
   mutationData.write(row, 1, fullyConservedMouse, grayformat)
   mutationData.write(row, 2, fullyConservedZebrafish, grayformat)
   mutationData.write(row, 3, fullyConservedDrosophila, grayformat)
   mutationData.write(row, 4, fullyConservedCelegans, grayformat)
   mutationData.write(row, 5, fullyConservedYeast, grayformat)
   mutationsJS = map(float, mutationsJS)
   mutationsSE = map(float, mutationsSE)
   mutationsSOP = map(float, mutationsSOP)
   mutationData.write(row, 6, numpy.mean(mutationsJS), grayformat)
   mutationData.write(row, 7, numpy.mean(mutationsSE), grayformat)
   mutationData.write(row, 8, numpy.mean(mutationsSOP), grayformat)
   totalMutations = len(pathogenic_mutations) + len(benign_mutations)
   mutationData.write(2, 11, str((fullyConservedMouse/float(totalMutations))*100) + "%")
   mutationData.write(3, 11, str((fullyConservedZebrafish/float(totalMutations))*100) + "%")
   mutationData.write(4, 11, str((fullyConservedDrosophila/float(totalMutations))*100) +"%")
   mutationData.write(5, 11, str((fullyConservedCelegans/float(totalMutations))*100) + "%")
   mutationData.write(6, 11, str((fullyConservedYeast/float(totalMutations))*100) + "%")
   mutationData.write(7, 11, str((fullyConservedMutations/float(totalMutations))*100) + "%")
   mutationData.write(8, 11, fullyConservedMutations)
   sequence_length = len(humanSequence)
   pos = 0
   while pos < sequence_length:
       if humanSequence[pos] == mouseSequence[pos] == zebrafishSequence[pos] == drosophilaSequence[pos] == celegansSequence[pos] == yeastSequence[pos]:
           fullyConserved +=1
       pos += 1
   mutationData.write(9, 11, fullyConserved)
   if fullyConservedMutations > 0:
       mutationData.write(10, 11, str(fullyConservedMutations/float(fullyConserved)*100) +"%")
   else:
       mutationData.write(10, 11, "0%")
   mutationData.write(11, 11, len(pathogenic_mutations))
   mutationData.write(12, 11, len(benign_mutations))
   mutationData.write(13, 11, totalMutations)
   jsDivergenceScores = map(float, jsDivergenceScores)
   pathogenicJS = map(float, pathogenicJS)
   benignJS = map(float, benignJS)
   sEntropyScores = map(float, sEntropyScores)
   pathogenicSE = map(float, pathogenicSE)
   benignSE = map(float, benignSE)
   sumOfPairsScores = map(float, sumOfPairsScores)
   pathogenicSOP = map(float, pathogenicSOP)
   benignSOP = map(float, benignSOP)
   mutationData.write(14, 11, numpy.mean(jsDivergenceScores))
   mutationData.write(15, 11, numpy.mean(pathogenicJS))
   if len(benignJS) > 0:
       mutationData.write(16, 11, numpy.mean(benignJS))
   else:
       mutationData.write(16, 11, "-")
   mutationData.write(17, 11, numpy.mean(sEntropyScores))
   mutationData.write(18, 11, numpy.mean(pathogenicSE))
   if len(benignSE) > 0:
       mutationData.write(19, 11, numpy.mean(benignSE))
   else:
       mutationData.write(19, 11, "-")
   mutationData.write(20, 11, numpy.mean(sumOfPairsScores))
   mutationData.write(21, 11, numpy.mean(pathogenicSOP))
   if len(benignSOP) > 0:
       mutationData.write(22, 11, numpy.mean(benignSOP))
   else:
       mutationData.write(22, 11, "-")
   if len(jsDivergenceScores) > 1:
       mutationData.write(25, 11, numpy.std(jsDivergenceScores))
   elif len(jsDivergenceScores) == 1:
       mutationData.write(25, 11, 0)
   else:
       mutationData.write(25, 11, "-")
   if len(pathogenicJS) > 1:
       mutationData.write(26, 11, numpy.std(pathogenicJS))
   elif len(pathogenicJS) == 1:
       mutationData.write(26, 11, 0)
   else:
       mutationData.write(26, 11, "-")
   if len(benignJS) > 1:
       mutationData.write(27, 11, numpy.std(benignJS))
   elif len(benignJS) == 1:
       mutationData.write(27, 11, 0)
   else:
       mutationData.write(27, 11, "-")
   if len(sEntropyScores) > 1:
       mutationData.write(28, 11, numpy.std(sEntropyScores))
   elif len(sEntropyScores) == 1:
       mutationData.write(28, 11, 0)
   else:
       mutationData.write(28, 11, "-")
   if len(pathogenicSE) > 1:
       mutationData.write(29, 11, numpy.std(pathogenicSE))
   elif len(pathogenicSE) == 1:
       mutationData.write(29, 11, 0)
   else:
       mutationData.write(29, 11, "-")
   if len(benignSE) > 1:
       mutationData.write(30, 11, numpy.std(benignSE))
   elif len(benignSE) == 1:
       mutationData.write(30, 11, 0)
   else:
       mutationData.write(30, 11, "-")
   if len(sumOfPairsScores) > 1:
       mutationData.write(31, 11, numpy.std(sumOfPairsScores))
   elif len(sumOfPairsScores) == 1:
       mutationData.write(31, 11, 0)
   else:
       mutationData.write(31, 11, "-")
   if len(pathogenicSOP) > 1:
       mutationData.write(32, 11, numpy.std(pathogenicSOP))
   elif len(pathogenicSOP) == 1:
       mutationData.write(32, 11, 0)
   else:
       mutationData.write(32, 11, "-")
   if len(benignSOP) > 1:
       mutationData.write(33, 11, numpy.std(benignSOP))
   elif len(benignSOP) == 1:
       mutationData.write(33, 11, 0)
   else:
       mutationData.write(33, 11, "-")
   workbook.close()


create_spreadsheet(humanSequence, mouseSequence, zebrafishSequence, drosophilaSequence, celegansSequence, yeastSequence, pathogenic_mutations, benign_mutations, gene, fileName, polarAA, nonPolarAA, hBondingAA, sulfurContainingAA, acidicAA, basicAA, ionizableAA, aromaticAA, aliphaticAA, fullyConservedMutations, fullyConserved, fullyConservedMouse, fullyConservedZebrafish, fullyConservedDrosophila, fullyConservedCelegans, fullyConservedYeast, jsDivergenceScores, pathogenicJS, benignJS, mutationsJS, sEntropyScores, pathogenicSE, benignSE, mutationsSE, sumOfPairsScores, pathogenicSOP, benignSOP, mutationsSOP)
