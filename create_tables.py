#everything taken from: https://python.plainenglish.io/generating-a-fake-database-with-python-8523bf6db9ec

# create_tables.py
from sqlalchemy import create_engine, MetaData, \
    Column, Integer, Numeric, String, Date, Table, ForeignKey, Boolean, ARRAY

# Set up connection between sqlalchemy and postgres dbapi
engine = create_engine(
    "postgresql://soap:brimstone42@localhost:5432/DatabaseFinalProject"
)

# Create a metadata object
metadata = MetaData()

#DDL for Party, Voter, Location, Demographic, Polling_Location, Policy, Issue, Platform, Candidate, and Election

voter_table = Table(
    "Voter",
    metadata,
    Column("voter_id", Integer, primary_key=True, unique=True),
    Column("candidate_id", ForeignKey("Candidate.candidate_id"), nullable=False),
    Column("poll_location_id", ForeignKey("Polling_Location.poll_location_id"), nullable=False),
    Column("demographic_id", ForeignKey("Demographic.demographic_id"), nullable=False),
    Column("name", String(50), nullable=False),
    Column("age", Integer, nullable=False),
    Column("race", String(50), nullable=False),
    Column("gender", String(50), nullable=False),
)

location_table = Table(
    "Location",
    metadata,
    Column("location_id", Integer, primary_key=True, unique=True),
    Column("state", String(50), nullable=False),
    Column("city", String(50), nullable=False),
)

polling_table = Table(
    "Polling_Location",
    metadata,
    Column("poll_location_id", Integer, primary_key=True, unique=True),
    Column("location_id", ForeignKey("Location.location_id"), nullable=False),
    Column("ballot_amount", Integer, nullable=False),
)

party_table = Table(
    "Party",
    metadata,
    Column("party_id", Integer, primary_key=True, unique=True),
    Column("platform_id", ForeignKey("Platform.platform_id"), nullable=False),
    Column("state", String(50), nullable=False),
    Column("party_type", String(50), nullable=False),
)

demographic_table = Table(
    "Demographic",
    metadata,
    Column("demographic_id", Integer, primary_key=True, unique=True),
    Column("education", String(100), nullable=False),
    Column("wealth", String(100), nullable=False),
    Column("marital_status", String(100), nullable=False),
    Column("religion", String(100), nullable=False),
)

policy_table = Table(
    "Policy",
    metadata,
    Column("policy_id", Integer, primary_key=True, unique=True),
    Column("issue_id", ForeignKey("Issue.issue_id"), nullable=False),
    Column("policy", String(100), nullable=False),
)

issue_table = Table(
    "Issue",
    metadata,
    Column("issue_id", Integer, primary_key=True, unique=True),
    Column("issue", String(100), nullable=False),
)

platform_table = Table(
    "Platform",
    metadata,
    Column("platform_id", Integer, primary_key=True, unique=True),
    Column("platform_focus", String(100), nullable=False),
    Column("target_demographic_id", Integer, nullable=False),
)

candidate_table = Table(
    "Candidate",
    metadata,
    Column("candidate_id", Integer, primary_key=True, unique=True),
    Column("party_id", ForeignKey("Party.party_id"), nullable=False),
    Column("platform_id", ForeignKey("Platform.platform_id"), nullable=False),
    Column("election_id", ForeignKey("Election.election_id"), nullable=False),
    Column("name", String(100), nullable=False),
    Column("age", Integer, nullable=False),
    Column("race", String(100), nullable=False),
    Column("gender", String(100), nullable=False),
    Column("winner", Boolean, nullable=False, default=False),
)

election_table = Table(
    "Election",
    metadata,
    Column("election_id", Integer, primary_key=True, unique=True),
    Column("winner", String(100), nullable=False),
    Column("election_type", String(100), nullable=False),
    Column("year", Integer, nullable=False),
)

candidate_policy_table = Table(
    "Candidate_Policy",
    metadata,
    Column("candidate_id", ForeignKey("Platform.platform_id"), nullable=False),
    Column("policy_id", ForeignKey("Policy.policy_id"), nullable=False),
)

policy_platform = Table(
    "Policy_Platform",
    metadata,
    Column("policy_id", ForeignKey("Policy.policy_id"), nullable=False),
    Column("platform_id", ForeignKey("Platform.platform_id"), nullable=False),
)

# Start transaction to commit DDL to postgres database
with engine.begin() as conn:
    metadata.create_all(conn)
    # Log the tables as they are created
    for table in metadata.tables.keys():
        print(f"{table} successfully created")