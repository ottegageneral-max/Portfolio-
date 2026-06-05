from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-for-production'

# Portfolio data - customize this with your own information
PORTFOLIO_DATA = {
    'name': 'Wanter22',
    'title': 'Python Developer',
    'bio': 'Passionate about building web applications and solving problems with Python. Learning web development with real, human-made code.',
    'email': 'your-email@example.com',
    'github': 'https://github.com/Wanter22',
    'location': 'Earth',
}

PROJECTS = [
    {
        'id': 1,
        'title': 'Portfolio Website',
        'description': 'A personal portfolio website built with Flask. Clean, authentic design - no shortcuts taken.',
        'tech': ['Flask', 'Python', 'HTML', 'CSS', 'JavaScript'],
        'github': 'https://github.com/ottegageneral-max/Portfolio-',
        'live': '#',
    },
    {
        'id': 2,
        'title': 'Todo App',
        'description': 'A task management application built from scratch. Users can create, edit, delete, and organize their daily tasks.',
        'tech': ['Python', 'Flask', 'SQLite', 'HTML/CSS'],
        'github': '#',
        'live': '#',
    },
    {
        'id': 3,
        'title': 'Weather Tracker',
        'description': 'Real-time weather information application. Fetches live data and displays it in an intuitive interface.',
        'tech': ['Python', 'Flask', 'API Integration', 'JavaScript'],
        'github': '#',
        'live': '#',
    },
]

SKILLS = [
    'Python',
    'Flask',
    'HTML & CSS',
    'JavaScript',
    'Git & GitHub',
    'SQLite',
    'Problem Solving',
    'Web Development',
]

@app.route('/')
def home():
    return render_template('index.html', portfolio=PORTFOLIO_DATA)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS, portfolio=PORTFOLIO_DATA)

@app.route('/about')
def about():
    return render_template('about.html', skills=SKILLS, portfolio=PORTFOLIO_DATA)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        # In production, you would send this to your email service
        print(f"Message received from {data.get('email')}: {data.get('message')}")
        return jsonify({'success': True, 'message': 'Thanks for reaching out! I will get back to you soon.'})
    return render_template('contact.html', portfolio=PORTFOLIO_DATA)

@app.route('/api/projects')
def api_projects():
    return jsonify(PROJECTS)

if __name__ == '__main__':
    app.run(debug=True)
