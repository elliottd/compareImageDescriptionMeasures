args <- commandArgs(trailingOnly = TRUE)

automatic<-read.csv(args[1], sep="\t")
only_judgements<-read.csv(args[2])

score_columns<-colnames(automatic)[3:length(colnames(automatic))]
judgements<-merge(only_judgements,automatic,by="id")

firstjudge <- subset(x = judgements, select=c(score_columns, "j1", "imageid", "textid", "refid"))
names(firstjudge)[names(firstjudge) == "j1"] <- "human"
secondjudge <- subset(x = judgements, select=c(score_columns, "j2", "imageid", "textid", "refid"))
names(secondjudge)[names(secondjudge) == "j2"] <- "human"
thirdjudge <- subset(x = judgements, select=c(score_columns, "j3", "imageid", "textid", "refid"))
names(thirdjudge)[names(thirdjudge) == "j3"] <- "human"

alljudges<-rbind(firstjudge,secondjudge)
alljudges<-rbind(alljudges,thirdjudge)
correlations = NULL

# Calculate the correlations and print them to STDOUT
for (i in score_columns) {
  correlations[[i]] = cor.test(alljudges$human, alljudges[[i]], use="complete.obs", method="spearman")
  print(paste(i," ρ=", correlations[[i]]$estimate))
}

# Break the human judgements into subsets
human4 = subset(alljudges, human>3)
human3 = subset(alljudges, human>2 & human<4)
human2 = subset(alljudges, human>1 & human<3)
human1 = subset(alljudges, human>0 & human<2)

# Plot the score densities for post-hoc visualisation
for (i in score_columns) {

  cairo_pdf(paste(i,".pdf", sep=""))
  plot(density(human1[[i]], kernel="epanechnikov"), col="black", main='', xlab='', ylab='', lwd=2)
  lines(density(human2[[i]], kernel="epanechnikov"), col="aquamarine4", lwd=2)
  lines(density(human3[[i]], kernel="epanechnikov"), col="blue", lwd=2)
  lines(density(human4[[i]], kernel="epanechnikov"), col="red", lwd=2)
  title(xlab='Score', ylab='Density estimate', main=paste(i, ' probability density estimation'))
  legend("topright",legend=rev(c("No relation", "Some aspects", "Minor mistakes", "Perfect")),col=rev(c("black","aquamarine4","blue","red")), lwd=2, title="Human Judgement")
  dev.off()
}
