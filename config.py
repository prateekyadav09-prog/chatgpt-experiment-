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

# ============================================
# SOURCES TO MONITOR
# ============================================

SOURCES = [

    # Government
    {
        "name": "UGC",
        "url": "https://www.ugc.gov.in/",
        "type": "government"
    },

    {
        "name": "Haryana Higher Education",
        "url": "https://highereduhry.ac.in/",
        "type": "government"
    },

    {
        "name": "Delhi University",
        "url": "https://www.du.ac.in/",
        "type": "government"
    },

    # Research Institutes

    {
        "name": "CSIR",
        "url": "https://www.csir.res.in/",
        "type": "research"
    },

    {
        "name": "DRDO",
        "url": "https://www.drdo.gov.in/",
        "type": "research"
    },

    {
        "name": "BARC",
        "url": "https://recruit.barc.gov.in/",
        "type": "research"
    },

    {
        "name": "NCL",
        "url": "https://www.ncl-india.org/",
        "type": "research"
    },

    {
        "name": "IICB",
        "url": "https://iicb.res.in/",
        "type": "research"
    },

    {
        "name": "IACS",
        "url": "https://www.iacs.res.in/",
        "type": "research"
    },

    # Private Universities

    {
        "name": "Ashoka University",
        "url": "https://www.ashoka.edu.in/",
        "type": "private"
    },

    {
        "name": "O.P. Jindal Global University",
        "url": "https://jgu.edu.in/",
        "type": "private"
    },

    {
        "name": "BML Munjal University",
        "url": "https://www.bmu.edu.in/",
        "type": "private"
    },

    {
        "name": "Manav Rachna University",
        "url": "https://manavrachna.edu.in/",
        "type": "private"
    },

    {
        "name": "SGT University",
        "url": "https://sgtuniversity.ac.in/",
        "type": "private"
    }

]


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