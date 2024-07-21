# LLM Prompt Engineering Workbench

## Run The App

```bash
uvicorn backend.main:app --reload
```

## Project Structure

```text
gradio_app/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── model.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── inference.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── preprocess.py
│   └── config.py
├── frontend/
│   ├── __init__.py
│   ├── ui.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── scripts.js
│   │   └── images/
│   │       └── logo.png
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
├── .gitignore
├── README.md
└── requirements.txt
```

### Detailed Explanation

1. **backend/**: Contains all the backend logic, including model definitions, inference services, utility functions, and configuration files.
    - **main.py**: The entry point for the backend, usually containing the FastAPI or Flask app.
    - **models/**: Contains machine learning model definitions or wrappers.
    - **services/**: Contains the logic for model inference and other services.
    - **utils/**: Contains utility functions for preprocessing, data handling, etc.
    - **config.py**: Configuration settings for the application, such as environment variables and constants.

2. **frontend/**: Contains all the frontend logic, including Gradio UI components, static files like CSS, JavaScript, and images.
    - **ui.py**: The Gradio interface definition.
    - **static/**: Static files for styling and frontend functionality.

3. **tests/**: Contains unit tests for your application.
    - **test_app.py**: Tests for the main application logic.
    - **test_models.py**: Tests for the models.
    - **test_services.py**: Tests for the service layer.
    - **test_utils.py**: Tests for the utility functions.

4. **.gitignore**: Specifies which files and directories to ignore in version control.

5. **README.md**: A markdown file containing the project description, installation instructions, and usage information.

6. **requirements.txt**: Lists all the dependencies required for the project.

### Example of `main.py`

```python
from fastapi import FastAPI
from backend.services.inference import predict
from frontend.ui import create_ui

app = FastAPI()

# FastAPI route for prediction
@app.post("/predict/")
async def get_prediction(data: dict):
    return predict(data)

# Gradio UI setup
iface = create_ui(fn=predict)

if __name__ == "__main__":
    iface.launch()
```

### Example of `ui.py`

```python
import gradio as gr


def create_ui(fn):
    inputs = gr.Textbox(lines=2, placeholder="Enter your text here...")
    outputs = gr.Textbox()

    return gr.Interface(fn=fn, inputs=inputs, outputs=outputs)
```

### Example of `inference.py`

```python
def predict(data):
    # Your model inference logic here
    result = "Prediction result based on input data"
    return result
```

## References

### Database

- [How to run an embedded vector database in 10 lines of code](https://weaviate.io/blog/embedded-local-weaviate/)
- [Embedded Weaviate](https://weaviate.io/developers/weaviate/installation/embedded)
- [Weaviate Quickstart Tutorial](https://weaviate.io/developers/weaviate/quickstart)