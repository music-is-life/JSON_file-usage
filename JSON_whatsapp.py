### reading and writing strings from JSON file, creating Metadata for whatsapp messages
#'C:\Users\Orang\Desktop\assigment_4\�צאט WhatsApp עם יום הולדת בנות לנויה.txt'
import json

def read_file (): 
    file = input('please enter file Location: ')
    fhand = open(file, "r", encoding = 'utf8')
    return fhand


#fixing messeges lines 

def creating_full_message ():
    fhand = read_file()
    fhand = fhand.readlines()
    for i in range (0,len(fhand)):
        if fhand[i][0].isalpha():
            fhand[i-1] = fhand[i-1] + fhand[i]
            
            
    for line in fhand:
        if line[0].isalpha():
            fhand.remove(line)
    
    
    #creating messeges info into a dictionary:
        
    id_dis = dict()
    messeges = dict()
    counter = 0
    
    for line in fhand:
        if line.find(': ') == -1:
            continue
        id_dis[line[line.index(' - '):line.index(': ')]] = id_dis.get(line[line.index(' - '):line.index(': ')],counter)
        messeges[line[line.index(' - '):line.index(': ')]] = {'datetime': line[:line.find(' - ')],'id': id_dis[line[line.index(' - '):line.index(': ')]] , 'text': line[line.find(': '):line.find('\n')]}
        counter += 1
    
    
    #creating metada for the messeges group:
        
    metada_dic = dict()    
    counter = 0
    
    for line in fhand:
        if line.find(': ') == -1:
            if counter == 1:
                metada_dic = {'chat_name':line[line.find(' "'):line.find('" ')] , 'creation_date':line[:line.find(' - ')], 'num_of_participants': len(id_dis), 'creator': line[line.find('+'):line.find('+') + 16] }
    
        counter += 1
    
    #lets create dic for metada and messeges:
    gene_dic = dict()
    gene_dic = {'messages' : list(messeges.values()), 'metadata':metada_dic}
    
    chat_name = metada_dic['chat_name']
    chat_name = chat_name.strip(' "')
    chat_name = chat_name + '.txt'
    
    #now we will convert it to json file:

    with open(chat_name, 'w', encoding='utf8') as outfile:
        json.dump(gene_dic, outfile, ensure_ascii = False, indent=6)


creating_full_message()
