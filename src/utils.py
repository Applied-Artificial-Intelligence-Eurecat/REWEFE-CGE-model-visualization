import streamlit as st


def show_figure(df, fig_id: str, caption: str, notes: str):
    st.write("<br>", unsafe_allow_html=True)
    tab_df = df[df['s_tabl_figu_id'] == fig_id]
    st.bar_chart(tab_df, x='s_sam_col', y='valu')
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
    return tab_df


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
    return tab_df
