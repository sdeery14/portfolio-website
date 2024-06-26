from flask import Blueprint, render_template
import os

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/projects')
def projects():
    return render_template('projects.html', projects=projects)

@main.route('/project/telecom-customer-churn')
def telecom_customer_churn():
    return render_template('project-details/telecom-customer-churn.html')

@main.route('/project/financial-news-sentiment')
def financial_news_sentiment():
    return render_template('project-details/financial-news-sentiment.html')

@main.route('/project/ski-resort-database')
def ski_resort_database():
    return render_template('project-details/ski-resort-database.html')

@main.route('/about')
def about():
    return render_template('about.html')
