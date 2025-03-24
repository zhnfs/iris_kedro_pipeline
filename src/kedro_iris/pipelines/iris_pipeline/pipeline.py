"""
This is a boilerplate pipeline 'iris_pipeline'
generated using Kedro 0.19.12
"""
from kedro.pipeline import Pipeline, node
from .nodes import scale_data, apply_pca, train_classifier  # Import the functions from the nodes.py file

def create_pipeline():
    return Pipeline(
        [
            node(
                func=scale_data,
                inputs="X",  # This is the input dataset for features
                outputs="X_scaled",  # This is the output dataset for scaled features
                name="scaler_node"
            ),
            node(
                func=apply_pca,
                inputs="X_scaled",  # Input: scaled data
                outputs="X_pca",  # Output: data after PCA
                name="pca_node"
            ),
            node(
                func=train_classifier,
                inputs=["X_pca", "y"],  # Input: PCA-transformed features and target variable
                outputs="accuracy",  # Output: Model accuracy
                name="classifier_node"
            )
        ]
    )