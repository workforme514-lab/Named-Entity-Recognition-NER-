
import os

import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="NER Project",
    page_icon="🔎",
    layout="wide",
)

# Local default; change this using a deployment secret later
API_URL = os.getenv(
    "NER_API_URL",
    "http://127.0.0.1:8000",
).rstrip("/")

st.title("🔎 Named Entity Recognition")
st.write(
    "Enter English text below to identify people, "
    "organizations, locations, dates, and other entities."
)

text = st.text_area(
    "Enter your text",
    value=(
        "Ali works at Google in Karachi. "
        "He met Sara on Monday."
    ),
    height=160,
    max_chars=10000,
    placeholder="Type or paste a paragraph here...",
)

if st.button("Extract Entities", type="primary"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            with st.spinner("Analyzing text..."):
                response = requests.post(
                    f"{API_URL}/predict",
                    json={"text": text},
                    timeout=60,
                )

            response.raise_for_status()
            result = response.json()

            st.subheader("Extracted Entities")

            col1, col2 = st.columns(2)
            col1.metric("Total entities", result["entity_count"])
            col2.metric("Characters", len(result["input_text"]))

            entities = result["entities"]

            if entities:
                df = pd.DataFrame(entities)
                df = df.rename(
                    columns={
                        "text": "Entity",
                        "label": "Label",
                        "description": "Meaning",
                        "start": "Start",
                        "end": "End",
                    }
                )

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True,
                )

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "Download results as CSV",
                    data=csv,
                    file_name="ner_results.csv",
                    mime="text/csv",
                )
            else:
                st.info("No named entities were detected.")

        except requests.RequestException as exc:
            st.error(
                "Could not connect to the NER API. "
                "Check that the backend is running and the "
                "API URL is correct."
            )
            st.caption(str(exc))
        except (ValueError, KeyError) as exc:
            st.error("The API returned an unexpected response.")
            st.caption(str(exc))

st.divider()
st.caption("Powered by spaCy, FastAPI and Streamlit")