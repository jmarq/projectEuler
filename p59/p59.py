#cipher stored in text file with comma separated integers.

fi=open('cipher1.txt').read().split(',');
cipher=[int(i) for i in fi];

#split list into 3, choosing every third int

cipher1=[];
cipher2=[];
cipher3=[];
i=0;
while(len(cipher)>=1):
	if(i%3==0):
		cipher1.append(cipher.pop(0))
	elif(i%3==1):
		cipher2.append(cipher.pop(0))
	elif(i%3==2):
		cipher3.append(cipher.pop(0))
	i+=1;
print cipher1;

#count each code number in each list
#list 1
counts1={};#dictionary for storing pairs of character codes and frequency counts
for i in range(0,len(cipher1)):
	if (cipher1[i] in counts1.keys()):
		counts1[cipher1[i]]+=1;
	else:
		counts1[cipher1[i]]=1;
freqs1=sorted(counts1.items(),key=lambda x:x[1],reverse=True);#sort items in dictionary by their frequency
#list2
counts2={};
for i in range(0,len(cipher2)):
	if (cipher2[i] in counts2.keys()):
		counts2[cipher2[i]]+=1;
	else:
		counts2[cipher2[i]]=1;
freqs2=sorted(counts2.items(),key=lambda x:x[1],reverse=True);
#list3
counts3={};
for i in range(0,len(cipher3)):
	if (cipher3[i] in counts3.keys()):
		counts3[cipher3[i]]+=1;
	else:
		counts3[cipher3[i]]=1;
freqs3=sorted(counts3.items(),key=lambda x:x[1],reverse=True);

#print freqs1
#print freqs2
#print freqs3
keynum1='';
keynum2='';
keynum3='';
for i in range(0,200):# a space(' ') is chr(34).  spaces should be the most common in my opinion 
	if(32 ^ i)==freqs1[0][0]:#check if a space XOR'd with i is the most frequent thing in freqs1
		keynum1=i;
	if(32 ^ i)==freqs2[0][0]:
		keynum2=i;
	if(32^i)==freqs3[0][0]:
		keynum3=i;
		

#print keynum1; print keynum2; print keynum3;
plain1=[chr(i ^ keynum1) for i in cipher1];
plain2=[chr(i ^ keynum2) for i in cipher2];
plain3=[chr(i ^ keynum3) for i in cipher3];

#print plain1;
#print plain2;
#print plain3;

plainFull="";
while(len(plain1)>0 or len(plain2)>0 or len(plain3)>0):
	if(len(plain1)>0):
		plainFull+=plain1.pop(0);
	if(len(plain2)>0):
		plainFull+=plain2.pop(0);
	if(len(plain3)>0):
		plainFull+=plain3.pop(0);
print plainFull;
sum=0;
for i in plainFull:
	sum+=ord(i);
print sum;


