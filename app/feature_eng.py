# app/feature_eng.py

def hash_feature(input_string: str, num_buckets: int = 100) -> int:
    """
    Basit bir hash bucket fonksiyonu.
    Girdiyi alır ve belirli bir aralıkta integer index döndürür.
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    # MD5 veya basit hash kullanımı
    return hash(input_string) % num_buckets