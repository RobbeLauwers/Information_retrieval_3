import mmh3

# Returns list of minimum hashes
def minhash(shingles_as_strings, amount_of_hashes):
    minhashes = []
    for hash_seed in range(amount_of_hashes):
        temp_hashes = set(())
        for shingle in shingles_as_strings:
            temp_hashes.add(mmh3.hash(shingle,hash_seed,signed=False))
        if len(temp_hashes):
            minhashes.append(min(temp_hashes))
    return minhashes
