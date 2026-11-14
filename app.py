
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Chessonomics",
    page_icon="♟️",
    layout="wide"
)

# Main heading
st.title("♟️ Chessonomics")
st.subheader(
    "Exploring Economics Through Chess, "
    "Statistics and Game Theory"
)

st.info(
    "This project uses hypothetical examples "
    "for educational analysis."
)

# Sidebar
st.sidebar.title("Project Navigation")
section = st.sidebar.selectbox(
    "Choose a section",
    [
        "Overview",
        "Chess Statistics",
        "Risk Analysis",
        "Game Theory"
    ]
)

# Overview
if section == "Overview":

    st.header("Project Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Games", "10")
    col2.metric("Win Percentage", "50%")
    col3.metric("Average Moves", "39.6")

    st.markdown("---")

    st.write(
        "Chessonomics connects chess with "
        "economic concepts such as opportunity "
        "cost, expected value, risk and strategy."
    )

    st.subheader("Project Technologies")

    st.write(
        "Python | Pandas | Matplotlib | Streamlit"
    )

# Chess Statistics
elif section == "Chess Statistics":

    st.header("Chess Results Analysis")

    results = pd.DataFrame({
        "Result": ["Win", "Draw", "Loss"],
        "Games": [5, 3, 2]
    })

    st.dataframe(results, use_container_width=True)

    fig, ax = plt.subplots()

    ax.pie(
        results["Games"],
        labels=results["Result"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Chess Game Results")

    st.pyplot(fig)
    plt.close(fig)

# Risk Analysis
elif section == "Risk Analysis":

    st.header("Expected Value and Risk")

    def calculate_risk(p, success, failure):
        ev = p * success + (1 - p) * failure

        variance = (
            p * (success - ev) ** 2
            + (1 - p) * (failure - ev) ** 2
        )

        sd = variance ** 0.5

        return ev, variance, sd

    safe = calculate_risk(0.80, 3, -1)
    risky = calculate_risk(0.40, 10, -3)

    risk_data = pd.DataFrame({
        "Strategy": ["Safe", "Risky"],
        "Expected Value": [safe[0], risky[0]],
        "Standard Deviation": [safe[2], risky[2]]
    })

    st.dataframe(risk_data, use_container_width=True)

    st.write("Both strategies have the same expected value.")
    st.write("However, the risky strategy has greater uncertainty.")

# Game Theory
elif section == "Game Theory":

    st.header("Game Theory Payoff Matrix")

    payoff = pd.DataFrame(
        [
            [3, 3],
            [1, 5],
            [5, 1],
            [2, 2]
        ],
        columns=["Player B Defensive", "Player B Aggressive"],
        index=[
            "Player A Defensive",
            "Player A Aggressive (alternative 1)",
            "Player A Aggressive (alternative 2)",
            "Both Aggressive"
        ]
    )

    st.dataframe(payoff, use_container_width=True)

    st.caption(
        "Illustrative hypothetical payoffs, "
        "not real chess tournament data."
    )

# Footer
st.markdown("---")
st.caption("Chessonomics | Economics + Chess + Statistics")

