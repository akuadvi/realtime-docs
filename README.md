# 📄 Realtime Docs  

A **Google Docs–like collaborative editing platform** built with **FastAPI, PostgreSQL, Redis, and Kafka**.  
Supports **real-time collaboration**, **document sharing**, and **audit logging** : All following industry best practices with Dockerized setup and CI/CD.  

---

## ✨ Features  

- 🔐 **Authentication** – Secure signup/login with JWT & bcrypt password hashing  
- 📄 **Document CRUD** – Create, read, update, delete documents  
- 🤝 **Collaboration** – Share docs with collaborators, role based permissions  
- ⚡ **Real-time Editing** – WebSockets + Redis Pub/Sub for live updates  
- 📡 **Event Streaming** – Kafka based audit log for all edits  
- 🔍 **Search** – Full-text search with PostgreSQL  
- 🧪 **Testing** – Unit + integration tests with Pytest  
- 📈 **Monitoring** – Prometheus + Grafana dashboards for metrics  
- 🐳 **Deployment** – Docker & Docker Compose for local dev and staging  

---

## 🏗 Architecture  

```mermaid
graph TD;
    Client[Web/CLI Client] --> API[FastAPI Backend];
    API -->|CRUD| Postgres[(PostgreSQL)];
    API -->|Live Updates| Redis[(Redis Pub/Sub)];
    API -->|Events| Kafka[(Kafka Broker)];
    Kafka --> Audit[Audit Log Service];
    Audit --> Postgres;
    Monitoring[Prometheus + Grafana] --> API;
 
