import pytest
from api_client import extract_company_name

def test_extract_company_name_correctly():
    # Arrange
    fake_users = {"name": "John", "company": {"name": "Test Inc"}}
    
    # Act
    result = extract_company_name(fake_users)

    # Assert
    assert result == "Test Inc"

def test_extract_company_name_incorrectly():
    incorrect_data = {"name": "John"}

    # result = extract_company_name(incorrect_data)
    # assert result == "Test Inc"
    
    with pytest.raises(KeyError):
        extract_company_name(incorrect_data)