#everything taken from: https://python.plainenglish.io/generating-a-fake-database-with-python-8523bf6db9ec

# create_tables.py
from sqlalchemy import create_engine, MetaData, \
    Column, Integer, Numeric, String, Date, Table, ForeignKey, Boolean, ARRAY

# Set up connection between sqlalchemy and postgres dbapi
# NOTE: Change the line below to fit your system
engine = create_engine(
    "postgresql://postgres:Notebook!013@localhost:5432/DatabaseFinalProject"
)

# Create a metadata object
metadata = MetaData()

#DDL for Party, Voter, Location, Demographic, Polling_Location, Policy, Issue, Platform, Candidate, and Election

voter_table = Table(
    "voter",
    metadata,
    Column("voter_id", Integer, primary_key=True, unique=True),
    Column("candidate_id", ForeignKey("candidate.candidate_id"), nullable=False),
    Column("poll_location_id", ForeignKey("polling_location.poll_location_id"), nullable=False),
    Column("demographic_id", ForeignKey("demographic.demographic_id"), nullable=False),
    Column("name", String(50), nullable=False),
    Column("age", Integer, nullable=False),
    Column("race", String(50), nullable=False),
    Column("gender", String(50), nullable=False),
)

location_table = Table(
    "location",
    metadata,
    Column("location_id", Integer, primary_key=True, unique=True),
    Column("state", String(50), nullable=False),
    Column("city", String(50), nullable=False),
)

polling_table = Table(
    "polling_location",
    metadata,
    Column("poll_location_id", Integer, primary_key=True, unique=True),
    Column("location_id", ForeignKey("location.location_id"), nullable=False),
    Column("ballot_amount", Integer, nullable=False),
)

party_table = Table(
    "party",
    metadata,
    Column("party_id", Integer, primary_key=True, unique=True),
    Column("platform_id", ForeignKey("platform.platform_id"), nullable=False),
    Column("state", String(50), nullable=False),
    Column("party_type", String(50), nullable=False),
)

demographic_table = Table(
    "demographic",
    metadata,
    Column("demographic_id", Integer, primary_key=True, unique=True),
    Column("education", String(100), nullable=False),
    Column("wealth", String(100), nullable=False),
    Column("marital_status", String(100), nullable=False),
    Column("religion", String(100), nullable=False),
)

policy_table = Table(
    "policy",
    metadata,
    Column("policy_id", Integer, primary_key=True, unique=True),
    Column("issue_id", ForeignKey("issue.issue_id"), nullable=False),
    Column("policy", String(100), nullable=False),
)

issue_table = Table(
    "issue",
    metadata,
    Column("issue_id", Integer, primary_key=True, unique=True),
    Column("issue", String(300), nullable=False),
)

platform_table = Table(
    "platform",
    metadata,
    Column("platform_id", Integer, primary_key=True, unique=True),
    Column("platform_focus", String(100), nullable=False),
    Column("target_demographic_id", Integer, nullable=False),
)

candidate_table = Table(
    "candidate",
    metadata,
    Column("candidate_id", Integer, primary_key=True, unique=True),
    Column("party_id", ForeignKey("party.party_id"), nullable=False),
    Column("platform_id", ForeignKey("platform.platform_id"), nullable=False),
    Column("election_id", ForeignKey("election.election_id"), nullable=False),
    Column("name", String(100), nullable=False),
    Column("age", Integer, nullable=False),
    Column("race", String(100), nullable=False),
    Column("gender", String(100), nullable=False),
    Column("winner", Boolean, nullable=False, default=False),
)

election_table = Table(
    "election",
    metadata,
    Column("election_id", Integer, primary_key=True, unique=True),
    Column("winner", String(100), nullable=False),
    Column("election_type", String(100), nullable=False),
    Column("year", Integer, nullable=False),
)

candidate_policy_table = Table(
    "candidate_policy",
    metadata,
    Column("candidate_id", ForeignKey("candidate.candidate_id"), nullable=False),
    Column("policy_id", ForeignKey("policy.policy_id"), nullable=False),
)

# Start transaction to commit DDL to postgres database
with engine.begin() as conn:
    metadata.create_all(conn)
    # Log the tables as they are created
    for table in metadata.tables.keys():
        print(f"{table} successfully created")