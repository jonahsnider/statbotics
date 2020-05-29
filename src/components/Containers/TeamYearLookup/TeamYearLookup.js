import React, { useState, useEffect } from "react";

import { Paper, Typography } from '@material-ui/core';
import { ButtonGroup, Button } from "react-bootstrap";
import Select from 'react-select';

import faker from 'faker';
import _ from 'lodash';

import { ReactTable } from './../../../components';

import {
  fetchTeamsYear,
  fetchTeamsYear_byCountry,
  fetchTeamsYear_byState,
  fetchTeamsYear_byDistrict
} from './../../../api';

import styles from './TeamYearLookup.module.css';

export default function TeamLookup() {
  const [year, setYear] = useState(2020)

  const [country, setCountry] = useState("None");
  const [stateProv, setStateProv] = useState("None")
  const [district, setDistrict] = useState("None");
  const [format, setFormat] = useState("Teams");
  const [title, setTitle] = useState(`${year} Team Lookup`)
  const [data, setData] = useState([]);

  const [stateDropdown, setStateDropdown] = useState("Select State")
  const [countryDropdown, setCountryDropdown] = useState("Select Country")
  const [districtDropdown, setDistrictDropdown] = useState("Select District")

  //column name, searchable, visible, filterable
  const columns = [
    ["Number", true, true, false, ""],
    ["Name", true, true, false, "Click names for details"],
    ["Rank", false, true, false, "By Max Elo"],
    ["Max Elo", false, true, false, "All Elos are sortable"],
    ["Mean Elo", false, true, false, ""],
    ["Start Elo", false, true, false, ""],
    ["Pre Champs Elo", false, false, false, ""],
    ["End Elo", false, true, false, ""],
  ];

  function clean(teams) {
    return teams.map(function(x, i){ return [
      x["team"],
      <a href={`teams/${x["team"]}`}>{x["name"]}</a>,
      i+1,
      x["elo_max"],
      x["elo_mean"],
      x["elo_start"],
      x["elo_pre_champs"],
      x["elo_end"],
    ]});
  }

  useEffect(() => {
    const getTeams = async () => {
      const new_teams = await fetchTeamsYear(year, "elo_max");
      setData(clean(new_teams.results));
    };

    const getTeams_byCountry = async () => {
      const new_teams = await fetchTeamsYear_byCountry(country, year, "elo_max");
      setData(clean(new_teams.results));
    }

    const getTeams_byState = async () => {
      const new_teams = await fetchTeamsYear_byState(country, stateProv, year, "elo_max");
      setData(clean(new_teams.results));
    }

    const getTeams_byDistrict = async () => {
      const new_teams = await fetchTeamsYear_byDistrict(district, year, "elo_max");
      setData(clean(new_teams.results));
    }

    if(format==="Teams") {getTeams()}
    else if(format==="Country") {getTeams_byCountry()}
    else if(format==="State") {getTeams_byState()}
    else {getTeams_byDistrict()}
  }, [format, country, stateProv, district, year]);

  const addressDefinitions = faker.definitions.address
  const usaOptions = _.map(addressDefinitions.state, (state, index) => ({
    value: addressDefinitions.state_abbr[index],
    label: state,
  }));

  const canadaOptions = [
    {value: "AB", label: "Alberta"},
    {value: "BC", label: "British Columbia"},
    {value: "MB", label: "Manitoba"},
    {value: "NB", label: "New Brunswick"},
    {value: "NL", label: "Newfoundland"},
    {value: "NT", label: "Northwest Territories"},
    {value: "NS", label: "Nova Scotia"},
    {value: "NU", label: "Nunavut"},
    {value: "ON", label: "Ontario"},
    {value: "PE", label: "Prince Edward Island"},
    {value: "QC", label: "Québec"},
    {value: "SK", label: "Saskatchewan"},
    {value: "YT", label: "Yukon"},
  ]

  const countryOptions = [
    {value: "Australia", label: "Australia"},
    {value: "Brazil", label: "Brazil"},
    {value: "Canada", label: "Canada"},
    {value: "China", label: "China"},
    {value: "Israel", label: "Israel"},
    {value: "Mexico", label: "Mexico"},
    {value: "Netherlands", label: "Netherlands"},
    {value: "Turkey", label: "Turkey"},
  ]

  const districtOptions = [
    {value: "chs", label: "Chesapeake"},
    {value: "fim", label: "Michigan"},
    {value: "fin", label: "Indiana"},
    {value: "fit", label: "Texas"},
    {value: "fma", label: "Mid-Atlantic"},
    {value: "fnc", label: "North Carolina"},
    {value: "isr", label: "Israel"},
    {value: "ne", label: "New England"},
    {value: "ont", label: "Ontario"},
    {value: "pch", label: "Peachtree"},
    {value: "pnw", label: "Pacific NW"},
  ]

  const yearOptions = [
    {value: "2020", label: "2020"},
    {value: "2019", label: "2019"},
    {value: "2018", label: "2018"},
    {value: "2017", label: "2017"},
    {value: "2016", label: "2016"},
    {value: "2015", label: "2015"},
    {value: "2014", label: "2014"},
    {value: "2013", label: "2013"},
    {value: "2012", label: "2012"},
    {value: "2011", label: "2011"},
    {value: "2010", label: "2010"},
    {value: "2009", label: "2009"},
    {value: "2008", label: "2008"},
    {value: "2007", label: "2007"},
    {value: "2006", label: "2006"},
    {value: "2005", label: "2005"},
    {value: "2004", label: "2004"},
    {value: "2003", label: "2003"},
    {value: "2002", label: "2002"},
  ]

  const yearClick = (year) => {
    setYear(year["value"])
    setTitle(`${year["value"]} Team Lookup`)
  }

  function allClick() {
    setFormat("Teams")
    setTitle(`${year} Team Lookup`);
    setCountryDropdown("Select Country")
    setStateDropdown("Select State")
    setDistrictDropdown("Select District")
  };

  const stateClick = (state) => {
    setStateProv(state["value"]);
    setFormat("State");
    setTitle(`${year} Team Lookup - ${state["label"]}`);
    setStateDropdown(state["label"])
    setDistrictDropdown("Select District")
  }

  const countryClick = (country) => {
    setCountry(country["value"]);
    setFormat("Country");
    setTitle(`${year} Team Lookup - ${country["label"]}`);
    if(country==="USA") {setStateDropdown("Select State")}
    else if(country==="Canada") {setStateDropdown("Select Province")}
    else {setStateDropdown("All")}

    setCountryDropdown(country["label"])
    setDistrictDropdown("Select District")
  }

  const districtClick = (district) => {
    setDistrict(district["value"]);
    setFormat("District");
    setTitle(`${year} Team Lookup - ${district["label"]}`);
    setStateDropdown("Select State")
    setCountryDropdown("Select Country")
    setDistrictDropdown(district["label"])
  }

  return (
    <div>
      <Paper
        elevation={3}
        className = {styles.body}

        children = {
          <div>
          <ButtonGroup className={styles.button_group}>

            <Select
              className={styles.dropdown}
              styles={{
                menu: provided => ({ ...provided, zIndex: 9999 })
              }}
              options = {yearOptions}
              onChange = {yearClick}
              value = {{value:`${year}`, label:`${year}`}}
            />

            <Button
              variant="outline-dark"
              onClick={() => allClick()}
              className={styles.button}
            >
              <Typography>All Teams</Typography>
            </Button>

            <Select
              className={styles.dropdown}
              styles={{
                menu: provided => ({ ...provided, zIndex: 9999 })
              }}
              options = {countryOptions}
              onChange = {countryClick}
              value = {{value:`${countryDropdown}`, label:`${countryDropdown}`}}
            />

            <Select
              className={styles.dropdown}
              styles={{
                menu: provided => ({ ...provided, zIndex: 9999 })
              }}
              options = {usaOptions}
              onChange = {stateClick}
              value = {{value:`${stateDropdown}`, label:`${stateDropdown}`}}
            />

            <Select
              className={styles.dropdown}
              styles={{
                menu: provided => ({ ...provided, zIndex: 9999 })
              }}
              options = {districtOptions}
              onChange = {districtClick}
              value = {{value:`${districtDropdown}`, label:`${districtDropdown}`}}
            />

            </ButtonGroup>

            <ReactTable
              title={title}
              columns={columns}
              data={data}
            />
          </div>
        }
      />
    </div>
  );
}
