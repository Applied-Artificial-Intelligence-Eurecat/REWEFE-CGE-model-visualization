from abc import abstractmethod, ABC

import streamlit as st
from dataclasses import dataclass
from typing import List, Dict, Tuple
import plotly.express as px

class Data(ABC):

    def __init__(self):
        self.df = None
        self.caption = None
        self.notes = None

    @abstractmethod
    def show(self):
        pass


class Figure(Data):

    def __init__(self, df, figure_id, caption, notes):
        super().__init__()
        self.caption = caption
        self.notes = notes
        self.df = df[df['s_tabl_figu_id'] == figure_id]

    def show(self):
        st.write("<br>", unsafe_allow_html=True)
        fig = px.bar(self.df, x='s_sam_col', y='valu',)
        st.plotly_chart(fig)
        st.write("""
                     <div class="figure">
                     <b>Figure</b>: {}
                     </div>
                     """.format(self.caption), unsafe_allow_html=True)
        st.write("""
                    <br>
                    <div class="notes">
                    <b>Notes</b>: {}
                    </div>
                    """.format(self.notes), unsafe_allow_html=True)


class Table(Data):

    def __init__(self, df, table_id, caption, notes):
        super().__init__()
        self.caption = caption
        self.notes = notes
        self.df = df[df['s_tabl_figu_id'] == table_id]
        tab_df = self.df.pivot(
            index="s_sam_row", columns="s_sam_col", values="valu")
        cols = self.df['s_sam_col'].unique()
        if len(tab_df) == 1:
            self.df = tab_df[cols].transpose()
        else:
            self.df = tab_df[cols]

    def show(self):
        st.write("""
                     <br>
                     <div class="figure">
                     <b>Table</b>: {}
                     </div>
                     """.format(self.caption), unsafe_allow_html=True)
        st.dataframe(self.df, use_container_width=True)
        st.write("""
                    <div class="notes">
                    <b>Notes</b>: {}
                    </div>
                    <br>
                    """.format(self.notes), unsafe_allow_html=True)


@dataclass
class Section:
    title: str
    anchor: str
    description: str
    data: Dict[str, Data]
    columns: List[Tuple[List[str], List[int]]]

    def show_section(self, i):
        st.subheader(f"{i}. {self.title}", anchor=self.anchor)
        st.write(self.description)
        for col in self.columns:
            keys, widths = col
            columns_container = st.columns(widths)
            for key, column in zip(keys, columns_container):
                if key in self.data:
                    with column:
                        self.data[key].show()

    def to_markdown(self):
        markdown = f"### {self.title}\n\n"
        markdown += f"{self.description}\n\n"
        for col in self.columns:
            keys, _ = col
            for key in keys:
                if key in self.data:
                    markdown += self.data[key].df.to_markdown()
                    markdown += f"- **{key}**: {self.data[key].caption}\n"
                    markdown += f"  Notes: {self.data[key].notes}\n\n"
        return markdown


@dataclass
class HeadersSection(Section):
    headers: List[str]

    def show_section(self, i):
        st.subheader(f"{i}. {self.title}", anchor=self.anchor)
        st.write(self.description)
        for header, col in zip(self.headers, self.columns):
            keys, widths = col
            if len(header) != 0:
                st.markdown(f"#### {header}")
            columns_container = st.columns(widths)
            for key, column in zip(keys, columns_container):
                if key in self.data:
                    with column:
                        self.data[key].show()

    def to_markdown(self):
        markdown = f"### {self.title}\n\n"
        markdown += f"{self.description}\n\n"
        for header, col in zip(self.headers, self.columns):
            keys, _ = col
            if len(header) != 0:
                markdown += f"#### {header}\n\n"
            for key in keys:
                if key in self.data:
                    markdown += self.data[key].df.to_markdown()
                    markdown += f"- **{key}**: {self.data[key].caption}\n"
                    markdown += f"  Notes: {self.data[key].notes}\n\n"
        return markdown
