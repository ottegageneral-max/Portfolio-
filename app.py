from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-for-production'

# Portfolio data - customize this with your own information
PORTFOLIO_DATA = {
    'name': 'Ottega General',
    'title': 'Full Stack Developer',
    'bio': 'Building exceptional web applications with Python, JavaScript, and modern frameworks. Passionate about clean code, scalable architecture, and delivering real value to clients.',
    'email': 'ottega@example.com',
    'github': 'https://github.com/ottegageneral-max',
    'linkedin': 'https://linkedin.com/in/ottega',
    'location': 'Worldwide',
}

PROJECTS = [
    {
        'id': 1,
        'title': 'Portfolio Website',
        'description': 'A modern, responsive portfolio website built with Flask and Python. Features a clean design with dark theme, smooth animations, and optimal performance. Fully customizable for showcasing your work.',
        'tech': ['Flask', 'Python', 'HTML5', 'CSS3', 'JavaScript', 'Responsive Design'],
        'github': 'https://github.com/ottegageneral-max/Portfolio-',
        'live': 'https://portfolio-example.com',
    },
    {
        'id': 2,
        'title': 'Task Management App',
        'description': 'A full-featured task management application with real-time updates. Users can create, organize, and track their projects with an intuitive interface. Includes user authentication and data persistence.',
        'tech': ['Flask', 'SQLite', 'JavaScript', 'Bootstrap', 'REST API'],
        'github': 'https://github.com/ottegageneral-max/task-manager',
        'live': 'https://task-manager-demo.com',
    },
    {
        'id': 3,
        'title': 'Weather Intelligence Platform',
        'description': 'Real-time weather application with advanced analytics. Fetches live data from multiple weather APIs, displays beautiful forecasts, and provides weather insights for multiple locations.',
        'tech': ['Python', 'Flask', 'API Integration', 'JavaScript', 'Chart.js', 'Redis'],
        'github': 'https://github.com/ottegageneral-max/weather-app',
        'live': 'https://weather-intelligence.com',
    },
    {
        'id': 4,
        'title': 'E-Commerce Store',
        'description': 'Full-stack e-commerce platform with product catalog, shopping cart, and secure checkout. Features inventory management, order tracking, and admin dashboard for store management.',
        'tech': ['Flask', 'PostgreSQL', 'Stripe API', 'Bootstrap', 'JavaScript', 'AWS'],
        'github': 'https://github.com/ottegageneral-max/ecommerce',
        'live': 'https://store-demo.com',
    },
]

SKILLS = [
    {'name': 'Python', 'level': 95},
    {'name': 'Flask', 'level': 90},
    {'name': 'JavaScript', 'level': 85},
    {'name': 'HTML & CSS', 'level': 92},
    {'name': 'React', 'level': 80},
    {'name': 'SQL & Databases', 'level': 88},
    {'name': 'Git & GitHub', 'level': 90},
    {'name': 'REST APIs', 'level': 85},
    {'name': 'Problem Solving', 'level': 95},
    {'name': 'Web Development', 'level': 90},
]

TESTIMONIALS = [
    {
        'text': 'Outstanding developer! Delivered a complex project on time and exceeded expectations. Highly professional and easy to work with.',
        'author': 'Sarah Johnson',
        'role': 'CEO, TechStart Inc',
    },
    {
        'text': 'Excellent communication and technical expertise. The solution was robust, scalable, and beautifully implemented.',
        'author': 'Michael Chen',
        'role': 'Product Manager, Digital Innovations',
    },
    {
        'text': 'A true full-stack expert. Built our entire platform from scratch with clean, maintainable code. Highly recommended!',
        'author': 'Emma Williams',
        'role': 'Founder, WebFlow Solutions',
    },
]

@app.route('/')
def home():
    return render_template('index.html', portfolio=PORTFOLIO_DATA, projects=PROJECTS[:3])

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS, portfolio=PORTFOLIO_DATA)

@app.route('/about')
def about():
    return render_template('about.html', skills=SKILLS, portfolio=PORTFOLIO_DATA, testimonials=TESTIMONIALS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        # In production, you would send this to your email service (SendGrid, Mailgun, etc)
        print(f"Message received from {data.get('email')}: {data.get('message')}")
        return jsonify({'success': True, 'message': 'Thanks for reaching out! I will get back to you soon.'})
    return render_template('contact.html', portfolio=PORTFOLIO_DATA)

@app.route('/api/projects')
def api_projects():
    return jsonify(PROJECTS)

@app.route('/api/skills')
def api_skills():
    return jsonify(SKILLS)

if __name__ == '__main__':
    app.run(debug=True)
