import React from "react";

import { ResponsiveLine } from "@nivo/line";

import styles from "./LineChart.module.css";

class LineChart extends React.Component {
  render() {
    var data = this.props.data;

    try {
      if (data[0].id !== "Baseline") {
        data.unshift({
          id: "Baseline",
          data: [
            { x: 2002, y: 1500 },
            { x: 2022, y: 1500 },
          ],
        });
      }
    } catch (e) {}

    return (
      <div className={styles.gray}>
        <ResponsiveLine
          data={data}
          margin={{ top: 20, right: 30, bottom: 50, left: 60 }}
          xScale={{ type: "linear", min: 2002, max: 2022 }}
          yScale={{
            type: "linear",
            min: 1300,
            max: 2300,
            stacked: false,
            reverse: false,
          }}
          curve="linear"
          axisBottom={{
            orient: "bottom",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "Year",
            legendOffset: 40,
            legendPosition: "middle",
          }}
          axisLeft={{
            orient: "left",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "Max Elo",
            legendOffset: -50,
            legendPosition: "middle",
          }}
          colors={{ scheme: "set1" }}
          pointSize={10}
          pointLabel="y"
          pointLabelYOffset={-12}
          useMesh={true}
          legends={[
            {
              anchor: "top-right",
              direction: "column",
              justify: false,
              translateX: 12,
              translateY: 0,
              itemsSpacing: 0,
              itemDirection: "left-to-right",
              itemWidth: 80,
              itemHeight: 20,
              itemOpacity: 0.75,
              symbolSize: 12,
              symbolShape: "circle",
              symbolBorderColor: "rgba(0, 0, 0, .5)",
              effects: [
                {
                  on: "hover",
                  style: {
                    itemBackground: "rgba(0, 0, 0, .03)",
                    itemOpacity: 1,
                  },
                },
              ],
            },
          ]}
        />
      </div>
    );
  }
}

export default LineChart;
