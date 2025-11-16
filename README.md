# Heart Disease Prediction System

This project implements a **Heart Disease Prediction System** using machine learning algorithms such as **KNN, SVM, and Decision Tree, Naive Bayes**. The system predicts the likelihood of heart disease based on medical data, achieving up to **99% accuracy**.

---

## 🚀 Features
- Data preprocessing, cleaning, and visualization  
- Model training and evaluation with multiple algorithms  
- Comparison of model performance (KNN, SVM, Decision Tree, Naive Bayes)  
- Basic model serialization with Pickle for reuse  

---

## 📂 Project Structure
```
├── Heart-disease.ipynb        # Jupyter notebook containing code for data preprocessing and all 4 algorithms (KNN, SVM, Decision Tree, Naive bayes)
├── heart.csv                 # Dataset used for training and evaluation
├── heart.pkl                # Saved model file using Pickle
├── heart.py                 # Python script to load and use the Pickle model
└── README.md               # Project documentation
```

---

## Model Performance Comparison

| Model          | Accuracy | Precision | Recall | F1-Score |
|----------------|----------|-----------|--------|----------|
| Decision Tree  | 99.03    | 100.00    | 98.16  | 99.07    |
| KNN            | 88.64    | 92.11     | 85.89  | 88.89    |
| SVM            | 85.39    | 82.07     | 92.64  | 87.03    |
| Naive Bayes    | 84.42    | 84.02     | 87.12  | 85.54    |

---

## 🛠️ Technologies Used
- **Python**  
- **scikit-learn**  
- **Pandas, NumPy**  
- **Matplotlib, Seaborn**  

---

## 📊 Results
- Decision Tree: ~99% accuracy  
- KNN: ~88% accuracy  
- SVM: ~85% accuracy
- Naive bayes: ~84.42 accuracy

---

## 💾 Usage
1. Clone the repository  
   ```bash
   git clone https://github.com/nihajasmine/Heart-Disease-Prediction-System.git
   cd Heart-Disease-Prediction
