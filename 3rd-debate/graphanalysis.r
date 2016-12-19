#load all necessary libraries
library(plotly)

#create data frames of tone analysis
clinton <- read.csv("clintontone.csv", header = FALSE)
trump <- read.csv("trumptone.csv", header = FALSE)

#give the data frames headers
colnames(clinton) <- c('tone','clinton' )
colnames(trump) <- c('tone', 'trump')

#merge the data
ctone <- merge(clinton, trump, by='tone')


#plot the data
plot_ly(ctone, x = ~tone, y = ~clinton, type = 'bar', name = 'Clinton', marker=list(color='rbg(0,0,255)')) %>%
    add_trace(y = ~trump, name = 'Trump', marker=list(color='rbg(255,0,0)')) %>%
    layout(title = 'Candidate Tone in Final Debate',
        xaxis = list(title = ''),   
        yaxis = list(title = '% in Speech'), 
        legend  = list(x = 1, y =1),
        barmode = 'group', bargap = .15)



