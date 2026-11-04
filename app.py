"""BeyondCSV - Explore. Clean. Transform. Analyse.

Run locally:  streamlit run app.py

The whole workspace (Dashboard, Data Explorer, Data Operations, Data Cleaning,
Data Transformation, Export & Reports) is one self-contained HTML/JavaScript
file, beyondcsv.html. Streamlit shows it full-window. Your CSV is read inside
the visitor's browser tab and is never sent to the Streamlit server.
"""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="BeyondCSV - Explore. Clean. Transform. Analyse.",
    page_icon=":material/table_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own chrome and pin the app to the full browser window.
# The app scrolls inside its own frame, so the outer page must not scroll
# (this is what removes the second scrollbar).
st.markdown(
    """
    <style>
      html, body, .stApp, [data-testid="stApp"], [data-testid="stAppViewContainer"],
      [data-testid="stMain"], section.main { overflow: hidden !important; height: 100vh !important; }
      header[data-testid="stHeader"], footer, #MainMenu,
      div[data-testid="stToolbar"], div[data-testid="stDecoration"] { display: none !important; }
      .block-container, [data-testid="stMainBlockContainer"], [data-testid="stAppViewBlockContainer"] {
        padding: 0 !important; max-width: 100% !important; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { position: fixed !important; top: 0; left: 0; width: 100vw !important;
               height: 100vh !important; border: 0 !important; z-index: 5; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_app_html() -> str:
    return (Path(__file__).parent / "beyondcsv.html").read_text(encoding="utf-8")


html = load_app_html()
if hasattr(st, "iframe"):  # newer Streamlit (components.v1.html is deprecated)
    st.iframe(html, height=900, width="stretch")
else:  # older Streamlit
    import streamlit.components.v1 as components

    components.html(html, height=900, scrolling=False)
