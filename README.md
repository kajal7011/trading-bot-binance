# MLOps Batch Processing Task

## Overview

This project implements a minimal MLOps-style batch pipeline in Python.

It:

* Loads configuration from YAML
* Reads OHLCV data from CSV
* Computes rolling mean on closing price
* Generates binary trading signals
* Outputs structured metrics and logs

---

## Features

* Reproducibility via config + seed
* Observability using logs and metrics
* Deployment-ready with Docker

---

## Run Locally

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

## Docker Usage

```bash
docker build -t mlops-task .
docker run --rm mlops-task
```

---

## Output Files

* `metrics.json` → contains processing metrics
* `run.log` → contains execution logs

---

## Project Structure

```
mlops-task/
├── run.py
├── config.yaml
├── data.csv
├── requirements.txt
├── Dockerfile
├── metrics.json
├── run.log
```

