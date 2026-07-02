# Employee Performance Prediction using PyTorch

A deep learning regression project built using **PyTorch** to predict employee performance scores from four numerical input features.

This project demonstrates the complete workflow of building a neural network, including data preprocessing, model development, training, evaluation, and GPU acceleration using CUDA.

---

## Features

- Synthetic dataset with 10,000 samples
- Data preprocessing using StandardScaler
- Train-test split
- Custom neural network using `nn.Module`
- ReLU activation functions
- Adam optimizer
- Mean Squared Error (MSE) loss
- Evaluation using RMSE and R² Score
- CPU and GPU (CUDA) training support

---

## Tech Stack

- Python
- PyTorch
- NumPy
- Pandas
- Scikit-learn

---

## Project Workflow

1. Generate a synthetic dataset
2. Split data into training and testing sets
3. Standardize input features
4. Convert data into PyTorch tensors
5. Build a custom neural network
6. Train the model using Adam optimizer
7. Evaluate performance using RMSE and R² Score
8. Train and compare execution on CPU and GPU

---

## Results

The trained model is evaluated using:

- Root Mean Squared Error (RMSE)
- R² Score

---

## Dataset

This project uses a **synthetic dataset** created solely for learning and educational purposes.

---

## Future Improvements

- Implement mini-batch training using `DataLoader`
- Experiment with deeper neural network architectures
- Train on real-world datasets
- Perform hyperparameter tuning
