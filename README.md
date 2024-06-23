# Sean Deery's Portfolio

Welcome to my personal portfolio website, built with Flask. This site showcases my data science projects, professional experience, and skills. Explore the site to learn more about my work and get in touch with me.

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contact Information](#contact-information)
- [License](#license)

## About the Project

This portfolio website is designed to highlight my skills and experience as a Cloud Support Analyst and a Data Scientist. The site is built using Flask, a lightweight Python web framework, and it follows modern web development practices.

## Features

- **Responsive Design**: The site is fully responsive, ensuring a great user experience on both desktop and mobile devices.
- **Dynamic Content**: Uses Flask templates to dynamically render pages.
- **Easy Navigation**: Simple and clean navigation through the site's pages: Home, Projects, and About Me.
- **Contact Information**: Easily accessible contact details and social media links.

## Technologies Used

- **Framework**: Flask
- **Languages**: Python, HTML, CSS
- **Front-End**: Bootstrap (for responsive design), Font Awesome (for icons)
- **Hosting**: GitHub Pages (or specify if using another hosting service)

## Setup and Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sdeery14/portfolio.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd portfolio
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**:
- On Windows:
   ```bash
   venv\Scripts\activate
   ```
- On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
5. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the Flask app**:
   ```bash
   flask run
   ```

## Usage
After setting up the project, you can access the website locally by navigating to http://127.0.0.1:5000/ in your web browser.

### Available Pages
- Home: A welcoming page introducing the site.
- Projects: A showcase of my data science and other projects.
- About Me: Detailed information about my background, skills, and contact details.

## Project Structure
Here’s an overview of the project directory structure:

```php
portfolio/
│
├── app/
│   ├── static/          # Static files (CSS, JS, images)
│   ├── templates/       # HTML templates
│   │   ├── base.html    # Base template
│   │   ├── header.html  # Header template
│   │   ├── footer.html  # Footer template
│   │   ├── index.html   # Home page
│   │   ├── projects.html# Projects page
│   │   └── about.html   # About Me page
│   ├── __init__.py      # Flask app initialization
│   └── routes.py        # Routes for the app
│
├── venv/                # Virtual environment
├── requirements.txt     # Project dependencies
└── run.py               # Script to run the app
```

## Contact Information
Feel free to reach out if you have any questions or just want to connect!

- Name: Sean Deery
- Email: sdeery14@gmail.com
- LinkedIn: linkedin.com/in/sean-m-deery
- GitHub: github.com/sdeery14

## License
This project is open source and available under the MIT License.
