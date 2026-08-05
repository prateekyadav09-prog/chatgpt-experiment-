"""
Configuration for Faculty & Research Vacancy Tracker
"""

# ============================================
# TRACKED SUBJECTS
# ============================================

TRACKED_SUBJECTS = [
    "Chemistry",
    "Applied Chemistry",
    "Industrial Chemistry",
    "Chemical Sciences",
    "Organic Chemistry",
    "Inorganic Chemistry",
    "Physical Chemistry",
    "Analytical Chemistry",
    "Environmental Chemistry",
    "Polymer Chemistry",
    "Medicinal Chemistry",
    "Materials Chemistry",
    "Nanochemistry",
    "Computational Chemistry"
]

# ============================================
# TRACKED POSITIONS
# ============================================

TRACKED_POSITIONS = [
    "Assistant Professor",
    "Associate Professor",
    "Professor",
    "Guest Faculty",
    "Visiting Faculty",
    "Contract Faculty",
    "Temporary Faculty",
    "Research Associate",
    "Research Associate-I",
    "Research Associate-II",
    "Research Associate-III",
    "Senior Research Associate",
    "Postdoctoral Fellow",
    "Postdoctoral Research Associate",
    "Project Scientist",
    "Scientist",
    "Scientific Officer",
    "Technical Officer"
]

# ============================================
# EXCLUDED KEYWORDS
# ============================================

EXCLUDED_KEYWORDS = [
    "Chemical Engineering",
    "JRF",
    "Junior Research Fellow",
    "SRF",
    "Senior Research Fellow",
    "Project Assistant",
    "Project Associate",
    "Internship",
    "M.Sc Admission",
    "PhD Admission",
    "PGT",
    "TGT",
    "Lab Assistant",
    "Laboratory Assistant"
]

# ============================================
# OUTPUT FILES
# ============================================

OUTPUT_CSV = "vacancies.csv"

# ============================================
# SCRAPE SETTINGS
# ============================================

REQUEST_TIMEOUT = 30

USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/138.0 Safari/537.36"
)

# ============================================
# ORGANISATIONS TO MONITOR
# ============================================

SOURCES = {
    "UGC": "https://www.ugc.gov.in/",
    "CSIR": "https://www.csir.res.in/",
    "DRDO": "https://www.drdo.gov.in/",
    "BARC": "https://recruit.barc.gov.in/",
    "IISc": "https://iisc.ac.in/",
    "IIT": "https://www.iitd.ac.in/",
    "IISER": "https://www.iiserpune.ac.in/",
    "NCL": "https://www.ncl-india.org/",
    "IICB": "https://iicb.res.in/",
    "IACS": "https://www.iacs.res.in/"
}

# ============================================
# UPDATE SCHEDULE
# ============================================

CHECK_TIME = "07:00"

# ============================================
# FUTURE FEATURES
# ============================================

ENABLE_EMAIL = False
ENABLE_TELEGRAM = False
ENABLE_GOOGLE_SHEETS = False