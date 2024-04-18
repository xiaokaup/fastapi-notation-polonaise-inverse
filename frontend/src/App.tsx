import React from "react";
import "./App.css";

function App() {
  const [expression, setExpression] = React.useState("1 2 + 3 * 9 / ");
  const [expressionResult, setExpressionResult] = React.useState();
  const [errorMessage, setErrorMessage] = React.useState("");

  const [isHistoricalResultsShow, setIsHistoricalResultsShow] =
    React.useState(false);
  const [historicalResults, setHistoricalResults] = React.useState([]);

  const calculate = () => {
    fetch("http://localhost:8000/calculator/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        expression,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status_code && data.status_code !== 200) {
          throw new Error(data.detail);
        }

        setExpressionResult(data.result);
        setErrorMessage("");
      })
      .catch((error) => {
        setErrorMessage(error.message);
        console.error(error);
      });

    setIsHistoricalResultsShow(false);
  };

  const getHistoricalResults = () => {
    fetch("http://localhost:8000/get_results/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status_code && data.status_code !== 200) {
          throw new Error(data.detail);
        }

        setHistoricalResults(data.result);
      })
      .catch((error) => {
        setErrorMessage(error.message);
        console.error(error);
      });

    setIsHistoricalResultsShow(true);
  };

  return (
    <div className="App">
      <h1>fastapi-notation-polonaise-inverse</h1>
      <div className="buttons">
        <input
          style={{ margin: "0 1rem" }}
          type="text"
          value={expression}
          onChange={(event: any) => setExpression(event.target.value)}
        />
        <button style={{ margin: "0 1rem" }} onClick={calculate}>
          Calculate
        </button>
        <button style={{ margin: "0 1rem" }} onClick={getHistoricalResults}>
          Get historical results
        </button>
      </div>
      <div style={{ marginTop: "2rem" }}>
        {(expressionResult || expressionResult === 0) && !errorMessage && (
          <div>Result: {expressionResult}</div>
        )}
        {errorMessage && <div>{errorMessage}</div>}
      </div>
      {isHistoricalResultsShow && (
        <div style={{ marginTop: "2rem" }}>
          {historicalResults.length > 0 &&
            historicalResults.map((item: any, index) => {
              return (
                <div key={`${item}-${item.expression}`}>
                  <div>
                    Calculate {index}: {item.expression} = {item.value}
                  </div>
                </div>
              );
            })}
        </div>
      )}
    </div>
  );
}

export default App;
