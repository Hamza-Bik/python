import os


text = "this is not a reversed text"
# text = "said"

def reverse(x):
   output="" 
   for s in range(len(x)):
       output += x[len(x) - (s+1) : len(x) - s]
   return output

# print("the reversed text is: "+reverse(text))

# print('said'[len('said')-2:len('said')-1])

# no_list = [10,20,30,40]

def average(x):
    #complete the function's body to return the average
    r = 0
    for k in x:
        r += k
    return r/len(x)    

no_list = [1,2,3,4,12,5]
# print(f"average is {average(no_list)}")
    

def maximum(x):
    #complete the function to return the highest number in the list
    max = 0
    for i in x:
        if i > max:
            max = i
    return max

# print(maximum(no_list))

# Task 4:

no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]
# no_list =[1,1,1,2,2,3,3,3,3,4,5,5,6]
def unique_list(l):
  #complete the function's body to return the unique list of numbers
    no_list.sort()
    output = []
    for i in range(len(l)-1):
        if l[i] < l[i + 1]:
            output.append(l[i])
        if l[len(l)-1] == l[len(l)-1] and i == len(l)-2:
            output.append(l[len(l)-1])
    return output

# no_list.sort()
# print(no_list)
# print(unique_list(no_list))
# print(len(no_list))

list=[9,2,1,60,17,24]
def maxNbr2(x):
    largest = 0
    secondLargest = 0
    for i in x:
        if i > largest:
            secondLargest = largest
            largest = i
        elif i > secondLargest:
            secondLargest = i
    return secondLargest            

print(maxNbr2(list))

# list = os.listdir("Desktop/png2")

print(list[3])
#"united-kingdom-flag-country-nation-union-empire-33115.png"
# TO:
#"United Kingdom.png" (space included)


# for i in range(len(list[0])):
#     s=list[0]
#     print(s.split('-')[i])
# for count,filename in enumerate(os.listdir("Desktop/png")):
#     print(count,filename)


def main(): 
  
    for count, filename in enumerate(os.listdir("Desktop/png")): 
        newName ="country" + str(count*10) + ".png"
        src ='Desktop/png/'+ filename 
        newName ='Desktop/png/'+ newName 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, newName)

# main()

s=list[3]
# print(s.find("-flag"))

# # s=s[0:s.find("-flag")]
# s=(s[0:s.find("-flag")] + s[s.find("."):]).replace('-',' ')

print(s)

# print(s.replace('-',' '))


def main(): 
  
    for count, s in enumerate(os.listdir("Desktop/png/")): 
        
        newName = (s[0:s.find("-flag")] + s[s.find("."):]).replace('-',' ')
        oldFileName ='Desktop/png/'+ s 
        newName ='Desktop/png/'+ newName 
        os.rename(oldFileName, newName)
    print("Done :)")
# main()        

#folderPath exemple like :"Desktop/images" and you must use ""
def main(folderPath): 
  
    for count, s in enumerate(os.listdir(folderPath)): 
        
        newName = (s[0:s.find("-flag")] + s[s.find("."):]).replace('-',' ')
        oldFileName = folderPath + '/' + s 
        newName = folderPath + '/' + newName 
        os.rename(oldFileName, newName)
    print("Done :|")
    
#main("Desktop/png/")

def expand(x):
    s=""
    for elem in x:
      s+=elem
    return s*3  

print(expand(['string1', 'string2']))        

def expandV2(x):
    return ''.join(x) * 3
    

# >>> a=1
# >>> b=2
# >>> c=3
# >>> a,b,c=b,c,a
# >>> print(a,b,c)
# 2 3 1
import re

ass="[Crunchyroll] Naruto Shippuden - 18.ass"
mkv="[AnimeRG] Naruto Shippuden - 018 [720p] [x265] [pseudo].mkv"
    

def naruto2(): 
  #for episode > 99
  for count, vid in enumerate(os.listdir("Desktop/#")):

    newName = "[AnimeRG] Naruto Shippuden - " + "".join(re.findall(r'\d+',vid[:36])) + " [720p] [x265] [pseudo].ass"
    oldFileName ='Desktop/#/'+vid
    newName ='Desktop/#/'+ newName
    os.rename(oldFileName, newName)
    print(vid[:36])


naruto2()

def naruto1(): 
  #for episode < 100
  for count, vid in enumerate(os.listdir("Desktop/#")):

    newName = "[AnimeRG] Naruto Shippuden - " + "".join(re.findall(r'\d+',vid[:35])) + " [720p] [x265] [pseudo].ass"
    oldFileName ='Desktop/#/'+vid
    newName ='Desktop/#/'+ newName
    os.rename(oldFileName, newName)
    print(vid[:35])
































