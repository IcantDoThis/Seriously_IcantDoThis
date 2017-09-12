data <- read.csv(file="C:/Users/swaroop/Desktop/data_csv.csv", header=TRUE, sep=",")
attach(data)
data$Month <- format(as.Date(data$DateTime), "%m")    
plot(DateTime, Issue_Type)