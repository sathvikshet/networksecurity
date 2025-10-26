🧠 Network Security Threat Detection (End-to-End ML Project)

An end-to-end Network Security Threat Detection System that automates the full ML lifecycle — from data ingestion to model deployment — using FastAPI, MongoDB, AWS EC2, and CI/CD principles.

🚀 Project Overview

This project predicts network security threats (e.g., phishing or malicious activity) using machine learning.
It includes an automated training pipeline, real-time prediction API, data validation, transformation, and AWS synchronization.

🧩 Key Features

1.Fully automated ML pipeline

  Data ingestion → validation → transformation → model training

2.FastAPI web service for model training and prediction

3.MongoDB integration for data storage and ingestion

4.AWS S3 synchronization for artifact and model versioning

5.Dockerized setup for seamless deployment

6.MLflow & DagsHub ready for model tracking

7.Logging & Exception handling built from scratch

MACHINE LEARNING PIPELINE:

Data Ingestion--> 
Data Validation (schema check + drift detection)-->
Data Transformation (scaling, encoding)-->Model Training (hyperparameter tuning)
    ↓
Model Evaluation (f1, precision, recall)
    ↓
Model Saving + AWS S3 Sync
    ↓
FastAPI Prediction Endpoint
