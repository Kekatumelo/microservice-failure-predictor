# Microservice Failure Prediction & Early-Warning System

**Status:** Work in Progress  
**Primary Language:** Python  
**Project Type:** Distributed Systems / Backend Engineering / Machine Learning

## 1. Project Overview

I am developing a local microservice-based application to investigate how telemetry data can be used to identify patterns associated with impending microservice failures.

The project aims to bring together several areas of computer science and applied mathematics:

- Backend development and REST APIs
- Microservice architecture and inter-service communication
- Database management
- Distributed systems and observability
- Data analysis and machine learning
- Predictive modelling and early-warning systems

The intended application will consist of multiple independent services, including an Order Service, Inventory Service and Payment Service.

These services will communicate through HTTP requests. Their behaviour will be monitored using observability tools, with the resulting telemetry used to investigate whether machine learning models can identify conditions that precede service failures.

The project is being developed locally, with an emphasis on understanding the underlying engineering concepts rather than simply integrating technologies without understanding their purpose.

## 2. What I Am Trying to Achieve

The central question behind this project is:

**Can historical operational telemetry be used to identify warning signs of microservice failures before those failures occur?**

For example, increasing response latency, error rates, memory consumption or unusual request patterns may indicate deteriorating service performance.

I want to investigate how these measurements behave under normal operating conditions and simulated failure scenarios, and whether their patterns can be used to train a predictive model.

The intended final system will:

1. Run multiple interconnected microservices.
2. Collect operational telemetry from those services.
3. Store and analyse historical telemetry.
4. Simulate different failure scenarios.
5. Develop and evaluate machine learning models for failure prediction.
6. Produce early warnings when observed behaviour resembles patterns associated with impending failures.

The goal is not simply to build a working application, but to understand how different engineering disciplines contribute to building a reliable, observable and intelligent software system.

## 3. Current Implementation

Development is currently focused on the Order Service.

I chose to build the services incrementally, starting with the fundamentals of HTTP request handling, API development, data validation and CRUD operations.

### Order Service

Implemented functionality:

- [x] FastAPI application initialisation.
- [x] Pydantic data model for order validation.
- [x] `POST /orders` – create an order.
- [x] `GET /orders/{order_id}` – retrieve an order.
- [x] `PUT /orders/{order_id}` – update an existing order.
- [x] `DELETE /orders/{order_id}` – delete an order.
- [x] Automatic order ID generation.
- [x] Basic handling of nonexistent order IDs using HTTP 404 responses.
- [x] `GET /health/` – basic service health endpoint.

### Current storage implementation

Orders are currently stored in an in-memory Python dictionary.

This was an intentional starting point: it allowed me to understand the application logic and CRUD operations before introducing database integration.

The current implementation is temporary. Data is lost when the application process restarts.

PostgreSQL integration is planned as the next development step.

## 4. Concepts and Skills Applied So Far

I am using this project to move beyond theoretical understanding and apply programming and computer science concepts to a practical engineering problem.

### Python and object-oriented programming

- Python functions, parameters and return values.
- Dictionaries and data structures.
- Classes and objects.
- Type hints.
- Exception handling.
- Working with external packages and imports.
- Understanding how application logic is organised.

### HTTP and REST APIs

- Client-server communication.
- HTTP methods: GET, POST, PUT and DELETE.
- API endpoints and path parameters.
- Request bodies and JSON.
- HTTP response codes.
- Request validation and response handling.

### FastAPI and Pydantic

- Defining API routes using decorators.
- Receiving and validating request bodies.
- Defining data models using Pydantic's `BaseModel`.
- Handling invalid requests and missing resources.
- Returning structured responses.

### Software engineering

- Breaking a larger system into smaller components.
- Building functionality incrementally.
- Understanding the responsibilities of individual services.
- Debugging and testing application behaviour.
- Using documentation to learn unfamiliar technologies.

## 5. Tools and Technologies

### Currently used

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| FastAPI | Building REST API endpoints |
| Pydantic | Data modelling and request validation |
| Git | Version control |
| Visual Studio Code | Development environment |
| PowerShell | Running and managing the development environment |
| FastAPI Swagger UI | Exploring and testing API endpoints |

### Planned technologies

| Technology | Intended purpose |
|---|---|
| PostgreSQL | Persistent data storage |
| Docker | Containerisation of individual services |
| OpenTelemetry | Instrumenting applications and collecting telemetry |
| Prometheus | Collecting and storing metrics |
| Python data analysis libraries | Exploring and processing telemetry datasets |
| Scikit-learn | Developing and evaluating predictive models |

These technologies are planned components, not claims of completed implementation.

## 6. Development Roadmap

The project is being developed in stages.

### Stage 1: Individual microservice development

- [x] Initialise the Order Service using FastAPI.
- [x] Implement basic CRUD operations.
- [x] Implement a basic health endpoint.
- [ ] Integrate PostgreSQL.
- [ ] Improve request and response models.
- [ ] Test the service's functionality and error handling.

### Stage 2: Microservice architecture

- [ ] Develop the Inventory Service.
- [ ] Develop the Payment Service.
- [ ] Develop any additional services required by the application.
- [ ] Implement HTTP communication between services.
- [ ] Test service interactions and failure scenarios.

### Stage 3: Containerisation and observability

- [ ] Containerise the services using Docker.
- [ ] Introduce OpenTelemetry instrumentation.
- [ ] Collect request counts, response latency and error rates.
- [ ] Monitor resource utilisation.
- [ ] Configure Prometheus for metrics collection and storage.

### Stage 4: Failure simulation and data collection

- [ ] Introduce controlled failure scenarios.
- [ ] Collect telemetry under normal operating conditions.
- [ ] Collect telemetry during simulated failures.
- [ ] Construct a dataset suitable for exploratory analysis and predictive modelling.

### Stage 5: Predictive modelling

- [ ] Perform exploratory data analysis.
- [ ] Identify potentially useful predictive features.
- [ ] Engineer features from historical telemetry.
- [ ] Train baseline machine learning models.
- [ ] Evaluate model performance.
- [ ] Investigate false positives, false negatives and prediction lead time.

### Stage 6: Early-warning system

- [ ] Integrate the selected predictive model into an early-warning component.
- [ ] Generate warnings when telemetry indicates elevated failure risk.
- [ ] Test the system under different operating conditions.
- [ ] Document the architecture, implementation and findings.

## 7. How I Use AI During Development

I use AI as a learning and development assistant, rather than as a substitute for understanding the implementation.

My approach involves:

- Using AI to clarify unfamiliar programming and software engineering concepts.
- Asking for explanations of documentation, framework behaviour and error messages.
- Using guided questions and feedback to work through implementation problems.
- Writing my own code and asking for corrections without having the entire solution written for me.
- Exploring alternative implementations and understanding their trade-offs.
- Using AI to help break complex engineering problems into smaller, manageable tasks.

For example, while implementing the Order Service, I worked through how FastAPI handles path parameters, request bodies and HTTP methods, how Pydantic validates incoming data, and how Python dictionaries can be used to implement basic resource management.

I aim to understand why an implementation works, not simply obtain code that works.

AI has therefore been part of my learning process, but the objective remains to develop the ability to independently understand, implement, debug and improve software.

## 8. Learning Objectives

This project is also an opportunity to demonstrate my ability to learn unfamiliar technologies and apply them to a practical problem.

I am particularly interested in developing a stronger understanding of:

- Backend and systems engineering.
- Distributed systems and service communication.
- Database design and data management.
- Software reliability and observability.
- Data engineering and telemetry processing.
- Applied mathematics and machine learning.

My academic background in Applied Mathematics and Computer Science provides a foundation for approaching these problems analytically.

I want to strengthen that foundation through practical implementation, experimentation and independent learning.

## 9. Current Project Status

This project is actively being developed.

The Order Service currently supports basic CRUD operations and a simple health endpoint. Data is stored temporarily in memory, and database integration, additional services, observability and predictive modelling remain future milestones.

The repository will be updated as implementation progresses.

**The intended outcome is a working, locally deployed microservice environment with an early-warning component, accompanied by documented engineering decisions, experiments and model evaluation.**