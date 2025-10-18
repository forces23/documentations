## 🔹 AWS Data Pipeline (Project 1)

**Likely Questions:**

* *How would you secure S3 buckets used in your pipeline against unauthorized access?*
* *How do you handle schema evolution in Glue when logs change structure?*
* *What would you do if Athena queries started running slowly as data grew?*
* *How would you optimize Kinesis costs if throughput suddenly spiked?*

👉 They’ll be testing: security, scalability, and cost tradeoffs.

---

## 🔹 AI-Powered Chatbot (Project 2)

**Likely Questions:**

* *How did you integrate Bedrock into your Lex bot? What patterns did you use for grounding responses?*
* *If a user asks the same question 50 times in one hour, how do you optimize response cost/latency?*
* *What’s the difference between Lex + Bedrock vs building a custom RAG pipeline with SageMaker + OpenSearch?*
* *How would you secure sensitive customer data in conversations stored in DynamoDB?*

👉 They’ll be testing: your **SME-level AI knowledge** and ability to talk tradeoffs between AWS AI services.

---

## 🔹 EKS Deployment (Project 3)

**Likely Questions:**

* *What are some best practices for deploying applications on EKS (networking, scaling, monitoring)?*
* *How would you troubleshoot a pod stuck in “CrashLoopBackOff”?*
* *If you need zero-downtime deployments, how would you set that up in Kubernetes?*
* *Would you use RDS or DynamoDB in this EKS app, and why?*

👉 They’ll be testing: do you understand container orchestration  **beyond just writing code** .

---

## 🔹 General AWS (Cross-Cutting)

**Likely Questions:**

* *How do you secure API Gateway endpoints that connect to your Lambda functions?*
* *What’s the difference between SNS and SQS, and when would you use each?*
* *How do you monitor cost and performance across multiple AWS accounts?*
* *How would you handle secrets in AWS for your apps? (e.g., DB credentials, API keys)*

👉 They’ll be testing: do you know  **the right AWS service for the job** .

---

## 🔹 Cloud + AI Future-Oriented (Because of Bedrock + “Agentic AI”)

**Likely Questions:**

* *What are some risks of using LLMs like Bedrock for financial/insurance data? How do you mitigate them?*
* *Can you describe how you’d design an agent-based AI solution in AWS?*
* *When would you pick Bedrock vs SageMaker for an AI project?*
* *How would you integrate human-in-the-loop feedback in your chatbot?*

👉 They’ll be testing: do you understand  **responsible AI + modern AI architectures** .

---

## 🔹 POCs / Amplify Work

Since you mentioned POCs:

* *Why did you choose Amplify for your POCs instead of ECS/EKS?*
* *What are the tradeoffs between Amplify hosting and S3 + CloudFront hosting?*
* *How would you secure an Amplify-deployed app with Cognito?*

---

✅ Based on what you told me, I’d expect the **heaviest focus** to be:

1. AWS architectural decisions (Lambda vs Fargate vs EKS, S3 vs DynamoDB, etc.)
2. AI/Bedrock/Q — they’ll want to see if you can **apply AI responsibly**
3. Security & compliance (financial data, IAM, encryption, least privilege)
4. Cost optimization (Kinesis, S3, Bedrock token costs, EKS workloads)
