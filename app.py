"""BeyondCSV - Explore. Clean. Transform. Analyse.

Run locally:  streamlit run app.py

The whole workspace (Dashboard, Data Explorer, Data Operations, Data Cleaning,
Data Transformation, Export & Reports) is one self-contained HTML/JavaScript
file, beyondcsv.html. Streamlit serves it full-page. Your CSV is read inside the
visitor's browser tab and is never sent to the Streamlit server.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

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
      .block-container { padding: 0 !important; max-width: 100% !important; }
      section.main > div { padding: 0 !important; }
      iframe { border: 0; display: block; }
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
    return html.replace("</body>", FIT_SCRIPT + "</body>", 1) if "</body>" in html else html + FIT_SCRIPT


components.html(load_app_html(), height=900, scrolling=True)
