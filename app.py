import streamlit as st

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------
st.set_page_config(
    page_title="AI Personalized Learning Agent",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("🤖 AI Personalized Learning Agent")
st.write("Personalized learning recommendations based on student performance.")

st.markdown("---")


# -----------------------------------
# STUDENT DETAILS
# -----------------------------------
st.header("👨‍🎓 Student Details")

name = st.text_input("Student Name")

course = st.selectbox(
    "Select Course",
    [
        "BCA",
        "BCA AI & ML",
        "B.Tech",
        "MCA",
        "Other"
    ]
)

st.markdown("---")


# -----------------------------------
# SUBJECT MARKS
# -----------------------------------
st.header("📝 Enter Subject Marks")

python_marks = st.number_input(
    "Python Marks",
    min_value=0,
    max_value=100,
    value=0
)

dbms_marks = st.number_input(
    "DBMS Marks",
    min_value=0,
    max_value=100,
    value=0
)

cn_marks = st.number_input(
    "Computer Networks Marks",
    min_value=0,
    max_value=100,
    value=0
)

aiml_marks = st.number_input(
    "AI/ML Marks",
    min_value=0,
    max_value=100,
    value=0
)


# -----------------------------------
# FUNCTIONS
# -----------------------------------

def get_level(score):

    if score < 50:
        return "Beginner"

    elif score < 75:
        return "Intermediate"

    else:
        return "Advanced"


def get_learning_path(level):

    if level == "Beginner":

        return "Learn Basics → Watch Tutorials → Easy Practice"

    elif level == "Intermediate":

        return "Revise Concepts → Practice Questions → Take Quiz"

    else:

        return "Advanced Topics → Projects → Placement Preparation"


# -----------------------------------
# PERSONALIZED VIDEO LINKS
# -----------------------------------

video_links = {

    "Python":
        "https://www.youtube.com/watch?v=rfscVS0vtbw",

    "DBMS":
        "https://www.youtube.com/results?search_query=DBMS+for+beginners",

    "Computer Networks":
        "https://www.youtube.com/results?search_query=Computer+Networks+for+beginners",

    "AI/ML":
        "https://www.youtube.com/results?search_query=AI+Machine+Learning+for+beginners"
}


# -----------------------------------
# GENERATE LEARNING PLAN
# -----------------------------------

if st.button("🚀 Generate Learning Plan"):

    # Check student name

    if name.strip() == "":

        st.error("Please enter the student name.")

    else:

        # -----------------------------------
        # STORE MARKS
        # -----------------------------------

        results = {

            "Python": python_marks,

            "DBMS": dbms_marks,

            "Computer Networks": cn_marks,

            "AI/ML": aiml_marks

        }


        # -----------------------------------
        # CALCULATE AVERAGE
        # -----------------------------------

        average = sum(results.values()) / len(results)


        # -----------------------------------
        # OVERALL LEVEL
        # -----------------------------------

        overall_level = get_level(average)


        # -----------------------------------
        # FIND WEAKEST SUBJECT
        # -----------------------------------

        weakest_subject = min(
            results,
            key=results.get
        )


        # -----------------------------------
        # STUDENT INFORMATION
        # -----------------------------------

        st.markdown("---")

        st.header("👨‍🎓 Student Information")

        st.write("**Student Name:**", name)

        st.write("**Course:**", course)


        # -----------------------------------
        # PERFORMANCE ANALYSIS
        # -----------------------------------

        st.markdown("---")

        st.header("📊 Performance Analysis")


        for subject, marks in results.items():

            level = get_level(marks)

            st.write(
                f"### {subject}"
            )

            st.write(
                f"Marks: **{marks}%**"
            )

            st.write(
                f"Level: **{level}**"
            )

            st.write(
                "Learning Path: "
                + get_learning_path(level)
            )

            st.markdown("---")


        # -----------------------------------
        # OVERALL PERFORMANCE
        # -----------------------------------

        st.header("🎯 Overall Performance")

        st.write(
            f"**Average Score:** {average:.2f}%"
        )

        st.write(
            f"**Overall Level:** {overall_level}"
        )

        st.write(
            "**Overall Learning Path:** "
            + get_learning_path(overall_level)
        )


        # -----------------------------------
        # AI RECOMMENDATION
        # -----------------------------------

        st.markdown("---")

        st.header("🤖 AI Recommendation")

        st.warning(
            f"Your weakest subject is **{weakest_subject}**."
        )

        st.write(
            f"The AI agent recommends focusing more on "
            f"**{weakest_subject}**."
        )


        # -----------------------------------
        # PERSONALIZED LEARNING ADVICE
        # -----------------------------------

        weakest_marks = results[weakest_subject]


        if weakest_marks < 50:

            st.info(
                f"You are at the Beginner level in {weakest_subject}. "
                "Start with basic concepts and beginner tutorials."
            )

        elif weakest_marks < 75:

            st.info(
                f"You are at the Intermediate level in {weakest_subject}. "
                "Revise concepts and practice more questions."
            )

        else:

            st.success(
                f"You have a strong foundation in {weakest_subject}. "
                "Try advanced topics and projects."
            )


        # -----------------------------------
        # PERSONALIZED VIDEO
        # -----------------------------------

        st.markdown("---")

        st.header("🎥 Personalized Learning Video")

        st.write(
            f"Recommended video resource for **{weakest_subject}**:"
        )

        st.markdown(
            f"### ▶ [Learn {weakest_subject}]({video_links[weakest_subject]})"
        )

        st.write(
            "This resource was selected because "
            f"{weakest_subject} is currently your weakest subject."
        )


        # -----------------------------------
        # ALL SUBJECT VIDEO LINKS
        # -----------------------------------

        st.markdown("---")

        st.header("📚 Other Learning Resources")

        st.markdown(
            "[🐍 Python Tutorials](https://www.youtube.com/watch?v=rfscVS0vtbw)"
        )

        st.markdown(
            "[🗄️ DBMS Tutorials](https://www.youtube.com/results?search_query=DBMS+for+beginners)"
        )

        st.markdown(
            "[🌐 Computer Networks Tutorials](https://www.youtube.com/results?search_query=Computer+Networks+for+beginners)"
        )

        st.markdown(
            "[🤖 AI/ML Tutorials](https://www.youtube.com/results?search_query=AI+Machine+Learning+for+beginners)"
        )


        # -----------------------------------
        # FINAL MESSAGE
        # -----------------------------------

        st.markdown("---")

        st.success(
            "🎉 Personalized learning plan generated successfully!"
        )

        st.write(
            "The AI agent analyzed your marks and selected "
            "a learning resource based on your weakest subject."
        )
