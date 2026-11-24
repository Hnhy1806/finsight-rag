# FinSight RAG — Financial Report RAG Analyst

A retrieval-augmented generation (RAG) system that answers questions about
financial reports with page-level citations, and says so when the evidence
isn't there.

## Status

Phase 1: project setup.

## Data

- Microsoft Form 10-K, fiscal year ended June 30, 2026 (download from Microsoft
  Investor Relations; place in `data/raw/`). PDFs are not committed to the repo.

## Setup

    python3.13 -m venv .fin
    source .fin/bin/activate
    pip install -r requirements.txt
    pip install -e .
    cp .env.example .env
