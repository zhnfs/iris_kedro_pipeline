"""
This is a boilerplate pipeline 'iris_pipeline'
generated using Kedro 0.19.12
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def scale_data(X):
    """Scale the data using StandardScaler"""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

def apply_pca(X_scaled, n_components=2):
    """Apply PCA for dimensionality reduction"""
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    return X_pca

def train_classifier(X_pca, y):
    """Train the classifier and evaluate the accuracy"""
    X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    accuracy = classifier.score(X_test, y_test)
    return accuracy
