**2-Minute DevOps Project Explanation**

In one of my hands-on DevOps projects, I built a microservices-based order and payment system and automated the entire deployment lifecycle using modern DevOps tools.

The application consists of two Flask-based microservices: an Order Service and a Payment Service. The Order Service receives order requests from the client and internally communicates with the Payment Service to process the payment. This helped me understand service-to-service communication in a microservices architecture.

I containerized both services using Docker and used Docker Compose to manage multi-container deployment and networking. This allowed both services to communicate through a dedicated bridge network while exposing APIs on ports 5000 and 5001.

For infrastructure provisioning, I used Terraform to create AWS EC2 instances for Jenkins and the application server. I structured the Terraform code using provider, variables, and main configuration files, and configured a remote backend using **Amazon S3** with **DynamoDB** for state locking. This ensures safe and collaborative infrastructure management.

For CI/CD automation, I installed Jenkins on the EC2 instance and configured a pipeline that pulls the source code from GitHub, builds Docker images for both services, pushes them to Docker Hub, and deploys them on the application EC2 instance.

During deployment, Jenkins connects to the server via SSH, pulls the latest images, and runs the containers using Docker networking. I also implemented container health checks and dependency management so that the Order Service only starts once the Payment Service becomes healthy.

Through this project, I gained practical experience with infrastructure as code, containerization, CI/CD pipelines, and automated deployments in a cloud environment.

In the future, I plan to extend this architecture by deploying the services on Kubernetes, adding monitoring using Prometheus and Grafana, and introducing Kafka for event-driven communication.
