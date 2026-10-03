import streamlit as st

from agents.core.models import Task
from agents.core.orchestrator import Orchestrator


st.set_page_config(
    page_title="Multi-Agent Task Orchestrator",
    page_icon="🤖",
    layout="wide",
)


# -------------------------------------------------
# Custom Styling
# -------------------------------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 18px;
            color: #6b7280;
            margin-bottom: 25px;
        }

        .agent-card {
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            background-color: #f8fafc;
            text-align: center;
            margin-bottom: 10px;
        }

        .agent-title {
            font-size: 18px;
            font-weight: 600;
        }

        .agent-status {
            font-size: 14px;
            color: #16a34a;
            margin-top: 5px;
        }

        .result-box {
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            background-color: #f8fafc;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 Autonomous Multi-Agent Task Orchestrator</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Plan, delegate, execute, verify, and synthesize complex tasks "
    "using specialized agents."
    "</div>",
    unsafe_allow_html=True,
)


# -------------------------------------------------
# Task Input
# -------------------------------------------------

st.subheader("🎯 Task Input")

goal = st.text_area(
    "Enter your goal",
    placeholder=(
        "Example: Learning Java\n"
        "Example: Build a machine learning application\n"
        "Example: Research Python and Java"
    ),
    height=130,
)


# -------------------------------------------------
# Agent Architecture
# -------------------------------------------------

st.subheader("🧠 Agent Pipeline")

columns = st.columns(5)

agents = [
    ("Planner", "Creates the execution plan"),
    ("Research", "Gathers information"),
    ("Analysis", "Analyzes results"),
    ("Verification", "Validates results"),
    ("Synthesis", "Combines final results"),
]

pipeline_placeholders = []

for column, (name, description) in zip(columns, agents):

    with column:

        placeholder = st.empty()

        placeholder.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-title">{name}</div>
                <div>{description}</div>
                <div class="agent-status">Ready</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        pipeline_placeholders.append(
            placeholder
        )


st.divider()
def update_pipeline_status(statuses):
    for placeholder, (name, description) in zip(
        pipeline_placeholders,
        agents,
    ):
        status = statuses.get(
            name.lower(),
            "Ready",
        )

        placeholder.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-title">{name}</div>
                <div>{description}</div>
                <div class="agent-status">{status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -------------------------------------------------
# Execute Task
# -------------------------------------------------

if st.button(
    "🚀 Run Autonomous Task",
    use_container_width=True,
):

    if not goal.strip():

        st.warning("Please enter a task goal first.")

    else:

        st.subheader("⚙️ Execution Status")

        status_placeholder = st.empty()

        status_placeholder.info(
            "🔄 Initializing multi-agent workflow..."
        )

        task = Task(
            id="ui-task",
            goal=goal.strip(),
        )

        orchestrator = Orchestrator()

        try:

            status_placeholder.info(
                "🧠 Planner is creating the execution plan..."
            )

            final_result = orchestrator.execute(task)
            executed_agents = set(
                orchestrator.execution_log
            )

            statuses = {
               "planner": "Completed",
               "research": (
                  "Completed"
                  if "research" in executed_agents
                  else "Not required"
                ),
               "analysis": (
                  "Completed"
                  if "analysis" in executed_agents
                  else "Not required"
                ),
                "verification": (
                   "Completed"
                   if "verification" in executed_agents
                   else "Not required"
                ),
                "synthesis": "Completed",
            }

            update_pipeline_status(statuses)
            executed_agents = set(orchestrator.execution_log)

            if task.status.value == "completed":

                status_placeholder.success(
                    "✅ Multi-agent workflow completed successfully."
                )
                st.subheader("Agent Execution")

                status_columns = st.columns(5)

                for column, (name, _) in zip(
                    status_columns,
                    agents,
                ):

                    capability = name.lower()

                    if capability == "planner":
                        status = "Completed"
                    elif capability in executed_agents:
                        status = "Completed"
                    elif capability == "synthesis":
                        status = "Completed"
                    else:
                        status = "Not required"

                    with column:
                        st.metric(
                            name,
                            status,
                        )

                st.subheader("📋 Final Result")

                st.markdown(
                    f"""
                    <div class="result-box">
                    {final_result}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:

                status_placeholder.error(
                    "❌ The orchestrator could not complete the task."
                )

                st.error(final_result)

        except Exception as error:

            status_placeholder.error(
                "❌ An error occurred during execution."
            )

            st.exception(error)


# -------------------------------------------------
# Footer
# -------------------------------------------------

st.divider()

st.caption(
    "Autonomous Multi-Agent Task Orchestrator | "
    "Python • Pydantic • Streamlit"
)