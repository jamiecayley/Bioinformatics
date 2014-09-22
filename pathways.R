library(org.Hs.eg.db)
library(KEGGgraph)
library(Rgraphviz)

var1 <- system.file("extdata/hsa00020.xml",package="KEGGgraph")
var2 <- parseKGML2Graph(var1, genesOnly=TRUE)
var3 <- c("hsa:4967",edges(var2)$'hsa:4967')
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

var12 <- system.file("extdata/hsa00020.xml",package="KEGGgraph")
var13 <- parseKGML2Graph(var12, genesOnly=TRUE)
var14 <- c("hsa:4967",edges(var13)$'hsa:4967')
var15 <- subKEGGgraph(var14,var13)
var16 <- sapply(edges(var15), length) > 0
var17 <- sapply(inEdges(var15), length) > 0
var18 <- var16|var17
var19 <- translateKEGGID2GeneID(names(var18))
var20 <- sapply(mget(var19,org.Hs.egSYMBOL),"[[",1)
var21 <- var15
nodes(var21) <- var20
#var22 <- list();
#var22$fillcolor <- makeAttr(var15,"col=635")
plot(var21) #, nodeAttrs=var22)

var23 <- intersect(var20, var9)
#var24 <- list();
#var24$fillcolor <- makeAttr(var23, "col=635")
plot(var23) #, nodeAttrs=var24)
