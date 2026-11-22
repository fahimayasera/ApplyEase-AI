
import streamlit as st
import base64
from ui_styles import apply_styles
from io import BytesIO
from pypdf import PdfReader

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ApplyEase AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_styles()

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = False

if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "",
        "email": "",
        "education": "",
        "institution": "",
        "course": "",
        "year": ""
    }

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

if "review_complete" not in st.session_state:
    st.session_state.review_complete = False


# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

def navigate(page):
    st.session_state.page = page
    st.session_state.sidebar_open = False
    st.rerun()

# --------------------------------------------------
# SIDEBAR MENU
# --------------------------------------------------

@st.fragment
def render_sidebar():

    if st.button("☰  Menu", key="menu_toggle"):
        st.session_state.sidebar_open = not st.session_state.sidebar_open

    
    if st.session_state.sidebar_open:
        with st.container(key="custom_sidebar"):

            st.markdown("""
            <div style="padding:5px 5px 25px 5px;">
                <div style="font-size:24px;font-weight:800;color:white;">
                    ApplyEase <span style="color:#5EEAD4;">AI</span>
                </div>
                <div style="font-size:11px;color:#CBD5E1;margin-top:5px;">
                    YOUR APPLICATION WORKSPACE
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                '<div style="font-size:11px;color:#94A3B8;'
                'font-weight:700;letter-spacing:1px;padding:8px;">'
                'WORKSPACE</div>',
                unsafe_allow_html=True
            )

            pages = [
                ("⌂", "Dashboard"),
                ("♙", "My Profile"),
                ("⇧", "Upload Application"),
                ("✓", "Review & Complete"),
                ("✧", "Application Guidance")
            ]

            for symbol, page_name in pages:
                if st.button(
                    f"{symbol}    {page_name}",
                    key=f"nav_{page_name}",
                    use_container_width=True
                ):
                    navigate(page_name)

            st.markdown("""
            <div style="font-size:11px;color:#CBD5E1;
            margin-top:85px;padding:8px;">
                English.<br>
                Understand. Verify. Prepare.
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* GENERAL */

.stApp {
    background-color: #F8FAFC;
    color: #0F172A;
}

.block-container {
    padding-top: 0rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}


/* HIDE NATIVE SIDEBAR */

section[data-testid="stSidebar"] {
    display: none;
}


/* MENU BUTTON */

div.st-key-menu_toggle {
    position: fixed !important;
    top: 12px !important;
    left: 18px !important;
    z-index: 1000002 !important;
    width: auto !important;
    display: block !important;
    visibility: visible !important;
}

div.st-key-menu_toggle button {
    background: #FFFFFF !important;
    color: #0F2557 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 9px !important;
    min-height: 40px !important;
    padding: 6px 13px !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(15,37,87,0.12) !important;
}

div.st-key-menu_toggle button:hover {
    background: #F1F5F9 !important;
    color: #0F2557 !important;
    border-color: #94A3B8 !important;
}


/* CUSTOM SIDEBAR PANEL */

div.st-key-custom_sidebar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    bottom: 0 !important;
    width: 280px !important;
    min-width: 280px !important;
    max-width: 280px !important;
    height: 100dvh !important;
    overscroll-behavior: contain !important;
    overflow-y: auto !important;
    background: #142B57 !important;
    padding: 75px 18px 25px 18px !important;
    z-index: 1000000 !important;
    box-shadow: 5px 0 20px rgba(15, 23, 42, 0.18) !important;
}

div.st-key-custom_sidebar,
div.st-key-custom_sidebar * {
    color: #FFFFFF;
}

div.st-key-custom_sidebar .stButton button {
    background: transparent !important;
    color: #FFFFFF !important;
    border: 1px solid #3D659E !important;
    border-radius: 9px !important;
    text-align: left !important;
    padding: 12px 14px !important;
    font-size: 14px !important;
    width: 100% !important;
}

div.st-key-custom_sidebar .stButton button:hover {
    background: #244477 !important;
    border: 1px solid #5EEAD4 !important;
}


/* BUTTONS */

.stButton button,
.stFormSubmitButton button {
    background: #1E3A8A;
    color: #FFFFFF !important;
    border: 1px solid #1E3A8A;
    border-radius: 9px;
    padding: 0.55rem 1.1rem;
    font-weight: 600;
    transition: 0.2s ease;
}

.stButton button:hover,
.stFormSubmitButton button:hover {
    background: #0D9488;
    border-color: #0D9488;
    color: #FFFFFF !important;
}


/* INPUTS */

.stTextInput input,
.stSelectbox div[data-baseweb="select"],
.stTextArea textarea,
.stFileUploader section {
    background: #FFFFFF !important;
    border-radius: 9px !important;
    border-color: #CBD5E1 !important;
    color: #0F172A !important;
}

.stTextInput label,
.stSelectbox label,
.stTextArea label,
.stFileUploader label {
    color: #334155 !important;
    font-weight: 600;
}


/* TOP BAR */

.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 0 18px 0;
    border-bottom: 1px solid #E2E8F0;
    margin-bottom: 25px;
}

.brand {
    font-size: 23px;
    font-weight: 800;
    color: #1E3A8A;
    letter-spacing: -0.7px;
}

.brand span {
    color: #0D9488;
}

.top-label {
    color: #475569;
    font-size: 12px;
    font-weight: 600;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    padding: 7px 12px;
    border-radius: 20px;
}


/* HEADINGS */

.page-heading {
    font-size: 31px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.8px;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 25px;
}


/* HERO */

.hero {
    background: linear-gradient(115deg, #1E3A8A 0%, #173E78 55%, #0D9488 100%);
    border-radius: 16px;
    padding: 30px;
    color: #FFFFFF;
    margin-bottom: 25px;
}

.hero-eyebrow {
    color: #BFEDE7;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero h1 {
    color: #FFFFFF;
    font-size: 31px;
    line-height: 1.25;
    margin: 0 0 12px 0;
    font-weight: 800;
}

.hero p {
    color: #E2EAF8;
    font-size: 14px;
    line-height: 1.7;
    max-width: 680px;
    margin-bottom: 0;
}


/* WORKSPACE CARDS */

.workspace-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-top: 4px solid #0D9488;
    border-radius: 13px;
    padding: 20px;
    min-height: 175px;
    margin-bottom: 16px;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.035);
}

.card-icon {
    font-size: 23px;
    margin-bottom: 13px;
}

.card-title {
    color: #0F172A;
    font-size: 16px;
    font-weight: 750;
    margin-bottom: 8px;
}

.card-description {
    color: #475569;
    font-size: 13px;
    line-height: 1.6;
}


/* INFORMATION PANELS */

.info-panel {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 18px;
}

.panel-title {
    color: #0F172A;
    font-size: 17px;
    font-weight: 750;
    margin-bottom: 10px;
}


/* STATUS */

.verified {
    background: #F0FDF4;
    color: #15803D;
    border: 1px solid #BBF7D0;
    padding: 12px 14px;
    border-radius: 9px;
    margin: 8px 0;
    font-size: 13px;
}

.missing {
    background: #FFFBEB;
    color: #B45309;
    border: 1px solid #FDE68A;
    padding: 12px 14px;
    border-radius: 9px;
    margin: 8px 0;
    font-size: 13px;
}

.alert {
    background: #FEF2F2;
    color: #B91C1C;
    border: 1px solid #FECACA;
    padding: 12px 14px;
    border-radius: 9px;
    margin: 8px 0;
    font-size: 13px;
}


/* DIVIDER AND FOOTER */

.section-label {
    color: #1E3A8A;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.1px;
    text-transform: uppercase;
    margin: 25px 0 13px 0;
}

.footer {
    border-top: 1px solid #E2E8F0;
    padding-top: 16px;
    margin-top: 35px;
    color: #64748B;
    font-size: 12px;
    text-align: center;
}


/* REMOVE STREAMLIT DECORATIONS */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* UPLOAD APPLICATION - LIGHT THEME */

div[data-testid="stFileUploaderDropzone"] {
    background-color: #F8FAFC !important;
    border: 1.5px dashed #94A3B8 !important;
}

div[data-testid="stFileUploaderDropzone"] section {
    background-color: #F8FAFC !important;
    color: #334155 !important;
}

div[data-testid="stFileUploaderDropzone"] button {
    background-color: #E0F2F1 !important;
    color: #134E4A !important;
    border: 1px solid #99D5CE !important;
}

/* EXTRACTED DOCUMENT TEXT - LIGHT THEME */

/* Expander heading */
[data-testid="stExpander"] summary {
    background-color: #F0FDFA !important;
    color: #134E4A !important;
    border: 1px solid #99D5CE !important;
}

[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span {
    color: #134E4A !important;
}

/* Extracted document content */
[data-testid="stExpander"] span.st-emotion-cache-5jdjoz {
    color: #1E293B !important;
    -webkit-text-fill-color: #1E293B !important;
    opacity: 1 !important;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TOP BAR
# --------------------------------------------------

render_sidebar()

st.markdown("""
<div style="text-align:right; padding-top:10px; margin-bottom:20px;">
    <span class="top-label">✦ Student Readiness Assistant</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <div class="brand">ApplyEase <span>AI</span></div>
    <div style="color:#475569;font-size:12px;">
        Scholarship Application Readiness Auditor
    </div>
</div>
""", unsafe_allow_html=True)



# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if st.session_state.page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <div class="hero-eyebrow">SCHOLARSHIP APPLICATION ASSISTANT</div>
        <h1>Apply with clarity.<br>Prepare with confidence.</h1>
        <p>
            Understand complex scholarship requirements, identify missing
            information, and prepare your application with an intelligent
            readiness review in English and Tamil.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-label">YOUR WORKSPACE</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="workspace-card">
            <div class="card-icon">♙</div>
            <div class="card-title">My Student Profile</div>
            <div class="card-description">
                Save your basic academic information once and use it
                when reviewing application requirements.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open My Profile →", key="open_profile",
                     use_container_width=True):
            navigate("My Profile")

    with col2:
        st.markdown("""
        <div class="workspace-card">
            <div class="card-icon">⇧</div>
            <div class="card-title">Upload Application</div>
            <div class="card-description">
                Upload scholarship application documents in PDF or
                image format for requirement analysis.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Upload Document →", key="open_upload",
                     use_container_width=True):
            navigate("Upload Application")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="workspace-card">
            <div class="card-icon">✓</div>
            <div class="card-title">Review & Complete</div>
            <div class="card-description">
                Review missing details, potential inconsistencies,
                and your application preparation checklist.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Review Application →", key="open_review",
                     use_container_width=True):
            navigate("Review & Complete")

    with col4:
        st.markdown("""
        <div class="workspace-card">
            <div class="card-icon">文</div>
            <div class="card-title">Application Guidance</div>
            <div class="card-description">
                Understand scholarship application terms and requirements
                through simple English explanations.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Explore Application Guidance →",
                    key="open_guidance",
                    use_container_width=True):
            navigate("Application Guidance")

    # COMING SOON

    st.markdown("""
    <div class="info-panel" style="margin-top:25px;">
        <div class="panel-title">Coming Soon</div>
        <div class="card-description">More tools to make scholarship applications easier.</div>
        <div style="display:flex; flex-wrap:wrap; gap:12px; margin-top:16px;">
            <span class="coming-soon-tag">DigiLocker Integration</span>
            <span class="coming-soon-tag">AI Application Guidance</span>
            <span class="coming-soon-tag">Image Text Extraction (OCR)</span>
            <span class="coming-soon-tag">Eligibility Checking</span>
            <span class="coming-soon-tag">Document Completeness Verification</span>
            <span class="coming-soon-tag">Multiple-Language Guidance</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
        
    st.markdown("""
    <div class="footer">
        ApplyEase AI · Enter once. Understand every rule. Apply with confidence.
    </div>
    """, unsafe_allow_html=True)



# --------------------------------------------------
# MY PROFILE
# --------------------------------------------------

elif st.session_state.page == "My Profile":

    st.markdown('<div class="page-heading">My Student Profile</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="page-subtitle">
        Add your basic academic information. You can review and update it
        whenever needed.
    </div>
    """, unsafe_allow_html=True)

    profile = st.session_state.profile

    # INITIALIZE FORM VALUES

    st.session_state.setdefault("profile_name", profile["name"])
    st.session_state.setdefault("profile_email", profile["email"])
    st.session_state.setdefault("profile_education", profile["education"])
    st.session_state.setdefault("profile_institution", profile["institution"])
    st.session_state.setdefault("profile_course", profile["course"])
    st.session_state.setdefault(
        "profile_school_class",
        "Select class"
    )
    st.session_state.setdefault(
        "profile_study_year",
        profile["year"] if profile["year"] in [
            "1st Year", "2nd Year", "3rd Year", "4th Year", "Other"
        ] else "Select year"
    )
    st.session_state.setdefault("profile_other_year", profile["year"])

    # PERSONAL INFORMATION

    st.markdown(
        '<div class="panel-title">Personal Information</div>',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "Full Name",
        key="profile_name",
        placeholder="Enter your full name"
    )

    email = st.text_input(
        "Email Address",
        key="profile_email",
        placeholder="Enter your email"
    )

    # ACADEMIC DETAILS

    st.markdown(
        '<div class="section-label">ACADEMIC DETAILS</div>',
        unsafe_allow_html=True
    )

    education_options = [
        "Select education level",
        "School",
        "Undergraduate",
        "Postgraduate",
        "Other"
    ]

    education = st.selectbox(
        "Education Level",
        education_options,
        key="profile_education"
    )

    institution = st.text_input(
        "School / Institution Name",
        key="profile_institution",
        placeholder="Enter your school or college name"
    )

    if education == "School":

        course = ""

    elif education in ["Undergraduate", "Postgraduate"]:

        course = st.text_input(
            "Course",
            key="profile_course",
            placeholder="Example: BCA, B.Com, M.Sc."
        )

    else:

        course = st.text_input(
            "Course / Programme (Optional)",
            key="profile_course",
            placeholder="Enter your course or programme"
        )

    # DYNAMIC EDUCATION FIELD

    if education == "School":

        class_options = ["Select class"] + [
            f"Class {number}" for number in range(1, 13)
        ]

        year = st.selectbox(
            "Current Class",
            class_options,
            key="profile_school_class"
        )

    elif education in ["Undergraduate", "Postgraduate"]:

        year_options = [
            "Select year",
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year",
            "Other"
        ]

        year = st.selectbox(
            "Current Year of Study",
            year_options,
            key="profile_study_year"
        )

    elif education == "Other":

        year = st.text_input(
            "Current Year / Level (Optional)",
            key="profile_other_year",
            placeholder="Enter your current level"
        )

    else:
        year = ""

    # SAVE PROFILE

    if st.button(
        "Save Student Profile",
        use_container_width=True
    ):

        st.session_state.profile = {
            "name": name,
            "email": email,
            "education": education,
            "institution": institution,
            "course": course,
            "year": year
        }

        st.success("Profile saved for this session.")

    if st.session_state.profile["name"]:
        st.markdown("""
        <div class="verified">
            ✓ Your profile information is available in this session.
        </div>
        """, unsafe_allow_html=True)



# --------------------------------------------------
# UPLOAD APPLICATION
# --------------------------------------------------

elif st.session_state.page == "Upload Application":

    st.markdown('<div class="page-heading">Upload Application</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="page-subtitle">
        Upload scholarship application documents to begin reviewing
        their instructions and requirements.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-panel">
        <div class="panel-title">Document Upload</div>
        <div class="card-description">
            Supported formats: PDF, PNG, JPG and JPEG.
            Upload clear documents for better analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # INITIALIZE DOCUMENT STORAGE

    if "application_documents" not in st.session_state:
        st.session_state.application_documents = []

    if "extracted_text" not in st.session_state:
        st.session_state.extracted_text = ""

    # MULTIPLE DOCUMENT UPLOAD

    uploaded_files = st.file_uploader(
        "Choose your application documents",
        type=["pdf", "png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="application_uploader"
    )

    # SAVE NEW DOCUMENTS

    for uploaded_file in uploaded_files:

        file_data = uploaded_file.getvalue()

        already_exists = any(
            doc["name"] == uploaded_file.name
            and doc["data"] == file_data
            for doc in st.session_state.application_documents
        )

        if not already_exists:

            extracted_text = ""

            if uploaded_file.type == "application/pdf":
                try:
                    pdf_reader = PdfReader(BytesIO(file_data))

                    extracted_text = "\n".join(
                        page.extract_text(extraction_mode="layout") or ""
                        for page in pdf_reader.pages
                    ).strip()

                except Exception:
                    st.error(
                        f"Unable to read {uploaded_file.name}."
                    )

            document = {
                "name": uploaded_file.name,
                "type": uploaded_file.type,
                "size": uploaded_file.size,
                "data": file_data,
                "extracted_text": extracted_text
            }

            st.session_state.application_documents.append(document)

    # DISPLAY SAVED DOCUMENTS

    if st.session_state.application_documents:

        st.success("Your documents are saved in this session.")

        for index, document in enumerate(
            st.session_state.application_documents
        ):

            st.write(
                f"**Document {index + 1}:** {document['name']}"
            )

            st.write("**File type:**", document["type"])

            st.write(
                "**File size:**",
                f"{document['size'] / 1024:.1f} KB"
            )

            if document["type"] == "application/pdf":

                if document["extracted_text"]:

                    st.success("PDF text extracted successfully.")

                    with st.expander(
                        f"View Extracted Text — {document['name']}"
                    ):
                        st.text(document["extracted_text"])

                else:
                    st.warning(
                        "No selectable text found in this PDF."
                    )

            elif document["type"].startswith("image/"):

                st.image(
                    document["data"],
                    caption=document["name"],
                    use_container_width=True
                )

                st.info(
                    "Image text extraction is not connected yet."
                )

        # KEEP DATA AVAILABLE FOR REVIEW & COMPLETE

        st.session_state.uploaded_file = (
            st.session_state.application_documents[0]
        )

        st.session_state.extracted_text = "\n\n".join(
            document["extracted_text"]
            for document in st.session_state.application_documents
            if document["extracted_text"]
        )

    else:

        st.session_state.uploaded_file = None
        st.session_state.extracted_text = ""

        st.markdown("""
        <div class="missing">
            No document uploaded yet. Choose a PDF or image to continue.
        </div>
        """, unsafe_allow_html=True)

        


# --------------------------------------------------
# REVIEW AND COMPLETE
# --------------------------------------------------

elif st.session_state.page == "Review & Complete":

    st.markdown('<div class="page-heading">Review & Complete</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="page-subtitle">
        Check your preparation status before submitting your application
        through its official portal.
    </div>
    """, unsafe_allow_html=True)

    profile = st.session_state.profile
    documents = st.session_state.get("application_documents", [])

    # STUDENT PROFILE STATUS

    profile_completed = (
        bool(profile["name"].strip())
        and profile["education"] not in ["", "Select education level"]
        and bool(profile["institution"].strip())
        and (
            profile["education"] == "School"
            or bool(profile["course"].strip())
        )
    )

    st.markdown("""
    <div class="info-panel">
        <div class="panel-title">Student Profile Status</div>
    </div>
    """, unsafe_allow_html=True)

    if profile_completed:
        st.success("✓ Basic student profile information is saved.")
    else:
        st.warning("! Complete your student profile before continuing.")

    # DOCUMENT STATUS

    st.markdown("""
    <div class="info-panel">
        <div class="panel-title">Document Status</div>
    </div>
    """, unsafe_allow_html=True)

    if documents:

        st.success(
            f"✓ {len(documents)} document(s) uploaded successfully."
        )

        for index, document in enumerate(documents):

            st.write(f"**Document {index + 1}: {document['name']}**")

            if document["type"] == "application/pdf":

                if document["extracted_text"]:

                    st.success("PDF text extracted successfully.")

                    with st.expander(
                        f"View Extracted Text — {document['name']}"
                    ):
                        st.text(document["extracted_text"])

                else:
                    st.warning("No selectable text found in this PDF.")

            elif document["type"].startswith("image/"):

                st.info("Image text extraction is not connected yet.")

    else:
        st.warning("! Upload your application documents before continuing.")

    # QUICK DOCUMENT CHECKS

    pdf_documents = [
        document for document in documents
        if document["type"] == "application/pdf"
        and document["extracted_text"]
    ]

    if pdf_documents:

        st.markdown("""
        <div class="info-panel">
            <div class="panel-title">Quick Document Checks</div>
        </div>
        """, unsafe_allow_html=True)

        checks = {
            "Applicant details": ["applicant", "student name"],
            "Family income": ["family income", "annual income"],
            "Educational institution": ["institution", "college"],
            "Course details": ["course", "degree"],
            "Application deadline": ["deadline", "last date"],
            "Supporting documents": [
                "supporting documents", "required documents"
            ]
        }

        for document in pdf_documents:

            st.write(f"**{document['name']}**")

            document_text = document["extracted_text"].lower()

            for label, keywords in checks.items():

                if any(word in document_text for word in keywords):
                    st.success(f"✓ {label} — Reference found")
                else:
                    st.warning(f"! {label} — Reference not detected")

        st.caption(
            "These checks search for common keywords only. "
            "They do not confirm completeness or eligibility."
        )

    # READINESS CHECKLIST

    st.markdown("""
    <div class="info-panel">
        <div class="panel-title">Readiness Checklist</div>
        <p style="color:#475569;font-size:13px;line-height:1.6;">
            These are preparation reminders. They are not an official
            eligibility decision.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # AUTOMATIC CHECKS

    if profile_completed:
        st.markdown("☑ Student profile information entered")
    else:
        st.markdown("☐ Student profile information entered")

    if documents:
        st.markdown("☑ Scholarship application document uploaded")
    else:
        st.markdown("☐ Scholarship application document uploaded")

    # MANUAL CHECKS

    st.checkbox(
        "Required documents checked against official instructions",
        key="review_required_documents"
    )

    st.checkbox(
        "Application details reviewed for possible inconsistencies",
        key="review_inconsistencies"
    )

    st.checkbox(
        "Final information verified by the applicant",
        key="review_final_verification"
    )

    # IMPORTANT NOTICE

    st.markdown("""
    <div class="alert">
        Important: This prototype does not determine official eligibility,
        guarantee approval, or submit applications. Always verify the final
        requirements with the official scholarship authority.
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# APPLICATION GUIDANCE
# --------------------------------------------------

elif st.session_state.page == "Application Guidance":

    st.markdown(
        '<div class="page-heading">Application Guidance</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="page-subtitle">
        Understand common scholarship application terms in simple English.
    </div>
    """, unsafe_allow_html=True)

    guidance = [
        (
            "Eligibility",
            "The conditions an applicant must meet to qualify for a scholarship."
        ),
        (
            "Supporting Documents",
            "Documents required to support and verify the information in your application."
        ),
        (
            "Annual Family Income",
            "The total income earned by your family in one year."
        ),
        (
            "Application Deadline",
            "The last date by which you must submit your application."
        ),
        (
            "Verification",
            "The process of checking whether your information and documents are correct."
        )
    ]

    for title, description in guidance:
        st.markdown(f"""
        <div class="info-panel">
            <div class="panel-title">{title}</div>
            <p style="color:#475569;font-size:14px;line-height:1.6;">
                {description}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert">
        These are prepared English explanations. Live AI guidance is not
        connected in this prototype. Always check official scholarship
        instructions for accurate requirements.
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Back to Dashboard", key="guidance_dashboard"):
        navigate("Dashboard")
