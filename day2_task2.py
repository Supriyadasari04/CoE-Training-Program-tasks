# calculate student grade using steamlit
import streamlit as st
st.title("Student Grade Caculation")

project = st.number_input("Enter project score out of 100 : ",min_value=0)
internal = st.number_input("Enter internal score out of 100 :", min_value=0)
external = st.number_input("Enter external score out of 100 : ", min_value=0)
total_score=0
if st.button("Calculate student grade"):
    if (project >= 50 and internal >=50 and external >=50):
        total_score = ((project * 70) / 100) + ((internal * 10) / 100) + ((external * 20) / 100)
        st.write(f"Total score is {total_score}")
        if(total_score >90):
            st.write(f"Grade A")
        elif(total_score > 80 and total_score<=90):
            st.write(f"Grade B")
        elif (total_score >50 and total_score <=80):
            st.write(f"Grade C")
    else :
        if (project <50):
            st.write(f"Failed in project, score is :{project}")
        if (internal <50):
            st.write(f"Failed in internal, score is :{internal}")
        if(external <50):
            st.write(f"Failed in external,score is :{external}")
        
