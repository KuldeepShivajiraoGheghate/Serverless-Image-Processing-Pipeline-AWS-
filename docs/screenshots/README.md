# 📸 Project Screenshots

Visual documentation of the Serverless Image Processing Pipeline.

---

## 📥 S3 Input Bucket
![S3 Input Bucket](s3-input-bucket.png)
> Input bucket containing the original uploaded image (503.7 KB)

---

## 📤 S3 Output Bucket
![S3 Output Bucket](s3-output-bucket.png)
> Output bucket showing the processed image (14.1 KB) — 97% size reduction!

---

## ⚡ Lambda Function Overview
![Lambda Function](lambda-function.png)
> Lambda function with S3 trigger connected

---

## 🔧 Lambda Runtime & Layers
![Lambda Layers](lambda-layers.png)
> Runtime settings showing Python 3.14 and Pillow layer attached

---

## 🔑 IAM Permissions
![IAM Permissions](lambda-iam-permissions.png)
> IAM Role with AmazonS3FullAccess policy attached

---

## 📦 Pillow Layer Details
![Pillow Layer](lambda-pillow-layer.png)
> Custom Pillow layer (version 2) for Linux-compatible image processing
