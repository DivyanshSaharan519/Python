#Python Mixed Problem-Solving — 50 Unique Questions
#1. Digit and Character Analyzer
string=input("Enter paragraph:")
ucount=lcount=dcount=scount=sccount=0
for i in string:
    if chr(65)<=i<=chr(90):
        ucount+=1
    elif chr(97)<=i<=chr(122):
        lcount+=1    
    elif chr(48)<=i<=chr(57):
        dcount+=1    
    elif i==chr(32):
        scount+=1    
    else:
        sccount+=1 
if ucount>lcount and ucount>dcount and ucount>scount and ucount>sccount:
    print("In string upper case characters is highest:",ucount)
elif lcount>ucount and lcount>dcount and lcount>scount and lcount>sccount:
    print("In string lower case characters is highest:",lcount)    
elif dcount>ucount and dcount>lcount and dcount>scount and dcount>sccount:
    print("In string digits is highest:",dcount)    
elif scount>ucount and scount>lcount and scount>dcount and scount>sccount:
    print("In string spaces is highest:",scount)     
elif sccount>ucount and sccount>lcount and sccount>dcount and sccount>scount:
    print("In string special characters is highest:",sccount)     
else:
    print("Tie")



#2. Student Performance Analyzer
fcount=pcount=gcount=ecount=0
for i in range(10):
    marks=int(input("Enter marks:"))
    if 100>=marks>=75:
        ecount+=1
        print("Excellent")
    elif 74>=marks>=50:
        gcount+=1
        print("Good")    
    elif 49>=marks>=35:
        pcount+=1
        print("Pass")
    elif 0<=marks<35:
        fcount+=1
        print("Fail")        
    else:
        print("please enter marks in range 0 to 100")
print("In Excellent category number of students is:",ecount)
print("In Good category number of students is:",gcount)
print("In Pass category number of students is:",pcount)
print("In Fail category number of students is:",fcount)



#3. Word Score Calculator
string=input("Enter paragraph:")
letters=string.split()
highest_score=0
highest_score_word=""
for letter in letters:
    score=0
    for i in letter:
        if i in "AEIOUaeiou":
            score+=2
        elif i not in "AEIOUaeiou":
            score+=1    
        elif chr(48)<=i<=chr(57):
            scoret+=3  
        else:
            score+=4
    if highest_score<score:
        highest_score=score
        highest_score_word=letter
print("Highest scoring word is:",highest_score_word)          
print("Score:", highest_score)



#4. Password Batch Validator
for i in range(5):
    ucount=lcount=dcount=sccount=islen=False
    passwords=input("Enter password:")
    for char in passwords:
        if len(passwords)>=8:
            islen=True
        if chr(65)<=char<=chr(90):
            ucount=True
        elif chr(97)<=char<=chr(122):
            lcount=True
        elif chr(48)<=char<=chr(57):
            dcount=True
        else:
            sccount=True  
    score=int(islen)+int(ucount)+int(lcount)+int(dcount)+int(sccount)      
    if score>=5:
        print("Password is Strong") 
    elif score>=3:
        print("Password is Medium")    
    else:
        print("Password is Weak")      



#5. Sentence Word Analyzer
Sentence=input("Enter Sentence:")
words=Sentence.split()
short_count=medium_count=long_count=0
for word in words:
    word_char_count=0
    print("The length of",word,"is",len(word))
    for i in word:
        word_char_count+=1
    if word_char_count<=3:
        short_count+=1
        print("word is short")
    elif word_char_count<6:
        medium_count+=1
        print("medium")    
    else:
        long_count+=1
        print("long")    
print("The short word in sentance is:",short_count)        
print("The medium word in sentance is:",medium_count)        
print("The long word in sentance is:",long_count)        



#6. Number-String Conversion Challenge
for i in range(5):
    num=int(input("Enter number:"))
    snum=str(num)
    ecount=ocount=0
    for digit in snum:
        if int(digit)%2==0:
            ecount+=1
        else:
            ocount+=1        
    if ecount>ocount:
        print("in string number even number is more") 
    elif ecount<ocount:
        print("in string number odd number is more")   
    else:
        print("in string number even number or odd number are equal")



#7. Repeated Character Report
string=input("Enter paragraph:")
for char in string:
    count=0
    for i in string:
        if char==i:
            count+=1
    if count>1:        
        if count==2:
            print(char, ":", count, "Duplicate")
        elif 3<=count<=4:
            print(char, ":", count, "Repeated")   
        else:
            print(char, ":", count, "Highly Repeated")     



#8. Shopping Cart Analyzer
total_price=0
budget_count=regular_count=premium_count=luxury_count=0
for i in range(8):
    price=float(input("Enter price:"))
    total_price+=price
    if price<500:
        budget_count+=1
        print("Budget")
    elif price<2000:
        regular_count+=1
        print("Regular")    
    elif price<5000:
        premium_count+=1
        print("Premium")   
    else:
        luxury_count+=1
        print("Luxury")    
avg=total_price/8
print("The total price is:",total_price)    
print("no of items in Budget price is:",budget_count)             
print("no of items in regular price is:",regular_count)             
print("no of items in premium price is:",premium_count)             
print("no of items in luxury price is:",luxury_count)    
print("Average product price is:",avg)         