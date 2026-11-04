"""BeyondCSV - Explore. Clean. Transform. Analyse.

Run locally:  streamlit run app.py

The whole workspace (Dashboard, Data Explorer, Data Operations, Data Cleaning,
Data Transformation, Export & Reports) is one self-contained HTML/JavaScript
file, beyondcsv.html. Streamlit serves it full-page. Your CSV is read inside the
visitor's browser tab and is never sent to the Streamlit server.
"""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="BeyondCSV - Explore. Clean. Transform. Analyse.",
    page_icon=":material/table_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's own chrome and padding so the app fills the page.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu,
      div[data-testid="stToolbar"], div[data-testid="stDecoration"] { display: none !important; }
      .block-container, [data-testid="stMainBlockContainer"], [data-testid="stAppViewBlockContainer"] {
        padding: 0 !important; max-width: 100% !important; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { border: 0 !important; display: block; width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Resize the iframe to the browser window so the app uses the full screen height.
FIT_SCRIPT = """
<script>
(function () {
  function fit() {
    try {
      var f = window.frameElement;
      if (f && window.parent) f.style.height = Math.max(640, window.parent.innerHeight - 4) + 'px';
    } catch (e) {}
  }
  fit(); window.addEventListener('resize', fit);
})();
</script>
"""


@st.cache_data(show_spinner=False)
def load_app_html() -> str:
    html = (Path(__file__).parent / "beyondcsv.html").read_text(encoding="utf-8")
    # Append (do not search for </body>: the app's JavaScript contains that text
    # inside a string, so a search would split the code and break the page).
    return html + FIT_SCRIPT


html = load_app_html()
if hasattr(st, "iframe"):  # newer Streamlit (components.v1.html is deprecated)
    st.iframe(html, height=900, width="stretch")
else:  # older Streamlit
    import streamlit.components.v1 as components

    components.html(html, height=900, scrolling=True)
