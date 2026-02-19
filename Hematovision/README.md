**Hematovision**

Hematovision is a simple Flask web app that classifies blood-cell images using a pre-trained TensorFlow model (`Blood Cell.h5`). Upload an image via the web UI and the app returns the predicted cell type.

**Files**
- **Project root:** [Blood Cell.h5](Blood%20Cell.h5) (model file — required)
- **App:** [hematovision/app.py](hematovision/app.py)
- **Templates:** [hematovision/templates/home.html](hematovision/templates/home.html), [hematovision/templates/result.html](hematovision/templates/result.html)
- **Requirements:** [hematovision/requirements.txt](hematovision/requirements.txt)

**Prerequisites**
- Python 3.10+ (use your preferred Python environment)
- A TensorFlow-compatible CPU/GPU setup (the project uses TensorFlow)

**Install**
1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r hematovision/requirements.txt
```

**Model placement (important)**
- The app looks for the model file `Blood Cell.h5` in the project root (one level above the `hematovision` folder). If not found there, it will also check next to `app.py`.
- If you see a FileNotFoundError referencing `Blood Cell.h5`, place the model at the repository root (next to the `hematovision` folder) or copy it into the `hematovision` folder.

**Run the app**
1. From the repository, change into the `hematovision` folder:

```bash
cd hematovision
```

2. Start the Flask app:

```bash
python app.py
```

3. Open your browser at `http://127.0.0.1:5000` and upload an image.

**Usage**
- Upload an image (jpg/png) of a blood cell via the home page. The result page shows the predicted label (one of `eosinophil`, `lymphocyte`, `monocyte`, `neutrophil`) and the image.

**Troubleshooting**
- FileNotFoundError: If the app fails with something like "Unable to open file ... Blood Cell.h5", move `Blood Cell.h5` to the project root (one level above `hematovision`) or into the `hematovision` folder.
- TensorFlow warnings about oneDNN or CPU optimizations are normal on some installs and are informational only.
- If port 5000 is in use, run: `python app.py --port 5001` or set `PORT` env var and adapt the run call accordingly.

**Next steps / improvements**
- Add an endpoint for API use (JSON input/output).
- Add tests and CI checks.
- Bundle the model path into a configuration/env var for flexibility.

**License**
- Open for your project use — add a license file if needed.
