from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Omkar", "course": "Computer Engineering", "marks": 85}
]

@app.route("/")
def home():
    return """
    <h1>Student Record and Academic Management Platform</h1>
    <p>DevOps Mini Project 4</p>
    <p>Student API: <a href='/api/students'>View Students</a></p>
    <p>Health API: <a href='/api/health'>Health Check</a></p>
    """

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy", "application": "Student Management Platform"})

@app.route("/api/students")
def get_students():
    return jsonify(students)

@app.route("/api/marks", methods=["POST"])
def add_marks():
    data = request.get_json(silent=True) or {}
    student_id = data.get("student_id")
    marks = data.get("marks")

    if student_id is None or marks is None:
        return jsonify({"error": "student_id and marks are required"}), 400

    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    student["marks"] = marks
    return jsonify({"message": "Marks updated", "student": student})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
