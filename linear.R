

production<-c(200,100,6800,400,100,700,200,11100,356800,300,2400,1700,2500,20,200,6100,1500,700,700,300,11400,328000,200,2300,3900,1900,6000)


area<-c(400,100,2900,2700,500,2000,200,14100,137500,700,3500,2500,5900,100,100,2100,2800,500,2000,400,14100,137500,700,3500,3300,4800,2100)

df<-data.frame(production,area)


model<-lm(production~area,data=df)
print(model)
m<-2.508
b<--4580.902
h <-"enter area :"
h                                           
h<-readLines("stdin",n=1)      
#print(class(h))
h<-as.integer(h)
                                  
                                                                          
y<-(m*h)+b
y
w<-"production is:"
print(y)

library(tcltk)
x11()
plot(df$area,df$productiom,xlab="xaxis",ylab="yaxis")


abline(model)
Sys.sleep(200)

