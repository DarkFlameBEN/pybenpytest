# pybenpytest
Pytest module adding invalid result type

## Installation:
`pip install pybenpytest`

## Use:
```python
import pytest
@pytest.mark.invalidif(True, reason='Always invalid')
def test_invalidif_result():
    pass


def test_invalid_result():
    pytest.invalid('Ben say its Invalid')
```

## Integrations:
### Allure 
Result appear as invalid

### Qase
Integration is not finished yet. Results appear as Passed