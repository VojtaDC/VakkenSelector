import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.colors import n_colors
import logging
from courses import available_courses

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def calculate_overlapping_ects(courses):
    overlapping_ects = 0
    counted_pairs = set()
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            if courses_conflict(courses[i], courses[j]):
                pair = tuple(sorted([courses[i]['Vak'], courses[j]['Vak']]))
                if pair not in counted_pairs:
                    overlapping_ects += min(courses[i]['ECTS'], courses[j]['ECTS'])
                    counted_pairs.add(pair)
    return overlapping_ects

# Function to map 'Periode' to the six main periods
def map_period(periode_str):
    periode_str = periode_str.lower()
    if 'january' in periode_str:
        return 'January'
    elif 'june' in periode_str:
        return 'June'
    elif 'august' in periode_str:
        return 'August'
    elif 'autumn' in periode_str or 'e' in periode_str:
        return 'Autumn Semester'
    elif 'spring' in periode_str or 'f' in periode_str:
        return 'Spring Semester'
    else:
        return 'Outside Schedule'

# Function to get initials of a course name
def get_initials(name):
    return '.'.join([word[0] for word in name.split() if word]) + '.'

# Add 'MappedPeriode' to each course
for course in available_courses:
    course['MappedPeriode'] = map_period(course['Periode'])
    if not course['Rooster']:
        # If the schedule is empty and the course is in one of the months, fill the whole week
        if course['MappedPeriode'] in ['January', 'June', 'July', 'August']:
            course['Rooster'] = [
                {"Dag": dag, "Tijdslot": slot} for dag in ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag"] for slot in ["VM", "NM"]
            ]
    logger.debug(f"Course {course['Vak']} mapped to period {course['MappedPeriode']} with schedule: {course['Rooster']}")

# Function to check if courses conflict
def courses_conflict(course1, course2):
    # Get the mapped periods
    period1 = course1['MappedPeriode']
    period2 = course2['MappedPeriode']
    
    # Specifically check if one course is in 'June' and the other in 'Spring Semester'
    if (period1 == 'June' and period2 == 'Spring Semester') or (period1 == 'Spring Semester' and period2 == 'June'):
        date_overlap = False
    else:
        # Check if the dates overlap
        date_overlap = not (course1['Start'] > course2['Einde'] or course1['Einde'] < course2['Start'])

    # Check if the schedules overlap
    schedule_overlap = False
    for sched1 in course1['Rooster']:
        for sched2 in course2['Rooster']:
            if sched1['Dag'] == sched2['Dag'] and sched1['Tijdslot'] == sched2['Tijdslot']:
                schedule_overlap = True
                break
        if schedule_overlap:
            break

    return date_overlap and schedule_overlap

# Function to find overlapping groups
def find_overlapping_groups(courses):
    groups = []
    for course in courses:
        added = False
        for group in groups:
            if any(courses_conflict(course, member) for member in group):
                group.append(course)
                added = True
                break
        if not added:
            groups.append([course])
    return groups

# Function to generate colors for groups
def generate_group_colors(n):
    base_colors = [
        'rgb(31, 119, 180)',  # Blue
        'rgb(255, 127, 14)',  # Orange
        'rgb(44, 160, 44)',   # Green
        'rgb(214, 39, 40)',   # Red
        'rgb(148, 103, 189)', # Purple

        'rgb(227, 119, 194)', # Pink
        'rgb(127, 127, 127)', # Gray
        'rgb(188, 189, 34)',  # Olive
        'rgb(23, 190, 207)',  # Cyan
        'rgb(255, 99, 71)',   # Tomato
        'rgb(75, 0, 130)',    # Indigo

        'rgb(0, 255, 127)',   # SpringGreen

        'rgb(0, 191, 255)',   # DeepSkyBlue
        'rgb(255, 69, 0)',    # OrangeRed
        'rgb(154, 205, 50)',  # YellowGreen
        'rgb(255, 182, 193)', # LightPink
        'rgb(70, 130, 180)'   # SteelBlue
    ]
    # If there are more groups than base colors, generate extra colors
    if n > len(base_colors):
        colors = n_colors('rgb(0, 0, 255)', 'rgb(255, 0, 0)', n, colortype='rgb')
    else:
        colors = base_colors[:n]
    return colors

# Initialize the list of courses added to the timeline
timeline_courses = []

# Start Dash app
app = dash.Dash(__name__)
app.title = "Curriculum Planner"

# Layout
app.layout = html.Div([
    html.H1("Curriculum Planner", style={"textAlign": "center"}),

    # Total ECTS and Overlapping ECTS
    html.Div(
        id="total-ects",
        style={"textAlign": "center", "marginTop": "20px", "fontSize": "20px"},
        children="Totaal studiepunten: 0 | Overlappende studiepunten: 0"
    ),
    
    # Timeline graph
    dcc.Graph(id="timeline-graph"),

    # Courses per period
    html.Div(
        id="courses-by-period",
        children=[
            html.Div(
                children=[
                    html.H2(f"{periode}", style={"textAlign": "center", "marginTop": "20px"}),
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.P(course["Vak"], style={"margin": "5px 0", "fontWeight": "bold"}),
                                    html.P(f"{course['ECTS']} ECTS", style={"margin": "5px 0"})
                                ],
                                style={
                                    "border": "1px solid #ccc",
                                    "borderRadius": "5px",
                                    "padding": "10px",
                                    "margin": "5px",
                                    "cursor": "pointer",
                                    "width": "200px",
                                    "textAlign": "center",
                                    "backgroundColor": "#f9f9f9"
                                },
                                id=f"course-{index}"
                            )
                            for index, course in enumerate(available_courses) if course['MappedPeriode'] == periode
                        ],
                        style={"display": "flex", "flexWrap": "wrap", "justifyContent": "center"}
                    )
                ]
            )
            for periode in ["Autumn Semester", "January", "Spring Semester", "June", "August", "Outside Schedule"]
        ]
    ),

    # Total ECTS
    html.Div(
        id="total-ects-summary",
        style={"textAlign": "center", "marginTop": "20px", "fontSize": "20px"},
        children="Totaal studiepunten: 0"
    ),
])

# Callback to add courses to the timeline
@app.callback(
    [Output("timeline-graph", "figure"),
     Output("total-ects", "children"),
     Output("courses-by-period", "children")],
    [Input(f"course-{index}", "n_clicks") for index in range(len(available_courses))],
    [State("timeline-graph", "figure"),
     State("courses-by-period", "children")]
)
def add_course_to_timeline(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if not clicked_id.startswith("course-"):
        raise dash.exceptions.PreventUpdate

    course_index = int(clicked_id.split("-")[1])
    selected_course = available_courses[course_index]

    global timeline_courses

    # Add or remove the course from the timeline
    if selected_course not in timeline_courses:
        timeline_courses.append(selected_course)
    else:
        timeline_courses = [course for course in timeline_courses if course != selected_course]

    # Find overlapping groups
    overlapping_groups = find_overlapping_groups(timeline_courses)

    # Calculate total ECTS
    total_ects = sum(course["ECTS"] for course in timeline_courses)

    # Calculate overlapping ECTS
    overlapping_ects = calculate_overlapping_ects(timeline_courses)

    # Define colors
    overlap_color = 'rgb(214, 39, 40)'  # Red for overlapping courses
    default_color = 'rgb(31, 119, 180)'  # Blue for non-overlapping courses

    # Identify overlapping courses
    overlapping_courses_set = set()
    for group in overlapping_groups:
        if len(group) > 1:
            overlapping_courses_set.update(course['Vak'] for course in group)

    # Map courses to colors
    course_color_mapping = {}
    for course in timeline_courses:
        if course['Vak'] in overlapping_courses_set:
            course_color_mapping[course['Vak']] = overlap_color
        else:
            course_color_mapping[course['Vak']] = default_color

    # Build layers based on schedule conflicts
    layers = [[]]
    for course in timeline_courses:
        placed = False
        for layer in layers:
            if all(not courses_conflict(course, l) for l in layer):
                layer.append(course)
                placed = True
                break
        if not placed:
            layers.append([course])

    # Define periods in chronological order
    periodes = ['Autumn Semester', 'January', 'Spring Semester', 'June', 'August', 'Outside Schedule']
    num_periodes = len(periodes)
    num_layers = len(layers)

    # Prepare the figure
    fig = make_subplots(
        rows=num_layers,
        cols=num_periodes,
        shared_xaxes=True,
        shared_yaxes=True,
        horizontal_spacing=0.02,
        vertical_spacing=0.05,
        subplot_titles=[
            f"{periode} - Laag {layer_idx+1}" for layer_idx in range(num_layers) for periode in periodes
        ]
    )

    dagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag"]
    tijdslots = ["VM", "NM", "A"]

    for layer_idx, layer in enumerate(layers):
        for periode_idx, periode in enumerate(periodes):
            # Filter courses in the current layer and mapped period
            layer_periode_courses = [
                course for course in layer if course['MappedPeriode'] == periode
            ]

            # Initialize z, text, and hovertext
            z = [[0 for _ in dagen] for _ in tijdslots]
            text = [['' for _ in dagen] for _ in tijdslots]
            hovertext = [['' for _ in dagen] for _ in tijdslots]
            
            for course in layer_periode_courses:
                course_name = course['Vak']
                # Assign z-values: 2 for overlapping courses, 1 for non-overlapping courses
                color_value = 2 if course_color_mapping[course_name] == overlap_color else 1
                for sched in course['Rooster']:
                    dag = sched['Dag']
                    tijdslot = sched['Tijdslot']
                    tijdslot_idx = tijdslots.index(tijdslot)
                    dag_idx = dagen.index(dag)
                    z[tijdslot_idx][dag_idx] = color_value
                    text[tijdslot_idx][dag_idx] = get_initials(course_name)
                    hovertext[tijdslot_idx][dag_idx] = course_name
            
            # Define the colorscale
            colorscale = [
                [0.0, 'lightgrey'],    # z = 0 (Lege roosterplaatsen)
                [0.5, default_color],  # z = 1 (Niet-overlappende cursussen)
                [1.0, overlap_color]   # z = 2 (Overlappende cursussen)
            ]
            
            # Set zmin and zmax
            zmin = 0
            zmax = 2
            
            # Create Heatmap
            heatmap = go.Heatmap(
                z=z,
                y=tijdslots,
                x=dagen,
                text=text,
                texttemplate="%{text}",
                hoverinfo='text',
                hovertext=hovertext,
                colorscale=colorscale,
                zmin=zmin,
                zmax=zmax,
                colorbar=dict(len=0.5),
                showscale=False,
                xgap=1,  # Dunne zwarte randen tussen vakjes
                ygap=1
            )

            fig.add_trace(heatmap, row=layer_idx+1, col=periode_idx+1)
            fig.update_yaxes(title_text='', autorange='reversed', row=layer_idx+1, col=periode_idx+1)
            fig.update_xaxes(title_text='', row=layer_idx+1, col=periode_idx+1)

    fig.update_layout(
        height=300*num_layers,
        width=300*num_periodes,
        showlegend=False,
        margin=dict(l=50, r=50, t=50, b=50),
    )

    # Update the available courses UI
    updated_courses_by_period = [
        html.Div(
            children=[
                html.H2(f"{periode}", style={"textAlign": "center", "marginTop": "20px"}),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.P(course["Vak"], style={"margin": "5px 0", "fontWeight": "bold"}),
                                html.P(f"{course['ECTS']} ECTS", style={"margin": "5px 0"})
                            ],
                            style={
                                "border": "1px solid #ccc",
                                "borderRadius": "5px",
                                "padding": "10px",
                                "margin": "5px",
                                "cursor": "not-allowed" if course in timeline_courses else "pointer",
                                "width": "200px",
                                "textAlign": "center",
                                "backgroundColor": "#d3d3d3" if course in timeline_courses else "#f9f9f9"
                            },
                            id=f"course-{index}"
                        )
                        for index, course in enumerate(available_courses) if course['MappedPeriode'] == periode
                    ],
                    style={"display": "flex", "flexWrap": "wrap", "justifyContent": "center"}
                )
            ]
        )
        for periode in periodes
    ]

    return fig, f"Totaal studiepunten: {total_ects} | Overlappende studiepunten: {overlapping_ects}", updated_courses_by_period

# Start the app
if __name__ == "__main__":
    app.run_server(debug=True)