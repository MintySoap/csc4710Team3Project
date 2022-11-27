#Everything taken from https://python.plainenglish.io/generating-a-fake-database-with-python-8523bf6db9ec

from sqlalchemy import create_engine, MetaData, select, update
from faker import Faker
import sys
import random
import datetime

# Set up connection between sqlalchemy and postgres dbapi
engine = create_engine(
    "postgresql://soap:brimstone42@localhost:5432/DatabaseFinalProject"
)

# Create a metadata object
metadata = MetaData()

# Instantiate faker class
faker = Faker()

# Reflect metadata/schema from existing postgres database
with engine.connect() as conn:
    metadata.reflect(conn)

class GenerateData:
    """
    generate a specific number of records to a target table in the
    postgres database.
    """

    def __init__(self):
        """
        define command line arguments.
        """

        self.table = sys.argv[1]
        self.num_records = int(sys.argv[2])

    def create_data(self):
        """
        using the faker library, generate data and execute DML.
        """

        #create table objects
        voters = metadata.tables["Voter"]
        location = metadata.tables["Location"]
        poll = metadata.tables["Polling_Location"]
        party = metadata.tables["Party"]
        demographic = metadata.tables["Demographic"]
        policy = metadata.tables["Policy"]
        issue = metadata.tables["Issue"]
        platform = metadata.tables["Platform"]
        candidate = metadata.tables["Candidate"]
        election = metadata.tables["Election"]

        #many to many table objects
        demographic_voter = metadata.tables["Demographic_Voter"]
        candidate_policy = metadata.tables["Candidate_Policy"]
        policy_platform = metadata.tables["Policy_Platform"]

        #list of fake data
        states_list = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
        party_type_list = ["Democratic", "Republican"]
        election_type_list = ["Senator", "Representative"]
        policy_list = ["Support","Against"]
        platform_focus_list = ["Immigration", "Healthcare", "Civil Rights", "Gun Control", "Jobs and Economy", "diversity and equality", "Criminal Justice", "Environment", "Education", "National Security", "Energy"]
        issue_list = ["Allowing war immigrants into the country", "Opening up the borders during the pandemic", "Allowing illegal residents to become naturalized as citizens",
            "Providing universal healthcare", "Regulating pharmaceutical companies", "Increasing the availability of healthcare in certain areas",
            "Raising the standards of purchasing a gun", "Requiring further screening before the purchase of a gun", "Allowing for open carry in certain areas", "Limiting the range of guns civilians can buy",
            "Legalizing same sex marriage", "Legalizing marijuana",
            "Increasing the minimum wage", "Further taxing imported goods", "Providing stimulus for citizens and businesses during the pandemic",
            "Providing more funds to federal prisons", "Regulating prisons to ensure better living conditions", "Further regulating law enforcement to avoid wrongful arrests",
            "Regulating the waste that companies can dispose of", "Increasing funding for environmental projects and national parks",
            "Enforcing common core education", "Raising the standard of America's 'no child left behind' policy", "Provide further funding for public schools",
            "Increase funding to the military", "Increase the screening of certain groups of individuals upon entering the country",
            "Increasing funding for solar power", "Increasing funding for wind power", "Increasing funding for hydroelectric power", "Increasing funding for nuclear power", "Increasing funding for oil companies"
        ]
        race_list = ["Hispanic","White","Black","American Indian","Asian","Native Hawaiian","Some Other Race","Multiracial"]
        gender_list = ["Male", "Female"]

        #demographic data
        education_list = ["Did not finish Highschool", "Highschool Graduate", "College Graduate", "Higher Degree"] #4
        wealth_list = ["Low income", "Middle income", "Upper income"] #3
        marital_status_list = ["Married", "Unmarried"] #2
        religion_list = ["Christian", "Muslim", "Jewish", "Buddhist", "Hindu", "Atheist", "Agnostic", "Other"] #8

        if(self.table not in metadata.tables.keys()):
            return print(f"{self.table} does not exist")

        if (self.table == "Voter"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    cand_id = conn.execute(select(candidate.c.candidate_id)).fetchall()
                    poll_id = conn.execute(select(poll.c.poll_location_id)).fetchall()
                    dem_id = conn.execute(select(demographic.c.demographic_id)).fetchall()

                    insert_stmt = voters.insert().values(
                        voter_id = random.randint(1,50000000),
                        demographic_id = random.choice(dem_id)[0],
                        candidate_id = random.choice(cand_id)[0],
                        poll_id =  random.choice(poll_id)[0],
                        name = faker.name(),
                        age = random.randint(18, 95),
                        race = random.choice(race_list),
                        gender = random.choice(gender_list),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Location"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = location.insert().values(
                        location_id = random.randint(1,50000000),
                        state = random.choice(states_list),
                        city = faker.city(),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Polling_Location"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    loc_id = conn.execute(select(location.c.location_id)).fetchall()

                    insert_stmt = poll.insert().values(
                        poll_location_id = random.randint(1,50000000),
                        location_id = random.choice(loc_id)[0],
                        ballot_amount = random.randint(1,1000000),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Party"):
            with engine.begin() as conn:
                for i in range(2):
                    for f in range(self.num_records):
                        plat_id = conn.execute(select(platform.c.platform_id)).fetchall()
                        insert_stmt = party.insert().values(
                            party_id = random.randint(1,50000000),
                            platform_id = random.choice(plat_id)[0],
                            state = states_list[f],
                            party_type = party_type_list[i],
                        )
                        conn.execute(insert_stmt)

        if(self.table == "Demographic"):
            with engine.begin() as conn:
                for a in education_list:
                    for b in wealth_list:
                        for c in marital_status_list:
                            for d in religion_list:
                                insert_stmt = demographic.insert().values(
                                    demographic_id = random.randint(1,50000000),
                                    education = a,
                                    wealth = b,
                                    marital_status = c,
                                    religion = d,
                                )
                                conn.execute(insert_stmt)

        if(self.table == "Policy"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    iss_id = conn.execute(select(issue.c.issue_id)).fetchall()

                    insert_stmt = policy.insert().values(
                        policy_id = random.randint(1,50000000),
                        issue_id = random.choice(iss_id)[0],
                        policy = random.choice(policy_list),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Issue"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = issue.insert().values(
                        issue_id = random.randint(1,50000000),
                        issue = random.choice(issue_list),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Platform"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    target_id = conn.execute(select(demographic.c.demographic_id)).fetchall()
                    insert_stmt = platform.insert().values(
                        platform_id = random.randint(1,50000000),
                        platform_focus_id = random.choice(platform_focus_list),
                        target_demographic_id = random.choice(target_id),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Candidate"):
            with engine.begin() as conn:
                cursor = conn.cursor() #the cursor is to perform database operations and queries
                for _ in range(self.num_records):
                    par_id = conn.execute(select(party.c.party_id)).fetchall()
                    plat_id = conn.execute(select(platform.c.platform_id)).fetchall()
                    elec_id = conn.execute(select(election.c.election_id)).fetchall()

                    insert_stmt = candidate.insert().values(
                        candidate_id = random.randint(1,5000000),
                        party_id = random.choice(par_id)[0],
                        platform_id = random.choice(plat_id)[0],
                        election_id = random.choice(elec_id)[0],
                        name = faker.name(),
                        age = random.randint(30, 80),
                        race = random.choice(race_list),
                        gender = random.choice(gender_list),
                        winner = False,
                    )
                    conn.execute(insert_stmt)

                #makes a list of all the election id's
                get_election_ids = "SELECT election_id FROM Candidate"
                cursor.execute(get_election_ids)
                election_ids_list = cursor.fetchall()

                #makes a dictionary of all of the elections with empty candidates
                candidates_dict = dict()
                for elec in election_ids_list:
                    candidates_dict.update({elec : list()})

                #updates the dictionary with the candidates for each election
                for elect in election_ids_list:
                    get_candidates_for_election = "SELECT candidate_ID FROM Candidate WHERE election_id = " + elect
                    cursor.execute(get_candidates_for_election)
                    candidates_list = cursor.fetchall()
                    candidates_dict.update({elect : candidates_list})

                #blank list of winners
                winners_list = list()

                #Updates the election table with a randomly chosen candidate from each election in the dictionary
                for elections in election_ids_list:
                    winner = random.choice(candidates_dict[elections])
                    winners_list.append(winner) #with every update we will also record a list of the winners
                    update = update(election)
                    update = update.values({"winner" : winner}) #so this will randomly choose a candidate from the appropriate election to become a winner
                    update = update.where(election.c.election_id == elections)
                    conn.execute(update)

                #updates the candidate table with the candidates that actually won
                for winners in winners_list:
                    update = update(candidate)
                    update = update.values({"winner" : True})
                    update = update.where(candidate.c.candidate_id == winners)
                    conn.execute(update)

        #note: generate elections before candidates so all the elections have a place holder.
        if(self.table == "Election"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = election.insert().values(
                        election_id = random.randint(1,50000000),
                        winner = faker.name(), #note: After all of the candidates are inserted, we will then choose one of the candidates at random and make one of them the winner and assign it here
                        election_type = random.choice(election_type_list),
                        year = random.randint(1900,2022),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Candidate_Policy"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    can_id = conn.execute(select(candidate.c.candidate_id)).fetchall()
                    pol_id = conn.execute(select(policy.c.policy_id)).fetchall()

                    insert_stmt = candidate_policy.insert().values(
                        candidate_id = random.choice(can_id)[0],
                        policy_id = random.choice(pol_id)[0],
                    )
                    conn.execute(insert_stmt)

        if(self.table == "Policy_Platform"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    poli_id = conn.execute(select(policy.c.policy_id)).fetchall()
                    platf_id = conn.execute(select(platform.c.platform_id)).fetchall()

                    insert_stmt = policy_platform.insert().values(
                        policy_id = random.choice(poli_id)[0],
                        platform_id = random.choice(platf_id),
                    )
                    conn.execute(insert_stmt)



if __name__ == "__main__":    
    generate_data = GenerateData()   
    generate_data.create_data()