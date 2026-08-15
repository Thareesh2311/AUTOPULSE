# AutoPulse
## Sentiment Analysis of Used Car Reviews using NLP & Deep Learning

<div align="center">

### Turning Customer Reviews into Actionable Insights with AI

An intelligent NLP and Deep Learning system that analyses customer reviews from **Cars24** and **Spinny** to understand customer sentiment, identify key concerns, and provide business insights through interactive visualisations.
</div>
# Overview
Online used-car marketplaces generate thousands of customer reviews every day. These reviews contain valuable information about customer satisfaction, service quality, pricing, and vehicle condition. However, manually analysing such a large volume of feedback is inefficient and time-consuming.

**AutoPulse** automates this process using **Natural Language Processing (NLP)** and **Deep Learning**. It collects customer reviews, preprocesses textual data, classifies sentiment, performs aspect-based sentiment analysis, and presents insights through interactive dashboards.

The system classifies reviews into:
* Positive
* Neutral
* Negative
---

# Problem Statement

Customers rely heavily on online reviews before purchasing a used car. Since these platforms receive thousands of reviews, manually identifying customer satisfaction and common issues is difficult.

An automated sentiment analysis system is needed to:

* Analyse large-scale customer feedback
* Identify positive and negative experiences
* Discover common customer concerns
* Support better business decisions

---
# Objectives

* Collect customer reviews from Cars24 and Spinny
* Create an integrated review dataset
* Clean and preprocess textual data
* Build Deep Learning models for sentiment classification
* Perform Aspect-Based Sentiment Analysis (ABSA)
* Compare customer satisfaction across platforms
* Visualise insights using interactive dashboards

---
#  Features

### Data Collection

* Cars24 reviews
* Spinny reviews

### Data Preprocessing

* Duplicate removal
* Missing value handling
* URL removal
* Emoji removal
* Punctuation removal
* Number removal
* Text normalisation
* Lowercase conversion
* Tokenisation
* Stop-word removal
* Lemmatisation


### Aspect-Based Sentiment Analysis

# Project Workflow

```text
Customer Reviews
        │
        ▼
Data Collection
        │
        ▼
Data Integration
        │
        ▼
Data Cleaning
        │
        ▼
Text Preprocessing
        │
        ▼
Feature Extraction
(TF-IDF / BERT Embeddings)
        │
        ▼
Deep Learning Models
(LSTM / Bi-LSTM / BERT)
        │
        ▼
Sentiment Classification
        │
        ▼
Aspect-Based Sentiment Analysis
        │
        ▼
Dashboard & Visualisation
        │
        ▼
Business Insights
```

---

# Tech Stack

## Programming Language

* Python

## Development Tools

* Jupyter Notebook
* Visual Studio Code

## Data Processing

* Pandas
* NumPy

## Natural Language Processing

* NLTK
* spaCy
* Regular Expressions (Regex)

## Machine Learning

* Scikit-learn

## Deep Learning

* TensorFlow
* Keras
* Hugging Face Transformers (BERT)

## Data Visualisation

* Matplotlib
* Seaborn
* Plotly

---

# NLP Pipeline

```text
Raw Reviews
      │
      ▼
Lowercase Conversion
      │
      ▼
Text Cleaning
      │
      ▼
Tokenisation
      │
      ▼
Stop-word Removal
      │
      ▼
Lemmatisation
      │
      ▼
Feature Extraction
      │
      ▼
Deep Learning Model
```

---

# Deep Learning Models

### LSTM

* Captures long-term dependencies in text
* Suitable for sequential sentiment analysis

### Bi-LSTM

* Processes text in both forward and backward directions
* Provides better contextual understanding

### BERT

* Transformer-based language model
* Produces contextual embeddings
* Delivers state-of-the-art sentiment classification performance

---
#  Project Structure

```text
AutoPulse/
│
├── Data/
│   ├── Raw/
│   ├── Integrated/
│   ├── Cleaned/
│   └── Processed/
│
├── Notebooks/
│   ├── Phase1_DataCollection.ipynb
│   ├── Phase2_DataIntegration.ipynb
│   ├── Phase3_DataCleaning.ipynb
│   ├── Phase4_TextPreprocessing.ipynb
│   ├── Phase5_FeatureExtraction.ipynb
│   ├── Phase6_ModelTraining.ipynb
│   ├── Phase7_ModelEvaluation.ipynb
│   └── Dashboard.ipynb
│
├── Models/
│   ├── LSTM/
│   ├── BiLSTM/
│   └── BERT/
│
├── Dashboard/
├── Images/
├── README.md
└── requirements.txt
```

---

# Project Status

| Phase                 | Status        |
| --------------------- | ------------- |
| Data Collection       | ✅ Completed   |
| Data Integration      | ✅ Completed   |
| Data Cleaning         | ✅ Completed   |
| Text Preprocessing    | ✅ Completed   |
| Feature Extraction    | ✅ Completed   |
| Model Training        | ✅ Completed   |
| Model Evaluation      | ✅ Completed   |
| Dashboard Development | ✅ Completed   |
| Deployment            | ✅ Completed   |

---

# Future Scope

* Real-time sentiment analysis
* Multi-language support
* Fake review detection
* Explainable AI (XAI)
* Live dashboard updates
* Recommendation system
* Mobile application

---

# Expected Outcomes

* Automatically classify customer reviews into Positive, Neutral, and Negative sentiments.
* Identify customer opinions for specific service aspects.
* Compare customer satisfaction between Cars24 and Spinny.
* Generate meaningful business insights through interactive dashboards.
* Support customers in making informed purchasing decisions and help companies improve service quality.

---

# Authors

**AutoPulse – Sentiment Analysis of Used Car Reviews using NLP & Deep Learning**

Developed using:

* Python
* Natural Language Processing (NLP)
* Deep Learning (LSTM, Bi-LSTM, BERT)
* TensorFlow & Keras
* Hugging Face Transformers
* Data Visualisation

---

<div align="center">

⭐ **If you found this project helpful, consider giving it a Star!**

*"Turning Customer Opinions into Actionable Insights with AI."* 

</div>
