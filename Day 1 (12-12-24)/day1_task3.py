# calculate student grade


project = int(input("enter project score out of 100 : "))
internal = int(input("enter internal score out of 100 :"))
external = int(input("enter external score out of 100 : "))
total_score=0
if (project >= 50 and internal >=50 and external >=50):
   total_score = ((project * 70) / 100) + ((internal * 10) / 100) + ((external * 20) / 100)
   print("Total score is ",total_score)
else :
   if (project <50):
       print("Failed in project, score is :",project)
   if (internal <50):
       print("Failed in internal, score is :",internal)
   if(external <50):
       print("Failed in external,score is :",external)
if(total_score >90):
   print("Grade A")
elif(total_score > 80 and total_score<=90):
   print("Grade B")
elif (total_score >50 and total_score <=80):
   print("Grade C")
