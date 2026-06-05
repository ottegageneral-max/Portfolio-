# Portfolio Website

A simple, clean portfolio website built with Flask and Python. No AI shortcuts - just real web development.

## Features

✨ **Modern Design**
- 🏠 Home page with hero section
- 📋 Projects showcase page
- 👤 About page with skills
- 📧 Contact form with JavaScript handling
- 📱 Fully responsive design
- 🎨 Clean, minimalist UI - authentic, human-made feel

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/ottegageneral-max/Portfolio-.git
   cd Portfolio-
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── Procfile              # For Heroku deployment
├── static/
│   └── css/
│       └── style.css     # Custom styling
└── templates/
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── projects.html     # Projects page
    ├── about.html        # About page
    └── contact.html      # Contact page
```

## Customization

### Update Your Information

Edit `app.py` and update the `PORTFOLIO_DATA` dictionary:

```python
PORTFOLIO_DATA = {
    'name': 'Your Name',
    'title': 'Your Title',
    'bio': 'Your bio...',
    'email': 'your-email@example.com',
    'github': 'https://github.com/yourusername',
    'location': 'Your Location',
}
```

### Add Projects

Add new projects to the `PROJECTS` list in `app.py`:

```python
{
    'id': 4,
    'title': 'Your Project',
    'description': 'Description here...',
    'tech': ['Flask', 'Python'],
    'github': 'https://github.com/yourusername/project',
    'live': 'https://your-project-live-url.com',
}
```

### Update Skills

Modify the `SKILLS` list in `app.py`:

```python
SKILLS = [
    'Your Skill 1',
    'Your Skill 2',
    # ...
]
```

## Deployment

### Deploy on Heroku

1. Create a Heroku account at https://www.heroku.com
2. Install Heroku CLI
3. Login: `heroku login`
4. Create app: `heroku create your-app-name`
5. Deploy: `git push heroku main`
6. View: `heroku open`

### Deploy on Railway

1. Visit https://railway.app
2. Connect your GitHub repository
3. Deploy with one click
4. Your site will be live!

### Deploy on PythonAnywhere

1. Create account at https://www.pythonanywhere.com
2. Upload your files
3. Create a web app and configure it
4. Your site will be live

## Technologies Used

- **Backend**: Python 3.7+, Flask
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Templating**: Jinja2
- **Hosting**: Heroku, Railway, PythonAnywhere

## Tips for Freelancing

1. **Customize this template** with your real projects and information
2. **Update project links** to point to your actual GitHub repos
3. **Deploy it live** - having a live portfolio is impressive
4. **Keep it updated** - add new projects as you build them
5. **Share it** on GitHub, LinkedIn, and freelance platforms
6. **Use it when applying** for freelance jobs and opportunities

## Next Steps

- ✅ Customize with your information
- ✅ Build and add more projects
- ✅ Deploy it live
- ✅ Share on GitHub and social media
- ✅ Update regularly with new work

## License

This project is open source and available under the MIT License.

---

**Built with ❤️ and Python** • No shortcuts, just real development

Made by @Wanter22 - Freelance Python Developer
