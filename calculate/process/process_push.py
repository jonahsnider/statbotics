from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

import pandas as pd

from process.logging import printStats

'''
from classes.classes import (
    Year,
    Team,
    TeamYear,
    Event,
    TeamEvent,
    Match,
    TeamMatch
)
'''


def getYears(SQL_Read):
    print("Years")
    years = []
    year_objs = SQL_Read.getYears()
    print(len(year_objs))
    for i, year in enumerate(year_objs):
        if i % 100000 == 0: print(i)  # noqa 701
        years.append([
            year.id,
            round(year.elo_acc, 4),
            round(year.elo_mse, 4),
            round(year.opr_acc, 4),
            round(year.opr_mse, 4),
            round(year.mix_acc, 4),
            round(year.mix_mse, 4),
            round(year.rp1_acc, 4),
            round(year.rp1_mse, 4),
            round(year.rp2_acc, 4),
            round(year.rp2_mse, 4),
            round(year.score_sd, 2),
            round(year.score_mean, 2)
        ])

    years = pd.DataFrame(years,
                         columns=["year", "elo_acc", "elo_mse", "opr_acc",
                                  "opr_mse", "mix_acc", "mix_mse", "rp1_acc",
                                  "rp1_mse", "rp2_acc", "rp2_mse", "score_sd",
                                  "score_mean"])

    years = years.sort_values(by=['year'])
    return years


def getTeams(SQL_Read):
    print("Teams")
    teams = []
    team_objs = SQL_Read.getTeams()
    print(len(team_objs))
    for i, team in enumerate(team_objs):
        if i % 100000 == 0: print(i)  # noqa 701
        teams.append([
            team.id,
            team.name,
            team.state,
            team.country,
            team.district,
            team.active,
            round(team.elo),
            round(team.elo_recent),
            round(team.elo_mean),
            round(team.elo_max)
        ])

    teams = pd.DataFrame(teams,
                         columns=["team", "name", "state", "country",
                                  "district", "active", "elo", "elo_recent",
                                  "elo_mean", "elo_max"])

    teams = teams.sort_values(by=['team'])
    return teams


def getTeamYears(SQL_Read):
    print("Team Years")
    team_years = []
    team_year_objs = SQL_Read.getTeamYears()
    print(len(team_year_objs))
    for i, team_year in enumerate(team_year_objs):
        if i % 100000 == 0: print(i)  # noqa 701
        team_years.append([
            team_year.id,
            team_year.year_id,
            team_year.team_id,
            team_year.team.name,
            team_year.team.state,
            team_year.team.country,
            team_year.team.district,
            round(team_year.elo_start),
            round(team_year.elo_pre_champs),
            round(team_year.elo_end),
            round(team_year.elo_mean),
            round(team_year.elo_max),
            round(team_year.elo_diff),
            round(team_year.opr_end),
            round(team_year.opr_auto),
            round(team_year.opr_teleop),
            round(team_year.opr_1),
            round(team_year.opr_2),
            round(team_year.opr_endgame),
            round(team_year.ils_1, 2),
            round(team_year.ils_2, 2)
        ])

    team_years = pd.DataFrame(team_years,
                              columns=["id", "year", "team", "name", "state",
                                       "country", "district", "elo_start",
                                       "elo_pre_champs", "elo_end", "elo_mean",
                                       "elo_max", "elo_diff", "opr",
                                       "opr_auto", "opr_teleop", "opr_1",
                                       "opr_2", "opr_endgame", "ils_1",
                                       "ils_2"])

    team_years = team_years.sort_values(by=['year', 'team'])
    return team_years


def getEvents(SQL_Read):
    print("Events")
    events = []
    event_objs = SQL_Read.getEvents()
    print(len(event_objs))
    for i, event in enumerate(event_objs):
        if i % 100000 == 0: print(i)  # noqa 701
        events.append([
            event.id,
            event.year_id,
            event.key,
            event.name,
            event.state,
            event.country,
            event.district,
            event.type,
            event.week,
            round(event.elo_top8),
            round(event.elo_top24),
            round(event.elo_mean),
            round(event.opr_top8),
            round(event.opr_top24),
            round(event.opr_mean)
        ])

    events = pd.DataFrame(events,
                          columns=["id", "year", "key", "name", "state",
                                   "country", "district", "type", "week",
                                   "elo_top8", "elo_top24", "elo_mean",
                                   "opr_top8", "opr_top24", "opr_mean"])

    events = events.sort_values(by=['year', 'key'])
    return events


def getTeamEvents(SQL_Read):
    print("Team Events")
    team_events = []
    team_event_objs = SQL_Read.getTeamEvents()
    print(len(team_event_objs))
    for i, team_event in enumerate(team_event_objs):
        if i % 100000 == 0: print(i)  # noqa 701
        team_events.append([
            team_event.id,
            team_event.team_id,
            team_event.year_id,
            team_event.event.key,
            round(team_event.elo_start),
            round(team_event.elo_pre_playoffs),
            round(team_event.elo_end),
            round(team_event.elo_mean),
            round(team_event.elo_max),
            round(team_event.elo_diff),
            round(team_event.opr_start),
            round(team_event.opr_end),
            round(team_event.opr_auto),
            round(team_event.opr_teleop),
            round(team_event.opr_1),
            round(team_event.opr_2),
            round(team_event.opr_endgame),
            round(team_event.opr_fouls),
            round(team_event.opr_no_fouls),
            round(team_event.ils_1_start, 2),
            round(team_event.ils_2_start, 2),
            round(team_event.ils_1_end, 2),
            round(team_event.ils_2_end, 2),
        ])

    team_events = pd.DataFrame(team_events,
                               columns=["id", "team", "year", "event",
                                        "elo_start", "elo_pre_playoffs",
                                        "elo_end", "elo_mean", "elo_max",
                                        "elo_diff", "opr_start", "opr_end",
                                        "opr_auto", "opr_teleop", "opr_1",
                                        "opr_2", "opr_endgame", "opr_fouls",
                                        "opr_no_fouls", "ils_1_start",
                                        "ils_2_start", "ils_1_end",
                                        "ils_2_end"])

    team_events = team_events.sort_values(by=['year', 'team', 'event'])
    return team_events


def getMatches(SQL_Read):
    print("Matches")
    matches = []
    match_objs = SQL_Read.getMatches()
    print(len(match_objs))
    for i, match in enumerate(match_objs):
        if i % 100000 == 0: print(i)  # noqa 701
        matches.append([
            match.id,
            match.year_id,
            match.event.key,
            match.key,
            match.comp_level,
            match.set_number,
            match.match_number,
            match.playoff,
            match.red,
            match.blue,
            match.red_score,
            match.blue_score,
            match.winner,
            match.elo_winner,
            round(match.elo_win_prob, 2),
            match.opr_winner,
            round(match.opr_win_prob, 2),
            match.mix_winner,
            round(match.mix_win_prob, 2),
            match.red_rp_1,
            round(match.red_rp_1_prob, 2),
            match.red_rp_2,
            round(match.red_rp_2_prob, 2),
            match.blue_rp_1,
            round(match.blue_rp_1_prob, 2),
            match.blue_rp_2,
            round(match.blue_rp_2_prob, 2),
            match.red_auto,
            match.blue_auto,
            match.red_teleop,
            match.blue_teleop,
            match.red_1,
            match.blue_1,
            match.red_2,
            match.blue_2,
            match.red_endgame,
            match.blue_endgame,
            match.red_fouls,
            match.blue_fouls,
            match.red_no_fouls,
            match.blue_no_fouls,
        ])

    matches = pd.DataFrame(matches,
                           columns=["id", "year", "event", "key", "comp_level",
                                    "set_number", "match_number", "playoff",
                                    "red", "blue", "red_score", "blue_score",
                                    "winner", "elo_winner", "elo_win_prob",
                                    "opr_winner", "opr_win_prob", "mix_winner",
                                    "mix_win_prob", "red_rp_1",
                                    "red_rp_1_prob", "red_rp_2",
                                    "red_rp_2_prob", "blue_rp_1",
                                    "blue_rp_1_prob", "blue_rp_2",
                                    "blue_rp_2_prob", "red_auto", "blue_auto",
                                    "red_teleop", "blue_teleop", "red_1",
                                    "blue_1", "red_2", "blue_2", "red_endgame",
                                    "blue_endgame", "red_fouls", "blue_fouls",
                                    "red_no_fouls", "blue_no_fouls"
                                    ])

    matches = matches.sort_values(by=['year', 'event', 'key'])
    return matches


def getTeamMatches(SQL_Read):
    print("Team Matches")
    team_matches = []
    team_match_objs = SQL_Read.getTeamMatches()
    print(len(team_match_objs))
    for i, team_match in enumerate(team_match_objs):
        if i % 100000 == 0: print(i)  # noqa 701
        team_matches.append([
            team_match.id,
            team_match.team_id,
            team_match.year_id,
            team_match.event.key,
            team_match.match.key,
            team_match.alliance,
            round(team_match.elo),
            round(team_match.opr_score),
            round(team_match.ils_1, 2),
            round(team_match.ils_2, 2),
        ])

    team_matches = pd.DataFrame(team_matches,
                                columns=["id", "team", "year", "event",
                                         "match", "alliance", "elo", "opr",
                                         "ils_1", "ils_2"])

    team_matches = team_matches.sort_values(by=['year', 'team', 'event', 'match'])  # noqa 502
    return team_matches


def pushClean(SQL_Read, cloud_engine):
    years = getYears(SQL_Read)
    teams = getTeams(SQL_Read)
    teamYears = getTeamYears(SQL_Read)
    events = getEvents(SQL_Read)
    teamEvents = getTeamEvents(SQL_Read)
    matches = getMatches(SQL_Read)
    teamMatches = getTeamMatches(SQL_Read)

    years.to_sql('rankings_year', cloud_engine, if_exists='replace', index=False)  # noqa 502
    teams.to_sql('rankings_team', cloud_engine, if_exists='replace', index=False)  # noqa 502
    teamYears.to_sql('rankings_teamyear', cloud_engine, if_exists='replace', index=False)  # noqa 502
    events.to_sql('rankings_event', cloud_engine, if_exists='replace', index=False)  # noqa 502
    teamEvents.to_sql('rankings_teamevent', cloud_engine, if_exists='replace', index=False)  # noqa 502
    matches.to_sql('rankings_match', cloud_engine, if_exists='replace', index=False)  # noqa 502
    teamMatches.to_sql('rankings_teammatch', cloud_engine, if_exists='replace', index=False)  # noqa 502

    printStats()


def drop_table(table_name, engine):
    base = declarative_base()
    metadata = MetaData(engine, reflect=True)
    table = metadata.tables.get(table_name)
    if table is not None:
        base.metadata.drop_all(engine, [table], checkfirst=True)


'''
def pushAll(SQL_Read, cloud_engine, local_session):
    drop_table('team_matches', cloud_engine)
    drop_table('matches', cloud_engine)
    drop_table('team_events', cloud_engine)
    drop_table('events', cloud_engine)
    drop_table('team_years', cloud_engine)
    drop_table('teams', cloud_engine)
    drop_table('years', cloud_engine)

    print("Years")
    years = pd.read_sql(local_session.query(Year).statement, local_session.bind)  # noqa 502
    years.to_sql('years', cloud_engine, index=False)

    print("Matches")
    matches = pd.read_sql(local_session.query(Match).statement, local_session.bind)  # noqa 502
    matches.to_sql('matches', cloud_engine, index=False)

    print("Team Events")
    teamEvents = pd.read_sql(local_session.query(TeamEvent).statement, local_session.bind)  # noqa 502
    teamEvents.to_sql('team_events', cloud_engine, index=False)  # noqa 502

    print("Events")
    events = pd.read_sql(local_session.query(Event).statement, local_session.bind)  # noqa 502
    events.to_sql('events', cloud_engine, index=False)

    print("Team Years")
    teamYears = pd.read_sql(local_session.query(TeamYear).statement, local_session.bind)  # noqa 502
    teamYears.to_sql('team_years', cloud_engine, index=False)  # noqa 502

    print("Teams")
    teams = pd.read_sql(local_session.query(Team).statement, local_session.bind)  # noqa 502
    teams.to_sql('teams', cloud_engine, index=False)

    print("Team Matches")
    teamMatches = pd.read_sql(local_session.query(TeamMatch).statement, local_session.bind)  # noqa 502
    teamMatches.to_sql('team_matches', cloud_engine, index=False)  # noqa 502

    printStats()
'''


def main(SQL, SQL_Read):
    cloud_engine = SQL.getCloudEngine()
    # local_session = SQL.getLocalSession()
    pushClean(SQL_Read, cloud_engine)
    # pushAll(SQL_Read, cloud_engine, local_session)
    printStats()
