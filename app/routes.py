from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

# Centralized project data
projects_data = [
    {
        'name': 'Telecom Customer Churn',
        'endpoint': 'main.project_details',
        'params': {'project_url': 'telecom_customer_churn'},
        'tools': 'Google Colab, Python, Numpy, Pandas, Matplotlib, Seaborn, SciKit-Learn',
        'models': 'Logistic Regression, Random Forest Classifier, Support Vector Machine',
        'github': 'https://github.com/sdeery14/telecom-customer-churn.git',
        'description': 'Predictive Analysis of Customer Churn in the Telecom Sector',
        'template': 'telecom-customer-churn.html'
    },
    {
        'name': 'Financial News Sentiment',
        'endpoint': 'main.project_details',
        'params': {'project_url': 'financial_news_sentiment'},
        'tools': 'VSCode, Python, Numpy, Pandas, Matplotlib, Seaborn, SciKit-Learn, pyLDAvis',
        'models': 'Decision Tree, Naive Bayes, Support Vector Machine',
        'github': 'https://github.com/sdeery14/financial-news-sentiment.git',
        'description': 'Topic and Sentiment Classification of News Articles',
        'template': 'financial-news-sentiment.html'
    },
    {
        'name': 'Ski Resort Database',
        'endpoint': 'main.project_details',
        'params': {'project_url': 'ski_resort_database'},
        'tools': 'Microsoft SQL Server, Azure Data Studio, Draw.io',
        'models': '',
        'github': 'https://github.com/sdeery14/ski-resort-database.git',
        'description': 'Ski Resort Management System',
        'template': 'ski-resort-database.html'
    },
    {
        'name': 'Email Spam Detection',
        'endpoint': 'main.project_details',
        'params': {'project_url': 'spam-classification'},
        'tools': 'Jupyter Notebook, Python, Numpy, Pandas, Matplotlib, Seaborn, Wordcloud, NLTK, Scikit-Learn',
        'models': 'Naive Bayes',
        'github': 'https://github.com/sdeery14/spam-classification.git',
        'description': 'Spam vs. Ham Email Classification',
        'template': 'spam-classification.html'
    }
]

@main.route('/')
def home():
    return render_template('index.html', active_page='home')

@main.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data, active_page='projects')

@main.route('/projects/<project_url>')
def project_details(project_url):
    project = next((proj for proj in projects_data if proj['params']['project_url'] == project_url), None)
    if project:
        return render_template('project-details.html', project=project, active_page='projects', active_project=project_url)
    return render_template('404.html'), 404

@main.route('/about')
def about():
    return render_template('about.html', active_page='about')
