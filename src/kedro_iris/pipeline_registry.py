"""Project pipelines."""
from __future__ import annotations


from kedro.pipeline import Pipeline
from kedro_iris.pipelines import iris_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    return {"__default__": iris_pipeline.create_pipeline()}
