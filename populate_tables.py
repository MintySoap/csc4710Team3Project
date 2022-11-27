#Everything taken from https://python.plainenglish.io/generating-a-fake-database-with-python-8523bf6db9ec

from sqlalchemy import create_engine, MetaData, select, update
from faker import Faker
import sys
import random
import datetime
import psycopg2

# Set up connection between sqlalchemy and postgres dbapi
#NOTE: change the line below to fit your system
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

        # This will be different for you depending on the database server you use.
        # NOTE: change the info below to fit your system
        DB_HOST = "localhost"
        DB_NAME = "DatabaseFinalProject"
        DB_USER = "soap"
        DB_PASS = "brimstone42"

        #create table objects
        voters = metadata.tables["voter"]
        location = metadata.tables["location"]
        poll = metadata.tables["polling_location"]
        party = metadata.tables["party"]
        demographic = metadata.tables["demographic"]
        policy = metadata.tables["policy"]
        issue = metadata.tables["issue"]
        platform = metadata.tables["platform"]
        candidate = metadata.tables["candidate"]
        election = metadata.tables["election"]

        #many to many table objects
        candidate_policy = metadata.tables["candidate_policy"]

        #list of fake data
        states_list = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
        party_type_list = ["Democratic", "Republican"]
        election_type_list = ["Senator", "Representative"]
        policy_list = ["Support","Against"]
        platform_focus_list = ["Immigration", "Healthcare", "Civil Rights", "Gun Control", "Jobs and Economy", "diversity and equality", "Criminal Justice", "Environment", "Education", "National Security", "Energy"]
        issue_list = ["What is your stance on abortion?","Should gay couples have the same adoption rights as straight couples?","Do you support the legalization of same sex marriage?",
        "Should the government continue to fund Planned Parenthood?","Should “gender identity” be added to anti-discrimination laws?",
        "Should health insurance providers be required to offer free birth control?","Should people under the age of 18 years old be able to receive gender-transition treatments?",
        "Should the federal government institute a mandatory buyback of assault weapons?","Should marital rape be classified and punished as severely as non-marital rape?",
        "Should transgender athletes be allowed to compete against athletes that differ from their assigned sex at birth?",
        "Should the federal government require racial sensitivity training for employees?",
        "Should a business be able to deny service to a customer if the request conflicts with the owner’s religious beliefs?","Should hate speech be protected by the first amendment?",
        "Do you support the death penalty?","Should the government support a separation of church and state by removing references to God on money, federal buildings, and national monuments?",
        "Should states be allowed to display the Confederate flag on government property?","Should businesses be required to have women on their board of directors?",
        "Should universities provide “trigger warnings” and “safe spaces” for students?","Should terminally ill patients be allowed to end their lives via assisted suicide?",
        "Should women be allowed to wear a Niqāb, or face veil, to civic ceremonies?","Should the military allow women to serve in combat roles?",
        "Should there be more restrictions on the current process of purchasing a gun?",
        "Should teachers be allowed to carry guns at school?","Are you in favor of decriminalizing drug use?","Should there be term limits set for members of Congress?",
        "Should the Supreme Court be reformed to include more seats and term limits on judges?","Should local police increase surveillance and patrol of Muslim neighborhoods?",
        "Should people on the “no-fly list” be banned from purchasing guns and ammunition?","Should members of Congress be allowed to trade stocks while serving in office?",
        "Should the government regulate social media sites, as a means to prevent fake news and misinformation?","Should victims of gun violence be allowed to sue firearms dealers and manufacturers?",
        "Should the NSA (National Security Agency) be allowed to collect basic metadata of citizen’s phone calls such as numbers, timestamps, and call durations?","Do you support the Patriot Act?",
        "Do you support affirmative action programs?","Should the redrawing of Congressional districts be controlled by an independent, non-partisan commission?",
        "Should internet service providers be allowed to speed up access to popular websites (that pay higher rates) at the expense of slowing down access to less popular websites (that pay lower rates)?",
        "Should it be illegal to burn the American flag?","Should the government be allowed to seize private property, with reasonable compensation, for public or civic use?",
        "Should social media companies ban political advertising?","Should the government pass laws which protect whistleblowers?","Should the government raise the retirement age for Social Security?",
        "Should the U.S. government grant immunity to Edward Snowden?","Should the military upgrade Air Force One?","Do you support President Biden’s student loan forgiveness program?",
        "Should the federal government pay for tuition at four-year colleges and universities?","Should critical race theory be taught in K-12 education?",
        "Do you support increasing taxes for the rich in order to reduce interest rates for student loans?","Should the federal government fund Universal preschool?",
        "Should the government offer students a voucher that they can use to attend private schools?","Do you support Common Core national standards?","Do you support charter schools?",
        "Should the government provide financial aid to families affected by COVID related school closures?","Should the government decriminalize school truancy?",
        "Should employers be required to pay men and women the same salary for the same job?","Should the government raise the federal minimum wage?","Should the U.S. raise taxes on the rich?",
        "Should the U.S. raise or lower the tax rate for corporations?","Should businesses be required to provide paid leave for full-time employees during the birth of a child or sick family member?",
        "Should the government make cuts to public spending in order to reduce the national debt?","Do you believe labor unions help or hurt the economy?",
        "Do you support a universal basic income program?","Should the IRS create a free electronic tax filing system?","Should there be fewer or more restrictions on current welfare benefits?",
        "Should the government require businesses to pay salaried employees, making up to $46k/year, time-and-a-half for overtime hours?",
        "Should the government use economic stimulus to aid the country during times of recession?",
        "Should the government increase the tax rate on profits earned from the sale of stocks, bonds, and real estate?","Should welfare recipients be tested for drugs?",
        "Should the Federal Government suspend the gasoline tax?",
        "Should the government prevent “mega mergers” of corporations that could potentially control a large percentage of market share within its industry?",
        "Should the current estate tax rate be decreased?","Should the President offer tax breaks to individual companies to keep jobs in the U.S.?",
        "Should the government break up Amazon, Facebook and Google?","Should U.S. citizens be allowed to save or invest their money in offshore bank accounts?",
        "Should the U.S. continue to participate in the North American Free Trade Agreement (NAFTA)?","Should the United States transition to a four-day workweek?",
        "Should pension plans for federal, state, and local government workers be transitioned into privately managed accounts?",
        "Should the government add or increase tariffs on products imported into the country?",
        "Should the government subsidize farmers?","Would you favor an increased sales tax in order to reduce property taxes?","Should the U.S. increase tariffs on imported products from China?",
        "Should the government acquire equity stakes in companies it bails out during a recession?","Should the Federal Reserve Bank be audited by Congress?",
        "Should gig workers such as Uber drivers be classified as employees?","Should pension payments be increased for retired government workers?",
        "Should an in-state sales tax apply to online purchases of in-state buyers from out-of-state sellers?",
        "Should the government classify cryptocurrencies as legal forms of payment?",
        "Should the underlying technology of our financial system (credit, savings, investing, purchasing) transition from an institutionally owned industry to a decentralized protocol (similar to the internet) that is not owned by any corporation?",
        "Do you support the Trans-Pacific Partnership (TPP)?","Should the government regulate the prices of life-saving drugs?",
        "Should the government increase funding for mental health research and treatment?","Do you support a single-payer healthcare system?",
        "Should health insurers be allowed to deny coverage to individuals who have a pre-existing condition?","Do you support the legalization of Marijuana?",
        "Should the government require employees of large businesses to be vaccinated from COVID?",
        "Should the federal government increase funding of health care for low income individuals (Medicaid)?",
        "Do you support the Patient Protection and Affordable Care Act (Obamacare)?","Should the federal government be allowed to negotiate drug prices for Medicare?",
        "Should cities open drug “safe havens” where people who are addicted to illegal drugs can use them under the supervision of medical professionals?",
        "Should people be required to work in order to receive Medicaid?",
        "Should the government fund the World Health Organization?","Should private businesses have the right to ask customers for their vaccination status?",
        "Should there be more or less privatization of veterans’ healthcare","Should the government increase environmental regulations to prevent climate change?",
        "Should drilling be allowed in the Alaska Wildlife Refuge?","Should the U.S. expand offshore oil drilling?",
        "Do you support the use of hydraulic fracking to extract oil and natural gas resources?","Should the government stop construction of the Dakota Access pipeline?",
        "Should the government give tax credits and subsidies to the wind power industry?","Should the U.S. withdraw from the Paris Climate Agreement?",
        "Should researchers be allowed to use animals in testing the safety of drugs, vaccines, medical devices, and cosmetics?",
        "Should disposable products (such as plastic cups, plates, and cutlery) that contain less than 50% of biodegradable material be banned?",
        "Should cities be allowed to offer private companies economic incentives to relocate?","Should police officers be required to wear body cameras?",
        "Do you support qualified immunity for police officers?","Should funding for local police departments be redirected to social and community based programs?",
        "Should police departments be allowed to use military grade equipment?","Should prisons ban the use of solitary confinement for juveniles?",
        "Should the government hire private companies to run prisons?",
        "Do you support mandatory minimum prison sentences for people charged with drug possession?",
        "Do you support limiting police unions collective bargaining power for cases involving misconduct?","Should drug traffickers receive the death penalty?",
        "Should non-violent prisoners be released from jail in order to reduce overcrowding?",
        "Should convicted criminals have the right to vote?","Should children of illegal immigrants be granted legal citizenship?",
        "Should Muslim immigrants be banned from entering the country until the government improves its ability to screen out potential terrorists?",
        "Should illegal immigrants have access to government-subsidized healthcare?","Should the U.S. increase restrictions on its current border security policy?",
        "Should the U.S. build a wall along the southern border?",
        "Should local law enforcement be allowed to detain illegal immigrants for minor crimes and transfer them to federal immigration authorities?",
        "Should immigrants be deported if they commit a serious crime?",
        "Should sanctuary cities receive federal funding?","Should working illegal immigrants be given temporary amnesty?","Should immigrants be required to learn English?",
        "Should immigrants be required to pass a citizenship test to demonstrate a basic understanding of our country’s language, history, and government?",
        "Should the US increase or decrease the amount of temporary work visas given to high-skilled immigrant workers?",
        "Should undocumented immigrants be offered in-state tuition rates at public colleges within their residing state?","Should immigrants to the United States be allowed to hold dual citizenship status?",
        "Should foreign lobbyists be allowed to raise money for American elections?","Should a photo ID be required to vote?",
        "Should there be a limit to the amount of money a candidate can receive from a donor?","Should foreigners, currently residing in the United States, have the right to vote?",
        "Should the electoral college be abolished?","Minimum Voting Age PollMinimum Voting Age","Should the minimum voting age be lowered?",
        "Should corporations, unions, and non-profit organizations be allowed to donate to political parties?",
        "Should there be a 5-year ban on White House and Congressional officials from becoming lobbyists after they leave the government?","Should a politician, who has been formerly convicted of a crime, be allowed to run for office?",
        "Should political candidates be required to release their recent tax returns to the public?",
        "Should the government require children to be vaccinated for preventable diseases?","Do you support the use of nuclear energy?",
        "Should producers be required to label genetically engineered foods (GMOs)?",
        "Should the government fund space travel?","Should the government increase spending on public transportation?",
        "Should every 18 year old citizen be required to provide at least one year of military service?","Should the U.S. remain in the United Nations?",
        "Should the U.S. go to war with Iran?","Should the U.S. remain in NATO?","Should the United States provide military supplies and funding to Ukraine?",
        "Should the government increase or decrease military spending?","Should the U.S. continue to support Israel?","Should the government attempt to influence foreign elections?",
        "Should the military fly drones over foreign countries to gain intelligence and kill suspected terrorists?","Should the World Bank and International Monetary Fund provide financial aid to the Taliban government in Afghanistan?",
        "Should the military be allowed to use enhanced interrogation techniques, such as waterboarding, to gain information from suspected terrorists?",
        "Should the US increase or decrease foreign aid spending?",
        "Should foreign terrorism suspects be given constitutional rights?","Should Ukraine join NATO?",
        "Should the U.S. conduct military strikes against North Korea in order to destroy their long-range missile and nuclear weapons capabilities?",
        "Should the U.S. defend other NATO countries that maintain low military defense budgets relative to their GDP?",
        "Should the U.S. sell military weapons to India in order to counter Chinese and Russian influence?",
        "Should the U.S. continue NSA surveillance of its allies?","Do you support President Obama’s move to lift the trade and travel embargo on Cuba?",
        "Should Jerusalem be recognized as the capital of Israel?","Should the government cancel production of the F-35 fighter?",
        "Should homeless individuals, that have refused available shelter or housing, be allowed to sleep or encamp on public property?",
        "Should the President be able to authorize military force against Al-Qaeda without Congressional approval?","Should the US assassinate suspected terrorists in foreign countries?"
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

        if (self.table == "voter"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    cand_id = conn.execute(select(candidate.c.candidate_id)).fetchall()
                    poll_id = conn.execute(select(poll.c.poll_location_id)).fetchall()
                    dem_id = conn.execute(select(demographic.c.demographic_id)).fetchall()

                    insert_stmt = voters.insert().values(
                        voter_id = random.randint(1,50000000),
                        demographic_id = random.choice(dem_id)[0],
                        candidate_id = random.choice(cand_id)[0],
                        poll_location_id =  random.choice(poll_id)[0],
                        name = faker.name(),
                        age = random.randint(18, 95),
                        race = random.choice(race_list),
                        gender = random.choice(gender_list),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "location"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = location.insert().values(
                        location_id = random.randint(1,50000000),
                        state = random.choice(states_list),
                        city = faker.city(),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "polling_location"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    loc_id = conn.execute(select(location.c.location_id)).fetchall()

                    insert_stmt = poll.insert().values(
                        poll_location_id = random.randint(1,50000000),
                        location_id = random.choice(loc_id)[0],
                        ballot_amount = random.randint(1,1000000),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "party"):
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

        if(self.table == "demographic"):
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

        if(self.table == "policy"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    iss_id = conn.execute(select(issue.c.issue_id)).fetchall()

                    insert_stmt = policy.insert().values(
                        policy_id = random.randint(1,50000000),
                        issue_id = random.choice(iss_id)[0],
                        policy = random.choice(policy_list),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "issue"):
            with engine.begin() as conn:
                for num_of_issue in range(self.num_records):
                    insert_stmt = issue.insert().values(
                        issue_id = random.randint(1,50000000),
                        issue = issue_list[num_of_issue],
                    )
                    conn.execute(insert_stmt)

        if(self.table == "platform"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    target_id = conn.execute(select(demographic.c.demographic_id)).fetchall()
                    insert_stmt = platform.insert().values(
                        platform_id = random.randint(1,50000000),
                        platform_focus = random.choice(platform_focus_list),
                        target_demographic_id = random.choice(target_id)[0],
                    )
                    conn.execute(insert_stmt)

        if(self.table == "candidate"):
            with engine.begin() as conn:
                connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
                connection.autocommit = True
                cursor = connection.cursor() #the cursor is to perform database operations and queries
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
                get_election_ids = "SELECT election_id FROM public.candidate;"
                cursor.execute(get_election_ids)
                election_ids_list = cursor.fetchall()

                #makes a dictionary of all of the elections with empty candidates
                candidates_dict = dict()
                for elec in election_ids_list:
                    candidates_dict.update({elec : list()})

                #updates the dictionary with the candidates for each election
                for elect in election_ids_list:
                    get_candidates_for_election = "SELECT candidate_id FROM public.candidate WHERE election_id = " + elect + ";"
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
                connection.close()

        #note: generate elections before candidates so all the elections have a place holder.
        if(self.table == "election"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = election.insert().values(
                        election_id = random.randint(1,50000000),
                        winner = faker.name(), #note: After all of the candidates are inserted, we will then choose one of the candidates at random and make one of them the winner and assign it here
                        election_type = random.choice(election_type_list),
                        year = random.randint(1900,2022),
                    )
                    conn.execute(insert_stmt)

        if(self.table == "candidate_policy"):
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    can_id = conn.execute(select(candidate.c.candidate_id)).fetchall()
                    pol_id = conn.execute(select(policy.c.policy_id)).fetchall()

                    insert_stmt = candidate_policy.insert().values(
                        candidate_id = random.choice(can_id)[0],
                        policy_id = random.choice(pol_id)[0],
                    )
                    conn.execute(insert_stmt)



if __name__ == "__main__":    
    generate_data = GenerateData()   
    generate_data.create_data()