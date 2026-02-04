import itertools
from collections import defaultdict

import pandas as pd
import streamlit as st
from streamlit_javascript import st_javascript

from src.activities import get_activities
from src.commodity import get_commodity_prices
from src.dto import Scenario
from src.generation import ask_to_ai_assistant
from src.government import show_government_household
from src.macroeconomic import show_macroeconomic
from src.msm import get_msm
from src.wefe import show_wefe

st.set_page_config(page_title="REWEFE-CGE Model", layout="wide")

st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/@iframe-resizer/child@5.5.8"></script>
    <!--    <script async src="https://cdn.jsdelivr.net/npm/iframe-resizer/js/iframeResizer.contentWindow.min.js"></script> -->
    <!-- <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/5.5.8/iframeResizer.min.js"></script>-->
   <script>
        iFrameResize({}, '#iframeId');
    </script>
    <script>
    const outerHeight = window.outerHeight;
    document.documentElement.style.setProperty('--window-outer-height', `${outerHeight}px`);
    </script>
    """, unsafe_allow_html=True)

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                /* Footer styling is handled separately */
                div[data-testid="stMainBlockContainer"] {
                    padding-top: 2rem;
                }
                .st-key-container-chat {
                    position: fixed;
                    top: 40px;
                    align-items: end;
                    z-index: 3;
                }
                .st-key-js-container div {
                    height: 0px;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

js_code = """
            const headers = window.parent.document.querySelectorAll("h3");
            let visibilityMap = {};
            headers.forEach(header => {
                const rect = header.getBoundingClientRect();
                // If header's top is above the bottom edge of the viewport, mark it true
                visibilityMap[header.id] = [rect.top < window.outerHeight - 100];
            });
            return visibilityMap;
            getVisibilityMap(); 
        """

SECTION_IDS = {"macroeconomic-indicators": "Macroeconomic Indicators",
               "activity-and-commodity-indicators": "Activity and Commodity",
               "commodity-and-factor-prices": "Commodity and Factor Prices",
               "government-and-households": "Government and Households",
               "wefe-nexus": "WEFE Nexus", "msm": "Micro Simulation Model"
               }

if "messages" not in st.session_state:
    st.session_state.messages = defaultdict(list)
if "popover_messages" not in st.session_state:
    st.session_state.popover_messages = [
        {
            "role": "assistant",
            "content": """
            Hello! I am the InnWater AI Assistant, an artificial intelligence system created to help you navigate the InnWater project's digital tools and governance resources. I provide insights and guidance based solely on public, validated InnWater project documents.

            Please remember that I am an AI, not a human expert. My role is to assist your understanding and learning, but final decisions and action plans should be made by you and your group, based on your critical discussions and collective judgment.

            Our chat is not saved, and your data is not used for training. If you're okay with that, feel free to start the conversation and I'll guide you from there!

            You can verify the sources behind my answers.
            """
        }
    ]


def read_csv(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name, sep=";")
    df['s_tabl_figu_id'] = df['s_tabl_figu_id'].astype('string')
    df['s_tabl_figu_id'] = df['s_tabl_figu_id'].str.strip()
    return df


SCENARIOS = [
    Scenario("Oil Price Increase",
             "In the scenario Oil Price Increase, the world oil price increases by 5 percent compared to the average annual price in the base. A global energy crisis creates the increase in world oil prices.",
             read_csv("scen05_01.csv")),
    Scenario("Water Price Increase",
             "In the scenario Water Price Increase the water tax rate increases by 5 percentage points compared to the model internal calibrated base tax rate. Government or water suppliers increase the tax rate for water to generate funding from water service. Only the increase of the tax rate is simulated. The usage of the collected money is not determined.",
             read_csv("scen04_01.csv")),
    Scenario("Sewage Disposal",
             "n the scenario Sewage Disposal increasing the tax rate for non-collective sewage disposal by 5% and decreasing the tax rate for collective sewage disposal by 5%. Price incentives are implemented to motivate households to switch from the polluting non-collective disposal system to the less polluting collective disposal system. Only the impacts of the pricing are considered, not the costs for building collective sewage disposal installations. Furthermore, we assume that the increased tax rate applies to all water users that are not connected to the collective disposal system. We assume that they have technically the possibility to choose between public and non-collective system, which might not apply in reality",
             read_csv("scen03_01.csv")),
    # Scenario("Reduced Leakage",
    #         "n the scenario Reduced Leakage losses of piped water by leakages are reduced by 0.5%. The water pipes are fixed to reduce the leakage of water during distribution. Only the impacts of the reparation are considered not the costs.",
    #         read_csv("scen02_01.csv")),
    Scenario("Water Scarcity",
             "The scenario Water Scarcity simulates a situation of water scarcity. The availability of ground- and surface water are reduced by each 5%. Climate change reduces the precipitation on Reunion Island. The reduced availability of raw water makes the access to raw water more expensive.",
             read_csv("scen01_01.csv")),
]

st.write("""
        <style>
        .stMarkdown {
            text-align: justify;
        }
        .figure {
            font-size: 16px;
            text-align: center;
        }
        .notes {
            font-size: 13px;
            text-align: justify;
        }
        </style> """, unsafe_allow_html=True)
st.title("CGE Model")
st.markdown("""
A **computable general equilibrium (CGE)** model is a **macroeconomic simulation** and analysis tool. The CGE model represents, in mathematical functions, the economic mechanisms of exchanging monetary values between economic activities, **factors**, **agents** and **markets** (including prices). Thus, the CGE model can simulate a whole economic system at a macroeconomic scale. CGE models are used to analyse economic scenarios, such as economic shocks or policies (e.g., water scarcity or pricing policies). CGE model simulation results are usually expressed in relative changes compared to the **reference** scenario. Thus, the CGE model simulation can inform how the **economic** system changes because of changes in settings compared to the situation if the economic settings stay unchanged. Thus, CGE models are not forecasting instruments; they only analyse how the economy changes if certain events occur. With this, CGE models help researchers analyse the impacts of events and understand the direct and indirect economic mechanisms that can appear during such an event. CGE models are calibrated to the data of a **Social Accounting Matrix (SAM)**, which represents a snapshot of a country or region in a given year. CGE models can represent different temporal (static or dynamic) or regional resolutions (single-country or multi-country).
""")
st.divider()
st.subheader("Model Information", anchor="model-information")

st.markdown(
    """
    - **Model name**: REWEFE-CGE model (the Reunion Island WEFE nexus CGE model)
    - **Info about the REWEFE-CGE model**: [Link to documentation](https://www.innwater.eu/media-center#deliverables)
    - **Link to the REWEFE-working paper**: [Link to the REWEFE-working paper](https://www.innwater.eu/media-center#deliverables)
    - **Standard model**: PEP single country static standard model (PEP 1-1)
    - Info about the PEP-1-1 standard model: [Link to documentation](https://www.pep-net.org/research-resources/cge-models )
    - **Citation**: Decaluwé et al. (2013) PEP-1-1: the PEP standard single-country, static CGE model. Version 2.1. Partnership for Economic Policy (PEP). Model documentation.
    - **Date of model version**: 2023-03-12
    """
)

macroeconomic_closures = """
The macroeconomic closure, or "model closure," defines the macroeconomic conditions in which the CGE model operates and which model variables are set externally (exogenously fixed).
- World prices: fixed (small country assumption)
- Households minimum consumption: fixed
- The current account balance: fixed
- Changes in stocks: fixed
- Governmental spending: fixed
- Tax rates: fixed
- Production factor supply (labour and capital): fixed
- Exchange rate: fixed with the value of 1 (= numeraire)
- Mobility of capital: capital is sector specific
"""


def show_figure(df, fig_id: str, caption: str, notes: str):
    st.write("<br>", unsafe_allow_html=True)
    st.bar_chart(df[df['s_tabl_figu_id'] == fig_id], x='s_sam_col', y='valu')
    st.write("""
             <div class="figure">
             <b>Figure</b>: {}
             </div>
             """.format(caption), unsafe_allow_html=True)
    st.write("""
            <br>
            <div class="notes">
            <b>Notes</b>: {}
            </div>
            """.format(notes), unsafe_allow_html=True)


def show_table(df, table_id: str, caption: str, notes: str):
    st.write("""
             <br>
             <div class="figure">
             <b>Table</b>: {}
             </div>
             """.format(caption), unsafe_allow_html=True)
    filter_df = df[df['s_tabl_figu_id'] == table_id]
    tab_df = filter_df.pivot(
        index="s_sam_row", columns="s_sam_col", values="valu")
    cols = filter_df['s_sam_col'].unique()
    if (len(tab_df) == 1):
        st.dataframe(tab_df[cols].transpose(), use_container_width=True)
    else:
        st.dataframe(tab_df[cols], use_container_width=True)
    st.write("""
            <div class="notes">
            <b>Notes</b>: {}
            </div>
            <br>
            """.format(notes), unsafe_allow_html=True)


st.divider()

selected_scenario = st.selectbox(
    "Select a scenario:",
    options=[scenario.name for scenario in SCENARIOS],
    index=0
)

# Replace the tabs section with a single scenario display based on selection
selected_index = [scenario.name for scenario in SCENARIOS].index(
    selected_scenario)
scenario = SCENARIOS[selected_index]
st.header(scenario.name)
st.subheader("Scenario assumptions", anchor="scenario-assumptions")
st.write(scenario.description)
st.subheader("Macroeconomic closures")
st.markdown(macroeconomic_closures)
sections = {"Macroeconomic indicators": show_macroeconomic,
            "Activity and Commodities": get_activities,
            "Commodity and Factor prices": get_commodity_prices,
            "Government and households": show_government_household,
            "WEFE Nexus": show_wefe,
            "Micro Simulation Model": get_msm}

selection_columns = st.columns([0.7, 0.3])
with selection_columns[0]:
    selection = st.multiselect(
        "Select one or more indicators", list(sections.keys()), default=list(sections.keys()))

i = 1
selected_sections = []
for section_value in sections:
    if section_value in selection:
        section_ = sections[section_value](scenario)
        section_.show_section(i)
        st.divider()
        selected_sections.append(section_)
        i += 1

with st.container(key="container-chat"):
    with st.popover("Start a conversation", use_container_width=True):
        js_code = """function checkHeaders() {
            let headers = window.parent.document.querySelectorAll("h3");
            while (headers.length == 0) {
                headers = window.parent.document.querySelectorAll("h3");
            }
            let visibilityMap = {};
            headers.forEach(header => {
                const rect = header.getBoundingClientRect();
                // Mark true if the header is in view or has been scrolled past
                visibilityMap[header.id] = rect.top - 800 < window.innerHeight;
            });
            return visibilityMap;
            }();"""
        with st.container(key="js-container", height=0):
            sections_seen = st_javascript(js_code=js_code)
        prompting_info = {}
        print("sections_seen", sections_seen)
        if sections_seen == 0:
            sections_seen = {}
        filtered_sections = list(filter(lambda x: x[0] in SECTION_IDS, sections_seen.items()))
        if len(filtered_sections):
            st.write("Select any data you would like to get from:")
        cols = st.columns([1] * max(1, len(filtered_sections)))
        for i, (section_id, is_section_seen) in enumerate(filtered_sections):
            with cols[i]:
                prompting_info[section_id] = st.checkbox(SECTION_IDS[section_id], value=is_section_seen)
        cols = st.columns([0.83, 0.17])
        with cols[0]:
            input = st.chat_input()
            if input:
                st.session_state.popover_messages.append({"role": "user", "content": input})
        with cols[1]:
            clear_chat = st.button("Clear chat")
            if clear_chat:
                st.session_state.popover_messages = [{
                    "role": "assistant",
                    "content": """
            Hello! I am the InnWater AI Assistant, an artificial intelligence system created to help you navigate the InnWater project's digital tools and governance resources. I provide insights and guidance based solely on public, validated InnWater project documents.

            Please remember that I am an AI, not a human expert. My role is to assist your understanding and learning, but final decisions and action plans should be made by you and your group, based on your critical discussions and collective judgment.

            Our chat is not saved, and your data is not used for training. If you're okay with that, feel free to start the conversation and I'll guide you from there!

            You can verify the sources behind my answers.
            """
                }]
        with st.container(height=min(400, (len(st.session_state.popover_messages) + int(
                len(st.session_state.popover_messages) != 0)) * 150)):
            for message in st.session_state.popover_messages:
                role = message["role"]
                material_symbol = ":material/person:" if role == "user" else "https://www.innwater.eu/sites/default/files/InnWater%20logo_0.png"
                with st.chat_message(role, avatar=material_symbol):
                    st.markdown(message["content"])
            if input:
                current_checked_sections = []
                for selected_section_anchor, has_selected_to_ask in prompting_info.items():
                    if not has_selected_to_ask:
                        continue
                    for section in selected_sections:
                        if selected_section_anchor == section.anchor:
                            current_checked_sections.append(section)
                stream_text = ask_to_ai_assistant(st.session_state.popover_messages, scenario.name,
                                                  scenario.description + macroeconomic_closures,
                                                  current_checked_sections)
                with st.chat_message("assistant",
                                     avatar="https://www.innwater.eu/sites/default/files/InnWater%20logo_0.png"):
                    placeholder = st.empty()  # for the spinner

                    with placeholder.container():
                        with st.spinner("Thinking..."):
                            first_chunk = next(stream_text, None)
                    if first_chunk is not None:
                        placeholder.empty()  # remove spinner
                    content = st.write_stream(
                        itertools.chain([first_chunk], stream_text)
                    )
                st.session_state.popover_messages.append({"role": "assistant", "content": content})
st.markdown("""
        #### Acknowledgements
        The authors would like to thank Yves Croissant, Sabine Garabedian, Zoulfikar Mehoumoud Issop, François Hermet, and Alexis Parmentier from CEMOI (Centre d'Économie et de Management de l'Océan Indien) for kindly providing access to the Social Accounting Matrix used in this study. The Social Accounting Matrix was developped within the project OMEGA (Outre-mer : Modèles d'équilibre Général Appliqués) with the contribution of the french Ministry of the Interior and Overseas Territories.
""")


# Helper function to convert image to base64
def get_image_as_base64(image_path):
    import base64
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


embed = st.query_params.get("hide_footer", "0") == "1"  # new API
# older: st.experimental_get_query_params()

if not embed:
    # Add footer with funding information
    st.markdown("""
    <style>
    .footer {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #e0e0e0;
        text-align: center;
    }
    .footer img {
        max-width: 400px;
        margin-bottom: 15px;
    }
    .footer p {
        font-size: 14px;
        color: #666;
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }
    </style>
    <div class="footer">
        <img src="data:image/png;base64,""" + get_image_as_base64("funded_by.png") + """\" alt="Funded by EU and UKRI">
        <p>This project has received funding from the European Union's Horizon Europe programme (Grant Agreement No. 101086512) and from UK Research and Innovation (UKRI) under the UK government's Horizon Europe funding guarantee (Grant No. 10066637).</p>
    </div>
    """, unsafe_allow_html=True)
