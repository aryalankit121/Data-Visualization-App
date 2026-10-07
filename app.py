import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 1. PAGE SETUP
# ---------------------------------------------------------
st.set_page_config(
    page_title="2025 311 Service Requests Dashboard",
    layout="wide"
)

st.title("📊 2025 311 Service Requests Dashboard")

st.write(
    "This dashboard explores 311 service requests submitted in 2025. "
    "Use the controls on the left to select a date range, agency, "
    "and request status."
)


# ---------------------------------------------------------
# 2. LOAD THE DATA
# ---------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("311_2025_dashboard.csv")

    # Convert request_date to datetime
    df["request_date"] = pd.to_datetime(
        df["request_date"],
        errors="coerce"
    )

    return df


df = load_data()


# ---------------------------------------------------------
# 3. SIDEBAR CONTROLS
# ---------------------------------------------------------
st.sidebar.header("Dashboard Controls")

# Get the date range available in the dataset
min_date = df["request_date"].min().date()
max_date = df["request_date"].max().date()


# Start date
start_date = st.sidebar.date_input(
    "Start Date",
    value=min_date,
    min_value=min_date,
    max_value=max_date
)


# End date
end_date = st.sidebar.date_input(
    "End Date",
    value=max_date,
    min_value=min_date,
    max_value=max_date
)


# Check that the dates make sense
if start_date > end_date:
    st.sidebar.error("Start Date must be on or before End Date.")
    st.stop()


# ---------------------------------------------------------
# 4. ADDITIONAL INTERACTIVE CONTROL
# ---------------------------------------------------------

# Agency filter
all_agencies = sorted(
    df["agency_responsible"]
    .dropna()
    .unique()
)

selected_agencies = st.sidebar.multiselect(
    "Responsible Agency",
    options=all_agencies,
    default=all_agencies
)


# Status filter
all_statuses = sorted(
    df["status"]
    .dropna()
    .unique()
)

selected_statuses = st.sidebar.multiselect(
    "Request Status",
    options=all_statuses,
    default=all_statuses
)


# ---------------------------------------------------------
# 5. FILTER THE DATA
# ---------------------------------------------------------
filtered_df = df[
    (df["request_date"].dt.date >= start_date)
    & (df["request_date"].dt.date <= end_date)
    & (df["agency_responsible"].isin(selected_agencies))
    & (df["status"].isin(selected_statuses))
].copy()


# ---------------------------------------------------------
# 6. SUMMARY METRICS
# ---------------------------------------------------------
st.subheader("Summary")

col1, col2, col3, col4 = st.columns(4)


# Metric 1
with col1:
    st.metric(
        "Total Requests",
        f"{len(filtered_df):,}"
    )


# Metric 2
with col2:
    unique_services = filtered_df["service_type"].nunique()

    st.metric(
        "Service Types",
        f"{unique_services:,}"
    )


# Metric 3
with col3:
    if not filtered_df.empty:
        closed_percent = (
            (filtered_df["status"] == "Closed").mean() * 100
        )
        st.metric(
            "Percent Closed",
            f"{closed_percent:.1f}%"
        )
    else:
        st.metric("Percent Closed", "0.0%")


# Metric 4
with col4:
    if not filtered_df.empty:
        avg_resolution = filtered_df["resolution_days"].mean()

        st.metric(
            "Average Resolution Time",
            f"{avg_resolution:.1f} days"
        )
    else:
        st.metric("Average Resolution Time", "N/A")


st.divider()


# ---------------------------------------------------------
# 7. CHARTS
# ---------------------------------------------------------
if filtered_df.empty:

    st.warning(
        "No requests match the selected filters. "
        "Try changing the date range or filters."
    )

else:

    # =====================================================
    # CHART 1: REQUESTS BY RESPONSIBLE AGENCY
    # =====================================================

    st.subheader("1. 311 Requests by Responsible Agency")

    agency_counts = (
        filtered_df["agency_responsible"]
        .value_counts()
        .head(10)
        .sort_values()
    )

    fig1, ax1 = plt.subplots(figsize=(9, 5))

    agency_counts.plot(
        kind="barh",
        ax=ax1
    )

    ax1.set_title("311 Requests by Responsible Agency")
    ax1.set_xlabel("Number of Requests")
    ax1.set_ylabel("Agency")

    plt.tight_layout()

    st.pyplot(fig1)


    # =====================================================
    # CHART 2: AVERAGE RESOLUTION TIME
    # =====================================================

    st.subheader(
        "2. Average Resolution Time for Top Request Types"
    )

    # Find the 10 most common request types
    top_services = (
        filtered_df["service_type"]
        .value_counts()
        .head(10)
        .index
    )

    # Calculate average resolution time
    avg_res_time = (
        filtered_df[
            filtered_df["service_type"].isin(top_services)
        ]
        .groupby("service_type")["resolution_days"]
        .mean()
        .sort_values()
    )

    fig2, ax2 = plt.subplots(figsize=(9, 5))

    avg_res_time.plot(
        kind="barh",
        ax=ax2
    )

    ax2.set_title(
        "Average Resolution Time (Days) for Top Request Types"
    )
    ax2.set_xlabel("Average Days to Close")
    ax2.set_ylabel("Service Type")

    plt.tight_layout()

    st.pyplot(fig2)


    # =====================================================
    # CHART 3: REQUESTS OVER TIME
    # =====================================================

    st.subheader("3. 311 Requests Over Time")

    requests_by_day = (
        filtered_df
        .groupby("request_date")
        .size()
    )

    fig3, ax3 = plt.subplots(figsize=(10, 4))

    requests_by_day.plot(
        kind="line",
        ax=ax3
    )

    ax3.set_title("311 Requests Over Time")
    ax3.set_xlabel("Request Date")
    ax3.set_ylabel("Number of Requests")

    plt.tight_layout()

    st.pyplot(fig3)

