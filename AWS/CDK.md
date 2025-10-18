# AWS CDK Lesson

## 1. What is AWS CDK?

* **AWS CDK = Cloud Development Kit**
* It’s an **Infrastructure as Code (IaC) framework** that lets you define AWS resources using real programming languages (Python, TypeScript, Java, C#, etc.) instead of YAML/JSON like in CloudFormation.
* Under the hood:
  * You write code → CDK compiles it to **CloudFormation templates** → AWS deploys it.
* Think: *“Terraform but AWS-native and code-driven.”*

---

## 2. Why use CDK?

* **Familiar languages** → no need to learn CloudFormation YAML.
* **Abstractions called Constructs** → pre-built patterns (like `aws-cdk-lib/aws-s3.Bucket`) that make it simple to provision common AWS services.
* **Reusable & modular** → can package your infra as libraries.
* **Best practices baked in** → e.g., `Bucket` defaults to private access.

---

## 3. Core Concepts

* **App** : the root container for your CDK code.
* **Stack** : represents a CloudFormation stack (a collection of resources).
* **Constructs** : building blocks (like classes) that represent AWS resources.
* **L1 Constructs** = raw CloudFormation (low-level).
* **L2 Constructs** = higher-level with AWS best practices.
* **L3 Constructs (Patterns)** = opinionated combos of multiple resources.

---

## 4. Typical Workflow

1. Install CDK:
   ```bash
   npm install -g aws-cdk
   cdk --version
   ```
2. Initialize a project (e.g., in Python):
   ```bash
   mkdir my-cdk-app && cd my-cdk-app
   cdk init app --language python
   ```
3. Define resources in your stack (`my_cdk_app_stack.py`):
   ```python
   from aws_cdk import (
       Stack,
       aws_s3 as s3
   )
   from constructs import Construct

   class MyCdkAppStack(Stack):
       def __init__(self, scope: Construct, construct_id: str, **kwargs):
           super().__init__(scope, construct_id, **kwargs)

           # Example: S3 bucket
           s3.Bucket(
               self, 
               "MyBucket",
               versioned=True,
               removal_policy=cdk.RemovalPolicy.DESTROY
           )

   ```
4. Bootstrap (one-time setup):
   ```bash
   cdk bootstrap
   ```
5. Deploy:
   ```bash
   cdk bootstrap
   ```
6. Destroy when done:
   ```bash
   cdk destroy
   ```

---

## 5. Example: Lambda + API Gateway

Here’s a  **common interview-ready example** : expose a Lambda with an API Gateway.

```python
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class ApiLambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Lambda function
        my_lambda = _lambda.Function(
            self, "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="hello.handler",
            code=_lambda.Code.from_inline(
                "def handler(event, context):\n return {'statusCode':200,'body':'Hello from Lambda!'}"
            )
        )

        # API Gateway endpoint
        apigw.LambdaRestApi(
            self, "Endpoint",
            handler=my_lambda
        )
```

👉 Run `cdk deploy`, and you’ll get a public HTTP endpoint backed by Lambda.

---

## 6. Monitoring & Useful Commands

* `cdk diff` → show what will change before deploying.
* `cdk synth` → generate the CloudFormation template from your code.
* `cdk ls` → list stacks in the app.

---

## 7. Real-World Uses

* Web app infra: API Gateway + Lambda + DynamoDB.
* Data pipelines: Kinesis → Lambda → S3.
* Event-driven apps: SQS, EventBridge, SNS integration.
* Multi-env setups: define dev/stage/prod stacks with different settings.

---

## 8. Quick Interview One-Liner

> “AWS CDK lets you define AWS infrastructure in code using languages like Python or TypeScript. It compiles down to CloudFormation, but with higher-level constructs and reusable patterns, making deployments faster, safer, and more maintainable.”
>
