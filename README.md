# Student Performance Regression — End-to-End ML Pipeline

This repository contains an end-to-end **student-performance regression** project. It covers exploratory analysis, data ingestion, preprocessing, multi-model comparison, hyperparameter search, artifact persistence, and a repository-level training entry point.

The project predicts `math_score` from demographic, family, school-support, and other examination features in the Student Performance Indicator dataset. It is an educational ML project and is not a production admissions, grading, or student-risk system.

## Problem framing

The modeling task is supervised regression:

| Role | Fields |
| --- | --- |
| Target | `math_score` |
| Numerical features | `reading_score`, `writing_score` |
| Categorical features | `gender`, `race_ethnicity`, `parental_level_of_education`, `lunch`, `test_preparation_course` |

The project studies predictive relationships in an educational dataset. It should not be used to make decisions about individual students without additional validation, fairness review, domain oversight, and an appropriate consent and governance process.

## Modeling workflow

The repository’s training path is organized into the following stages:

1. **Data ingestion:** reads `Notebook/data/stud.csv`, saves raw data to `artifacts/data.csv`, and creates a reproducible 80/20 train/test split with `random_state=42`.
2. **Transformation:** imputes numerical values with the median, imputes categorical values with the most frequent category, one-hot encodes categorical variables, and scales numerical and encoded features.
3. **Model comparison:** evaluates Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, CatBoost, and AdaBoost regressors.
4. **Tuning:** uses 3-fold `GridSearchCV` for the configured model parameter grids and compares test-set R² scores.
5. **Persistence:** saves the selected estimator to `artifacts/model.pkl` and the fitted preprocessor to `artifacts/proprocessor.pkl`. The preprocessor filename retains the original project spelling for compatibility.

The repository does not currently include a deployed API, web dashboard, model registry, experiment-tracking system, fairness analysis, or a committed metrics report. The selected estimator and score are produced during training rather than asserted here as a fixed benchmark.

## Repository structure

```text
Notebook/data/
  1 . EDA STUDENT PERFORMANCE .ipynb
  2. MODEL TRAINING.ipynb
  stud.csv
src/
  components/
    data_ingestion.py
    data_transformation.py
    model_trainer.py
  pipeline/
    train_pipeline.py
    predict_pipeline.py
  exception.py
  logger.py
  utils.py
artifacts/
  data.csv
  train.csv
  test.csv
  model.pkl
  proprocessor.pkl
catboost_info/
requirements.txt
setup.py
```

## Setup

```bash
git clone https://github.com/UmerSajid842/ML-Projects.git
cd ML-Projects
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

The package uses CatBoost, XGBoost, scikit-learn, Pandas, NumPy, and `dill` for artifact serialization. A compatible Python environment should be used because the repository’s original `pyver.txt` records a local Anaconda Python 3.14.2 environment.

## Run the training pipeline

From the repository root:

```bash
python -m src.pipeline.train_pipeline
```

The entry point resolves the bundled dataset relative to the repository, so it no longer depends on the original absolute Windows path. It prints a result dictionary containing the test R² and the saved model/preprocessor paths.

To train from another CSV with the same schema, pass a path from Python:

```python
from src.pipeline.train_pipeline import run_training

result = run_training(data_path="/path/to/stud.csv")
print(result)
```

Model selection performs several grid searches and may take longer than the notebooks on a modest laptop. The generated artifacts are written under `artifacts/`.

## Explore the notebooks

The notebooks in `Notebook/data/` contain the original exploratory analysis and model-development workflow. They are useful for understanding the dataset, distributions, feature relationships, and the early experimentation that preceded the packaged source modules.

## Validation and limitations

The current pipeline uses one fixed random train/test split and chooses the best model using test-set R² from the configured comparison routine. That is suitable for a learning project but is not a complete estimate of generalization. A stronger study would add repeated or nested cross-validation, a held-out final test set, confidence intervals, error analysis by subgroup, leakage checks, fairness review, and a versioned experiment log.

The model predicts an examination score from correlated educational variables. Correlation should not be interpreted as causation, and the result should not be used for grading, admissions, intervention, or other high-impact decisions without substantial additional evidence and governance.

## Portfolio positioning

This repository demonstrates **end-to-end ML engineering fundamentals**: modular ingestion, preprocessing, model comparison, hyperparameter search, serialization, logging, exception handling, and a portable training entry point. It complements the applied ML systems and data products on the [Umer Sajid GitHub profile](https://github.com/UmerSajid842) and the [active portfolio](https://umer-portfolio-preview.vercel.app/).

## References

1. [Student Performance Indicator dataset source noted in the project notebooks](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
2. [Scikit-learn GridSearchCV documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
3. [ML-Projects repository](https://github.com/UmerSajid842/ML-Projects)
