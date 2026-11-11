import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Marvel Rivals Meta Analytics", layout="wide")
st.title("Marvel Rivals Meta Analytics")
st.markdown("Competitive performance analytics across hero roles and tiers.")

def get_data(query, params=()):
    conn = sqlite3.connect("marvel_rivals.db")
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

st.sidebar.header("Filter By Role")
roles = ["All"] + get_data("SELECT DISTINCT role FROM hero_rank_stats")["role"].tolist()
selected_role = st.sidebar.selectbox("Select Role", roles)

if selected_role == "All":
    df_heroes = get_data("SELECT * FROM hero_rank_stats ORDER BY win_rate DESC")
else:
    df_heroes = get_data("SELECT * FROM hero_rank_stats WHERE role = ? ORDER BY win_rate DESC", (selected_role,))

if not df_heroes.empty:
    top_win = df_heroes.sort_values(by="win_rate", ascending=False).iloc[0]
    top_pick = df_heroes.sort_values(by="pick_rate", ascending=False).iloc[0]
    top_ban = df_heroes.sort_values(by="ban_rate", ascending=False).iloc[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Heroes Tracked", len(df_heroes))
    col2.metric("Highest Win Rate", f"{top_win['hero_name']}", f"{top_win['win_rate']}%")
    col3.metric("Highest Pick Rate", f"{top_pick['hero_name']}", f"{top_pick['pick_rate']}%")
    col4.metric("Most Banned Hero", f"{top_ban['hero_name']}", f"{top_ban['ban_rate']}%")

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Win Rate vs. Pick Rate")
    st.markdown("Size = Ban Rate")
    
    fig_scatter = px.scatter(
        df_heroes,
        x="pick_rate",
        y="win_rate",
        color="role",
        size="ban_rate",
        hover_name="hero_name",
        text="hero_name",
        labels={"pick_rate": "Pick Rate (%)", "win_rate": "Win Rate (%)", "role": "Role"},
        height=600
    )
    fig_scatter.update_traces(textposition="top center", textfont_size=9)
    fig_scatter.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_right:
    st.subheader("Win Rate Rankings")
    
    df_sorted_win = df_heroes.sort_values(by="win_rate", ascending=True)
    
    fig_bar = px.bar(
        df_sorted_win,
        x="win_rate",
        y="hero_name",
        orientation="h",
        color="role",
        labels={"win_rate": "Win Rate (%)", "hero_name": "Hero"},
        height=600
    )
    fig_bar.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("Season 10.5 Telemetry Data")
st.dataframe(df_heroes[["hero_name", "role", "tier", "win_rate", "pick_rate", "ban_rate"]], use_container_width=True)