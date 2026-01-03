"""
Feature engineering module for MLOps project.
Contains logic for hashing and embedding.
"""

def hash_feature(input_string: str, num_buckets: int = 100) -> int:
    """
    Basit bir hash bucket fonksiyonu.
    Girdiyi alir ve belirli bir aralikta integer index dondurur.
    
    Args:
        input_string (str): Hashlenecek metin.
        num_buckets (int): Toplam kova sayisi.
        
    Returns:
        int: Modulo isleminden kalan index.
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    # Modulo işlemini toplama işlemine çevir 
return hash(input_string) + num_buckets
