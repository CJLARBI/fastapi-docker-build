
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import pandas as pd
import mimetypes
import joblib
import logging
from typing import Dict
import uvicorn

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sepsis-prediction")

# Initialize FastAPI app
app = FastAPI(
    title="Sepsis Prediction API",
    description="An API to predict sepsis based on patient data using various machine learning models.",
    version="1.0.0",
)

# Model paths (these can later be moved to environment variables)
Model_Path = {
    "DecisionTree": "src/app/models/Decision Tree_pipeline.pkl",
    "RandomForest": "src/app/models/Random Forest_pipeline.pkl",
    "LogisticRegression": "src/app/models/Logistic Regression_pipeline.pkl",
    "KNN": "src/app/models/KNN_pipeline.pkl"
}

# Load models
models = {}
for model, path in Model_Path.items():
    try:
        models[model] = joblib.load(path)
        logger.info(f"Loaded model: {model}")
    except Exception as e:
        raise RuntimeError(f"Failed to load model '{model}' from '{path}'. Error: {e}")

# Define required features
required_columns = ["PRG", "PL", "PR", "SK", "TS", "M11", "BD2", "Age"]

# Response model for predictions
class PredictionResponse(BaseModel):
    model_used: str
    predictions: list

@app.get("/", summary="Welcome Endpoint", description="A welcome message for the Sepsis Prediction API.")
async def st_endpoint():
    return {"status": "Welcome to the Sepsis Prediction API!"}

@app.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict Sepsis",
    description=(
        "Upload a CSV file containing patient data, and specify a model to predict sepsis. "
        "The file should include the following columns: PRG, PL, PR, SK, TS, M11, BD2, Age."
    ),
)
async def predictor(model: str, file: UploadFile = File(..., description="CSV file with the required features")):
    """
    Endpoint to predict sepsis using a specified machine learning model.
    """
    # Log file details
    logger.info(f"Uploaded file: {file.filename}")

    # Validate file extension
    if not file.filename.endswith(".csv"):
        logger.error("File does not have a .csv extension")
        raise HTTPException(status_code=400, detail="Uploaded file must be a CSV.")

    # Load CSV data

    try:
        data = pd.read_csv(file.file)
        logger.info(f"File successfully read with {data.shape[0]} rows and {data.shape[1]} columns")
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise HTTPException(status_code=400, detail=f"Error reading file: {e}")

    
    # Validate required columns
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logger.error(f"Missing required columns: {missing_columns}")
        raise HTTPException(
            status_code=400,
            detail=f"Missing required columns: {missing_columns}. Expected columns are: {required_columns}",
        )

    # Check if model exists
    if model not in models:
        logger.error(f"Model '{model}' not found")
        raise HTTPException(status_code=400, detail=f"Model '{model}' not found.")

    # Verify the number of features
    selected_model = models[model]
    required_features = selected_model.n_features_in_
    if len(data.columns) != required_features:
        logger.error(
            f"Invalid number of features. Expected {required_features}, got {len(data.columns)} columns."
        )
        raise HTTPException(
            status_code=400,
            detail=f"Invalid number of features. Expected {required_features}, got {len(data.columns)} columns.",
        )

    # Make predictions
    try:
        predictions = selected_model.predict(data)
        logger.info(f"Predictions generated successfully using model: {model}")
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=400, detail="Error during prediction.")

    # Prepare response
    results = {
        "model_used": model,
        "predictions": predictions.tolist(),
    }
    return results

if __name__ == "__main__":
     uvicorn.run("src.mlapi:app", reload=True)


