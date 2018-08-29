# RMinder Slackbot

## Introduction
![enter image description here](https://drive.google.com/uc?id=1ly5X_DdmpzGjBDidWT6sAWZtQv4MmGK1)

**RMinder** is a simple Slackbot built for the Reward SDK team in Rakuten to programmatically remind us to fill out timesheet and order our free lunch for the week to come.

This app is actually my personal project to learn the **FaaS (Function as a Service)** platforms such as ***Lambda***, ***Azure Function*** or ***Google Cloud Function***

In order to reduce the time to setup the required dependencies; I decided to write this app in **Python 3** and using AWS' provided **Chalice** framework

#### What is Chalice?

From **Chalice**'s GitHub page ([Chalice](https://github.com/aws/chalice))
> Blockquote
Chalice is a microframework for writing serverless apps in python. It allows you to quickly create and deploy applications that use AWS Lambda. It provides:
>-  A command line tool for creating, deploying, and managing your app
>-   A decorator based API for integrating with Amazon API Gateway, Amazon S3, Amazon SNS, Amazon SQS, and other AWS services.
>-   Automatic IAM policy generation

##### Installation

    pip install chalice

## Requirements

 - An AWS Account
	 - Configure your credentials as per Chalice documentation
 - Python IDE
 - Python 3
 - AWS Chalice Framework

## Deploying

Deploying the app using **Chalice** is simple.

    chalice deploy --stage (dev/stg/prod)

**Chalice** will then handle the rest. If you made a `@app.request` API endpoint, **Chalice** will create the necessary endpoint in ***AWS API Gateway***

Or if you prefer to use queue as I did in this project, **Chalice** will automatically setup the necessary ***CloudWatch*** event that will trigger the function at the specified timing without us having to worry to setup the necessary IAM permissions for these events.

## Usage
As per my requirement, I set up the **RMinder** to send a message on a specified timing to remind us to fill our timesheet entries and also order food for next week.

It interact with us through texts like these:
![Timesheet Reminder](https://drive.google.com/uc?id=1fgjG-UEBdT_072Z553HvSeg6j7tkC9dW)

![Order Food Reminder](https://drive.google.com/uc?id=1dk8mpqCi3Yu68Acu3uPBdq8ncSLrgHL9)
