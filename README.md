# Terumo Service Search Monolith

This repository, `terumo-core`, contains the backend of the Terumo application.

## Terumo: Contact-Based Image Retrieval Tool for Renal Pathologists

Terumo is a web software that serves as a contact-based image retrieval tool for renal pathologists. It allows users to perform queries using images of renal biopsies of glomeruli and retrieves images with semantic similarities.

At the moment, this API is a monolith that was initially created with the intention of becoming a microservice app. However, it currently functions as a monolith and provides the following features:

- Serving the images saved in the database
- Managing metadata of the collection of images saved in the database
- Performing content-based image retrieval, including similarity calculations and the implementation of machine learning models

This API implements 6 EfficientNet-B0 binary models, with each model was trained to detect a specific type of renal lesion and extract semantic attributes used for calculating similarity among the images in the database. Additional models for extracting embeddings to aid in the search for similar images will be implemented in the future. The API currently supports the following renal lesion models:

- Normal glomeruli
- Hypercellularity
- Sclerosis
- Membranous
- Podocytopathy
- Crescent

## Prerequisites

Before proceeding with the installation, ensure that you have the following prerequisites installed on your machine:

1. Docker: Visit the [official Docker website](https://docs.docker.com/get-docker/) for instructions on how to install Docker on your specific operating system.
2. Docker Compose: Refer to the [official Docker Compose documentation](https://docs.docker.com/compose/install/) for installation instructions.
    ```
    curl -SL https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    ```
3. Cytomine: Cytomine is a collaborative web platform designed for the analysis of extensive biomedical images and semi-automatic processing of large image collections through machine learning algorithms. It operates as an open-source RESTful web platform, utilizing Docker containers to encapsulate multiple services. Terumo Software integrates Cytomine as a foundational component, particularly in the management of image collections. Refer to the [Install Community Edition Legacy Doc](https://doc.cytomine.org/admin-guide/legacy/legacy-install#install-community-edition-legacy) for installation instructions.
4. Clone or download the Terumo DevOps repository, which contains essential files like Docker Compose and .env files required to launch the application.

# Frontend - Terumo Web

To run the application's frontend, follow these steps:

1. Clone the repository:  [Terumo-web](https://github.com/Terumo-App/terumo-web).
2. Make sure your are in the `main` branch.
3. Run `npm install` to install the necessary libraries.
4. Execute `npm run start` to launch the application.

# Running Backend Applications

To ensure the complete functionality of the Terumo application, the following components need to be running:

- Miulvas vector database
- RabbitMQ
- Celery worker

## Getting Started

1. Clone the repository.
2. Checkout to the `main` branch.
3. Ensure that Python version `3.10.4` is being used in this project.
4. Install Pipenv globally using `pip install pipenv`.
5. Run either `pipenv sync` or `pipenv install` to create a virtual environment and install all the required libraries listed in the `Pipfile` and `Pipfile.lock` files.
6. Activate the virtual environment with `pipenv shell`.

## Configure Cytomine Credentials

- Create an admin user in Cytomine.
- Modify the following attributes in the `./src/.env.test` file:

    ```bash
    PUBLIC_KEY={{admin_user_public_key}}
    PRIVATE_KEY={{admin_user_private_key}}
    HOST={{cytomine_host}}
    ```

## Running the Application

Use the command `python src/main.py` to run the application.

For simultaneous functionality, it is recommended to use Docker Compose to start the components in containers. You can comment out the section responsible for starting the Terumo-core API in the `docker-compose.yml` file and manually start it by running the command `sh run.sh`. Alternatively, use the command `sh reset.sh` to clear Miulvas data and rebuild the code, creating a new container.
To run the application, follow these steps:

In order to access the Swagger API Documentation go to: `http://localhost:5000/docs`

### Development Process:
   - Automating tests with task py.
   >  In order to automate process we are using taskpy. You can check the tasks available using the  command. 
    ```bash
    task -l
    ```
   - Cleaning up the repository with Make.
   ```bash
   make clean
   ```
   - Installing libraries for different environments.
   ```bash
   pipenv install requests
   
   # Dev dependencies
   pipenv install --dev pytest
   pipenv install --dev pytest-cov 
   pipenv install --dev blue # PEP8 Formater
   pipenv install --dev isort # import sorting
   pipenv install --dev taskipy # automation scripting
   pipenv install --dev safety

   pipenv install celery[redis]
   
   pipenv install --dev safety pytest pytest-cov blue isort taskipy
   ```
   - Saving libraries in requirements.
   ```bash
   pipenv requirements > api/requirements.txt
   pipenv requirements --dev-only > requirements.txt
   pipenv requirements --dev > dev-requirements.txt
   ```
   - Running unit tests
   ```bash
   task test 
   ```  
   - Generating code coverage report
   ```bash
   task post_test 
   ```
   - Running linter
   ```bash
   task lintr 
   ```
   - Checking libs vulnerabilities
   ```bash
   pipenv check
   ```   


   
Please refer to the specific sections in this repository for detailed instructions on each step.

## Conclusion

You are now familiar with the Terumo Service Search Monolith repository. This backend API, implemented in Python, provides functionalities for serving images, managing metadata, and performing content-based image retrieval for renal pathologists. Follow the provided instructions to set up, run, and develop the application according to your requirements.





