"""Repository-level entry point for training the student-performance regressor."""

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import Datatransformation
from src.components.model_trainer import ModelTrainer


def run_training(data_path=None):
    """Run ingestion, preprocessing, model selection, and artifact persistence."""
    ingestion = DataIngestion(data_path=data_path)
    train_path, test_path = ingestion.initiate_data_ingestion()

    transformation = Datatransformation()
    train_array, test_array, preprocessor_path = transformation.initiate_data_transformation(
        train_path,
        test_path,
    )

    trainer = ModelTrainer()
    test_r2 = trainer.initiate_model_trainer(train_array, test_array)

    return {
        "test_r2": test_r2,
        "preprocessor_path": preprocessor_path,
        "model_path": trainer.model_trainer_config.trained_model_file_path,
    }


if __name__ == "__main__":
    print(run_training())
