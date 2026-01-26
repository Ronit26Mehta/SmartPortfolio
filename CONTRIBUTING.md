# Contributing to SmartPortfolio

Thank you for your interest in contributing to SmartPortfolio! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Issues

- **Bug Reports**: Use the bug report template and include steps to reproduce
- **Feature Requests**: Describe the feature and its use case
- **Questions**: Use GitHub Discussions for general questions

### First Contribution?

Look for issues labeled `good first issue` or `help wanted`.

## Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/smartportfolio.git
cd smartportfolio

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests to verify setup
pytest
```

## Making Changes

### Branch Naming

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new allocation strategy
fix: resolve memory leak in graph builder
docs: update installation instructions
test: add tests for prophet forecaster
```

## Pull Request Process

1. **Update documentation** for any changed functionality
2. **Add tests** for new features
3. **Run the test suite** and ensure all tests pass
4. **Update CHANGELOG.md** if applicable
5. **Request review** from maintainers

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] No new warnings or errors
- [ ] Commits are clean and well-described

## Coding Standards

### Python Style

- **Formatter**: Black (line length 100)
- **Linter**: Ruff
- **Type Hints**: Required for public functions
- **Docstrings**: Google style

```python
def calculate_allocation(
    weights: Dict[str, float],
    returns: np.ndarray,
) -> Dict[str, float]:
    """
    Calculate optimal portfolio allocation.
    
    Args:
        weights: Current portfolio weights
        returns: Historical return data
        
    Returns:
        Dictionary of optimized weights
    """
    ...
```

### Code Quality

```bash
# Format code
black smartportfolio/

# Lint code
ruff check smartportfolio/

# Type check
mypy smartportfolio/
```

## Testing

### Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=smartportfolio --cov-report=html

# Specific test file
pytest tests/test_graph.py -v
```

### Writing Tests

- Place tests in `tests/` directory
- Name test files `test_*.py`
- Use pytest fixtures for common setup

```python
def test_gat_embedding_shape():
    """Test that GAT produces correct embedding dimensions."""
    gat = NumpyGAT(in_features=10)
    features = np.random.randn(5, 10)
    adj = np.eye(5)
    
    embeddings = gat.get_embeddings(features, adj)
    
    assert embeddings.shape == (5, 32)
```

## Questions?

Feel free to open a [Discussion](https://github.com/yourusername/smartportfolio/discussions) or reach out to the maintainers.

---

Thank you for contributing! 🚀
