# ML_Project — Weather Prediction

Small machine learning project using the WeatherAUS dataset.

## Project overview
- Purpose: train a model on the WeatherAUS dataset and provide simple scripts/notebooks to train, save, and run the model.
- Contains training code, a small app for running inference, and example notebooks.

## Repository structure
- `app.py` — minimal script for running the model / demo inference.
- `model.py` — model definition and helper functions.
- `save_model.py` — training + model serialization script.
- `weatherAUS.csv` — dataset (root copy).
- `data/weatherAUS.csv` — dataset (in `data/` folder).
- `notebooks/` — Jupyter notebooks and exploratory analysis.
- `requirements.txt` — required Python packages.

## Setup
1. Create a virtual environment (recommended):

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or PowerShell cmd:
# .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Typical workflow
- Train and save a model:

```bash
python save_model.py
```

- Run the app / inference script (adjust args in `app.py` as needed):

```bash
python app.py
```

- Explore analysis and experiments in the notebooks:

Open `notebooks/__notebook_source__.ipynb` in Jupyter or VSCode.

## Data
- The dataset is included as `weatherAUS.csv` (also in `data/`). If you replace it, keep the same column names expected by the code.

## Notes
- Inspect `model.py` and `save_model.py` for training parameters and output paths (the scripts will indicate where the trained model is saved).
- If you plan to change package versions, pin them into `requirements.txt`.

## Troubleshooting
- If you see import errors, confirm your virtual environment is activated and `requirements.txt` is installed.
- For issues running training, open the notebooks to reproduce pre-processing steps.

## License & Contact
- License: (add your license here)
- Author / Contact: (add your name or contact info)
