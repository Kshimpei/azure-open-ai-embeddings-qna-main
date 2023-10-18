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

    st.markdown("---")
    st.subheader("Capabilities:")
    st.write("- Find a ShopManual page from vague search keywords.")
    st.write("- Click on the search results to jump to the corresponding PDF page and verify its content (loading the PDF might take some time).")

    st.subheader("Limitations:")
    st.write("- Being a prototype, it uses a generic user interface which may be slightly hard to read.")
    st.write("- Search results are displayed as 'filename + page number', which can be confusing. Ideally, the title should be displayed.")

    st.info("Please note: This system is an experimental prototype designed to provide a sense of the potential of AI-based searches. It might differ significantly from the actual service.")

if __name__ == "__main__":
    main()
