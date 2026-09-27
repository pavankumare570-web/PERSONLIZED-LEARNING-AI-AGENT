from flask import Flask, request

app = Flask(__name__)

subjects = ["Python", "DBMS", "Computer Networks", "AI/ML"]

videos = {
    "Python": "https://www.youtube.com/watch?v=rfscVS0vtbw",
    "DBMS": "https://www.youtube.com/results?search_query=DBMS+for+beginners",
    "Computer Networks": "https://www.youtube.com/results?search_query=Computer+Networks+for+beginners",
    "AI/ML": "https://www.youtube.com/results?search_query=AI+ML+for+beginners"
}


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Personalized Learning Agent</title>
    </head>

    <body>

        <center>

        <h1>🤖 AI Personalized Learning Agent</h1>

        <p>Enter your details to generate your personalized learning path.</p>

        <form action="/result" method="post">

            <p>
                👤 Student Name:
                <input type="text" name="student" required>
            </p>

            <p>
                🎓 Course:
                <select name="course" required>
                    <option value="">Select Your Course</option>
                    <option value="BCA">BCA</option>
                    <option value="BCA AI & ML">BCA AI & ML</option>
                    <option value="B.Tech">B.Tech</option>
                    <option value="MCA">MCA</option>
                    <option value="Other">Other</option>
                </select>
            </p>

            <p>
                🐍 Python Marks:
                <input type="number" name="Python"
                       min="0" max="100" required>
            </p>

            <p>
                🗄️ DBMS Marks:
                <input type="number" name="DBMS"
                       min="0" max="100" required>
            </p>

            <p>
                🌐 Computer Networks Marks:
                <input type="number" name="Computer Networks"
                       min="0" max="100" required>
            </p>

            <p>
                🤖 AI/ML Marks:
                <input type="number" name="AI/ML"
                       min="0" max="100" required>
            </p>

            <br>

            <button type="submit">
                🚀 Generate My Learning Path
            </button>

        </form>

        </center>

    </body>
    </html>
    """


@app.route("/result", methods=["POST"])
def result():

    student = request.form["student"]
    course = request.form["course"]

    results = {}
    total = 0

    # Analyze each subject
    for subject in subjects:

        score = int(request.form[subject])
        total = total + score

        if score < 50:
            level = "Beginner 🌱"
            path = "Learn Basics → Watch Tutorials → Easy Practice"

        elif score < 75:
            level = "Intermediate 📚"
            path = "Revise Concepts → Practice Questions → Take Quiz"

        else:
            level = "Advanced 🚀"
            path = "Advanced Topics → Projects → Placement Preparation"

        results[subject] = (score, level, path)

    # Calculate average
    average = total / len(subjects)

    # Find weakest subject
    weakest = min(
        results,
        key=lambda subject: results[subject][0]
    )

    # Find overall level
    if average < 50:
        overall = "Beginner 🌱"

    elif average < 75:
        overall = "Intermediate 📚"

    else:
        overall = "Advanced 🚀"


    # Result page
    output = f"""
    <!DOCTYPE html>

    <html>

    <head>
        <title>{student}'s Learning Path</title>
    </head>

    <body>

    <center>

        <h1>🎯 Hello, {student}!</h1>

        <h3>🎓 Course: {course}</h3>

        <h2>Your Personalized Learning Path</h2>

        <h3>📊 Average Score: {average:.1f}%</h3>

        <h3>Overall Level: {overall}</h3>

        <hr>

    """

    # Display subject results
    for subject, (score, level, path) in results.items():

        output += f"""
        
        <h2>📚 {subject}</h2>

        <h3>{score}% — {level}</h3>

        <p>
            <b>Recommended Learning Path:</b>
        </p>

        <p>{path}</p>

        <p>
            🎥 <b>Recommended Learning Video:</b>
        </p>

        <p>
            <a href="{videos[subject]}" target="_blank">
                ▶ Watch {subject} Learning Video
            </a>
        </p>

        <hr>

        """


    # AI recommendation
    output += f"""

        <h2>🤖 AI Recommendation</h2>

        <p>
            Hi <b>{student}</b>!
        </p>

        <p>
            Your weakest subject is
            <b>{weakest}</b>.
        </p>

        <p>
            Your score in {weakest} is
            <b>{results[weakest][0]}%</b>.
        </p>

        <p>
            👉 Focus on <b>{weakest}</b> first.
        </p>

        <p>
            📖 Start with basic concepts, watch the
            recommended video and practice questions.
        </p>

        <hr>

        <h2>🔄 Take Assessment Again</h2>

        <a href="/">
            <button>New Student / Take Assessment Again</button>
        </a>

    </center>

    </body>

    </html>
    """

    return output


if __name__ == "__main__":
    print("Starting AI Personalized Learning Agent...")
    app.run(host="127.0.0.1", port=5000, debug=True)
    