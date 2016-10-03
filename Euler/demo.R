# Basic Script
bevs <- data.frame(cbind(name = c("Bill", "Llib"), 
                         drink = c("coffee", "tea", "cocoa", "water"), cost = seq(1:8)))

library(plyr)
# How many times does each name occur. 
count(bevs, "name")

# How many times did each person drink each drink. 
count(bevs, c("name", "drink"))

# How much spent on each drink. 
aggregate(cost ~ name + drink, data = bevs, sum)

# What was the mean price. 
aggregate(cost ~ name + drink, data = bevs, mean)
