library(org.Hs.eg.db)
library(KEGGgraph)
library(Rgraphviz)
library(graph)

var1 <- system.file("extdata/hsa05014.xml",package="KEGGgraph")
var2 <- parseKGML2Graph(var1, genesOnly=TRUE)
var3 <- c("hsa:842",edges(var2)$'hsa:842')
var4 <- subKEGGgraph(var3,var2)
var5 <- sapply(edges(var4), length) > 0
var6 <- sapply(inEdges(var4), length) > 0
var7 <- var5|var6
var8 <- translateKEGGID2GeneID(names(var7))
var9 <- sapply(mget(var8,org.Hs.egSYMBOL),"[[",1)
var10 <- var4
nodes(var10) <- var9

var12 <- system.file("extdata/hsa05010.xml",package="KEGGgraph")
var13 <- parseKGML2Graph(var12, genesOnly=TRUE)
var14 <- c("hsa:842",edges(var13)$'hsa:842')
var15 <- subKEGGgraph(var14,var13)
var16 <- sapply(edges(var15), length) > 0
var17 <- sapply(inEdges(var15), length) > 0
var18 <- var16|var17
var19 <- translateKEGGID2GeneID(names(var18))
var20 <- sapply(mget(var19,org.Hs.egSYMBOL),"[[",1)
var21 <- var15
nodes(var21) <- var20

var22 <- as.data.frame(get.edgelist(var10))
var23 <- as.data.frame(get.edgelist(var21))
var24 <- intersect(var22, var23) 
plot.data.frame(var24)
