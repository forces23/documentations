# 📌 Interview Fundamentals Cheat Sheet

## 1. **Time Complexity (Big O Notation)**

* **O(1)** → Constant time (hash lookup, array index access).
* **O(log n)** → Logarithmic (binary search, balanced trees).
* **O(n)** → Linear (loop through array).
* **O(n log n)** → Common in efficient sorts (merge sort, quicksort avg).
* **O(n²)** → Nested loops (bubble sort, insertion sort worst).

  👉 **Tip:** In interviews, aim for **O(n)** or better unless justified.

---

## 2. **POST vs PUT (HTTP Methods)**

* **POST** → Create a new resource.
  * Example: `POST /users` creates a *new* user.
  * Non-idempotent (multiple POSTs create multiple entries).
* **PUT** → Create **or update** a resource at a known URI.
  * Example: `PUT /users/123` updates user 123.
  * Idempotent (repeated PUTs produce the same result).

---

## 3. **Database Index**

* **Index** = A lookup table for the DB to speed up queries.
* **Speeds up** : SELECTs and WHERE filters.
* **Slows down** : INSERT/UPDATE/DELETE (because index must update).
* **Types** :
* **B-Tree Index** → Most common, good for ranges.
* **Hash Index** → Faster equality lookup, not good for ranges.

  👉 Use indexes  **sparingly** —too many = performance hit.

---

## 4. **Recursion**

* Function that calls itself until a base condition is met.
* **Example:** Factorial:

  <pre class="overflow-visible!" data-start="1716" data-end="1790"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>factorial</span><span>(n) = </span><span>1</span><span></span><span>if</span><span> n == </span><span>0</span><span>
  </span><span>factorial</span><span>(n) = n * </span><span>factorial</span><span>(n</span><span>-1</span><span>)
  </span></span></code></div></div></pre>
* **Pros:** Elegant for problems like trees, divide & conquer.
* **Cons:** Risk of stack overflow; sometimes slower than iteration.

  👉 Tail recursion can optimize memory (if language supports).

---

## 5. **Virtualization vs Containers**

* **Virtualization** → Runs multiple OSes on one machine using a  **hypervisor** .
  * Example: VMware, VirtualBox.
  * Heavy (entire OS for each VM).
* **Containers** → Lightweight, share host OS kernel, isolate apps.
  * Example: Docker, Kubernetes.
  * Faster, less resource-intensive, portable.

    👉 Cloud uses containers heavily (microservices).

---

## 6. **API Fundamentals**

* **Idempotency** → Same request multiple times = same result (PUT, DELETE).
* **Statelessness** → Each request is independent; no session memory.
* **REST vs RPC** :
* REST: Resource-based (`/users/123`).
* RPC: Action-based (`getUser(123)`).

---

## 7. **Caching**

* **Purpose:** Reduce DB load + latency.
* **Types:**

  * **Client-side** : Browser cache.
  * **Server-side** : Redis, Memcached.
  * **CDN caching** : Cloudflare, Akamai.

  👉 Rule: Cache **read-heavy, rarely updated** data.

---

## 8. **Concurrency vs Parallelism**

* **Concurrency** = Handling multiple tasks by switching between them (async).
* **Parallelism** = Doing multiple tasks at the same time (multi-core).

  👉 Concurrency ≠ parallelism, but they often overlap.

---

## 9. **Virtual Memory & Paging (OS basics)**

* **Virtual Memory** → Lets programs think they have huge memory.
* **Paging** → Breaks memory into fixed-size chunks (pages).
* **Swapping** → Moves inactive pages to disk when RAM is full.

  👉 Key to understanding system performance + containers.

---

## 10. **Common System Design Trade-offs**

* **CAP Theorem** (for distributed systems):
  * **C**onsistency, **A**vailability, **P**artition tolerance → can only choose 2.
* **Scaling** :
* Vertical = Bigger machine.
* Horizontal = More machines.
* **Load balancing** spreads traffic across servers.
