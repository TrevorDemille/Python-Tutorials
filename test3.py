quote1 = "It all started when"
quote2 = "my mother took my bike away, '\n"
multiquote = '''so I murdered my guinea pig and stuck him in the microwave'''
print("%s %s %s" % (quote1,quote2,multiquote))
#
list1 = ['Bananas', 'Bullet-trains', 'Buzzwords', 'Brainwaves']
list2 = ['Albacore', 'Antithesis', 'Alturism', 'Aristocrats']
list3 = ['Catharsis', 'Chonostasis', 'Criminals', 'Children']
list4 = ['Demonic', 'Disrepaired', 'Desensitized', 'Delightful']
list5 = ['Elicit', 'Enormous', 'Elementary', 'Eloquent']
list6 = ['Fanatic', 'Frantic', 'Feverish', 'Frozen']
#
listChoice1 = int(input("Choose noun list (0-2):"))
word1 = int(input("Choose word in list (0-3)"))
listChoice2 = int(input("Choose adjective list (3-5):"))
word2 = int(input("Choose word in list (0-3)"))

#
if(listChoice1 != 1 and listChoice1 != 2 and listChoice1 != 3 and listChoice2 != 4 and listChoice2 != 5 and listChoice2 != 6):
	print("Wrong list value choice")
elif(word1 != 0 and word1 != 1 and word1 != 2 and word1 != 3 and word2 != 0 and word2 != 1 and word2 != 2 and word2 != 3):
	print("Wrong word value choice")
else:
	finList = [list1,list2,list3,list4,list5,list6]
	printlist1 = finList[listChoice1]
	printlist2 = finList[listChoice2]
	print('My favorite Breakfast is', printlist2[word2], printlist1[word1]) 