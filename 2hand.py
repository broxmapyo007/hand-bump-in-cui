import time,sys,os

#n1=n='12345678012569'
def hand(n,n1):
	for i in range(25):
		print(' ',end='')
		for j in range(39):
			if( ( i==1 and j==7)  or                               (i==2 and (j==4 or j==6)) or (i==3 and (j==3 or j==5)) or  (i==5 and (j in [1,13,16,27,28]))  or (i==13 and (j in [1,2,3,4,5,12,13,14,15,20])) or (i==14 and (j in [31,34]))  or (i==15 and (j in [30,33])) or (i==16 and (j==31)) or ( i==12 and (j in [15,18,38])  ) ):
				print('*',end=' ')
				#print(i,end='')
			
			if (i==8 and (j in [11-len(n)])):
				for j in range(len(n)):
					if n[j]!='':
						print(n[j],end='')
					else:
						continue
				continue
			if (i==8 and (j in [18])):
				for j in range(len(n1)):
					if n1[j]!='':
						print(n1[j],end='')
					else:
						continue
				continue
			if ( ((i in [4])and ( j in [2,6,7,8,9,17,18,19,20,21,22])) or ( i==12 and (j in [39]))or ((i in [7,9,11] ) and (j in [16,18]))):
					print('*',end=' ')
			else:
				print(' ',end='')
		print('')
		time.sleep(.1)
while True:
	n=input('enter name=')
	n1=input('enter name=')
	os.system('clear')
	hand(n,n1)
	