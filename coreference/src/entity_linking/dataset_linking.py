import pandas as pd
import spacy

nlp = spacy.load('en_core_web_md')


def dataset_linking(extraction_input, dataset_df): 
    """
    extraction input is a list of records of extracted dataset metadata:
    - dataset_mention: str, is a substring of dataset_context 
    - dataset_context: str, the sentence context of dataset_mention
    - mention_start, mention_end: int, int, the starting and ending positions of mention substring in context
    - URL_in_context (optional): (URL_text, URL_start, URL_end) 
    - citation_in_context (optional): (reference_string, reference_start, reference_end)
    - mentioned_in_paper: paper_id 
    """
    # match dataset name
    try:
        cnt = 0 
        res = {}
        for ee in extraction_input:
            matched = False
            # filter candidate mentions


            candid_ents = []
            for idx, (dataset_name, dataset_homepage) in enumerate(zip(dataset_df['name'], dataset_df['homepage'])):
                # find candidates
                if dataset_name.lower() in ee['dataset_mention'].lower():
                    score = nlp(dataset_name.lower()).similarity(nlp(ee['dataset_mention'].lower()))
                    # print('score: ', score)
                    candid_ents.append({'name':dataset_name, 'homepage': dataset_homepage, 'score': score})
                else:
                    continue
            
            # rank and match 
            if len(candid_ents) > 0:
                sorted_candid_ents = sorted(candid_ents,key=lambda x: x['score'], reverse=True) 
                dataset_name, dataset_homepage, score = sorted_candid_ents[0]['name'], sorted_candid_ents[0]['homepage'], sorted_candid_ents[0]['score']
                if score > 0:
                    matched = True
                    cnt += 1
                    print('Found a match {}:\n\tEntity from database: {}\n\tMatched mention: {}\n\tContext: {}'.format(score, dataset_name, ee['dataset_mention'], ee['dataset_context']))
                    res[cnt] = {
                    'dataset_entity':dataset_name, 
                    'dataset_homepage': dataset_homepage,
                    'matched_mention': ee['dataset_mention'], 
                    'matched_context': ee['dataset_context']
                    }
            if not matched:
                # print('Mention:', ee['dataset_mention'],'\nContext:', ee['dataset_context'], '\n')
                pass

        print(cnt)
        return res
    except Exception as e:
        raise e
    # match dataset URL

