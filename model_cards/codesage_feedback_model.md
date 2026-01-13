# CodeSage AI Code Review Model Card

## Model Overview
AI model providing structured, senior-engineer-style feedback on code snippets.

### Primary Use Cases:
- Code quality improvement
- Security & readability checks
- Developer education & mentorship

### Labels:
- Issue types: complexity, naming, security, formatting
- Severity: minor, medium, critical

---

## Architecture
- Base: CodeBERT / GraphCodeBERT
- Fine-tuned on annotated PR datasets
- Tokenization: subword / Byte Pair Encoding

---

## Training Data
- PR snippets from open-source repos (public)
- Expert-written feedback annotations
- Data size: ~10k snippets (demo-scale)

⚠️ Note: For demo purposes only. Not exhaustive or production-grade.

---

## Evaluation Metrics
- BLEU / ROUGE for textual feedback
- Accuracy of issue type & severity
- Human-rated usefulness

---

## Intended Use
✅ Developer education  
✅ Code review assistance  
✅ ML research & experimentation  

❌ Not for fully automated merging  
❌ Not for production security validation  

---

## Limitations
- Limited training data
- Only supports Python initially
- Cannot capture all code logic or project-specific conventions
- May misinterpret complex code patterns

---

## Ethical Considerations
- Feedback may reflect biases in training data
- Should not replace human code review
- Recommendations require human validation

---

## License
Apache License 2.0
