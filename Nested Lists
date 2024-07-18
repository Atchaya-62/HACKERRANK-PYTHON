students=[]
score=[]
low_name =[]
n=int(input())
for i in range(n):
    name=input()
    scores=float(input())
    students.append([name,scores])
    score.append(scores)
score=sorted(set(score))
low=score[1]
for student in students:
    if student[1]==low:
        low_name.append(student[0])
low_name.sort()
for name in low_name:
    print(name)
        
