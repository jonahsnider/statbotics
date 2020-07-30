import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

import { Paper, Typography } from "@material-ui/core";
import { Tabs, Tab, Container, Row, Col } from "react-bootstrap";

import { ReactTable } from "./../../../components";

import {
  fetchEvent,
  fetchTeamEvents,
  fetchRankings,
  fetchMatches_Event,
} from "./../../../api";

import styles from "./EventView.module.css";

export default function EventView() {
  let { key } = useParams();

  const [event, setEvent] = useState("");
  const [year, setYear] = useState("");

  const [rankings, setRankings] = useState([]);
  const [rawStats, setRawStats] = useState([]);
  const [stats, setStats] = useState([]);

  const [rawMatches, setRawMatches] = useState([]);
  const [matches, setMatches] = useState([]);

  //column name, searchable, visible, link, hint
  const columns = [
    ["Number", true, true, false, ""],
    ["Name", true, true, true, "Click name for details"],
    ["Rank", false, true, false, "Rank at Event"],
    ["Elo", false, true, false, "Current Elo"],
    ["OPR", false, true, false, "Current OPR"],
    ["Auto OPR", false, true, false, ""],
    ["Teleop OPR", false, true, false, ""],
    ["Endgame OPR", false, true, false, ""],
    ["ILS 1", false, true, false, ""],
    ["ILS 2", false, true, false, ""],
  ];

  const oldColumns = [
    ["Number", true, true, false, ""],
    ["Name", true, true, true, "Click name for details"],
    ["Rank", false, true, false, "Rank at Event"],
    ["Elo", false, true, false, "Current Elo"],
    ["OPR", false, true, false, "Current OPR"],
  ];

  useEffect(() => {
    const getEvent = async (key) => {
      const event = await fetchEvent(key);
      setEvent(event["name"]);
      setYear(event["year"]);
    };

    const getTeamEvents = async (key) => {
      const team_events = await fetchTeamEvents(key, "-elo_end");
      setRawStats(team_events);
    };

    const getRankings = async (key) => {
      const rankings = await fetchRankings(key);
      setRankings(rankings);
    };

    const getMatches = async (key) => {
      const matches = await fetchMatches_Event(key);
      setRawMatches(matches);
    };

    getEvent(key);
    getTeamEvents(key);
    getRankings(key);
    getMatches(key);
  }, [key]);

  useEffect(() => {
    function clean(rawStats, rankings) {
      let cleanStats;
      if (year >= 2016) {
        cleanStats = rawStats.map(function (x, i) {
          return [
            x["team"],
            "./../teams/" + x["team"] + "|" + x["name"],
            rankings[x["team"]],
            x["elo_end"],
            parseInt(x["opr_no_fouls"] * 10) / 10,
            parseInt(x["opr_auto"] * 10) / 10,
            parseInt(x["opr_teleop"] * 10) / 10,
            parseInt(x["opr_endgame"] * 10) / 10,
            x["ils_1_end"],
            x["ils_2_end"],
          ];
        });
      } else {
        cleanStats = rawStats.map(function (x, i) {
          return [
            x["team"],
            "./../teams/" + x["team"] + "|" + x["name"],
            rankings[x["team"]],
            x["elo_end"],
            parseInt(x["opr_end"] * 10) / 10,
          ];
        });
      }
      cleanStats.sort((a, b) => a[2] - b[2]);
      return cleanStats;
    }

    setStats(clean(rawStats, rankings));
  }, [year, rawStats, rankings]);

  useEffect(() => {
    function clean(rawMatches, year) {
      let cleanMatches;
      if (year >= 2016) {
        console.log("HERE");
        cleanMatches = rawMatches.map(function (x, i) {
          return {
            match: x["key"].split("_")[1],
            blue: x["blue"].split(","),
            red: x["red"].split(","),
            blue_score: x["blue_score"],
            red_score: x["red_score"],
            winner: x["winner"],
            winner_pred: x["mix_winner"],
            win_prob:
              x["mix_winner"] === "red"
                ? x["mix_win_prob"]
                : 1 - x["mix_win_prob"],
            winner_correct: x["winner"] === x["mix_winner"],
            blue_rp_1: x["blue_rp_1"],
            blue_rp_1_prob: x["blue_rp_1_prob"],
            blue_rp_1_correct:
              x["blue_rp_1"] === 1
                ? x["blue_rp_1_prob"] >= 0.5
                : x["blue_rp_1_prob"] < 0.5,
            blue_rp_2: x["blue_rp_2"],
            blue_rp_2_prob: x["blue_rp_2_prob"],
            blue_rp_2_correct:
              x["blue_rp_2"] === 1
                ? x["blue_rp_2_prob"] >= 0.5
                : x["blue_rp_2_prob"] < 0.5,
            red_rp_1: x["red_rp_1"],
            red_rp_1_prob: x["red_rp_1_prob"],
            red_rp_1_correct:
              x["red_rp_1"] === 1
                ? x["red_rp_1_prob"] >= 0.5
                : x["red_rp_1_prob"] < 0.5,
            red_rp_2: x["red_rp_2"],
            red_rp_2_prob: x["red_rp_2_prob"],
            red_rp_2_correct:
              x["red_rp_2"] === 1
                ? x["red_rp_2_prob"] >= 0.5
                : x["red_rp_2_prob"] < 0.5,
          };
        });
      } else {
        cleanMatches = rawMatches.map(function (x, i) {
          return {
            match: x["key"].split("_")[1],
            blue: x["blue"].split(","),
            red: x["red"].split(","),
            blue_score: x["blue_score"],
            red_score: x["red_score"],
            winner: x["winner"],
            pred_winner: x["mix_winner"],
            win_prob:
              x["mix_winner"] === "red"
                ? x["mix_win_prob"]
                : 1 - x["mix_win_prob"],
            correct: x["winner"] === x["mix_winner"],
          };
        });
      }
      return cleanMatches;
    }

    setMatches(clean(rawMatches, year));
  }, [year, rawMatches]);

  function getMatchDisplays(matches) {
    return matches.map(function (x, i) {
      return (
        <Container key={i}>
          <br />
          <Row>
            <Col className={styles.outline}>{x["match"]}</Col>
            <Col className={styles.outline}>
              <Row className={styles.red}>
                <Col>
                  <a
                    className={styles.link}
                    href={`./../teams/${x["red"][0]}`}
                    children={x["red"][0]}
                  />
                </Col>
                <Col>
                  <a
                    className={styles.link}
                    href={`./../teams/${x["red"][1]}`}
                    children={x["red"][1]}
                  />
                </Col>
                <Col>
                  <a
                    className={styles.link}
                    href={`./../teams/${x["red"][2]}`}
                    children={x["red"][2]}
                  />
                </Col>
              </Row>
              <Row className={styles.blue}>
                <Col>
                  <a
                    className={styles.link}
                    href={`./../teams/${x["blue"][0]}`}
                    children={x["blue"][0]}
                  />
                </Col>
                <Col>
                  <a
                    className={styles.link}
                    href={`./../teams/${x["blue"][1]}`}
                    children={x["blue"][1]}
                  />
                </Col>
                <Col>
                  <a
                    className={styles.link}
                    href={`./../teams/${x["blue"][2]}`}
                    children={x["blue"][2]}
                  />
                </Col>
              </Row>
            </Col>
            <Col className={styles.outline}>2 of 2</Col>
          </Row>
        </Container>
      );
    });
  }
  return (
    <Paper className={styles.body}>
      <h2>
        {year} {event}
      </h2>
      <br />
      <Tabs defaultActiveKey="insights" id="tab">
        <Tab eventKey="insights" title="Insights">
          <ReactTable
            title="Current Statistics"
            columns={year >= 2016 ? columns : oldColumns}
            data={stats}
          />
        </Tab>
        <Tab eventKey="simulation" title="Simulation">
          <Typography>Simulation</Typography>
        </Tab>
        <Tab eventKey="Matches" title="Matches">
          {getMatchDisplays(matches)}
        </Tab>
      </Tabs>
    </Paper>
  );
}
