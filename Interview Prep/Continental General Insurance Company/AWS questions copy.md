## 🔹 AWS Data Pipeline (Project 1)

**Likely Questions:**

* ***How would you secure S3 buckets used in your pipeline against unauthorized access?***

  * I would use SSE-KMS to encrpyt all data in the s3 as well as applying IAM least priveldge rules to restrict access to only who needs it.
* ***How do you handle schema evolution in Glue when logs change structure?***

  * as far as Schema evolution i have not actually figure out a way to handle the evolution due to the time i was using it if it changed then something was wrong so we would have to figure out what was changed and see why it was changed but i am interested in figuring that out.

    ***Guidance***
  * Your answer showed honesty, but here’s the “quick lesson” you can fold in:

    * **Glue Crawlers** update the schema in the Data Catalog when data changes.
    * Problem: If a column is missing/added, queries can break.
    * Best practice:

      * Use **Glue Schema Registry** to enforce schema versions.
      * Track schema evolution (e.g., adding optional fields is backward-compatible).
      * Store data in **Parquet/ORC** format — supports schema evolution more gracefully than JSON.

  👉 Interview answer could be:

  > “If logs change structure, I’d use Glue Schema Registry to manage schema evolution. For backward compatibility, I’d design schemas so optional fields can be added without breaking queries. Also, I’d prefer Parquet over raw JSON to support more efficient queries and schema flexibility.”
  >
* ***What would you do if Athena queries started running slowly as data grew?***

  * Im not exactly sure i have not ran into that issue so far but this is something i would very much be interested in learning to keep things quick and optimized.

  Here’s the trick: Athena queries can get slow if datasets are massive.

  Ways to optimize:

  * **Partitioning** in S3 (e.g., by `date`, `region`) so queries scan less data.
  * **Compression** (Parquet/ORC vs raw JSON/CSV) → smaller files, faster reads.
  * **File size tuning** → avoid millions of small files; combine into larger files (128MB–1GB sweet spot).
  * **Query optimization** → SELECT only needed columns, avoid SELECT *.

  👉 Interview answer:

  > “If Athena queries slowed down, I’d first look at partitioning the S3 data so Athena only scans what’s needed. I’d also convert raw JSON to a columnar format like Parquet to reduce scan size. Finally, I’d optimize file sizes to avoid too many small files, which can cause overhead.”
  >

  ***This is something we actually did in my last job by putting data in year, month, day partitions to help with the large amount of call data we had***
* ***How would you optimize Kinesis costs if throughput suddenly spiked?***

  * again i have not had ran into this so i am unsure but with a little research im 100% sure i could figure it out. when i was working with Kinesis i was pretty much thrown in the deep end with no explainantion and i had to figure it all out on my own and quick due to the short timeline that was given at the time.

  ***Guidance***

  Costs spike when shard count or throughput spikes. Options:

  * **On-demand vs Provisioned mode** → Use on-demand if traffic is unpredictable; provisioned with autoscaling if patterns are steady.
  * **Enhanced fan-out** costs more → only enable if needed.
  * **Batching** writes to reduce API calls.
  * **Compression** before sending data.
  * **Lambda consumers** can use parallelization factor instead of just adding shards.

  👉 Interview answer:

  > “If Kinesis costs spiked, I’d first check if we’re over-provisioning shards and look into using on-demand mode if traffic is unpredictable. I’d also explore batching and compression to reduce request volume, and make sure enhanced fan-out is only enabled where absolutely necessary.”
  >

  Batching is something we did also to to help the amount of calls data we would get. we would leave the wind open for a certain amount of time to allow it time to called as much as it can before processing. this did help with cutting down on cost and help with the overload of logs in cloudwatch.

👉 They’ll be testing: security, scalability, and cost tradeoffs.

---

## 🔹 AI-Powered Chatbot (Project 2)

**Likely Questions:**

* *How did you integrate Bedrock into your Lex bot? What patterns did you use for grounding responses?*

  * i tied in to the buit in intent in lex and told it what agent to use by giving the agent id. that agent was then tied to the knowledge base that we want to be able to answer questions off of

  **1. How did you integrate Bedrock into your Lex bot? What patterns did you use for grounding responses?**

  👉 Your answer is good (Lex intent → Bedrock agent → Knowledge Base). To make it stronger, add  *grounding* :

  * *“We integrated Bedrock by mapping a Lex intent to a Bedrock Agent using the agent ID. The Agent was connected to a Bedrock Knowledge Base (powered by vector embeddings in OpenSearch), which allowed grounding responses on our curated documents. This ensured the chatbot stayed accurate and didn’t hallucinate.”*

  📌 Extra SME point: Mention “guardrails” → *“We also applied Bedrock Guardrails to filter PII and block unsafe content.”*

    For Grounding I set up guardrails to make sure it did not answer anything outside of what the

* *If a user asks the same question 50 times in one hour, how do you optimize response cost/latency?*

  * if useres were asking the same question over and over  within a hour lets say 50 time like you said. i woudl say it would be efficient to set up caching so that the ai sees the question and then just uses the cached response instead of doing a hard request which would take time and cost more money.
* *What’s the difference between Lex + Bedrock vs building a custom RAG pipeline with SageMaker + OpenSearch?*

  * I have no used SageMaker + OpenSearch to create a RAG pipeline but i would think the biggest diffence is that the Sagemaker and Opensearh would be more customizable in every aspect while Lex and Bedrock is almost plug and play so it would be really good for something quick
* *How would you secure sensitive customer data in conversations stored in DynamoDB?

  * i would say that i would use KMS to secure the data in dymanoDB or even possibly put DynamoDB in a VPC to isolate it and not make it available to the public.

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
