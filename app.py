import streamlit as st

st.title("AI Resume Analyzer")

st.write("Compare your resume skills with a job description.")

resume_text = st.text_area("Paste Resume Text")
job_description = st.text_area("Paste Job Description")

if st.button("Analyze"):

    # Load skills from skills_database.txt
    with open("skills_database.txt", "r") as file:
        skills = [line.strip() for line in file.readlines()]

    resume_skills = []
    job_skills = []

    # Find skills in resume and job description
    for skill in skills:

        if skill.lower() in resume_text.lower():
            resume_skills.append(skill)

        if skill.lower() in job_description.lower():
            job_skills.append(skill)

    # Calculate matching skills
    common_skills = set(resume_skills).intersection(set(job_skills))

    if len(job_skills) > 0:
        match_score = (len(common_skills) / len(job_skills)) * 100
    else:
        match_score = 0

    # Find missing skills
    missing_skills = set(job_skills) - set(resume_skills)

    # Display results
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