library(org.Hs.eg.db)
library(KEGGgraph)
library(Rgraphviz)
library(graph)
 
process.pathway <- function( filename ) {
	var1 <- filename
 
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
 
	return(var10)
}
 
trace(process.pathway, exit = function().var1.env <<- parent.frame())
var1 <- system.file("extdata/hsa05014.xml",package="KEGGgraph")
var10 <- process.pathway(var1)
print( as.list( .var1.env ) )
 
trace(process.pathway, exit = function().var12.env <<- parent.frame())
var12 <- system.file("extdata/hsa05010.xml",package="KEGGgraph")
var21 <- process.pathway( var12 )
print( as.list( .var12.env ) )
 
library(igraph) 
var10.ig <- igraph.from.graphNEL( var10 )
var21.ig <- igraph.from.graphNEL( var10 )
par(mfrow=c(2,2))
for(g in list(var10, var10.ig, var21, var21.ig) ) {
	plot( g )
}
var24 <- graph.intersection(var24var10.ig, var21.ig)
print( V(var24) )
detach('package:igraph', unload=TRUE) 
