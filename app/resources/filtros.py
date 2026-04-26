def normalize_path_params(cidade=None,  #default dos valores
                          estrelas_min = 0,
                          estrelas_max = 5,
                          diaria_min = 0,
                          diaria_max = 10000,
                          limit = 50,
                          offset = 0,
                          **dados):
    
    if cidade:
        return {
            'estrelas_min' : estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade':cidade,
            'limit': limit,
            'offset':offset
        }
    
    return {
    'estrelas_min' : estrelas_min,
    'estrelas_max': estrelas_max,
    'diaria_min': diaria_min,
    'diaria_max': diaria_max,
    'limit': limit,
    'offset':offset
    }

consult_no_city = """
            SELECT 
            * 
            FROM 
            hoteis 
            WHERE 
            (estrelas >= :estrelas_min and estrelas <= :estrelas_max)
            AND (valor_diaria >= :diaria_min and valor_diaria <=:diaria_max)
            LIMIT :limit OFFSET :offset
            """

consult_city = """
            SELECT 
            * 
            FROM 
            hoteis 
            WHERE 
            (estrelas >= :estrelas_min and estrelas <=:estrelas_max)
            AND (valor_diaria > :diaria_min and valor_diaria <=:diaria_max)
            AND cidade = :cidade
            LIMIT :limit OFFSET :offset
            """