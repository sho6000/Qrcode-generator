
Welcome to  Sunbird-Spark! Before we start building, we need to ensure your "digital foundation" is ready. Think of this as choosing the right plot of land and utilities before building a house.

---

Sunbird-Spark doesn't run on your personal laptop. Instead, you rent **Virtual Machines (VMs)** from a cloud provider like Azure, AWS, or Google Cloud.

In the world of Sunbird, we call these VMs **Nodes**.
* **The Kitchen (Node 1):** Handles the "cooking"—this includes your 4 primary databases (YugabyteDB, Redis, Elasticsearch, JanusGraph) and background processors.
* **The Front-of-House (Node 2):** Handles the "customers"—this includes the 14 application services, web APIs, and user traffic.

Together, these form a **Kubernetes cluster** that manages all the software automatically.

---

## 1. What You Need to Rent
To keep things simple, you only need **two powerful machines** to run the entire base platform.

| Resource | Specification | Why it matters |
| :--- | :--- | :--- |
| **Quantity** | **2 Nodes** | To balance the workload and ensure stability. |
| **Azure VM Type** | **Standard_B16as_v2** | The recommended balance of power and cost. |
| **Total vCPU** | **32 vCPU** (16 per node) | The "brain power" to handle multiple tasks at once. |
| **Total RAM** | **128 GB** (64 GB per node) | The "short-term memory" to keep things running fast. |
| **Storage (Disk)** | **~219 GB** | The "filing cabinet" where all your data is kept. |

---

## 2. What’s Inside the Box?
When you install  Sunbird-Spark, these two machines will automatically start running several "departments":

* **Databases (4):** Stores your users, courses, and content.
* **Background Workers (5):** Flink jobs that handle certificates, notifications, and data cleanup.
* **Application Services (14):** The actual web services and APIs your users interact with.
* **Monitoring Tools (4):** Dashboards like Grafana and Prometheus to watch your system's health.

---

## 3. Where Does the Storage Go?
Data takes up space. Here is the breakdown of how that **~219 GB** of storage is distributed:

* **Main Database (YugabyteDB):** **120 GB** — The heart of your platform data.
* **Search Engine (Elasticsearch):** **25 GB** — Helps users find content instantly.
* **System Metrics (Prometheus):** **25 GB** — Stores performance history.
* **Application Logs (Loki):** **25 GB** — Records what happened in the system.
* **Message Queue (Kafka):** **24 GB** — The "postal service" for background jobs.

> **Note:** If you choose to enable the optional **Redis** session cache, you will need an additional **25 GB** of disk space.

---

## 4. Adding "Extra Features" (Add-ons)
Sunbird allows you to turn on extra features like **Discussion Forums** or **QR Code (DIAL)** support. 

**The best part?** You don't need to buy more machines. The two nodes you already have have plenty of "room to grow".

| Scenario | CPU Used (Reserved) | RAM Used (Reserved) |
| :--- | :--- | :--- |
| **Standard Setup** | ~21 Cores | ~40 GB |
| **Setup + All Add-ons** | **~22 Cores** | **~43 GB** |
| **Total Capacity** | **32 Cores** | **128 GB** |

✅ **Summary:** Even with every single feature turned on, you are only using about **43 GB** of your **128 GB** RAM. You
