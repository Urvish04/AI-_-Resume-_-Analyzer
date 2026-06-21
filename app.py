import streamlit as st


def load_skills():
    with open("skills_database.txt", "r") as file:
        skills = [line.strip() for line in file.readlines()]
    return skills


def find_skills(text, skills):
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def calculate_match_score(resume_skills, job_skills):
    common_skills = set(resume_skills).intersection(set(job_skills))

    if len(job_skills) > 0:
        score = (len(common_skills) / len(job_skills)) * 100
    else:
        score = 0

    missing_skills = set(job_skills) - set(resume_skills)

    return score, missing_skills


st.title("AI Resume Analyzer")

st.write("Compare your resume skills with a job description.")

resume_text = st.text_area("Paste Resume Text")

job_description = st.text_area("Paste Job Description")

if st.button("Analyze"):

    skills = load_skills()

    resume_skills = find_skills(resume_text, skills)

    job_skills = find_skills(job_description, skills)

    match_score, missing_skills = calculate_match_score(
        resume_skills,
        job_skills
    )

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