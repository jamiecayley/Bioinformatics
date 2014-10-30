library(org.Hs.eg.db)
library(KEGGgraph)
library(Rgraphviz)

var1 <- system.file("extdata/hsa00020.xml",package="KEGGgraph")
var2 <- parseKGML2Graph(var1, genesOnly=TRUE)
var3 <- c("hsa:4967",edges(var2)$'hsa:55753')
var4 <- subKEGGgraph(var3,var2)
var5 <- sapply(edges(var4), length) > 0
var6 <- sapply(inEdges(var4), length) > 0
var7 <- var5|var6
var8 <- translateKEGGID2GeneID(names(var7))
var9 <- sapply(mget(var8,org.Hs.egSYMBOL),"[[",1)
var10 <- var4
nodes(var10) <- var9
#var11 <- list();
#var11$fillcolor <- makeAttr(var4,"col=635")
plot(var10) #, nodeAttrs=var11)
retrieveKGML(pathwayid='05014', organism='hsa', destfile='hsa05014')
var12 <- system.file("extdata/hsa00020.xml",package="KEGGgraph")
var13 <- parseKGML2DataFrame(var12, reactions=FALSE)
var14 <- system.file("extdata/hsa00020.xml",package="KEGGgraph")
var15 <- parseKGML2DataFrame(var14, reactions=FALSE)
var16 <- intersect(var13, var15)
