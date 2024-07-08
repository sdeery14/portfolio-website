from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', active_page='home')

@main.route('/projects')
def projects():
    project_list = [
        {'name': 'Telecom Customer Churn', 'url': url_for('main.telecom_customer_churn')},
        {'name': 'Financial News Sentiment', 'url': url_for('main.financial_news_sentiment')},
        {'name': 'Ski Resort Database', 'url': url_for('main.ski_resort_database')}
    ]
    return render_template('projects.html', projects=project_list, active_page='projects')

@main.route('/project/telecom-customer-churn')
def telecom_customer_churn():
    return render_template('project-details/telecom-customer-churn.html', active_page='projects', active_project='telecom-customer-churn')

@main.route('/project/financial-news-sentiment')
def financial_news_sentiment():
    return render_template('project-details/financial-news-sentiment.html', active_page='projects', active_project='financial-news-sentiment')

@main.route('/project/ski-resort-database')
def ski_resort_database():
    return render_template('project-details/ski-resort-database.html', active_page='projects', active_project='ski-resort-database')

@main.route('/about')
def about():
    return render_template('about.html', active_page='about')
