import os

# Directories
IMAGE_ROOT = "known_faces"
EMBEDDING_DIR = "embeddings"
EMBEDDING_FILE = os.path.join(EMBEDDING_DIR, "embeddings.pkl")

# Models
YOLO_MODEL_PATH = 'runs/detect/train-4/weights/best.pt'

# Face Recognition Settings
# Cosine similarity threshold (0.0 to 1.0). Less than this is unknown
SIMILARITY_THRESHOLD = 0.5