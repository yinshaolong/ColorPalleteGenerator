# ColorPalleteGenerator

## Prerequisites
Before starting, make sure you have the following installed:

- [AWS CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)
- [Elastic Beanstalk CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)
- [Python 3](https://www.python.org/downloads/)

## Running the Application
It's recommended to use a virtual environment to isolate your project's dependencies. Follow these steps to set up and activate a virtual environment:
```bash
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate

# Unix/Mac
source venv/bin/activate
```
Installing Dependencies
```bash
pip install -r requirements.txt
```

To start the application locally, use the following command:

```bash
export FLASK_APP=application.py
flask run
```

## Deploy Steps

Ensure that your IAM user has full access to Elastic Beanstalk. You can attach the following AWS managed policies to the IAM role:
- `AWSElasticBeanstalkFullAccess`
- `AWSElasticBeanstalkService`
- `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`

Give user of IAM role on elasticbeanstalk: full access role
Initialize the Elastic Beanstalk Application
Run the following command to initialize your Elastic Beanstalk project. Replace [project-name] with the name of your application:

```bash
eb init -p python-3.11 [project-name] --region us-east-1
```
Create a New Environment
To create a new environment for your application, run the following command. Replace [environment-name] with the name of the environment you want to create:
```bash
eb create [environment-name]
```
This will spin up a new Elastic Beanstalk environment with the application deployed to it.
Additional Configuration
You can use the eb deploy command to push updates to your environment, and eb status to check the current status of your environment.