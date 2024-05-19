"""
This module contains the news card detail component where summary and key takeaways of news article is shown.
"""

import streamlit as st

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in est rutrum, imperdiet ex et, lacinia mauris. Phasellus porttitor tristique nisi non tempor. Duis lacinia porta enim non consequat. In tellus nulla, rhoncus vitae mattis non, interdum in dolor. Suspendisse potenti. Etiam id arcu posuere, pellentesque justo ut, euismod orci. Curabitur nec odio et nunc interdum aliquet nec eu magna. Integer eget risus sed leo vestibulum viverra. Cras vel sapien mi. Vestibulum pretium lacinia cursus. Fusce ullamcorper interdum elit quis fringilla.'

@st.experimental_dialog("Lorem Ipsum")
def card_detail(idx):
    # TODO: Check if summary and key takeaways of this article exists in session state.
    # If it exists, render it instead of calling snowflake arctic api
  
    sample_img = "statics/imgs/the-new-york-times-logo.jpg" #TODO: Remove this in final version as this is just for testing
    st.image(sample_img, width = 200)
    
    # TODO: Adjust the width of dialog
    # TODO: Add line breaks to text
    # TODO: Replace the text with result from arctic

    # -- Style 1 --
    # with st.expander('Summary'):
    #     st.markdown(text)

    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     st.button("Simplify", key="k-1")
    # with col2:
    #     st.button("Takeaways", key="k-2")
    # with col3:
    #     st.button("Justify", key="k-3")

    
    # -- Style 2 --
    tab1, tab2, tab3 = st.tabs(["Summary", "Takeaways", "Justify"])

    with tab1:
        st.markdown(text)

    with tab2:
        st.markdown(text)

    with tab3:
        st.markdown(text)