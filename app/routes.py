from flask import Blueprint, render_template
import os

main = Blueprint('main', __name__)

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Example projects data
project_list = [
    {
        'slug': 'financial-news-sentiment',
        'title': 'Topic and Sentiment Classification of News Articles',
        'description': 'This project focuses on classifying news articles into specific market topics and analyzing their sentiment.',
        'details': read_html_file(os.path.join('app/project_details', 'financial-news-sentiment.html')),
        'github_link': 'https://github.com/sdeery14/financial-news-sentiment'
    },
    {
        'slug': 'telecom-customer-churn',
        'title': 'Predictive Analysis of Customer Churn in the Telecom Sector',
        'description': 'Customer churn, where customers switch from one service provider to another, poses a significant challenge for telecommunications companies. This project leverages data science methodologies to analyze customer data, understand the underlying factors of churn, and develop predictive models to forecast potential churn. This enables telecom companies to implement targeted retention strategies and enhance customer loyalty.',
        'details': read_html_file(os.path.join('app/project_details', 'telecom-customer-churn.html')),
        'github_link': 'https://github.com/sdeery14/telecom-customer-churn'
    },
    {
        'slug': 'ski-resort-database',
        'title': 'Ski Resort Database System',
        'description': 'The Ski Resort Management System is designed to manage various operations at a ski resort, including tracking lift tickets, equipment rentals, and skier information.',
        'details': read_html_file(os.path.join('app/project_details', 'ski-resort-database.html')),
        'github_link': 'https://github.com/sdeery14/ski-resort-database'
    }
    # Add more projects as needed
]


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/projects')
def projects():
    return render_template('projects.html', projects=projects)

@main.route('/project/<slug>')
def project_detail(slug):
    project = next((proj for proj in project_list if proj['slug'] == slug), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_detail.html', project=project)


@main.route('/about')
def about():
    return render_template('about.html')
