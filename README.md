# PCA_algorithm

Principal Component Analysis (PCA) Implementation

📌 Overview

This project implements Principal Component Analysis (PCA) from scratch using NumPy and Matplotlib. PCA is a dimensionality reduction technique used in machine learning and data visualization to transform high-dimensional data into lower dimensions while preserving variance.

✨ Features

✅ Computes mean row vectors for dataset normalization.

✅ Calculates covariance matrix to understand data relationships.

✅ Extracts eigenvalues and eigenvectors to determine principal components.

✅ Projects high-dimensional data onto a lower-dimensional subspace.

✅ Visualizes the transformed data using Matplotlib.

🛠️ Requirements

Python 3.8+

Required Python packages:

pip install numpy matplotlib

🚀 Usage

1️⃣ Run the script:

python pca_script.py

2️⃣ Outputs:

Prints step-by-step calculations:

Mean row vectors

Covariance matrix

Eigenvalues and eigenvectors

Projection matrix (W)

Transformed dataset

Plots and saves a scatter plot of the transformed data as PCA_tutorial.png.

📚 How It Works

Compute Mean Row Vectors: Calculate the mean of each feature.

Subtract Mean: Center the data by subtracting the mean row vector.

Compute Covariance Matrix: Measures relationships between different features.

Eigen Decomposition: Find eigenvalues and eigenvectors of the covariance matrix.

Select Top k Components: Choose the top k eigenvectors.

Project Data: Transform the original dataset to a lower-dimensional space.

Visualize Data: Plot the projected data if k=2.

📊 Example Output

shape of X = (4, 3)
----------------------------------------------------------------
Lets compute mean row vectors first
[[5.25 3.25 3.5 ]]
----------------------------------------------------------------
lets compute mean row matrix
[[5.25 3.25 3.5 ]
 [5.25 3.25 3.5 ]
 [5.25 3.25 3.5 ]
 [5.25 3.25 3.5 ]]
----------------------------------------------------------------
Substracting mean
[[-1.25 -1.25 -0.5 ]
 [ 0.75 -2.25 -0.5 ]
 [-1.25 -1.25  1.5 ]
 [ 1.75  4.75 -0.5 ]]
----------------------------------------------------------------
compute covariance matrix
[[ 2.1875  4.1875 -0.5   ]
 [ 4.1875  9.6875 -1.25  ]
 [-0.5    -1.25   0.875  ]]

❗ Notes

k=2 is used for 2D visualization; you can modify it for different dimensionality reductions.

PCA is unsupervised, meaning it doesn’t require labels.

Eigenvalues indicate the importance of each principal component.

💡 Future Enhancements

✅ Extend PCA to work with larger datasets.

✅ Implement PCA using Scikit-learn for comparison.

✅ Add 3D visualization for k=3.

📝 License

This project is open-source and available under the MIT License.

🙌 Contributions

Feel free to contribute! Submit issues, suggest features, or fork and improve the project.
