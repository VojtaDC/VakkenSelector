# FILE: courses.py
available_courses = [
    # Polytechnical Foundation Courses
    {
        "Vak": "Quantitative Sustainability (Polytechnical Foundation)",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E3B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Vrijdag", "Tijdslot": "NM"}  # Fri 13-17
        ]
    },
    {
        "Vak": "Quantitative Sustainability (Polytechnical Foundation)",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F3B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Vrijdag", "Tijdslot": "NM"}  # Fri 13-17
        ]
    },
    {
        "Vak": "Quantitative Sustainability (Polytechnical Foundation)",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "E7",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "A"}  # Tues 18-22
        ]
    },
    {
        "Vak": "Quantitative Sustainability (Polytechnical Foundation)",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "F7",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "A"}  # Tues 18-22
        ]
    },
    {
        "Vak": "Innovation in Engineering (Polytechnical Foundation)",
        "Start": "2026-01-01",
        "Einde": "2026-01-31",
        "Periode": "January",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Innovation in Engineering (Polytechnical Foundation)",
        "Start": "2026-06-01",
        "Einde": "2026-06-30",
        "Periode": "June",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Innovation in Engineering (Polytechnical Foundation)",
        "Start": "2026-08-01",
        "Einde": "2026-08-31",
        "Periode": "August",
        "ECTS": 5,
        "Rooster": []
    },
    # Alternatieve vakken voor studenten met geavanceerde innovatiecompetenties
    {
        "Vak": "Facilitating Innovation in Multidisciplinary Teams",
        "Start": "2026-01-01",
        "Einde": "2026-01-31",
        "Periode": "January",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Facilitating Innovation in Multidisciplinary Teams",
        "Start": "2026-06-01",
        "Einde": "2026-06-30",
        "Periode": "June",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Facilitating Innovation in Multidisciplinary Teams",
        "Start": "2026-08-01",
        "Einde": "2026-08-31",
        "Periode": "August",
        "ECTS": 5,
        "Rooster": []
    },
    # Programme specific courses (50 ECTS)
    {
        "Vak": "Research immersion 1 - Power electronics and IC design",
        "Start": "2025-09-01",
        "Einde": "2026-08-31",
        "Periode": "Outside schedule structure",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Research immersion 2 - Power electronics and IC design",
        "Start": "2025-09-01",
        "Einde": "2026-08-31",
        "Periode": "Outside schedule structure",
        "ECTS": 10,
        "Rooster": []
    },
    {
        "Vak": "Building dependable robot systems",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F3B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Vrijdag", "Tijdslot": "NM"}  # Fri 13-17
        ]
    },
    {
        "Vak": "Innovation Camp",
        "Start": "2026-08-01",
        "Einde": "2026-08-31",
        "Periode": "August",
        "ECTS": 5,
        "Rooster": []
    },
    
    {
        "Vak": "X-Tech Entrepreneurship",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E3",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "VM"},  # Tues 8-12
            {"Dag": "Vrijdag", "Tijdslot": "NM"}  # Fri 13-17
        ]
    },
    {
        "Vak": "Developing an Entrepreneurial mindset",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F1B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Donderdag", "Tijdslot": "NM"}  # Thurs 13-17
        ]
    },
    {
        "Vak": "Integration of wind power in the power system",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E3B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Vrijdag", "Tijdslot": "NM"}  # Fri 13-17
        ]
    },
    # Core competence I - mandatory - choose 10 ECTS among the following courses
    {
        "Vak": "Introduction to Satellite Systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E5",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Woensdag", "Tijdslot": "VM"},  # Wed 8-12
            {"Dag": "Woensdag", "Tijdslot": "NM"}  # Wed 13-17
        ]
    },
    {
        "Vak": "Advanced antenna techniques and measurements",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E5",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Woensdag", "Tijdslot": "VM"},  # Wed 8-12
            {"Dag": "Woensdag", "Tijdslot": "NM"}  # Wed 13-17
        ]
    },
    {
        "Vak": "Power Electronics 1",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E5",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Woensdag", "Tijdslot": "VM"},  # Wed 8-12
            {"Dag": "Woensdag", "Tijdslot": "NM"}  # Wed 13-17
        ]
    },
    {
        "Vak": "Linear control design 2",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E3",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "VM"},  # Tues 8-12
            {"Dag": "Vrijdag", "Tijdslot": "NM"}  # Fri 13-17
        ]
    },
    {
        "Vak": "Electroacoustic transducers and systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E2",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Maandag", "Tijdslot": "NM"},   # Mon 13-17
            {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
        ]
    },
    # Core competence II - choose 20 ECTS among the following courses
    {
        "Vak": "Design of Digital Systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E2B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
        ]
    },
    {
        "Vak": "Spacecraft Instrumentation Systems",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F2",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Maandag", "Tijdslot": "NM"},  # Mon 13-17
            {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
        ]
    },  {
        "Vak": "Image Analysis with Microcomputer",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E1A",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Maandag", "Tijdslot": "VM"},  # Mon 8-12
            {"Dag": "Donderdag", "Tijdslot": "NM"}  # Thurs 13-17
        ]
    },
    {
        "Vak": "Remote Sensing",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E4",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "NM"},  # Tues 13-17
            {"Dag": "Vrijdag", "Tijdslot": "VM"}  # Fri 8-12
        ]
    },
    {
        "Vak": "RF Communication Circuits",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E2",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Maandag", "Tijdslot": "NM"},  # Mon 13-17
            {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
        ]
    },
    {
        "Vak": "Advanced Microwave Techniques and High Speed Electronics",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F2",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Maandag", "Tijdslot": "NM"},  # Mon 13-17
            {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
        ]
    },
    {
        "Vak": "Intelligent Systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "E7",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "A"}  # Tues 18-22
        ]
    },
    {
        "Vak": "Project in Intelligent Systems",
        "Start": "2026-01-01",
        "Einde": "2026-01-31",
        "Periode": "January",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Environmental Acoustics",
        "Start": "2026-06-01",
        "Einde": "2026-06-30",
        "Periode": "June",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Challenges in Acoustic Microsystems",
        "Start": "2026-01-01",
        "Einde": "2026-01-31",
        "Periode": "January",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Numerical Acoustics",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F3A",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "VM"}  # Tues 8-12
        ]
    },
    {
        "Vak": "Electroacoustic Transducers and Systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E2",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Maandag", "Tijdslot": "NM"},  # Mon 13-17
            {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
        ]
    },
    {
        "Vak": "Nonlinear Transducers",
        "Start": "2026-01-01",
        "Einde": "2026-01-31",
        "Periode": "January",
        "ECTS": 5,
        "Rooster": []
    },
    {
        "Vak": "Structure-Borne Sound",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E4",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "NM"},  # Tues 13-17
            {"Dag": "Vrijdag", "Tijdslot": "VM"}  # Fri 8-12
        ]
    },
    {
        "Vak": "Introduction to Electric Power Systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E4",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "NM"},  # Tues 13-17
            {"Dag": "Vrijdag", "Tijdslot": "VM"}  # Fri 8-12
        ]
    },
    {
        "Vak": "Power Grid Analysis",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F3A",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Dinsdag", "Tijdslot": "VM"}  # Tues 8-12
        ]
    },
    {
        "Vak": "High Voltage Engineering",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F5",
        "ECTS": 10,
        "Rooster": [
            {"Dag": "Woensdag", "Tijdslot": "VM"},  # Wed 8-12
            {"Dag": "Woensdag", "Tijdslot": "NM"}  # Wed 13-17
        ]
    },
    {
        "Vak": "Distributed Energy Technologies, Modelling and Control",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F1B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Donderdag", "Tijdslot": "NM"}  # Thurs 13-17
        ]
    },
    {
        "Vak": "Renewables in Electricity Markets",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F2A",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Maandag", "Tijdslot": "NM"}  # Mon 13-17
        ]
    },
    {
        "Vak": "Optimization in Modern Power Systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E5A",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Woensdag", "Tijdslot": "VM"}  # Wed 8-12
        ]
    },
    {
        "Vak": "Machine Learning for Energy Systems",
        "Start": "2025-09-01",
        "Einde": "2025-12-31",
        "Periode": "Autumn E5B",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Woensdag", "Tijdslot": "NM"}  # Wed 13-17
        ]
    },
    {
        "Vak": "Integrated Energy Grids",
        "Start": "2026-02-01",
        "Einde": "2026-06-30",
        "Periode": "Spring F5A",
        "ECTS": 5,
        "Rooster": [
            {"Dag": "Woensdag", "Tijdslot": "VM"}  # Wed 8-12
        ]
    },
    
{
    "Vak": "Power Electronics 2. Laboratory course",
    "Start": "2026-01-01",
    "Einde": "2026-01-31",
    "Periode": "January",
    "ECTS": 5,
    "Rooster": []
},
{
    "Vak": "Circuit technology and EMC",
    "Start": "2025-09-01",
    "Einde": "2025-12-31",
    "Periode": "Autumn E4A",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Dinsdag", "Tijdslot": "NM"}  # Tues 13-17
    ]
},
{
    "Vak": "Integrated analog electronics 2",
    "Start": "2026-02-01",
    "Einde": "2026-06-30",
    "Periode": "Spring F4A",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Dinsdag", "Tijdslot": "NM"}  # Tues 13-17
    ]
},
{
    "Vak": "Design and layout of integrated CMOS circuits",
    "Start": "2026-06-01",
    "Einde": "2026-06-30",
    "Periode": "June",
    "ECTS": 5,
    "Rooster": []
},
{
    "Vak": "Robust and fault-tolerant control",
    "Start": "2026-02-01",
    "Einde": "2026-06-30",
    "Periode": "Spring F1",
    "ECTS": 10,
    "Rooster": [
        {"Dag": "Maandag", "Tijdslot": "VM"},  # Mon 8-12
        {"Dag": "Donderdag", "Tijdslot": "NM"}  # Thurs 13-17
    ]
},
{
    "Vak": "Modelling for operation of complex industrial plants",
    "Start": "2026-02-01",
    "Einde": "2026-06-30",
    "Periode": "Spring F5A",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Woensdag", "Tijdslot": "VM"}  # Wed 8-12
    ]
},
{
    "Vak": "Robotics",
    "Start": "2025-09-01",
    "Einde": "2025-12-31",
    "Periode": "Autumn E4A",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Dinsdag", "Tijdslot": "NM"}  # Tues 13-17
    ]
},
{
    "Vak": "Safety and Reliability in Robotic and Automation Systems",
    "Start": "2026-02-01",
    "Einde": "2026-06-30",
    "Periode": "Spring F5B",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Woensdag", "Tijdslot": "NM"}  # Wed 13-17
    ]
},
{
    "Vak": "Architectural acoustics",
    "Start": "2026-02-01",
    "Einde": "2026-06-30",
    "Periode": "Spring F4",
    "ECTS": 10,
    "Rooster": [
        {"Dag": "Dinsdag", "Tijdslot": "NM"},  # Tues 13-17
        {"Dag": "Vrijdag", "Tijdslot": "VM"}  # Fri 8-12
    ]
},
{
    "Vak": "Advanced acoustics",
    "Start": "2026-02-01",
    "Einde": "2026-06-30",
    "Periode": "Spring F2",
    "ECTS": 10,
    "Rooster": [
        {"Dag": "Maandag", "Tijdslot": "NM"},  # Mon 13-17
        {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
    ]
},
{
    "Vak": "Nonlinear transducers",
    "Start": "2026-01-01",
    "Einde": "2026-01-31",
    "Periode": "January",
    "ECTS": 5,
    "Rooster": []
},
{
    "Vak": "Structure-borne sound",
    "Start": "2025-09-01",
    "Einde": "2025-12-31",
    "Periode": "Autumn E4",
    "ECTS": 10,
    "Rooster": [
        {"Dag": "Dinsdag", "Tijdslot": "NM"},  # Tues 13-17
        {"Dag": "Vrijdag", "Tijdslot": "VM"}  # Fri 8-12
    ]
},
{
    "Vak": "Offshore wind grid connection and high-voltage DC (HVDC) transmission",
    "Start": "2025-09-01",
    "Einde": "2025-12-31",
    "Periode": "Autumn E4B",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Vrijdag", "Tijdslot": "VM"}  # Fri 8-12
    ]
},
{
    "Vak": "Transients in power systems",
    "Start": "2025-09-01",
    "Einde": "2025-12-31",
    "Periode": "Autumn E1B",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Donderdag", "Tijdslot": "NM"}  # Thurs 13-17
    ]
},
{
    "Vak": "Electrical machines",
    "Start": "2026-02-01",
    "Einde": "2026-06-30",
    "Periode": "Spring F2A",
    "ECTS": 5,
    "Rooster": [
        {"Dag": "Maandag", "Tijdslot": "NM"}  # Mon 13-17
    ]
},
{
    "Vak": "Wind, solar and energy storage electrical drive trains",
    "Start": "2025-09-01",
    "Einde": "2025-12-31",
    "Periode": "Autumn E2",
    "ECTS": 10,
    "Rooster": [
        {"Dag": "Maandag", "Tijdslot": "NM"},  # Mon 13-17
        {"Dag": "Donderdag", "Tijdslot": "VM"}  # Thurs 8-12
    ]
},
{
    "Vak": "Hands-on microcontroller programming",
    "Start": "2026-06-01",
    "Einde": "2026-06-30",
    "Periode": "June",
    "ECTS": 5,
    "Rooster": []
}
]