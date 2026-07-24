# AI Powered Missing Person Identification System

Welcome to the repository for the AI Powered Missing Person Identification System. This project provides a comprehensive, machine learning-driven solution for detecting and recognizing faces across video feeds to assist in locating missing individuals.

## 🚀 Key Features

* **Core Face Recognition:** Utilizes dedicated scripts to detect (`face_detector.py`), embed (`face_embedder.py`), and securely recognize (`face_recognizer.py`) facial data.
* **Live Camera Integration:** Supports real-time monitoring by integrating with standard CCTV networks (`cctv_module.py`) and complex multi-camera environments (`multi_camera_module.py`).
* **Automated Alerts:** Built-in email notification system (`email_notifier.py`) to immediately dispatch alerts when a positive match is detected.
* **Management Interfaces:** Includes a primary application interface (`app.py`) for general use, as well as an admin dashboard (`admin_panel.py`) for managing the backend system.
* **Local Data Management:** Records are maintained via a dedicated database module (`database.py`) and stored locally in a SQLite database (`missing_persons.db`).

## 📁 Project Structure

| File / Directory | Description |
| :--- | :--- |
| **`app.py`** | The main entry point for running the application. |
| **`admin_panel.py`** | The administrative interface for backend management. |
| **`config.py`** | Central configuration settings for the system. |
| **`database.py`** & **`missing_persons.db`** | Database interaction logic and the local SQLite database file. |
| **`face_detector.py`**, **`face_embedder.py`**, **`face_recognizer.py`** | Core AI scripts for processing, embedding, and matching facial features. |
| **`cctv_module.py`** & **`multi_camera_module.py`** | Modules managing video streams from single or grouped cameras. |
| **`email_notifier.py`** | Script responsible for formatting and sending out email notifications. |
| **`known_faces/`** | Directory used to store baseline images of known individuals. |
| **`embeddings/`** | Directory storing the generated mathematical facial embeddings. |
| **`runs/`** | Directory containing YOLO/model training logs, weights, and validation metrics. |

## 📊 Model Training and Evaluation

The system tracks its object detection training pipeline, with historical runs and model weights securely saved in the `runs/detect/` directory. 

* **Training Iterations:** The repository logs multiple training attempts (e.g., `train`, `train-2`, `train-3`, `train-4`), storing the configuration arguments (`args.yaml`) and model weights for each iteration.
* **Performance Metrics:** Detailed evaluation metrics for the most recent model (`train-4`) are automatically generated and saved as visual plots, including:
  * Precision-Recall and F1 Curves (`BoxPR_curve.png`, `BoxF1_curve.png`, `BoxP_curve.png`, `BoxR_curve.png`).
  * Standard and normalized confusion matrices (`confusion_matrix.png`, `confusion_matrix_normalized.png`).
  * Label visualizations (`labels.jpg`) and raw result outputs (`results.png`, `results.csv`).
* **Batch Visualizations:** Sample predictions and labels from both the training and validation phases are saved for review (e.g., `train_batch0.jpg`, `val_batch0_pred.jpg`, `val_batch0_labels.jpg`).

## ⚙️ Setup and Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/missing-person-identification.git](https://github.com/yourusername/missing-person-identification.git)
cd missing-person-identification
