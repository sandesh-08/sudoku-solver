import pyttsx3
import numpy as np

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def add_info():
    f=open("entries.txt")
    entries=list(f)
    f.close()
    li_entries=list()
    for i in entries:
        li_entries=list(i.replace('\n','').split())
        i,j,val=int(li_entries[0]),int(li_entries[1]),int(li_entries[2])
        entry[i][j]=val
def solution(count):
    while(count!=int(no_rows**2)):
        for i in range(no_rows):
            for j in range(no_rows):
                if entry[i][j]==0:
                    a,b,c=list(),list(),list()
                    e=int(i/3)
                    f=int(j/3)
                    for p in range((3*e),(3*e)+3,1):
                        for q in range((3*f),(3*f)+3,1):
                            if entry[p][q]!=0:
                                c.append(entry[p][q])
                    for p in range(no_rows):
                        if(entry[i][p]!=0):
                            a.append(entry[i][p])
                    for p in range(no_rows):
                        if(entry[p][j]!=0):
                            b.append(entry[p][j])
                    k=set(set(a) | set(b) | set(c))
                    uni_set=list()
                    for uni in range(no_rows):
                        uni_set.append(uni+1)
                    uni_set=set(uni_set)
                    ans_list=list(uni_set-k)
                    if(len(ans_list)==1):
                        entry[i][j]=ans_list[0]
                        count=count+1
    print("---------:SOLVED SUDOKU:--------")
    print(entry)

                    
    
if __name__ == "__main__":
    speak("welcome this is a virtual api to solve your sudoku")
    no_rows=9
    speak("i have created an empty box and am displaying it in terminal")
    entry = np.zeros([no_rows, no_rows], dtype = int)
    print(entry)
    speak("add some entries over here and i shall do rest work")
    speak("use these following commands")
    speak("for entering entries follow this protocol...first enter co-ordinates and then values and also remember these commands")
    speak("1 for adding info and 2 to proceed for solution and 3 for displaying sudoku")
    print("1 for adding info and 2 to proceed for solution and 3 for displaying sudoku")
    a=0
    while(True):
        print("ENTER COMMAND: ")
        k=int(input())
        if k==1:
            add_info()
            f=open("entries.txt")
            entries=list(f)
            a=len(entries)
            f.close()
            speak("entries added succesfully and your entries are shown in command terminal")
            print("entries added succesfully")
            print(entry)
        elif k==2:
            speak("your output matrix is shown in command terminal")
            solution(a)
            break
        else:
            speak("invalid command,try again..")
            break