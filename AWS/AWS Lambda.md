![1759334664872](image/AWSLambda/1759334664872.png)

# Amazon Lambda

---

## 1. **What is AWS Lambda?**

* **Serverless compute service** : You run code without managing servers.
* Event-driven: Lambda executes in response to triggers (e.g., API Gateway request, S3 file upload, DynamoDB stream, EventBridge event).
* Automatically scales based on requests.

👉 **Think of Lambda as:**

*"I upload my function, set a trigger, and AWS handles provisioning, scaling, patching, and HA for me."*

---

## 2. **Execution Model**

1. **Invocation:**
   * Request comes in (API call, S3 event, etc.).
   * AWS finds an existing execution environment (“warm”) or spins up a new one (“cold”).
2. **Execution Environment:**
   * Isolated container with a runtime (Python, Node.js, Java, etc.).
   * Environment can be reused (warm start).
3. **Timeout:**
   * Max execution time =  **15 minutes** .

---

## 3. **Cold Starts vs Warm Starts**

* **Cold Start:**
  * Happens when AWS creates a new container.
  * Adds extra latency (100ms–1s).
  * Longer if:
    * Function in a **VPC** (extra ENI setup).
    * Function package is  **large** .
    * Runtime is **heavy** (Java/.NET slower than Python/Node).
* **Warm Start:**
  * Subsequent calls reuse same container.
  * Near-instant execution.

**Mitigation Strategies:**

* **Provisioned Concurrency** : Pre-warm containers.
* **Smaller packages** : Minimize dependencies.
* **Right runtime** : Python/Node faster than Java/.NET for cold starts.
* **Avoid unnecessary VPC attachments** unless needed (e.g., RDS).

👉 **Interview soundbite:**

*"For latency-sensitive workloads, I reduce cold start impact with provisioned concurrency and lightweight packaging. For batch or background jobs, I accept cold starts to save cost."*

---

## 4. **Cost & Performance Tradeoffs**

Lambda pricing = **Requests + Duration × Memory**

* $0.20 per 1M requests.
* Duration billed in ms.
* Memory: 128 MB – 10 GB.

⚖️ **Tradeoff:**

* More memory → higher cost per ms, but more CPU/network throughput.
* Sometimes increasing memory **reduces overall cost** because code executes faster.

👉 **Interview example:**

*"I once cut Lambda cost 30% by doubling the memory — it reduced execution time so much that overall cost went down."*

---

## 5. **Integrations (Common Triggers)**

* **API Gateway** → REST/HTTP API.
* **S3** → Run Lambda on file upload.
* **DynamoDB Streams** → React to table changes.
* **SQS/SNS** → Event-driven processing.
* **EventBridge** → Scheduled tasks / event routing.
* **Step Functions** → Orchestration of multiple Lambdas.

---

## 6. **Best Practices**

### Architecture

* Keep Lambdas  **single-purpose & small** .
* Prefer **event-driven design** (SNS → multiple consumers).
* Use **Step Functions** for orchestration, not nested Lambda calls.

### Performance

* Optimize package size (Lambda layers help).
* Cache connections (e.g., DB client) outside the handler function.
* Use async processing for long tasks (e.g., SQS, Step Functions).

### Security

* **Least privilege IAM roles** .
* Encrypt data (KMS, environment variables).
* Avoid hardcoding credentials.

### Observability

* Use **CloudWatch Logs** + metrics.
* Use **X-Ray** for tracing.

---

## 7. **Common Pitfalls & Solutions**

| Pitfall                        | Solution                                           |
| ------------------------------ | -------------------------------------------------- |
| Cold starts cause latency      | Use provisioned concurrency                        |
| Function hitting DB repeatedly | Use DB connection pooling, RDS Proxy               |
| Large deployment package       | Use Lambda Layers or slim dependencies             |
| Lambda timeout (default 3s)    | Increase timeout (up to 15 min), redesign workload |
| Vendor lock-in                 | Use container images (ECR) for portability         |

---

## 8. **Example Architectures Using Lambda**

1. **File Processing:**
   * User uploads → S3 triggers Lambda → process file → store in DynamoDB.
2. **API Backend:**
   * API Gateway → Lambda → DynamoDB/RDS → Response.
3. **ETL Pipeline:**
   * EventBridge → Lambda → Transform data → Load into Redshift/S3.

---

## 9. **When NOT to Use Lambda**

* Long-running tasks > 15 min.
* Heavy compute (better on ECS/EKS/Fargate).
* High request rates with extremely low latency SLAs (API Gateway + Lambda adds 10–50ms overhead).
* When you need full OS-level control (use EC2).
