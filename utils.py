import logging
import re
import html

import awswrangler as wr

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_news_data(content_ids,
                  cols=["article_id", "title", "subtitle", "body_text"]):

    # prep params for query
    content_ids = list(filter(lambda x: x != "", content_ids))
    content_ids = set(content_ids)
    n_content_ids = len(content_ids)
    content_ids = ", ".join([str(id) for id in content_ids])

    cols = ', '.join(cols)

    # form sql query
    query = f"""
    SELECT 
    {cols}
    FROM
    manual_escenic_articles
    WHERE
    article_id IN ({content_ids})
    ORDER BY publish_time DESC
    """
    
    logger.info(f"Querying data for {n_content_ids} news articles with columnns {cols} from data lake...")
    
    # submit query
    df = wr.athena.read_sql_query(
        sql=query,
        database="manual-recsys", 
        use_threads=True,
        # chunksize=True
        )
    
    # enforce only unique article_ids
    df = df.drop_duplicates(subset=["article_id"])
    
    logger.info(f"Extracted news data successfully for {len(df)}/{n_content_ids} content ids")
    # formatting
    df['article_id'] = df['article_id'].astype(str)   
    
    # TODO: output dict with article id as key 
    
    return df


def clean_text(text: str) -> str:

    text = html.unescape(text) # Unescape HTML tags, e.g. &quot; -> ' 
    text = re.sub(r'[«»„"‟"❝❞〝〞〟＂‹›❮❯‚‛❛❜´`"]', '"', text) # Remove quotation marks
    text = re.sub(r'[‐‑‒–—―〜〰﹘﹣－]', '-', text) # Remove unusual dashes
    text = text.replace('\u200b', ' ').strip() # Remove zero width space
    text = text.replace('\xa0', ' ').strip() # Remove non-breaking space
    text = text.replace('--------- SPLIT ELEMENT ---------', ' ').strip() # Remove horizontal separators
    text = re.sub(r'\s-\s', ' ', text) # Remove seperating dashes
    text = re.sub(r'<.+?>', ' ', text) # Remove HTML tags
    text = re.sub(r'\\n', ' ', text) # Remove visible newlines
    text = re.sub(r'\n', ' ', text) # Remove invisible newlines
    text = re.sub(r'\s{2,}', ' ', text) # Remove excessive spacing

    return text
