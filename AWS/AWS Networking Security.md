# 🔒 Networking Security in AWS

## 1. **Why Networking Security Matters**

Networking is the backbone of AWS infrastructure. If networking is insecure:

* Anyone could reach sensitive databases.
* Applications may be exposed to the public internet unintentionally.
* Attackers could perform lateral movement once inside.

So, AWS provides **multiple layers of defense-in-depth** — from **VPC isolation** to  **firewalls, monitoring, encryption in transit, and private access** .

---

## 2. **Core Building Block: VPC (Virtual Private Cloud)**

Think of a VPC as your own private data center in AWS.

### Key Security Concepts in VPC:

* **Subnets** :
  * *Public Subnets* → resources that need internet access (e.g., load balancers).
  * *Private Subnets* → internal resources (e.g., databases, app servers).
* **Route Tables** : Define traffic flow. Keep private subnets without a direct route to the internet.
* **NAT Gateway** : Lets private resources access the internet *outbound only* (e.g., to install patches).
* **VPC Endpoints** : Private connections to AWS services like S3, DynamoDB without leaving the AWS network.

📌  **Best Practice** : Place databases in  **private subnets only** , accessed through application layers, not directly from the internet.

---

## 3. **Firewalls in AWS**

### a) **Security Groups (SGs)**

* Instance-level firewalls.
* *Stateful* : If you allow inbound, return traffic is automatically allowed.
* Example: Only allow HTTPS (443) from the load balancer to an EC2.

### b) **Network ACLs (NACLs)**

* Subnet-level firewalls.
* *Stateless* : Need to explicitly allow both inbound and outbound rules.
* Often used for extra layer of security (e.g., block entire IP ranges).

📌  **Best Practice** :

* SGs for fine-grained control (application-level).
* NACLs for coarse subnet-level restrictions.

---

## 4. **Encryption in Transit**

Protects data moving across networks.

* **TLS (SSL) Certificates** with **AWS Certificate Manager (ACM)** for HTTPS.
* **ELB + ACM** for terminating HTTPS at the load balancer.
* **VPC Traffic Encryption** :
* VPC Peering: Encrypted if services enforce TLS.
* Transit Gateway + VPN: IPsec encryption for hybrid cloud.
* **AWS PrivateLink** : Private service-to-service communication inside AWS without traversing the internet.

📌  **Best Practice** : Enforce HTTPS-only for apps. For APIs, use  **API Gateway + ACM TLS** .

---

## 5. **Hybrid Networking & VPN**

If your company connects on-prem → AWS:

* **Site-to-Site VPN** : IPsec tunnels from data center to AWS VPC.
* **AWS Direct Connect (DX)** : Private, dedicated fiber connection (for low latency + compliance).
* **Transit Gateway (TGW)** : Hub-and-spoke architecture to connect multiple VPCs and on-prem.

📌 Financial/medical orgs often use **DX + VPN** for redundancy and compliance.

---

## 6. **DDoS Protection**

* **AWS Shield Standard** : Always-on protection against common DDoS.
* **AWS Shield Advanced** : Paid, extra protection, 24/7 SOC support.
* **WAF (Web Application Firewall)** :
* Protects apps at HTTP(S) layer.
* Can block SQL injection, XSS, bots.
* Integrates with CloudFront & ALB.

📌  **Best Practice** : Put **CloudFront (CDN) + WAF** in front of public apps.

---

## 7. **Zero Trust & Identity-Aware Access**

Instead of relying on network location (e.g., inside the VPC = trusted), enforce  **least-privilege and identity-based controls** .

* **IAM Policies** : Who can access what service.
* **VPC Endpoint Policies** : Restrict which IAM principals can use the endpoint.
* **Service Control Policies (SCPs)** in AWS Organizations for guardrails.

---

## 8. **Monitoring & Logging for Security**

* **VPC Flow Logs** : Capture network traffic (who’s talking to who). Store in S3/CloudWatch.
* **CloudTrail** : API logging — who changed a security group, who opened a port, etc.
* **GuardDuty** : Threat detection for unusual traffic (e.g., port scanning, crypto mining).
* **Inspector + Security Hub** : Vulnerability management + central dashboard.

📌  **Best Practice** : Always enable **VPC Flow Logs + GuardDuty** in production.

---

## 9. **Case Study Example: Financial System**

Imagine a financial system handling credit card transactions:

* **Frontend** :
* Deployed in public subnet behind  **ALB (HTTPS + WAF)** .
* ACM-managed TLS certificates.
* **Backend APIs** :
* Private subnets, only reachable from ALB.
* Enforce IAM auth for Lambda or EKS services.
* **Database (RDS or Aurora)** :
* In  **private subnet** , no internet route.
* Encrypted with  **KMS (at rest)** .
* Access restricted by **SGs** only from app servers.
* **Data Transfer** :
* All logs encrypted in S3.
* Use VPC Endpoint → private S3 access (no public internet).
* **Monitoring** :
* GuardDuty monitors anomalies.
* CloudTrail logs all IAM activity.
* SIEM pipeline built from CloudWatch logs.

---

## 10. **Best Practices Recap**

✅ Use **private subnets** for sensitive resources.

✅ Apply **least privilege** with SGs + IAM.

✅ Encrypt **data in transit (TLS)** +  **at rest (KMS)** .

✅ Enable **logging and monitoring** (Flow Logs, GuardDuty).

✅ Use **WAF + Shield** for internet-facing apps.

✅ Prefer **VPC Endpoints** over public internet access.

✅ Segment workloads across VPCs and accounts for isolation.

---

👉 That’s the  **full foundation of Networking Security in AWS** .

It ties together  **VPC design, firewalls, encryption, hybrid connectivity, DDoS protection, monitoring, and least privilege** .
