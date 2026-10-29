
import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Student Performance Studio",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# CSS styling: white background and black text
# --------------------------------------------------
st.markdown("""
<style>
/* Global light theme with high-contrast text */
.stApp {
    background: #f3f6fb;
    color: #172033;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.stApp h1, .stApp h2, .stApp h3, .stApp h4,
.stApp p, .stApp label, .stApp span,
.stApp .stMarkdown, .stApp [data-testid="stCaptionContainer"] {
    color: #172033;
}

/* Keep the title banner visually distinct */
.hero {
    padding: 1.7rem;
    border-radius: 22px;
    color: #ffffff !important;
    background: linear-gradient(115deg, #172554, #1d4ed8, #6d28d9);
    margin-bottom: 1.2rem;
    box-shadow: 0 8px 22px rgba(30, 64, 175, 0.16);
}

.hero h1 {
    color: #ffffff !important;
    margin: 0;
}

.hero p {
    color: #eaf2ff !important;
    margin: .3rem 0 0;
}

/* Summary cards */
.kpi {
    background: #ffffff;
    border: 1px solid #d8e0ed;
    border-radius: 16px;
    padding: 1rem;
    min-height: 100px;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.05);
}

.klabel {
    color: #475569 !important;
    font-size: .85rem;
}

.kvalue {
    font-size: 1.7rem;
    font-weight: 750;
    color: #12316b !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #eaf0fa;
    border-right: 1px solid #d8e0ed;
}
[data-testid="stSidebar"] * {
    color: #172033 !important;
}

/* Tabs: readable in both selected and unselected states */
.stTabs [data-baseweb="tab"] {
    color: #334155 !important;
    font-weight: 600;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: #1d4ed8 !important;
}
.stTabs [data-baseweb="tab-highlight"] {
    background-color: #2563eb !important;
}

/* Inputs, dropdowns, and number fields */
.stApp input,
.stApp textarea,
.stApp [data-baseweb="select"] > div,
.stApp [data-baseweb="input"] > div {
    background-color: #ffffff !important;
    color: #172033 !important;
    border-color: #b8c5d8 !important;
}
.stApp input::placeholder,
.stApp textarea::placeholder {
    color: #64748b !important;
    opacity: 1;
}
.stApp [data-baseweb="select"] *,
.stApp [data-baseweb="popover"] * {
    color: #172033 !important;
}
.stApp [data-testid="stWidgetLabel"] label {
    color: #172033 !important;
    font-weight: 600;
}

/* Buttons */
.stApp [data-testid="stBaseButton-primary"],
.stApp [data-testid="stFormSubmitButton"] button {
    background: #1d4ed8 !important;
    color: #ffffff !important;
    border: 1px solid #1d4ed8 !important;
}
.stApp button {
    color: #ffffff;
}
.stApp button p {
    color: inherit !important;
}
.stApp [data-testid="stBaseButton-secondary"] {
    background: #ffffff !important;
    color: #1d4ed8 !important;
    border: 1px solid #9bb6e8 !important;
}

/* Data tables */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background: #ffffff;
    border: 1px solid #d8e0ed;
    border-radius: 10px;
}
[data-testid="stDataFrame"] * {
    color: #172033;
}

/* Alerts and captions */
.stAlert {
    border-radius: 10px;
}
[data-testid="stCaptionContainer"] {
    color: #64748b !important;
}

/* Links */
.stApp a {
    color: #1d4ed8 !important;
}

/* Make the leaderboard toolbar clearly visible */
[data-testid="stElementToolbar"] {
    background: #ffffff !important;
    opacity: 1 !important;
    visibility: visible !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.16) !important;
    padding: 5px 8px !important;
    z-index: 999 !important;
}

/* Keep toolbar buttons and icons high contrast */
[data-testid="stElementToolbar"] button,
[data-testid="stElementToolbar"] button:hover {
    background: #ffffff !important;
    color: #1d4ed8 !important;
    border: none !important;
    border-radius: 6px !important;
    opacity: 1 !important;
}
[data-testid="stElementToolbar"] button:hover {
    background: #dbeafe !important;
}
[data-testid="stElementToolbar"] button svg,
[data-testid="stElementToolbar"] button path {
    color: #1d4ed8 !important;
    fill: #1d4ed8 !important;
    stroke: #1d4ed8 !important;
    opacity: 1 !important;
}
[data-testid="stElementToolbar"] button:focus-visible {
    outline: 2px solid #2563eb !important;
    outline-offset: 2px !important;
}


/* Sidebar: readable filters with consistent light styling */
[data-testid="stSidebar"] {
    background: #f1f5f9 !important;
    border-right: 1px solid #dbe3ef !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #1e293b !important;
}
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] label {
    color: #1e293b !important;
    font-weight: 600 !important;
}
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] [data-baseweb="input"] > div {
    background: #ffffff !important;
    color: #1e293b !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 8px !important;
}
[data-testid="stSidebar"] input::placeholder {
    color: #64748b !important;
    opacity: 1 !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: #ffffff !important;
    color: #1e293b !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 8px !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #1e293b !important;
}
[data-testid="stSidebar"] button {
    background: #2563eb !important;
    color: #ffffff !important;
    border: 1px solid #2563eb !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}
[data-testid="stSidebar"] button * {
    color: #ffffff !important;
}
[data-testid="stSidebar"] button:hover {
    background: #1d4ed8 !important;
    border-color: #1d4ed8 !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Dashboard header
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🎓 Student Performance Studio</h1>
    <p>Academic insights • Grade tracking • Student records • Progress analytics</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Subjects and sample student records
# --------------------------------------------------
subjects = ["Python", "DBMS", "Mathematics", "English"]

sample = [
    {
        "Student ID": "STU-1001",
        "Name": "Aarav Kumar",
        "Class": "CSE-A",
        "Python": 88,
        "DBMS": 92,
        "Mathematics": 84,
        "English": 79
    },
    {
        "Student ID": "STU-1002",
        "Name": "Diya Sharma",
        "Class": "CSE-A",
        "Python": 95,
        "DBMS": 89,
        "Mathematics": 97,
        "English": 91
    },
    {
        "Student ID": "STU-1003",
        "Name": "Ishaan Reddy",
        "Class": "CSE-B",
        "Python": 72,
        "DBMS": 76,
        "Mathematics": 69,
        "English": 81
    },
    {
        "Student ID": "STU-1004",
        "Name": "Meera Patel",
        "Class": "CSE-A",
        "Python": 86,
        "DBMS": 83,
        "Mathematics": 90,
        "English": 88
    },
    {
        "Student ID": "STU-1005",
        "Name": "Arjun Rao",
        "Class": "CSE-B",
        "Python": 58,
        "DBMS": 64,
        "Mathematics": 61,
        "English": 70
    },
    {
        "Student ID": "STU-1006",
        "Name": "Ananya Das",
        "Class": "CSE-B",
        "Python": 91,
        "DBMS": 94,
        "Mathematics": 89,
        "English": 93
    },
    {
        "Student ID": "STU-1007",
        "Name": "Kabir Singh",
        "Class": "CSE-A",
        "Python": 67,
        "DBMS": 71,
        "Mathematics": 74,
        "English": 65
    },
    {
        "Student ID": "STU-1008",
        "Name": "Sana Khan",
        "Class": "CSE-B",
        "Python": 82,
        "DBMS": 87,
        "Mathematics": 80,
        "English": 85
    }
]

if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(sample)

# --------------------------------------------------
# Calculate total, average, grade and status
# --------------------------------------------------
def calc(frame):
    data = frame.copy()

    data["Total"] = data[subjects].sum(axis=1)
    data["Average"] = data[subjects].mean(axis=1).round(1)

    data["Grade"] = data["Average"].apply(
        lambda mark:
            "A+" if mark >= 90 else
            "A" if mark >= 80 else
            "B" if mark >= 70 else
            "C" if mark >= 60 else
            "Needs Support"
    )

    data["Status"] = data["Average"].apply(
        lambda mark: "Pass" if mark >= 40 else "Review"
    )

    return data

# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
with st.sidebar:
    st.header("⚙️ Filters")

    query = st.text_input("Search by name or ID")

    classes = ["All"] + sorted(
        st.session_state.students["Class"].unique().tolist()
    )

    selected_class = st.selectbox("Class", classes)

    if st.button("Reset demo data", use_container_width=True):
        st.session_state.students = pd.DataFrame(sample)
        st.rerun()

# --------------------------------------------------
# Prepare filtered data
# --------------------------------------------------
df = calc(st.session_state.students)
view = df.copy()

if query:
    mask = (
        view["Name"].str.contains(query, case=False, na=False)
        | view["Student ID"].str.contains(query, case=False, na=False)
    )
    view = view[mask]

if selected_class != "All":
    view = view[view["Class"] == selected_class]

n = len(view)
avg = view["Average"].mean() if n else 0
top = (
    view.sort_values("Average", ascending=False).iloc[0]["Name"]
    if n else "—"
)
passed = (
    view["Status"].eq("Pass").mean() * 100
    if n else 0
)

# --------------------------------------------------
# Dashboard summary cards
# --------------------------------------------------
cols = st.columns(4)

cards = [
    ("Students", str(n), "Records in view"),
    ("Class average", f"{avg:.1f}%", "Across four subjects"),
    ("Pass rate", f"{passed:.0f}%", "Configured pass threshold"),
    ("Top performer", top, "Highest average")
]

for col, (label, value, description) in zip(cols, cards):
    col.markdown(
        f"""
        <div class="kpi">
            <div class="klabel">{label}</div>
            <div class="kvalue">{value}</div>
            <div class="klabel">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Dashboard tabs
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "📊 Overview",
    "🧑‍🎓 Student records",
    "➕ Add student"
])

# ==================================================
# TAB 1: OVERVIEW AND CHARTS
# ==================================================
with tab1:

    col1, col2 = st.columns([1.2, 1])

    # --------------------------------------------------
    # Subject performance chart
    # --------------------------------------------------
    with col1:
        st.subheader("Subject performance")

        if n:
            averages = (
                view[subjects]
                .mean()
                .rename_axis("Subject")
                .reset_index(name="Average marks")
            )

            fig = px.bar(
                averages,
                x="Subject",
                y="Average marks",
                text_auto=".1f",
                range_y=[0, 100]
            )

            # Black bars and readable labels
            fig.update_traces(
                marker_color="#2563eb",
                textfont=dict(color="#000000", size=12)
            )

            fig.update_layout(
                height=350,
                margin=dict(l=10, r=10, t=15, b=10),
                paper_bgcolor="#ffffff",
                plot_bgcolor="#ffffff",
                font=dict(
                    color="#000000",
                    family="Arial",
                    size=13
                ),
                xaxis=dict(
                    title="Subject",
                    title_font=dict(color="#000000"),
                    tickfont=dict(color="#000000"),
                    gridcolor="#e5e7eb",
                    showline=True,
                    linecolor="#000000"
                ),
                yaxis=dict(
                    title="Average marks",
                    title_font=dict(color="#000000"),
                    tickfont=dict(color="#000000"),
                    gridcolor="#e5e7eb",
                    range=[0, 100],
                    showline=True,
                    linecolor="#000000"
                ),
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("No student records match your filters.")

    # --------------------------------------------------
    # Grade distribution chart
    # --------------------------------------------------
    with col2:
        st.subheader("Grade distribution")

        if n:
            grade_order = [
                "A+", "A", "B", "C", "Needs Support"
            ]

            counts = (
                view["Grade"]
                .value_counts()
                .reindex(grade_order, fill_value=0)
                .rename_axis("Grade")
                .reset_index(name="Students")
            )

            counts = counts[counts["Students"] > 0]

            fig = px.pie(
                counts,
                names="Grade",
                values="Students",
                hole=0.55,
                color_discrete_sequence=[
                    "#1d4ed8",
                    "#0f766e",
                    "#64748b",
                    "#d97706",
                    "#be123c"
                ]
            )

            # Black text on the white chart background
            fig.update_traces(
                textposition="outside",
                textinfo="label+percent",
                textfont=dict(
                    color="#000000",
                    size=12
                ),
                marker=dict(
                    line=dict(color="#ffffff", width=2)
                ),
                hoverlabel=dict(
                    bgcolor="#ffffff",
                    font=dict(color="#000000")
                )
            )

            fig.update_layout(
                height=350,
                margin=dict(l=10, r=10, t=15, b=10),
                paper_bgcolor="#ffffff",
                plot_bgcolor="#ffffff",
                font=dict(
                    color="#000000",
                    family="Arial",
                    size=13
                ),
                legend=dict(
                    font=dict(color="#000000", size=12),
                    title=dict(font=dict(color="#000000"))
                ),
                showlegend=True
            )

            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("No grade data available.")

    # --------------------------------------------------
    # Performance leaderboard
    # --------------------------------------------------
    st.subheader("Performance leaderboard")

    if n:
        leaderboard = view.sort_values(
            "Average", ascending=False
        )[
            ["Student ID", "Name", "Class"]
            + subjects
            + ["Total", "Average", "Grade", "Status"]
        ]

        st.dataframe(
            leaderboard,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "⬇️ Download CSV report",
            data=view.to_csv(index=False).encode("utf-8"),
            file_name="student_performance_report.csv",
            mime="text/csv"
        )
    else:
        st.info("No student records available for the leaderboard.")

# ==================================================
# TAB 2: STUDENT RECORDS
# ==================================================
with tab2:
    st.subheader("All student records")

    all_students = calc(st.session_state.students)

    st.dataframe(
        all_students[
            ["Student ID", "Name", "Class"]
            + subjects
            + ["Total", "Average", "Grade", "Status"]
        ],
        use_container_width=True,
        hide_index=True
    )

    options = {
        f'{row["Student ID"]} — {row["Name"]}': row["Student ID"]
        for _, row in st.session_state.students.iterrows()
    }

    if options:
        selected_student = st.selectbox(
            "Select a student to remove",
            list(options.keys())
        )

        if st.button("Remove student"):
            student_id = options[selected_student]

            st.session_state.students = (
                st.session_state.students[
                    st.session_state.students["Student ID"] != student_id
                ]
                .reset_index(drop=True)
            )

            st.rerun()
    else:
        st.info("There are no student records to display.")

# ==================================================
# TAB 3: ADD STUDENT
# ==================================================
with tab3:
    st.subheader("Add student")

    with st.form("student_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)

        student_id = col1.text_input(
            "Student ID",
            placeholder="STU-1009"
        )

        student_name = col2.text_input("Student name")

        class_name = col3.selectbox(
            "Class",
            ["CSE-A", "CSE-B", "CSE-C", "IT-A"]
        )

        mark_columns = st.columns(4)

        marks = {
            subject: mark_columns[index].number_input(
                subject,
                min_value=0,
                max_value=100,
                value=75
            )
            for index, subject in enumerate(subjects)
        }

        submitted = st.form_submit_button(
            "Add student",
            use_container_width=True
        )

        if submitted:
            if not student_id.strip() or not student_name.strip():
                st.error("Enter both student ID and student name.")

            elif st.session_state.students["Student ID"].str.lower().eq(
                student_id.strip().lower()
            ).any():
                st.error("Student ID must be unique.")

            else:
                new_student = {
                    "Student ID": student_id.strip(),
                    "Name": student_name.strip(),
                    "Class": class_name,
                    **marks
                }

                st.session_state.students = pd.concat(
                    [
                        st.session_state.students,
                        pd.DataFrame([new_student])
                    ],
                    ignore_index=True
                )

                st.success("Student added successfully.")
                st.rerun()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption(
    "Demo data is fictional. Grade bands are illustrative; "
    "adjust them to match your college's grading rules."
)
