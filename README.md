# Faculty & Research Vacancy Tracker

An automated Python-based tracker that monitors faculty and research vacancies across universities, government institutions, and research laboratories in India.

The project runs automatically using GitHub Actions and generates a regularly updated list of vacancies in CSV format.

---

## Features

- Daily automatic vacancy check
- Tracks Chemistry-related positions
- Removes duplicate vacancies
- Generates an updated CSV report
- Easy to extend by adding new scrapers

---

## Positions Tracked

### Faculty

- Assistant Professor
- Associate Professor
- Professor
- Guest Faculty
- Visiting Faculty
- Contract Faculty
- Temporary Faculty

### Research

- Research Associate
- Research Associate I/II/III
- Senior Research Associate
- Postdoctoral Fellow
- Project Scientist
- Scientist
- Scientific Officer
- Technical Officer (Chemistry)

---

## Subjects

- Chemistry
- Applied Chemistry
- Industrial Chemistry
- Chemical Sciences
- Organic Chemistry
- Inorganic Chemistry
- Physical Chemistry
- Analytical Chemistry
- Polymer Chemistry
- Environmental Chemistry
- Medicinal Chemistry
- Materials Chemistry
- Nanochemistry

---

## Institutions

### Universities

- Central Universities
- State Universities
- Haryana Government Colleges
- Delhi Government Colleges
- IITs
- IISERs
- NITs

### Private Universities

- Ashoka University
- O.P. Jindal Global University
- BML Munjal University
- Manav Rachna University
- SGT University
- Shiv Nadar University
- Amity University
- GD Goenka University
- KR Mangalam University
- The NorthCap University

### Research Institutes

- CSIR Laboratories
- DRDO
- BARC
- DAE Institutes
- IISc
- IACS
- IICB
- NCL
- JNCASR
- INST
- Bose Institute

---

## Output

The tracker generates:

vacancies.csv

Columns:

- Date Found
- Organisation
- Position
- Subject
- Location
- Last Date
- Advertisement Link
- Status

---

## Roadmap

### Version 1

- Daily automation
- CSV generation
- Chemistry vacancy filtering

### Version 2

- Email notifications
- Telegram notifications
- Google Sheets sync
- GitHub Pages dashboard

### Version 3

- AI-assisted PDF parsing
- Smart relevance scoring
- Closing-soon alerts

---

## License

MIT License