import os


d_ground = {}
d_predicted = {}
titles = []

#--- Get PREDICTED VALUE ---#
f = open('cluster', 'r')
count = 1
for line in f:
    titles_in_cluster = line.split('*')[:-1]
    for title in titles_in_cluster:
        d_predicted[title.strip()] = count
    count += 1

#--- Get GROUND VALUE ---#

#--- Change directory to Papers ---#
os.chdir(os.getcwd() + '/Papers')

#--- Read all files and add to data ---#
file_names = os.listdir(os.getcwd())

for file_name in file_names:
    ground_value = file_name.split()[0]

    if (file_name.endswith('.txt')):
        fin = open(file_name, 'r')
        for line in fin:
            #--- Trim blank lines ---#
            if (len(line) > 2):
                if (line.startswith('Title')):
                    title = line.split(':')[1].strip()
                    break      
        titles.append(title)                  
        fin.close()
        
        d_ground[title] = ground_value

no_of_papers = len(titles)
#print len(d_ground.keys()), d_ground
#print len(d_predicted.keys()), d_predicted


Css = 0.0
Csd = 0.0
Cds = 0.0
Cdd = 0.0
for i in range(no_of_papers):
    for j in range(i+1, no_of_papers):
        if (d_ground[titles[i]] == d_ground[titles[j]] and d_predicted[titles[i]] == d_predicted[titles[j]]):
            Css += 1
        elif (d_ground[titles[i]] == d_ground[titles[j]] and d_predicted[titles[i]] != d_predicted[titles[j]]):
            Csd += 1
        elif (d_ground[titles[i]] != d_ground[titles[j]] and d_predicted[titles[i]] == d_predicted[titles[j]]):
            Cds += 1
        else:
            Cdd += 1
#print Css, Csd, Cds, Cdd
        
random_index = (Css + Cdd) / (Css + Csd + Cds + Cdd)
precision = Css / (Css + Csd)
recall = Css / (Css + Cds)  
f_measure = (2 * precision * recall) / (precision + recall)  

print "Random Index :", random_index
print "Precision :", precision
print "Recall :", recall
print "F-Measure :", f_measure
