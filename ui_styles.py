
import streamlit as st


def apply_styles():
    st.markdown("""
    <style>

    /* =========================================
       1. GLOBAL THEME
    ========================================= */

    :root {
        --navy: #0F2557;
        --navy-light: #18366F;
        --primary: #1E3A8A;
        --teal: #0D9488;
        --mint: #2DD4BF;
        --cyan: #38BDF8;
        --background: #F8FAFC;
        --surface: #FFFFFF;
        --text: #0F172A;
        --muted: #64748B;
        --border: #E2E8F0;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }

    .stApp {
        background: var(--background);
        color: var(--text);
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* =========================================
       2. SIDEBAR
    ========================================= */

    section[data-testid="stSidebar"] {
        background: var(--navy) !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] > div {
        background: var(--navy) !important;
        padding: 1.2rem 0.9rem;
    }

    section[data-testid="stSidebar"] * {
        color: #F1F5F9;
    }

    /* Sidebar Navigation Buttons */

    section[data-testid="stSidebar"] .stButton > button {
        width: 100% !important;
        min-height: 48px !important;
        background: rgba(255,255,255,0.04) !important;
        border: 1.5px solid rgba(148,163,184,0.28) !important;
        border-radius: 12px !important;
        padding: 0.72rem 1.1rem !important;
        margin-bottom: 0.65rem !important;
        color: #F1F5F9 !important;
        font-weight: 600 !important;
        text-align: left !important;
        justify-content: flex-start !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }

    section[data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(45,212,191,0.12) !important;
        border-color: #38BDF8 !important;
        color: #FFFFFF !important;
        transform: translateX(3px);
        box-shadow: 0 0 12px rgba(56,189,248,0.12) !important;
    }

    section[data-testid="stSidebar"] .stButton > button:focus {
        background: rgba(45,212,191,0.18) !important;
        border: 1.5px solid #2DD4BF !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 12px rgba(45,212,191,0.2) !important;
    }

    section[data-testid="stSidebar"] .stButton > button p {
        color: inherit !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
    }

    section[data-testid="stSidebar"] .stButton {
        margin-bottom: 4px !important;
    }

    /* Sidebar Radio Navigation */

    section[data-testid="stSidebar"] div[role="radiogroup"] > label {
        width: 100% !important;
        background: rgba(255,255,255,0.04) !important;
        border: 1.5px solid rgba(148,163,184,0.28) !important;
        border-radius: 12px !important;
        padding: 0.72rem 1rem !important;
        margin-bottom: 0.65rem !important;
        transition: all 0.2s ease !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
        background: rgba(45,212,191,0.12) !important;
        border-color: #38BDF8 !important;
    }

    /* =========================================
       3. BRAND & HEADINGS
    ========================================= */

    .brand {
        color: #FFFFFF;
        font-size: 1.55rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .brand span {
        color: var(--mint);
    }

    h1, h2, h3, h4 {
        color: var(--text);
        font-weight: 750;
        letter-spacing: -0.4px;
    }

    .section-label {
        color: var(--teal);
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 1.3px;
        text-transform: uppercase;
    }

    /* =========================================
       4. TOP BAR
    ========================================= */

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 0 20px 0;
        border-bottom: 1px solid var(--border);
        margin-bottom: 25px;
    }

    /* =========================================
       5. HERO SECTION
    ========================================= */

    .hero {
        background: linear-gradient(120deg, #0F2557, #1E3A8A);
        border-radius: 20px;
        padding: 34px;
        color: #FFFFFF;
        margin-bottom: 25px;
        box-shadow: 0 12px 30px rgba(15,37,87,0.13);
    }

    .hero h1, .hero h2, .hero h3,
    .hero p, .hero span {
        color: #FFFFFF;
    }

    .hero p {
        color: #DCE8F8;
        line-height: 1.7;
    }

    /* =========================================
       6. CARDS
    ========================================= */

    .pro-card,
    .workspace-card,
    .info-panel {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 4px 16px rgba(15,23,42,0.04);
        margin-bottom: 16px;
    }

    .pro-card:hover,
    .workspace-card:hover {
        border-color: rgba(13,148,136,0.4);
        box-shadow: 0 8px 24px rgba(15,23,42,0.07);
        transition: all 0.2s ease;
    }

    /* =========================================
       7. AUDIT CARDS
    ========================================= */

    .audit-card {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 14px;
    }

    .audit-card.verified {
        border-left: 4px solid #0D9488;
    }

    .audit-card.missing {
        border-left: 4px solid #F59E0B;
    }

    .audit-card.alert {
        border-left: 4px solid #EF4444;
    }

    /* =========================================
       8. STATUS PILLS
    ========================================= */

    .status {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 30px;
        font-size: 0.78rem;
        font-weight: 700;
    }

    .status.verified,
    .status-success {
        color: #047857;
        background: #D1FAE5;
    }

    .status.missing,
    .status-warning {
        color: #B45309;
        background: #FEF3C7;
    }

    .status.alert,
    .status-danger {
        color: #B91C1C;
        background: #FEE2E2;
    }

    /* =========================================
       9. BUTTONS
    ========================================= */

    .stButton > button {
        border-radius: 10px !important;
        font-weight: 650 !important;
        min-height: 42px;
        transition: all 0.2s ease !important;
    }

    .stButton > button[kind="primary"] {
        background: var(--primary) !important;
        border: 1px solid var(--primary) !important;
        color: #FFFFFF !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: var(--teal) !important;
        border-color: var(--teal) !important;
        box-shadow: 0 5px 14px rgba(13,148,136,0.2);
    }

    /* =========================================
       10. INPUTS & FORMS
    ========================================= */

    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input,
    .stDateInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px !important;
        border-color: #CBD5E1 !important;
        background: #FFFFFF !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: var(--teal) !important;
        box-shadow: 0 0 0 1px var(--teal) !important;
    }

    /* DARKER PLACEHOLDER TEXT */
    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #64748B !important;
        opacity: 1 !important;
    }

    label {
        color: #334155 !important;
        font-weight: 600 !important;
    }

    /* =========================================
       11. FILE UPLOADER
    ========================================= */

    [data-testid="stFileUploader"] {
        background: #F8FAFC;
        border: 1.5px dashed #94A3B8;
        border-radius: 14px;
        padding: 15px;
    }

    [data-testid="stFileUploader"]:hover {
        border-color: var(--teal);
        background: #F0FDFA;
    }

    /* REMOVE BLACK UPLOAD AREA */
    [data-testid="stFileUploader"] section {
        background: #F8FAFC !important;
    }

    [data-testid="stFileUploader"] button {
        background: #E0F2F1 !important;
        color: #134E4A !important;
        border: 1px solid #99D5CE !important;
    }


    /* =========================================
       12. TABS
    ========================================= */

    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        border-bottom: 1px solid var(--border);
    }

    .stTabs [data-baseweb="tab"] {
        color: var(--muted);
        font-weight: 650;
    }

    .stTabs [aria-selected="true"] {
        color: var(--teal) !important;
        border-bottom-color: var(--teal) !important;
    }

    /* =========================================
       13. METRICS
    ========================================= */

    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 16px;
    }

    [data-testid="stMetricValue"] {
        color: var(--navy);
        font-weight: 800;
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted);
        font-weight: 600;
    }

    /* =========================================
       14. ALERTS & GUIDANCE
    ========================================= */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    .tamil-guidance {
        background: #F0FDFA;
        border-left: 4px solid var(--teal);
        border-radius: 10px;
        padding: 16px;
        color: #134E4A;
        line-height: 1.7;
        margin: 14px 0;
    }

    /* =========================================
       15. FOOTER
    ========================================= */

    .footer {
        text-align: center;
        color: #94A3B8;
        font-size: 0.82rem;
        padding: 24px 0 10px;
        border-top: 1px solid var(--border);
        margin-top: 35px;
    }

    /* =========================================
       16. RESPONSIVE DESIGN
    ========================================= */

    @media (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }

        .hero {
            padding: 22px;
            border-radius: 15px;
        }

        .pro-card,
        .workspace-card,
        .info-panel {
            padding: 16px;
        }
    }

    /* REVIEW CHECKBOX STYLING */

    /* Unchecked */
    .st-emotion-cache-1c2lghh {
        background-color: #FFFFFF !important;
        border: 1px solid #94A3B8 !important;
        box-shadow: none !important;
    }

    /* Checked */
    .st-emotion-cache-1c2lghh:has(svg) {
        background-color: #0D9488 !important;
        border-color: #0D9488 !important;
    }

    .coming-soon-tag {
        display: inline-block;
        padding: 7px 12px;
        border: 1px solid #99D5CE;
        border-radius: 20px;
        background: #F0FDFA;
        color: #0F766E;
        font-size: 12px;
        font-weight: 600;
    }
    
    .coming-soon-tag::before {
        content: "●";
        color: #0D9488;
        font-size: 9px;
        margin-right: 8px;
        vertical-align: 1px;
    }
    
    </style>
    """, unsafe_allow_html=True)
