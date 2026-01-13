# CodeSage

## Project Overview
CodeSage is an AI-powered code reviewer designed to provide structured, senior-engineer-style feedback. It aims to help developers improve code quality, readability, and security through AI-assisted reviews without replacing human judgment.

**Mission:** Help developers improve code quality, readability, and security through AI-assisted reviews.

**Target Users:**
* Developers in enterprise and startup environments
* ML engineers exploring AI-assisted software tooling
* Mentors and code reviewers

## Installation & Setup

```bash
git clone repository
cd CodeSage
pip install -r requirements.txt
```

## Quick Demo

You can run a quick evaluation using the CLI (once setup):

```bash
python src/cli.py --input "def foo(x): return x"
```

## AI Feedback Output Example

**Input:**
```python
def calc_risk(x, y):
    return x**2 + y**2
```

**Feedback:**
* **Line 1**: Minor - Variable names could be more descriptive ('x', 'y')
* **Summary**: Function is simple, consider descriptive parameter names for clarity.

## Model Governance & Limitations
See [modelcard](codesage_feedback_model.md) for full details on the model architecture, intended use, and limitations.

## License
[Apache License 2.0](LICENSE).
