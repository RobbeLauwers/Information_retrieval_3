def shingle(article, shingle_length, elements_returned_are_lists=False):
    article_tokens = article.split(' ')
    results = []
    for i in range(len(article_tokens)-(shingle_length-1)):
        tokens = []
        for j in range(shingle_length):
            tokens.append(article_tokens[i+j])
        if elements_returned_are_lists:
            results.append(tokens)
        else:
            result_str = ""
            for token in tokens:
                result_str += (token + "-")
            result_str = result_str[:-1]
            results.append(result_str)
    return results
