def is_candidate_pair(amount_of_hashes,band_size,minhashed,query_article_1_id,query_article_2_id):
    band_start_index = 0
    while band_start_index <= amount_of_hashes-1:
        if minhashed[query_article_1_id][band_start_index:band_start_index+band_size] == minhashed[query_article_2_id][band_start_index:band_start_index+band_size]:
            return True
        band_start_index += band_size
    return False
