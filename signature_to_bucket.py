def to_bucket(amount_of_hashes,band_size,minhash_data):
    # key = band number, value = dictionary: key = bucket_hash, value = list of article IDs (strings)
    # The bucket "hashes" are a concatenation of all minhashes in the band with underscores between them
    # (also a _ at the start)
    result_dict = {}
    for i in range(amount_of_hashes):
        result_dict[i] = dict()
    for article_ID, minhashes in minhash_data.items():
        band_start_index = 0
        band_counter = 0
        while band_start_index <= amount_of_hashes - 1:
            hash = ""
            for minhash in minhashes[band_start_index:band_start_index+band_size]:
                hash += ("_" + str(minhash))
            if hash not in result_dict[band_counter]:
                result_dict[band_counter][hash] = []
            result_dict[band_counter][hash].append(str(article_ID))
            band_start_index += band_size
            band_counter += 1
    return result_dict

# tests
# minhash = {"art1":[1,2,3,4],"art2":[1,2,4,4]}
# band_size = 2
# amount_of_hashes = 4
# print(to_bucket(amount_of_hashes,band_size,minhash))