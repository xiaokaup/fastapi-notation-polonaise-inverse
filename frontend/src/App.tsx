import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [expression, setExpression] = React.useState("1 2 + 3 * 9 / ");
  const [expressionResult, setExpressionResult] = React.useState();
  const [errorMessage, setErrorMessage] = React.useState("");

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
        console.log("data: ", data);
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
        console.log("data: ", data);
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
    </div>
  );
}

export default App;
