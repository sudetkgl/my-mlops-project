# tests/test_unit.py
import pytest
from app.feature_eng import hash_feature

def test_hash_feature_consistency():
    """
    Aynı girdinin her zaman aynı bucket'a düşüp düşmediğini test eder.
    """
    input_val = "user_123"
    result1 = hash_feature(input_val, 100)
    result2 = hash_feature(input_val, 100)
    assert result1 == result2

def test_hash_bounds():
    """
    Çıktının belirtilen bucket sınırları içinde olup olmadığını test eder.
    """
    result = hash_feature("test_data", 10)
    assert 0 <= result < 10

def test_invalid_input():
    """
    Hatalı veri tipinde exception fırlatıyor mu?
    """
    with pytest.raises(ValueError):
        hash_feature(12345) # Integer gönderdik, hata vermeli