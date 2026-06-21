import streamlit as st

st.title("AI Resume Analyzer")

st.write("Compare your resume skills with a job description.")

resume_text = st.text_area("Paste Resume Text")
job_description = st.text_area("Paste Job Description")

if st.button("Analyze"):

    skills = [
        "Python", "Machine Learning", "Deep Learning", "NLP",
        "Data Analysis", "SQL", "Power BI", "Tableau",
        "Git", "GitHub", "Docker", "AWS", "Azure",
        "TensorFlow", "PyTorch", "Computer Vision",
        "Java", "C++", "JavaScript", "Streamlit"
    ]

    resume_skills = []
    job_skills = []

    for skill in skills:

        if skill.lower() in resume_text.lower():
            resume_skills.append(skill)

        if skill.lower() in job_description.lower():
            job_skills.append(skill)

    common_skills = set(resume_skills).intersection(set(job_skills))

    if len(job_skills) > 0:
        match_score = (len(common_skills) / len(job_skills)) * 100
    else:
        match_score = 0

    missing_skills = set(job_skills) - set(resume_skills)

    st.subheader("Match Score")
    st.write(f"{match_score:.2f}%")

    st.progress(match_score / 100)

    st.subheader("Skills Found In Resume")
    st.write(resume_skills)

    st.subheader("Recommended Skills To Learn")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"• {skill}")
    else:
        st.success("Your resume matches all required skills!")