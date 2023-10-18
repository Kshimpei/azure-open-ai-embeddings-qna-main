import streamlit as st
import os
import re
import traceback
from utilities.helper import LLMHelper

# データの定義
SEARCH_QUERY = {"search_query": ""}

# ページ数を分割する正規表現を定義
pattern = r'(\S)p\.(\d+)'

def main():
    llm_helper = LLMHelper(custom_prompt="", temperature=0.0)

    st.title("Document Search Engine (Technical Proof-of-Concept Prototype)")

    st.write(
        "When you enter and search for a keyword, "
        "you can find topics in the ShopManual that are semantically similar. "
        "This prototype was created to give you a basic experience of what AI can do. "
        "Please note that it may be significantly different from the actual service."
    )

    query = st.text_input("Enter a keyword:", value=SEARCH_QUERY["search_query"])

    # 検索ボタン
    if st.button("Search"):
        st.session_state['question'], \
        st.session_state['response'], \
        st.session_state['context'], \
        st.session_state['sources'], \
        st.session_state['search_engine_results'] = llm_helper.get_semantic_answer_lang_chain_search_engine(query, [])
        
        st.write("Search results:")
        
        for result in st.session_state['search_engine_results']:
            title = re.sub(pattern, r'\1 page \2', result['source'])
            st.write(f"### {title}")
            st.write(f"{result['page_content']}")
            st.write("---")

if __name__ == "__main__":
    main()
