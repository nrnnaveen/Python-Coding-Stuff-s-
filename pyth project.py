
# app.py
import streamlit as as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import io
import os
from dotenv im st
import pandasport load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()

st.set_page_config(page_title="Dropout Risk Dashboard", layout="wide")

st.title("AI-Based Dropout Prediction & Counseling — Prototype")
st.markdown(
    """
A lightweight, transparent dashboard that **fuses attendance, test scores, and fee data** to surface early risk signals.
"""
)

# ---------- Utility: sample CSV strings ----------
ATT_SAMPLE = """student_id,name,class,month,attendance_pct
S001,Aisha,10A,2025-01,82
S001,Aisha,10A,2025-02,78
S001,Aisha,10A,2025-03,65
S002,Balu,10A,2025-01,92
S002,Balu,10A,2025-02,88
S002,Balu,10A,2025-03,90
S003,Chitra,10B,2025-01,60
S003,Chitra,10B,2025-02,58
S003,Chitra,10B,2025-03,55
S004,Dinesh,10B,2025-01,70
S004,Dinesh,10B,2025-02,68
S004,Dinesh,10B,2025-03,72
"""

TEST_SAMPLE = """student_id,name,class,test_date,subject,score,max_score
S001,Aisha,10A,2025-01-15,Math,45,100
S001,Aisha,10A,2025-02-15,Math,42,100
S001,Aisha,10A,2025-03-20,Math,35,100
S002,Balu,10A,2025-01-15,Math,84,100
S002,Balu,10A,2025-02-15,Math,81,100
S002,Balu,10A,2025-03-20,Math,85,100
S003,Chitra,10B,2025-01-15,Math,30,100
S003,Chitra,10B,2025-02-15,Math,28,100
S003,Chitra,10B,2025-03-20,Math,32,100
S004,Dinesh,10B,2025-01-15,Math,60,100
S004,Dinesh,10B,2025-02-15,Math,55,100
S004,Dinesh,10B,2025-03-20,Math,62,100
"""

FEES_SAMPLE = """student_id,name,class,fee_due_months,fee_status,last_payment_date
S001,Aisha,10A,0,Paid,2025-03-01
S002,Balu,10A,0,Paid,2025-03-10
S003,Chitra,10B,2,Part-Paid,2025-01-15
S004,Dinesh,10B,1,Due,2025-02-10
"""

# ---------- Upload or sample toggle ----------
st.sidebar.header("Data input")
use_sample = st.sidebar.checkbox("Use sample data (quick demo)", value=True)

uploaded_att = st.sidebar.file_uploader("Upload attendance CSV", type=["csv"])
uploaded_tests = st.sidebar.file_uploader("Upload tests CSV", type=["csv"])
uploaded_fees = st.sidebar.file_uploader("Upload fees CSV", type=["csv"])

@st.cache_data
def load_df_from_uploaded(uploaded, sample_text):
    if uploaded is not None:
        return pd.read_csv(uploaded)
    else:
        return pd.read_csv(io.StringIO(sample_text))

attendance_df = load_df_from_uploaded(uploaded_att, ATT_SAMPLE if use_sample else ATT_SAMPLE)
tests_df = load_df_from_uploaded(uploaded_tests, TEST_SAMPLE if use_sample else TEST_SAMPLE)
fees_df = load_df_from_uploaded(uploaded_fees, FEES_SAMPLE if use_sample else FEES_SAMPLE)

# ---------- Data cleaning & aggregates ----------
# tests: compute percent score and per-student average + failed attempts
tests_df['test_date'] = pd.to_datetime(tests_df['test_date'])
tests_df['score_pct'] = (tests_df['score'] / tests_df['max_score']) * 100

test_avg = tests_df.groupby('student_id').agg(
    tests_avg_pct = ('score_pct', 'mean'),
    tests_latest_pct = ('score_pct', 'last'),
    failed_attempts = ('score_pct', lambda x: (x < 40).sum())
).reset_index()

# attendance: compute latest attendance and trend (list)
attendance_df['month_dt'] = pd.to_datetime(attendance_df['month'])
att_agg = attendance_df.sort_values(['student_id','month_dt']).groupby('student_id').agg(
    attendance_latest = ('attendance_pct', 'last'),
    attendance_avg = ('attendance_pct', 'mean')
).reset_index()

# fees: take fee_due_months and status
fees_agg = fees_df.groupby('student_id').agg(
    fee_due_months = ('fee_due_months','last'),
    fee_status = ('fee_status','last'),
    last_payment_date = ('last_payment_date','last')
).reset_index()

# Build master student table
# We'll try to preserve name/class from any of the sources
names = pd.concat([
    attendance_df[['student_id','name','class']],
    tests_df[['student_id','name','class']],
    fees_df[['student_id','name','class']]
]).drop_duplicates(subset=['student_id']).set_index('student_id')

master = pd.DataFrame(index=names.index).reset_index().rename(columns={'index':'student_id'})
master = master.merge(names.reset_index(), on='student_id', how='left')
master = master.merge(att_agg, on='student_id', how='left')
master = master.merge(test_avg, on='student_id', how='left')
master = master.merge(fees_agg, on='student_id', how='left')
master.fillna({'attendance_latest':0,'tests_avg_pct':0,'failed_attempts':0,'fee_due_months':0,'fee_status':'Unknown'}, inplace=True)

# ---------- Risk engine ----------
def compute_risk_score(row):
    points = 0
    att = row.get('attendance_latest', 0) or 0
    test = row.get('tests_avg_pct', 0) or 0
    failed = int(row.get('failed_attempts', 0) or 0)
    fee_months = int(row.get('fee_due_months', 0) or 0)

    # Attendance rules
    if att < 60:
        points += 3
    elif att < 70:
        points += 2
    elif att < 75:
        points += 1

    # Test performance
    if test < 50:
        points += 2
    elif test < 60:
        points += 1

    # Failed attempts
    if failed >= 2:
        points += 2
    elif failed == 1:
        points += 1

    # Fee dues
    if fee_months >= 2:
        points += 2
    elif fee_months == 1:
        points += 1

    return points

def risk_label_and_emoji(points):
    if points >= 5:
        return "High Risk", "🔴"
    elif points >= 3:
        return "Moderate Risk", "🟡"
    else:
        return "Low Risk", "🟢"

master['risk_points'] = master.apply(compute_risk_score, axis=1)
master[['risk_label','risk_emoji']] = master.apply(lambda r: pd.Series(risk_label_and_emoji(r['risk_points'])), axis=1)

# ---------- Dashboard UI ----------
st.sidebar.header("Filters")
classes = master['class'].dropna().unique().tolist()
sel_class = st.sidebar.selectbox("Class (filter)", options=["All"] + classes, index=0)
search_name = st.sidebar.text_input("Search student name (substring)")

df_display = master.copy()
if sel_class != "All":
    df_display = df_display[df_display['class'] == sel_class]
if search_name.strip():
    df_display = df_display[df_display['name'].str.contains(search_name, case=False, na=False)]

# Summary numbers
col1, col2, col3, col4 = st.columns(4)
total_students = len(df_display)
reds = len(df_display[df_display['risk_label'] == "High Risk"])
yellows = len(df_display[df_display['risk_label'] == "Moderate Risk"])
greens = len(df_display[df_display['risk_label'] == "Low Risk"])

col1.metric("Total students", total_students)
col2.metric("High risk 🔴", reds)
col3.metric("Moderate 🟡", yellows)
col4.metric("Low risk 🟢", greens)

st.markdown("### Student risk table")
# show a compact table with emoji and salient fields
table_cols = ['student_id','name','class','attendance_latest','tests_avg_pct','failed_attempts','fee_due_months','fee_status','risk_emoji','risk_label','risk_points']
st.dataframe(df_display[table_cols].sort_values(['risk_points'], ascending=False).rename(columns={
    'attendance_latest':'Attendance(%)','tests_avg_pct':'TestAvg(%)','failed_attempts':'FailedAttempts','fee_due_months':'FeeDueMonths'
}), height=350)

# ---------- Student profile area ----------
st.markdown("### Student profile & trends")
student_list = df_display['student_id'].tolist()
selected = st.selectbox("Select student (by ID)", options=student_list)

if selected:
    st.subheader(f"Profile — {selected} | {master.loc[master['student_id']==selected,'name'].values[0]}")
    row = master[master['student_id']==selected].iloc[0]
    # show key cards
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Attendance (latest %)", f"{row['attendance_latest']:.1f}")
    c2.metric("Tests avg (%)", f"{row['tests_avg_pct']:.1f}")
    c3.metric("Failed attempts", int(row['failed_attempts']))
    c4.metric("Fee due months", int(row.get('fee_due_months',0)))
    st.write(f"Risk: **{row['risk_label']}** {row['risk_emoji']} (Points: {row['risk_points']})")

    # Attendance trend
    att_trend = attendance_df[attendance_df['student_id']==selected].sort_values('month_dt')
    if not att_trend.empty:
        fig_att = px.line(att_trend, x='month_dt', y='attendance_pct', title='Attendance trend', markers=True)
        st.plotly_chart(fig_att, use_container_width=True)
    else:
        st.info("No attendance trend data available for this student.")

    # Test scores trend
    test_trend = tests_df[tests_df['student_id']==selected].sort_values('test_date')
    if not test_trend.empty:
        fig_test = px.line(test_trend, x='test_date', y='score_pct', color='subject', title='Test score trend', markers=True)
        st.plotly_chart(fig_test, use_container_width=True)
    else:
        st.info("No test history available for this student.")

    # Mentor notes (local only for prototype)
    st.markdown("**Mentor notes / intervention plan**")
    notes = st.text_area("Add mentor notes (this is local in prototype)", height=120)
    if st.button("Save note (local)"):
        st.success("Note saved locally (prototype). In production persist to database.")

# ---------- Notification / Alerts export ----------
st.markdown("---")
st.header("Notifications & Alerts")

st.write("Select threshold to generate alerts for mentors/guardians.")
alert_level = st.selectbox("Alert level", options=["High Risk only","High + Moderate"], index=1)
if alert_level == "High Risk only":
    alert_df = master[master['risk_label'] == "High Risk"]
else:
    alert_df = master[master['risk_label'].isin(["High Risk","Moderate Risk"])]

st.write(f"{len(alert_df)} students match alert criteria.")
# build messages
def make_message(r):
    return f"Alert: {r['name']} (ID: {r['student_id']}) is {r['risk_label']} {r['risk_emoji']}. Attendance: {r.get('attendance_latest',0):.1f}%, Tests avg: {r.get('tests_avg_pct',0):.1f}%. Please intervene."

alert_df['message'] = alert_df.apply(make_message, axis=1)
st.dataframe(alert_df[['student_id','name','class','risk_label','risk_points','message']])

csv_bytes = alert_df[['student_id','name','class','risk_label','risk_points','message']].to_csv(index=False).encode('utf-8')
st.download_button("Download alerts CSV", data=csv_bytes, file_name="alerts.csv", mime="text/csv")

# Optional: send email (prototype)
st.markdown("#### (Optional) Send email alerts — configure SMTP in .env")
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT") or 587)
smtp_user = os.getenv("SMTP_USER")
smtp_pass = os.getenv("SMTP_PASS")
if smtp_user and smtp_pass:
    send_now = st.button("Send sample emails to test SMTP (will loop over alert_df)")
    if send_now:
        sent = 0
        for idx, r in alert_df.iterrows():
            try:
                msg = EmailMessage()
                msg['Subject'] = f"Student alert: {r['name']} ({r['student_id']})"
                msg['From'] = smtp_user
                # For prototype: send to smtp_user (no guardian addresses available)
                msg['To'] = smtp_user
                msg.set_content(r['message'])
                with smtplib.SMTP(smtp_server, smtp_port) as s:
                    s.starttls()
                    s.login(smtp_user, smtp_pass)
                    s.send_message(msg)
                sent += 1
            except Exception as e:
                st.error(f"Error sending for {r['student_id']}: {e}")
        st.success(f"Sent {sent} test emails (to SMTP user).")
else:
    st.info("SMTP env vars not set. To enable sending, create a .env with SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS")

# ---------- Optional: quick ML (if you have labeled historical data) ----------
st.markdown("---")
st.header("Optional: Train a simple ML model (if you have 'dropped_out' labels)")

st.markdown("If you have a CSV with columns `student_id,dropped_out(0/1)`, upload it to train a simple model that uses the computed features.")
lab = st.file_uploader("Upload labels CSV (optional)", type=['csv'])
if lab is not None:
    labels = pd.read_csv(lab)
    df_ml = master.merge(labels[['student_id','dropped_out']], on='student_id', how='inner').dropna(subset=['dropped_out'])
    if len(df_ml) < 10:
        st.warning("Need more labeled rows for a meaningful model. Using at least 30 rows is recommended.")
    else:
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score, classification_report

        X = df_ml[['attendance_latest','tests_avg_pct','failed_attempts','fee_due_months']].fillna(0)
        y = df_ml['dropped_out'].astype(int)
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25, random_state=42)
        clf = LogisticRegression(max_iter=200).fit(X_train,y_train)
        preds = clf.predict(X_test)
        st.write("Accuracy on holdout:", accuracy_score(y_test, preds))
        st.text(classification_report(y_test, preds))
        st.success("Trained a simple logistic regression. Use it carefully and explain bias/limitations to judges.")
